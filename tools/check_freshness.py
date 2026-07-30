"""Report country files whose tax year has fallen behind.

Stale rates are this repository's real failure mode. Nothing breaks when a
threshold is a year out of date - the engine keeps returning confident,
well-formatted, wrong numbers. This script makes that visible on a schedule
rather than waiting for someone to notice.

    python tools/check_freshness.py               # report, exit 0
    python tools/check_freshness.py --max-age 1   # exit 1 if anything is older

`--max-age` is the number of years a file may lag the current calendar year.
The default of 1 reflects reality: for most of 2026, tax year 2025 is the
correct and current year to model, because that is the year being filed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "countries"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--max-age",
        type=int,
        default=1,
        help="how many years a country file may lag the current year (default: 1)",
    )
    parser.add_argument(
        "--year",
        type=int,
        default=dt.date.today().year,
        help="treat this as the current year (for testing)",
    )
    args = parser.parse_args(argv)

    stale: list[tuple[str, int]] = []
    current: list[tuple[str, int]] = []

    for path in sorted(DATA_DIR.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        age = args.year - int(payload["tax_year"])
        entry = (payload["country"], payload["tax_year"])
        (stale if age > args.max_age else current).append(entry)

    print(f"Current year: {args.year}; allowed lag: {args.max_age} year(s)\n")
    print(f"{len(current)} country file(s) within the allowed lag.")

    if not stale:
        print("\nNothing is stale.")
        return 0

    print(f"\n{len(stale)} country file(s) need updating:\n")
    for country, year in stale:
        print(f"  {country:<24} tax year {year}")
    print(
        "\nUpdate the rates, thresholds and reporting.deadlines from the URLs in\n"
        "each file's `sources`, then bump `tax_year`. See CONTRIBUTING.md."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
