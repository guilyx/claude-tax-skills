"""The computation pipeline shared by all 30 countries.

Every country's tax bill is assembled in the same order:

    gross income
      - deductible social security contributions
      - standard / employment-expense deduction
      - personal allowance (possibly tapered)
      - user-supplied deductions
    = taxable income
      -> national schedule            (brackets, flat rate, or formula)
      + regional / municipal schedule (Nordics, Japan, Switzerland, Canada, ...)
      + surcharges                    (solidarity levies, high-income surtaxes)
      - credits                       (non-refundable first, then refundable)
    = total income tax
    net = gross - employee social security - total income tax

Countries that lack a layer simply omit it from their JSON. Running everything
through one pipeline is what makes the 30 country results comparable, and it
means a reviewer only has to understand this file to audit any of them.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping, Optional

from .schedules import (
    apply_schedule,
    contribution_amount,
    schedule_marginal_rate,
)

MARGINAL_PROBE = 100.0


@dataclass
class Profile:
    """The taxpayer facts the engine needs. Everything is annual, in local currency."""

    employment_income: float = 0.0
    self_employment_income: float = 0.0
    other_income: float = 0.0
    filing_status: str = "single"
    region: Optional[str] = None
    children: int = 0
    dependants: int = 0
    deductions: float = 0.0
    credits: float = 0.0
    local_rate: Optional[float] = None
    months: int = 12

    @property
    def gross_income(self) -> float:
        return self.employment_income + self.self_employment_income + self.other_income


@dataclass
class LineItem:
    """One row in the audit trail, so every number can be traced to a rule."""

    label: str
    amount: float
    note: str = ""

    def as_dict(self) -> Dict[str, Any]:
        return {"label": self.label, "amount": round(self.amount, 2), "note": self.note}


@dataclass
class ComputationResult:
    country: str
    iso2: str
    tax_year: int
    currency: str
    profile: Profile
    gross_income: float = 0.0
    taxable_income: float = 0.0
    employee_social_security: float = 0.0
    employer_social_security: float = 0.0
    national_income_tax: float = 0.0
    regional_income_tax: float = 0.0
    surcharges: float = 0.0
    credits_applied: float = 0.0
    total_income_tax: float = 0.0
    net_income: float = 0.0
    deductions: List[LineItem] = field(default_factory=list)
    social_security_lines: List[LineItem] = field(default_factory=list)
    tax_lines: List[LineItem] = field(default_factory=list)
    credit_lines: List[LineItem] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    marginal_wedge: float = 0.0

    @property
    def total_burden(self) -> float:
        """Income tax plus the employee's own social security."""
        return self.total_income_tax + self.employee_social_security

    @property
    def effective_tax_rate(self) -> float:
        return self.total_income_tax / self.gross_income if self.gross_income else 0.0

    @property
    def effective_burden_rate(self) -> float:
        return self.total_burden / self.gross_income if self.gross_income else 0.0

    def as_dict(self) -> Dict[str, Any]:
        return {
            "country": self.country,
            "iso2": self.iso2,
            "tax_year": self.tax_year,
            "currency": self.currency,
            "inputs": {
                "employment_income": self.profile.employment_income,
                "self_employment_income": self.profile.self_employment_income,
                "other_income": self.profile.other_income,
                "filing_status": self.profile.filing_status,
                "region": self.profile.region,
                "children": self.profile.children,
            },
            "gross_income": round(self.gross_income, 2),
            "taxable_income": round(self.taxable_income, 2),
            "deductions": [item.as_dict() for item in self.deductions],
            "social_security": {
                "employee_total": round(self.employee_social_security, 2),
                "employer_total": round(self.employer_social_security, 2),
                "lines": [item.as_dict() for item in self.social_security_lines],
            },
            "income_tax": {
                "national": round(self.national_income_tax, 2),
                "regional": round(self.regional_income_tax, 2),
                "surcharges": round(self.surcharges, 2),
                "credits": round(self.credits_applied, 2),
                "total": round(self.total_income_tax, 2),
                "lines": [item.as_dict() for item in self.tax_lines],
                "credit_lines": [item.as_dict() for item in self.credit_lines],
            },
            "totals": {
                "total_income_tax": round(self.total_income_tax, 2),
                "employee_social_security": round(self.employee_social_security, 2),
                "total_burden": round(self.total_burden, 2),
                "net_income": round(self.net_income, 2),
                "net_monthly": round(self.net_income / 12, 2),
                "effective_tax_rate": round(self.effective_tax_rate, 4),
                "effective_burden_rate": round(self.effective_burden_rate, 4),
                "marginal_wedge": round(self.marginal_wedge, 4),
            },
            "warnings": self.warnings,
        }


def _status_block(data: Mapping[str, Any], key: str, status: str) -> Mapping[str, Any]:
    """Pick the variant of a block that matches the filing status, if any.

    Joint-filing countries (US, DE, FR, PT, ...) publish a different table per
    status. Countries that tax individually just have one block and the status
    is ignored, which is why callers never have to know which kind they are in.
    """
    block = data.get(key) or {}
    by_status = block.get("by_filing_status")
    if not by_status:
        return block
    if status in by_status:
        merged = {k: v for k, v in block.items() if k != "by_filing_status"}
        merged.update(by_status[status])
        return merged
    default = block.get("default_filing_status", "single")
    merged = {k: v for k, v in block.items() if k != "by_filing_status"}
    merged.update(by_status.get(default, {}))
    return merged


def _tapered(amount: float, taper: Optional[Mapping[str, Any]], income: float) -> float:
    """Withdraw an allowance above a threshold (the UK 100k trap, and friends)."""
    if not taper:
        return amount
    threshold = float(taper["threshold"])
    if income <= threshold:
        return amount
    rate = float(taper.get("rate", 0.5))
    reduced = amount - (income - threshold) * rate
    return max(float(taper.get("floor", 0.0)), reduced)


def _region_block(data: Mapping[str, Any], region: Optional[str]) -> Optional[Mapping[str, Any]]:
    regions = data.get("regions") or {}
    if not regions:
        return None
    if region and region.upper() in regions:
        return regions[region.upper()]
    default = data.get("default_region")
    if default and default in regions:
        return regions[default]
    return None


def _social_security(
    data: Mapping[str, Any],
    profile: Profile,
    result: ComputationResult,
) -> float:
    """Return the portion of employee contributions that is income-tax deductible."""
    block = data.get("social_security") or {}
    deductible = 0.0

    employment_base = profile.employment_income
    self_base = profile.self_employment_income

    for rule in block.get("employee", []):
        base = employment_base if rule.get("base", "employment") == "employment" else profile.gross_income
        amount = contribution_amount(base, rule)
        if amount <= 0 and not rule.get("always_show"):
            continue
        result.employee_social_security += amount
        result.social_security_lines.append(
            LineItem(f"Employee: {rule['name']}", amount, rule.get("note", ""))
        )
        if rule.get("deductible", False):
            deductible += amount

    if self_base > 0:
        for rule in block.get("self_employed", []):
            amount = contribution_amount(self_base, rule)
            if amount <= 0:
                continue
            result.employee_social_security += amount
            result.social_security_lines.append(
                LineItem(f"Self-employed: {rule['name']}", amount, rule.get("note", ""))
            )
            if rule.get("deductible", False):
                deductible += amount

    for rule in block.get("employer", []):
        amount = contribution_amount(employment_base, rule)
        if amount <= 0:
            continue
        result.employer_social_security += amount
        result.social_security_lines.append(
            LineItem(f"Employer: {rule['name']}", amount, rule.get("note", ""))
        )

    return deductible


def _deductions(
    data: Mapping[str, Any],
    profile: Profile,
    deductible_ss: float,
    result: ComputationResult,
) -> float:
    total = 0.0

    if deductible_ss > 0:
        total += deductible_ss
        result.deductions.append(
            LineItem("Deductible social security contributions", deductible_ss)
        )

    standard = _status_block(data, "standard_deduction", profile.filing_status)
    if standard:
        amount = float(standard.get("amount", 0.0))
        rate = standard.get("rate")
        if rate is not None:
            amount = max(amount, profile.employment_income * float(rate))
            cap = standard.get("cap")
            if cap is not None:
                amount = min(amount, float(cap))
        amount = _tapered(amount, standard.get("taper"), profile.gross_income)
        if amount > 0:
            total += amount
            result.deductions.append(
                LineItem(standard.get("name", "Standard deduction"), amount, standard.get("note", ""))
            )

    allowance = _status_block(data, "personal_allowance", profile.filing_status)
    if allowance:
        amount = float(allowance.get("amount", 0.0))
        amount += float(allowance.get("per_child", 0.0)) * profile.children
        amount += float(allowance.get("per_dependant", 0.0)) * profile.dependants
        amount = _tapered(amount, allowance.get("taper"), profile.gross_income)
        if amount > 0:
            total += amount
            result.deductions.append(
                LineItem(allowance.get("name", "Personal allowance"), amount, allowance.get("note", ""))
            )

    if profile.deductions:
        total += profile.deductions
        result.deductions.append(LineItem("User-supplied deductions", profile.deductions))

    return total


def _surcharges(
    data: Mapping[str, Any],
    profile: Profile,
    base_tax: float,
    taxable: float,
    result: ComputationResult,
) -> float:
    total = 0.0
    for rule in data.get("surcharges", []) or []:
        base_kind = rule.get("base", "tax")
        base = {
            "tax": base_tax,
            "taxable_income": taxable,
            "gross_income": profile.gross_income,
        }[base_kind]
        threshold = float(rule.get("threshold", 0.0))
        if base <= threshold:
            continue
        chargeable = base - threshold if rule.get("above_threshold_only", True) else base
        if "schedule" in rule:
            amount = apply_schedule(chargeable, rule["schedule"])
        else:
            amount = chargeable * float(rule.get("rate", 0.0))
        if amount <= 0:
            continue
        total += amount
        result.tax_lines.append(LineItem(rule["name"], amount, rule.get("note", "")))
    return total


def _credits(
    data: Mapping[str, Any],
    profile: Profile,
    gross_tax: float,
    result: ComputationResult,
) -> float:
    """Apply credits, respecting the non-refundable limit.

    Non-refundable credits can only wipe out tax that exists; refundable ones
    (child benefits in several systems) can push the bill negative. Getting this
    wrong is one of the most common manual-calculation errors, so the engine
    tracks the remaining headroom explicitly.
    """
    applied = 0.0
    headroom = max(0.0, gross_tax)

    for rule in data.get("credits", []) or []:
        if rule.get("filing_status") and rule["filing_status"] != profile.filing_status:
            continue
        amount = float(rule.get("amount", 0.0))
        amount += float(rule.get("per_child", 0.0)) * profile.children
        amount += float(rule.get("per_dependant", 0.0)) * profile.dependants
        if rule.get("rate") is not None:
            amount += profile.gross_income * float(rule["rate"])
        if rule.get("cap") is not None:
            amount = min(amount, float(rule["cap"]))
        amount = _tapered(amount, rule.get("taper"), profile.gross_income)
        if rule.get("per_child") and profile.children == 0 and not rule.get("amount"):
            continue
        if amount <= 0:
            continue
        if not rule.get("refundable", False):
            amount = min(amount, headroom)
            headroom -= amount
        if amount <= 0:
            continue
        applied += amount
        result.credit_lines.append(LineItem(rule["name"], amount, rule.get("note", "")))

    if profile.credits:
        extra = min(profile.credits, headroom) if headroom > 0 else 0.0
        if extra > 0:
            applied += extra
            result.credit_lines.append(LineItem("User-supplied credits", extra))

    return applied


def _compute_core(data: Mapping[str, Any], profile: Profile) -> ComputationResult:
    result = ComputationResult(
        country=data["country"],
        iso2=data["iso2"],
        tax_year=data["tax_year"],
        currency=data["currency"],
        profile=profile,
    )
    result.gross_income = profile.gross_income
    result.warnings = list(data.get("warnings", []))

    deductible_ss = _social_security(data, profile, result)
    total_deductions = _deductions(data, profile, deductible_ss, result)
    taxable = max(0.0, profile.gross_income - total_deductions)
    result.taxable_income = taxable

    schedule = _status_block(data, "income_tax", profile.filing_status)
    region_block = _region_block(data, profile.region)

    if region_block and region_block.get("replaces_national"):
        # Scotland sets its own rates and bands instead of the UK-wide ones,
        # rather than adding a layer on top of them.
        schedule = region_block["schedule"]

    splitting = float(schedule.get("income_splitting_factor", 1.0) or 1.0)
    splitting += float(schedule.get("income_splitting_per_child", 0.0)) * profile.children
    if splitting and splitting != 1.0:
        # Germany's Splittingverfahren and France's quotient familial: tax one
        # share of the income, then multiply the tax back up by the number of
        # shares. This is what makes a household with children pay less than the
        # same income earned by one person alone.
        national = apply_schedule(taxable / splitting, schedule) * splitting
    else:
        national = apply_schedule(taxable, schedule)
    result.national_income_tax = national
    if national > 0:
        result.tax_lines.append(
            LineItem(schedule.get("name", "National income tax"), national, schedule.get("note", ""))
        )

    regional = 0.0
    local = data.get("local_tax")
    if region_block and region_block.get("replaces_national"):
        regional = 0.0
    elif region_block and "schedule" in region_block:
        regional = apply_schedule(taxable, region_block["schedule"])
        result.tax_lines.append(
            LineItem(
                f"{region_block.get('name', profile.region or 'Regional')} income tax",
                regional,
                region_block.get("note", ""),
            )
        )
    elif local:
        rate = profile.local_rate
        if rate is None and region_block and "rate" in region_block:
            rate = float(region_block["rate"])
        if rate is None:
            rate = float(local.get("default_rate", 0.0))
        base = max(0.0, taxable - float(local.get("extra_allowance", 0.0)))
        regional = base * rate
        if regional > 0:
            result.tax_lines.append(
                LineItem(
                    local.get("name", "Local income tax"),
                    regional,
                    local.get("note", f"rate {rate:.2%}"),
                )
            )
    result.regional_income_tax = regional

    result.surcharges = _surcharges(data, profile, national + regional, taxable, result)

    gross_tax = national + regional + result.surcharges
    result.credits_applied = _credits(data, profile, gross_tax, result)

    result.total_income_tax = gross_tax - result.credits_applied
    result.net_income = profile.gross_income - result.employee_social_security - result.total_income_tax
    return result


def compute(data: Mapping[str, Any], profile: Profile) -> ComputationResult:
    """Compute a full result plus the marginal wedge on the next 100 of income.

    The wedge is measured numerically rather than read off a bracket table
    because bracket edges are only part of the story: contribution ceilings,
    tapered allowances and surcharge thresholds all move the real marginal rate,
    and users almost always care about that number rather than the headline one.
    """
    result = _compute_core(data, profile)

    probe = Profile(**{**profile.__dict__})
    if probe.employment_income > 0 or probe.gross_income == 0:
        probe.employment_income += MARGINAL_PROBE
    else:
        probe.self_employment_income += MARGINAL_PROBE
    probed = _compute_core(data, probe)
    delta_burden = (probed.total_income_tax + probed.employee_social_security) - (
        result.total_income_tax + result.employee_social_security
    )
    result.marginal_wedge = delta_burden / MARGINAL_PROBE
    return result
