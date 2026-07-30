"""Structural checks for the country data files.

These are not tax-correctness checks - no program can tell you whether 42% is
this year's top rate. They catch the mechanical mistakes that silently produce
wrong numbers: brackets out of order, a missing open-ended top bracket, rates
entered as 42 instead of 0.42, or a required field left out.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Mapping

from .loader import data_dir

REQUIRED_TOP_LEVEL = ["country", "iso2", "tax_year", "currency", "income_tax", "reporting"]
REQUIRED_REPORTING = ["tax_year_end", "authority", "deadlines"]


def _check_brackets(brackets: List[Mapping[str, Any]], where: str) -> List[str]:
    problems: List[str] = []
    if not brackets:
        return [f"{where}: empty bracket list"]
    previous = 0.0
    for index, bracket in enumerate(brackets):
        rate = bracket.get("rate")
        if rate is None:
            problems.append(f"{where}[{index}]: missing rate")
            continue
        if not 0 <= float(rate) <= 1:
            problems.append(
                f"{where}[{index}]: rate {rate} outside 0-1; rates are decimals (0.42, not 42)"
            )
        up_to = bracket.get("up_to")
        if up_to is None:
            if index != len(brackets) - 1:
                problems.append(f"{where}[{index}]: open-ended bracket must be last")
            continue
        if float(up_to) <= previous:
            problems.append(
                f"{where}[{index}]: threshold {up_to} not greater than previous {previous}"
            )
        previous = float(up_to)
    if brackets[-1].get("up_to") is not None:
        problems.append(f"{where}: top bracket must be open-ended (up_to: null)")
    return problems


def _check_schedule(schedule: Mapping[str, Any], where: str) -> List[str]:
    kind = schedule.get("type", "progressive")
    if kind == "progressive":
        return _check_brackets(schedule.get("brackets", []), f"{where}.brackets")
    if kind == "flat":
        rate = schedule.get("rate")
        if rate is None or not 0 <= float(rate) <= 1:
            return [f"{where}: flat schedule needs a rate between 0 and 1"]
        return []
    if kind == "piecewise_polynomial":
        if not schedule.get("zones"):
            return [f"{where}: piecewise_polynomial schedule needs zones"]
        return []
    if kind == "none":
        return []
    return [f"{where}: unknown schedule type {kind!r}"]


def _check_schedule_behaviour(schedule: Mapping[str, Any], where: str) -> List[str]:
    """Evaluate the schedule across a range and check it behaves like a tax.

    A rate table can be structurally perfect and still wrong - a mis-transcribed
    formula constant, for instance, produces negative tax at ordinary incomes.
    Sampling the curve catches that class of mistake cheaply, which pure schema
    checking never will.
    """
    from .schedules import apply_schedule  # local import keeps validate importable alone

    problems: List[str] = []
    previous = -1.0
    for income in (0, 5_000, 15_000, 30_000, 60_000, 120_000, 300_000, 1_000_000):
        try:
            tax = apply_schedule(float(income), schedule)
        except Exception as exc:  # pragma: no cover - defensive
            return [f"{where}: schedule failed to evaluate at {income}: {exc}"]
        if tax < -0.01:
            problems.append(f"{where}: negative tax {tax:,.2f} at income {income:,}")
        if tax > income + 0.01:
            problems.append(f"{where}: tax {tax:,.2f} exceeds income {income:,}")
        if tax + 0.01 < previous:
            problems.append(f"{where}: tax decreases between incomes (at {income:,})")
        previous = tax
    return problems


def validate_country(payload: Mapping[str, Any], filename: str = "") -> List[str]:
    problems: List[str] = []
    prefix = filename or payload.get("iso2", "?")

    for key in REQUIRED_TOP_LEVEL:
        if key not in payload:
            problems.append(f"{prefix}: missing required field {key!r}")

    iso2 = payload.get("iso2", "")
    if len(iso2) != 2 or not iso2.isupper():
        problems.append(f"{prefix}: iso2 should be a two-letter uppercase code, got {iso2!r}")

    income_tax = payload.get("income_tax") or {}
    by_status = income_tax.get("by_filing_status")
    if by_status:
        for status, block in by_status.items():
            merged = {**income_tax, **block}
            where = f"{prefix}.income_tax.{status}"
            problems.extend(_check_schedule(merged, where))
            problems.extend(_check_schedule_behaviour(merged, where))
    else:
        problems.extend(_check_schedule(income_tax, f"{prefix}.income_tax"))
        problems.extend(_check_schedule_behaviour(income_tax, f"{prefix}.income_tax"))

    for name, block in (payload.get("regions") or {}).items():
        if "schedule" in block:
            problems.extend(_check_schedule(block["schedule"], f"{prefix}.regions.{name}"))
        elif "rate" not in block:
            problems.append(f"{prefix}.regions.{name}: needs either a schedule or a rate")

    for group in ("employee", "employer", "self_employed"):
        for index, rule in enumerate((payload.get("social_security") or {}).get(group, [])):
            where = f"{prefix}.social_security.{group}[{index}]"
            if "name" not in rule:
                problems.append(f"{where}: missing name")
            rate = rule.get("rate")
            if rule.get("type") != "fixed" and (rate is None or not 0 <= float(rate) <= 1):
                problems.append(f"{where}: rate {rate!r} should be a decimal between 0 and 1")

    reporting = payload.get("reporting") or {}
    for key in REQUIRED_REPORTING:
        if key not in reporting:
            problems.append(f"{prefix}: reporting.{key} is required")
    if not reporting.get("deadlines"):
        problems.append(f"{prefix}: reporting.deadlines must list at least one deadline")

    if not payload.get("sources"):
        problems.append(f"{prefix}: at least one official source URL is required for verification")

    return problems


def validate_all() -> Dict[str, List[str]]:
    """Validate every country file. Returns ``{filename: [problems]}``."""
    findings: Dict[str, List[str]] = {}
    for path in sorted(data_dir().glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        problems = validate_country(payload, path.name)
        if problems:
            findings[path.name] = problems
    return findings


def summarise(findings: Mapping[str, List[str]], total: int) -> str:
    if not findings:
        return f"OK: {total} country files validated, no structural problems found."
    lines = [f"{sum(len(v) for v in findings.values())} problem(s) across {len(findings)} file(s):"]
    for filename, problems in findings.items():
        lines.append(f"\n{filename}")
        lines.extend(f"  - {problem}" for problem in problems)
    return "\n".join(lines)


def count_files() -> int:
    return len(list(data_dir().glob("*.json")))


if __name__ == "__main__":  # pragma: no cover
    print(summarise(validate_all(), count_files()))
