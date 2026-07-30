"""Property tests that run against every real country file.

These deliberately avoid asserting specific tax amounts. Rates change every
year, and a test suite that hard-codes them becomes a maintenance burden that
gets deleted. What these check instead is that each country behaves like a tax
system: nobody ends up better off by earning more, the arithmetic reconciles,
and the documentation a skill depends on is actually present.
"""

import pytest

from taxcalc import available_countries, load_country
from taxcalc.engine import Profile, compute
from taxcalc.validate import count_files, validate_all

ALL = [country["iso2"] for country in available_countries()]
# One income per country in its own currency, chosen to sit somewhere in the
# middle of that country's income distribution.
TYPICAL_INCOME = {
    "JP": 6_000_000,
    "KR": 60_000_000,
    "IN": 1_500_000,
    "HK": 600_000,
    "SE": 500_000,
    "NO": 700_000,
    "DK": 500_000,
    "CZ": 900_000,
    "PL": 150_000,
    "BR": 100_000,
}


def income_for(iso2: str) -> float:
    return TYPICAL_INCOME.get(iso2, 70_000)


def test_the_dataset_covers_thirty_countries():
    assert len(ALL) == 30


def test_all_country_files_are_structurally_valid():
    findings = validate_all()
    assert findings == {}, f"{count_files()} files checked; problems: {findings}"


@pytest.mark.parametrize("iso2", ALL)
class TestEveryCountry:
    def test_computation_reconciles(self, iso2):
        data = load_country(iso2)
        result = compute(data, Profile(employment_income=income_for(iso2)))
        assert result.net_income == pytest.approx(
            result.gross_income - result.employee_social_security - result.total_income_tax
        )

    def test_tax_is_never_negative_and_never_exceeds_income(self, iso2):
        data = load_country(iso2)
        result = compute(data, Profile(employment_income=income_for(iso2)))
        assert result.total_income_tax >= 0
        assert result.total_burden <= result.gross_income

    def test_earning_more_never_leaves_you_with_less(self, iso2):
        """No income level should have a marginal wedge above 100%.

        A cliff like that is almost always a data error - a threshold entered as
        a band width, or a credit that vanishes abruptly instead of tapering.
        """
        data = load_country(iso2)
        base = income_for(iso2)
        previous_net = None
        for multiplier in (0.25, 0.5, 1, 1.5, 2, 3, 5, 10):
            result = compute(data, Profile(employment_income=base * multiplier))
            if previous_net is not None:
                assert result.net_income >= previous_net - 0.01, (
                    f"{iso2}: net income falls as gross rises at {base * multiplier:,.0f}"
                )
            previous_net = result.net_income

    def test_effective_rate_does_not_exceed_the_marginal_wedge_at_the_top(self, iso2):
        data = load_country(iso2)
        result = compute(data, Profile(employment_income=income_for(iso2) * 10))
        assert result.effective_burden_rate <= result.marginal_wedge + 0.02

    def test_reporting_block_has_what_the_reporting_skills_need(self, iso2):
        reporting = load_country(iso2)["reporting"]
        assert reporting["authority"]
        assert reporting["tax_year_end"]
        assert len(reporting["deadlines"]) >= 3
        assert reporting.get("penalties"), f"{iso2} has no penalty information"
        assert reporting.get("who_must_file"), f"{iso2} does not say who must file"

    def test_country_documents_its_own_limitations(self, iso2):
        """Every country must carry sources and honest caveats.

        A number without a way to check it is worse than no number, because it
        looks authoritative. The skills quote these fields directly.
        """
        data = load_country(iso2)
        assert data["sources"], f"{iso2} has no source URLs"
        assert data.get("quirks"), f"{iso2} lists no country-specific traps"
        assert data.get("residency", {}).get("test"), f"{iso2} has no residence test"

    def test_both_skills_are_named_and_follow_the_naming_convention(self, iso2):
        skills = load_country(iso2).get("skills", {})
        assert skills.get("calculation", "").endswith("-tax-calculation")
        assert skills.get("reporting", "").endswith("-tax-reporting")


def test_countries_with_no_income_tax_return_zero():
    for iso2 in ("AE", "SA"):
        result = compute(load_country(iso2), Profile(employment_income=500_000))
        assert result.total_income_tax == 0


def test_lookup_accepts_iso_code_name_and_file_stem():
    by_code = load_country("DE")
    assert load_country("de")["iso2"] == by_code["iso2"]
    assert load_country("Germany")["iso2"] == by_code["iso2"]


def test_unknown_country_raises_with_a_helpful_message():
    from taxcalc import CountryNotFound

    with pytest.raises(CountryNotFound) as excinfo:
        load_country("Atlantis")
    assert "available" in str(excinfo.value)
