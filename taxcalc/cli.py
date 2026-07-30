"""Command line interface.

    python -m taxcalc list
    python -m taxcalc calc DE --employment 85000 --status married_joint
    python -m taxcalc calc FR --employment 60000 --children 2 --json
    python -m taxcalc compare 90000 --countries US,GB,DE,SG
    python -m taxcalc info PT
    python -m taxcalc deadlines JP
    python -m taxcalc validate

Skills call this instead of doing arithmetic in prose. A wrong number in a tax
answer is worse than no answer, and the same input should always give the same
output no matter who asks.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict, List

from .engine import Profile, compute
from .loader import CountryNotFound, available_countries, load_country
from .report import render_markdown_table, render_text
from .validate import count_files, summarise, validate_all


def _profile_from_args(args: argparse.Namespace) -> Profile:
    return Profile(
        employment_income=args.employment,
        self_employment_income=args.self_employment,
        other_income=args.other_income,
        filing_status=args.status,
        region=args.region,
        children=args.children,
        dependants=args.dependants,
        deductions=args.deductions,
        credits=args.credits,
        local_rate=args.local_rate,
    )


def cmd_list(args: argparse.Namespace) -> int:
    countries = available_countries()
    if args.json:
        print(json.dumps(countries, indent=2))
        return 0
    print(f"{'ISO':<5}{'Country':<26}{'Currency':<10}{'Tax year':<10}")
    print("-" * 51)
    for country in countries:
        print(
            f"{country['iso2']:<5}{country['country']:<26}"
            f"{country['currency']:<10}{country['tax_year']:<10}"
        )
    print(f"\n{len(countries)} countries available.")
    return 0


def cmd_calc(args: argparse.Namespace) -> int:
    data = load_country(args.country)
    result = compute(data, _profile_from_args(args))
    if args.json:
        print(json.dumps(result.as_dict(), indent=2))
    elif args.markdown:
        print(render_markdown_table(result))
    else:
        print(render_text(result, data))
    return 0


def cmd_compare(args: argparse.Namespace) -> int:
    codes = (
        [code.strip() for code in args.countries.split(",") if code.strip()]
        if args.countries
        else [country["iso2"] for country in available_countries()]
    )
    rows: List[Dict[str, Any]] = []
    for code in codes:
        try:
            data = load_country(code)
        except CountryNotFound as exc:
            print(f"warning: {exc}", file=sys.stderr)
            continue
        profile = Profile(
            employment_income=args.income,
            filing_status=args.status,
            children=args.children,
            region=args.region,
        )
        result = compute(data, profile)
        rows.append(
            {
                "iso2": result.iso2,
                "country": result.country,
                "currency": result.currency,
                "income_tax": result.total_income_tax,
                "employee_social_security": result.employee_social_security,
                "total_burden": result.total_burden,
                "net_income": result.net_income,
                "effective_burden_rate": result.effective_burden_rate,
                "marginal_wedge": result.marginal_wedge,
            }
        )
    rows.sort(key=lambda row: row["effective_burden_rate"])

    if args.json:
        print(json.dumps(rows, indent=2))
        return 0

    print(
        f"Gross employment income {args.income:,.0f} (local currency units), "
        f"status={args.status}, children={args.children}"
    )
    print(
        "Amounts are in each country's own currency - no FX conversion is applied, "
        "so compare rates rather than absolute amounts.\n"
    )
    header = f"{'ISO':<5}{'Country':<24}{'Income tax':>14}{'Social sec':>13}{'Net':>14}{'Burden':>9}{'Marginal':>10}"
    print(header)
    print("-" * len(header))
    for row in rows:
        print(
            f"{row['iso2']:<5}{row['country'][:23]:<24}"
            f"{row['income_tax']:>14,.0f}{row['employee_social_security']:>13,.0f}"
            f"{row['net_income']:>14,.0f}{row['effective_burden_rate']:>8.1%}"
            f"{row['marginal_wedge']:>10.1%}"
        )
    return 0


def cmd_info(args: argparse.Namespace) -> int:
    data = load_country(args.country)
    if args.json:
        print(json.dumps(data, indent=2))
        return 0
    print(f"{data['country']} ({data['iso2']}) - tax year {data['tax_year']}, currency {data['currency']}")
    residency = data.get("residency", {})
    if residency:
        print("\nRESIDENCE")
        for key, value in residency.items():
            print(f"  {key}: {value}")
    print("\nHEADLINE FIGURES")
    for key, value in (data.get("headline") or {}).items():
        print(f"  {key}: {value}")
    quirks = data.get("quirks") or []
    if quirks:
        print("\nTHINGS THAT CATCH PEOPLE OUT")
        for quirk in quirks:
            print(f"  - {quirk}")
    print("\nSOURCES")
    for source in data.get("sources", []):
        print(f"  {source.get('name', 'source')}: {source.get('url', '')}")
    return 0


def cmd_deadlines(args: argparse.Namespace) -> int:
    data = load_country(args.country)
    reporting = data.get("reporting", {})
    if args.json:
        print(json.dumps(reporting, indent=2))
        return 0
    print(f"{data['country']} - filing calendar for tax year {data['tax_year']}")
    print(f"  Tax year ends: {reporting.get('tax_year_end')}")
    print(f"  Authority:     {reporting.get('authority')}")
    if reporting.get("portal"):
        print(f"  Portal:        {reporting['portal']}")
    print("\nDEADLINES")
    for deadline in reporting.get("deadlines", []):
        print(f"  {deadline.get('date', '?'):<22} {deadline.get('what', '')}")
        if deadline.get("note"):
            print(f"  {'':<22} ({deadline['note']})")
    forms = reporting.get("forms", [])
    if forms:
        print("\nFORMS")
        for form in forms:
            print(f"  {form.get('id', ''):<16} {form.get('name', '')}")
    penalties = reporting.get("penalties")
    if penalties:
        print("\nPENALTIES")
        for key, value in penalties.items():
            print(f"  {key}: {value}")
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    findings = validate_all()
    print(summarise(findings, count_files()))
    return 1 if findings else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="taxcalc",
        description="Personal income tax estimates across 30 countries.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="list available countries")
    p_list.add_argument("--json", action="store_true")
    p_list.set_defaults(func=cmd_list)

    p_calc = sub.add_parser("calc", help="compute tax for one country")
    p_calc.add_argument("country", help="ISO2 code, e.g. DE")
    p_calc.add_argument("--employment", type=float, default=0.0, help="gross employment income")
    p_calc.add_argument("--self-employment", type=float, default=0.0, dest="self_employment")
    p_calc.add_argument("--other-income", type=float, default=0.0, dest="other_income")
    p_calc.add_argument("--status", default="single", help="filing status, e.g. married_joint")
    p_calc.add_argument("--region", default=None, help="state/province/canton/municipality code")
    p_calc.add_argument("--children", type=int, default=0)
    p_calc.add_argument("--dependants", type=int, default=0)
    p_calc.add_argument("--deductions", type=float, default=0.0, help="extra deductible amounts")
    p_calc.add_argument("--credits", type=float, default=0.0, help="extra non-refundable credits")
    p_calc.add_argument("--local-rate", type=float, default=None, dest="local_rate")
    p_calc.add_argument("--json", action="store_true")
    p_calc.add_argument("--markdown", action="store_true")
    p_calc.set_defaults(func=cmd_calc)

    p_cmp = sub.add_parser("compare", help="same income across several countries")
    p_cmp.add_argument("income", type=float)
    p_cmp.add_argument("--countries", default=None, help="comma-separated ISO2 codes")
    p_cmp.add_argument("--status", default="single")
    p_cmp.add_argument("--children", type=int, default=0)
    p_cmp.add_argument("--region", default=None)
    p_cmp.add_argument("--json", action="store_true")
    p_cmp.set_defaults(func=cmd_compare)

    p_info = sub.add_parser("info", help="residence rules, headline rates, known traps")
    p_info.add_argument("country")
    p_info.add_argument("--json", action="store_true")
    p_info.set_defaults(func=cmd_info)

    p_dead = sub.add_parser("deadlines", help="filing calendar, forms and penalties")
    p_dead.add_argument("country")
    p_dead.add_argument("--json", action="store_true")
    p_dead.set_defaults(func=cmd_deadlines)

    p_val = sub.add_parser("validate", help="structural check of all country data files")
    p_val.set_defaults(func=cmd_validate)

    return parser


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except CountryNotFound as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
