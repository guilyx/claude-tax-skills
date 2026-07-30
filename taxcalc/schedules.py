"""Rate-schedule primitives.

A "schedule" turns an amount of taxable income into an amount of tax. Real tax
codes only use a few shapes, and all of them are represented here:

``progressive``            ordered brackets, each rate applied to the slice of
                           income falling inside that bracket
``flat``                   a single rate on the whole base
``piecewise_polynomial``   Germany-style continuous formula zones
``none``                   no tax at this layer (e.g. UAE personal income tax)

Keeping these separate from the country data means a bug fixed here is fixed
for every country at once.
"""

from __future__ import annotations

from typing import Any, Mapping, Sequence

INF = float("inf")


def _upper(bracket: Mapping[str, Any]) -> float:
    """Return the top of a bracket; ``null``/missing ``up_to`` means unbounded."""
    up_to = bracket.get("up_to")
    return INF if up_to is None else float(up_to)


def progressive_tax(taxable: float, brackets: Sequence[Mapping[str, Any]]) -> float:
    """Apply ordered marginal brackets to ``taxable``.

    Brackets are cumulative thresholds, not band widths: ``up_to`` is the income
    level at which the band ends. This is how published rate tables are written,
    so the JSON can be transcribed straight from an official source without
    intermediate arithmetic (and therefore without a chance to fat-finger it).
    """
    if taxable <= 0:
        return 0.0
    tax = 0.0
    lower = 0.0
    for bracket in brackets:
        upper = _upper(bracket)
        if taxable > lower:
            band = min(taxable, upper) - lower
            tax += band * float(bracket["rate"])
        lower = upper
        if taxable <= upper:
            break
    return tax


def marginal_rate(taxable: float, brackets: Sequence[Mapping[str, Any]]) -> float:
    """Rate that applies to the next unit of income."""
    lower = 0.0
    for bracket in brackets:
        upper = _upper(bracket)
        if taxable <= upper:
            return float(bracket["rate"])
        lower = upper
    return float(brackets[-1]["rate"]) if brackets else 0.0


def piecewise_polynomial_tax(taxable: float, zones: Sequence[Mapping[str, Any]]) -> float:
    """Evaluate a continuous formula schedule (the German EStG §32a shape).

    Each zone is ``tax = poly((x - offset) / divisor) + constant`` where ``poly``
    is given by ``coeffs`` in descending powers. A flat top zone is expressed as
    ``coeffs: [rate]`` with ``offset: 0, divisor: 1`` and a negative constant,
    so one evaluator covers both the curved and the linear parts.
    """
    if taxable <= 0:
        return 0.0
    for zone in zones:
        if taxable <= _upper(zone):
            offset = float(zone.get("offset", 0.0))
            divisor = float(zone.get("divisor", 1.0))
            y = (taxable - offset) / divisor
            value = 0.0
            for coeff in zone.get("coeffs", []):
                value = value * y + float(coeff)
            return value + float(zone.get("constant", 0.0))
    return 0.0


def apply_schedule(taxable: float, schedule: Mapping[str, Any]) -> float:
    """Dispatch to the right primitive based on ``schedule['type']``."""
    kind = schedule.get("type", "progressive")
    if kind == "none":
        return 0.0
    if kind == "flat":
        return max(0.0, taxable) * float(schedule["rate"])
    if kind == "progressive":
        return progressive_tax(taxable, schedule["brackets"])
    if kind == "piecewise_polynomial":
        return piecewise_polynomial_tax(taxable, schedule["zones"])
    raise ValueError(f"unknown schedule type: {kind!r}")


def schedule_marginal_rate(taxable: float, schedule: Mapping[str, Any]) -> float:
    """Marginal rate of any schedule type (numeric for formula schedules)."""
    kind = schedule.get("type", "progressive")
    if kind == "none":
        return 0.0
    if kind == "flat":
        return float(schedule["rate"])
    if kind == "progressive":
        return marginal_rate(taxable, schedule["brackets"])
    if kind == "piecewise_polynomial":
        step = 1.0
        base = piecewise_polynomial_tax(taxable, schedule["zones"])
        return (piecewise_polynomial_tax(taxable + step, schedule["zones"]) - base) / step
    raise ValueError(f"unknown schedule type: {kind!r}")


def contribution_amount(base: float, rule: Mapping[str, Any]) -> float:
    """Compute one social-security style contribution.

    Supports an annual ceiling (income above it is not charged), a floor (income
    below it is exempt), and a flat annual amount. Ceilings are the usual source
    of "why is my effective rate falling?" questions, so they are modelled
    explicitly rather than folded into an average rate.
    """
    if rule.get("type") == "fixed":
        return float(rule.get("amount", 0.0))
    charged = max(0.0, base)
    floor = rule.get("floor")
    if floor is not None:
        if charged <= float(floor):
            return 0.0
        if rule.get("floor_mode", "exempt_below") == "reduce_base":
            charged -= float(floor)
    ceiling = rule.get("ceiling")
    if ceiling is not None:
        charged = min(charged, float(ceiling))
    amount = charged * float(rule.get("rate", 0.0))
    cap = rule.get("max_amount")
    if cap is not None:
        amount = min(amount, float(cap))
    return amount
