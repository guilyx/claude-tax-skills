"""Human-readable rendering of a :class:`~taxcalc.engine.ComputationResult`.

Skills read this output and quote the relevant parts back to the user, so the
format is optimised for being pasted: fixed column widths, one concept per line,
and every subtotal shown rather than implied.
"""

from __future__ import annotations

from typing import Any, Mapping

from .engine import ComputationResult

LABEL_WIDTH = 38
AMOUNT_WIDTH = 22
WIDTH = LABEL_WIDTH + AMOUNT_WIDTH + 2


def _line(label: str, amount: float, currency: str, note: str = "") -> str:
    text = f"{amount:,.2f} {currency}"
    row = f"  {label[:LABEL_WIDTH]:<{LABEL_WIDTH}}{text:>{AMOUNT_WIDTH}}"
    return f"{row}   ({note})" if note else row


def render_text(result: ComputationResult, data: Mapping[str, Any] | None = None) -> str:
    cur = result.currency
    out = [
        "=" * WIDTH,
        f"{result.country} - personal tax estimate, tax year {result.tax_year}",
        "=" * WIDTH,
        "",
        "INCOME",
        _line("Employment income", result.profile.employment_income, cur),
    ]
    if result.profile.self_employment_income:
        out.append(_line("Self-employment income", result.profile.self_employment_income, cur))
    if result.profile.other_income:
        out.append(_line("Other income", result.profile.other_income, cur))
    out.append(_line("Gross income", result.gross_income, cur))
    out.append("")

    if result.deductions:
        out.append("DEDUCTIONS AND ALLOWANCES")
        for item in result.deductions:
            out.append(_line(item.label, item.amount, cur, item.note))
        out.append(_line("Taxable income", result.taxable_income, cur))
        out.append("")

    if result.social_security_lines:
        out.append("SOCIAL SECURITY")
        for item in result.social_security_lines:
            out.append(_line(item.label, item.amount, cur))
        out.append(_line("Employee total", result.employee_social_security, cur))
        if result.employer_social_security:
            out.append(
                _line("Employer total (not withheld)", result.employer_social_security, cur)
            )
        out.append("")

    out.append("INCOME TAX")
    for item in result.tax_lines:
        out.append(_line(item.label, item.amount, cur, item.note))
    for item in result.credit_lines:
        out.append(_line(f"less {item.label}", -item.amount, cur))
    out.append(_line("Total income tax", result.total_income_tax, cur))
    out.append("")

    out.append("RESULT")
    out.append(_line("Total income tax", result.total_income_tax, cur))
    out.append(_line("Employee social security", result.employee_social_security, cur))
    out.append(_line("Total burden", result.total_burden, cur))
    out.append(_line("Net income (annual)", result.net_income, cur))
    out.append(_line("Net income (monthly)", result.net_income / 12, cur))
    out.append("")
    out.append(f"  {'Effective income tax rate':<{LABEL_WIDTH}}{result.effective_tax_rate:>{AMOUNT_WIDTH}.2%}")
    out.append(f"  {'Effective total burden':<{LABEL_WIDTH}}{result.effective_burden_rate:>{AMOUNT_WIDTH}.2%}")
    out.append(f"  {'Marginal rate on next 100':<{LABEL_WIDTH}}{result.marginal_wedge:>{AMOUNT_WIDTH}.2%}")

    if result.warnings:
        out.append("")
        out.append("NOTES AND LIMITATIONS")
        for warning in result.warnings:
            out.append(f"  - {warning}")

    if data and data.get("sources"):
        out.append("")
        out.append(f"  Verify against: {data['sources'][0].get('url', '')}")

    out.append("=" * WIDTH)
    out.append(
        "Estimate only, not tax advice. Confirm against the official source\n"
        "before filing or making a financial decision."
    )
    return "\n".join(out)


def render_markdown_table(result: ComputationResult) -> str:
    """Compact table for dropping into a written answer or report."""
    cur = result.currency
    rows = [
        ("Gross income", result.gross_income),
        ("Taxable income", result.taxable_income),
        ("National income tax", result.national_income_tax),
    ]
    if result.regional_income_tax:
        rows.append(("Regional / local income tax", result.regional_income_tax))
    if result.surcharges:
        rows.append(("Surcharges", result.surcharges))
    if result.credits_applied:
        rows.append(("Credits", -result.credits_applied))
    rows.extend(
        [
            ("Total income tax", result.total_income_tax),
            ("Employee social security", result.employee_social_security),
            ("Net income", result.net_income),
        ]
    )
    out = [f"| Item | Amount ({cur}) |", "| --- | ---: |"]
    out.extend(f"| {label} | {amount:,.2f} |" for label, amount in rows)
    out.append(f"| **Effective rate** | **{result.effective_burden_rate:.2%}** |")
    return "\n".join(out)
