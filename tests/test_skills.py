"""Tests for the skill files themselves.

Skills and country data drift apart easily: a country gets renamed, a skill
directory is added without data behind it, or a description loses the trigger
words that make the skill fire. These tests make that drift fail loudly instead
of quietly degrading the skills' usefulness.
"""

import re
from pathlib import Path

import pytest

from taxcalc import available_countries, load_country

REPO = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO / "skills"
SKILL_DIRS = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def frontmatter_of(skill_dir: Path) -> dict:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    assert match, f"{skill_dir.name}: SKILL.md must start with a YAML frontmatter block"
    fields, key = {}, None
    for line in match.group(1).splitlines():
        if re.match(r"^\w[\w-]*:", line):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
        elif key and line.strip():
            fields[key] += " " + line.strip()
    return fields


def test_there_are_sixty_skills_covering_thirty_countries():
    assert len(SKILL_DIRS) == 60
    calculation = [d for d in SKILL_DIRS if d.name.endswith("-tax-calculation")]
    reporting = [d for d in SKILL_DIRS if d.name.endswith("-tax-reporting")]
    assert len(calculation) == 30
    assert len(reporting) == 30
    # Every calculation skill has a reporting twin and vice versa.
    stems = {d.name.rsplit("-tax-", 1)[0] for d in SKILL_DIRS}
    assert len(stems) == 30


def test_every_country_points_at_skills_that_exist():
    names = {path.name for path in SKILL_DIRS}
    for country in available_countries():
        skills = load_country(country["iso2"])["skills"]
        for kind in ("calculation", "reporting"):
            assert skills[kind] in names, (
                f"{country['country']} references skill {skills[kind]!r} which has no directory"
            )


def test_every_skill_is_referenced_by_a_country():
    referenced = set()
    for country in available_countries():
        referenced.update(load_country(country["iso2"])["skills"].values())
    orphans = {path.name for path in SKILL_DIRS} - referenced
    assert not orphans, f"skills with no country data behind them: {sorted(orphans)}"


@pytest.mark.parametrize("skill_dir", SKILL_DIRS, ids=lambda p: p.name)
class TestEverySkill:
    def test_frontmatter_name_matches_the_directory(self, skill_dir):
        assert frontmatter_of(skill_dir)["name"] == skill_dir.name

    def test_description_is_substantial_enough_to_trigger_reliably(self, skill_dir):
        """Descriptions are the only thing the model sees when deciding to load a skill.

        A terse description means the skill silently never fires, which is the
        most common failure mode for a skill collection this size. The floor
        here is deliberately generous - it only catches placeholders.
        """
        description = frontmatter_of(skill_dir)["description"]
        assert len(description) > 200, f"{skill_dir.name}: description is too thin to trigger on"
        assert "Use this" in description or "Use whenever" in description

    def test_body_points_at_the_shared_workflow(self, skill_dir):
        body = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        expected = (
            "references/calculation-workflow.md"
            if skill_dir.name.endswith("-calculation")
            else "references/reporting-workflow.md"
        )
        assert expected in body, f"{skill_dir.name}: does not reference {expected}"

    def test_body_shows_a_runnable_engine_command(self, skill_dir):
        body = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        assert "python -m taxcalc" in body

    def test_engine_commands_name_a_country_that_exists(self, skill_dir):
        body = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        codes = {country["iso2"] for country in available_countries()}
        for command in re.findall(r"python -m taxcalc (?:calc|info|deadlines) (\w+)", body):
            assert command in codes, f"{skill_dir.name}: unknown country code {command!r}"

    def test_skill_stays_short_enough_to_load_cheaply(self, skill_dir):
        lines = (skill_dir / "SKILL.md").read_text(encoding="utf-8").splitlines()
        assert len(lines) < 200, f"{skill_dir.name}: {len(lines)} lines; move detail to references/"


def test_shared_references_exist():
    for name in (
        "calculation-workflow.md",
        "reporting-workflow.md",
        "disclaimers.md",
        "residency-and-cross-border.md",
    ):
        assert (REPO / "references" / name).is_file(), f"missing references/{name}"
