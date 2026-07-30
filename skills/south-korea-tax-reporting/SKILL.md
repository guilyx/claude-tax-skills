---
name: south-korea-tax-reporting
description: Handle Korean tax filing — the February year-end settlement, the May global income tax return, Hometax, overseas financial account reporting, and NTS penalties. Use this whenever someone asks when Korean taxes are due, whether they need to file in May, what yeonmal jeongsan requires, how to use Hometax, how to report foreign accounts or income, how to elect the foreign flat tax, or what happens if they file late.
---

# Korean tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to South Korea.

## Get the calendar

```bash
python -m taxcalc deadlines KR
```

## Two events, and most people only have the first

| Date | What |
| --- | --- |
| February 2026 | Year-end settlement with the employer for 2025 |
| 1–31 May 2026 | Global income tax return for 2025 |
| 30 June 2026 | Extended deadline where an external audit applies |
| 31 May 2026 | Payment; instalments available above 10m KRW |
| Two months from disposal | Preliminary capital gains return on property |

An employee with a single employer completes the February settlement and files
nothing in May. A May return is required for business income, two or more
employers, other income above thresholds, or foreign income.

## The February settlement is a documentation exercise

Hometax's **simplified year-end settlement service** opens in mid-January and
provides most deduction data pre-collected. What you do is download it, add
anything missing, and submit to the employer.

For foreign residents the commonly missing items are housing-related — the
monthly rent tax credit requires the lease contract and proof of payment, and it
is not in the simplified data. Getting a receipt for cash rent from a landlord
after the fact is difficult, so the practical advice is to pay rent by bank
transfer from the start.

## Overseas financial account reporting

Residents whose overseas financial accounts exceeded **500,000,000 KRW** on any
month-end during the year must report them in June. The penalty is up to 20% of
the unreported balance, and it applies regardless of whether any income arose.

The threshold is high enough that most people are unaffected and low enough that
anyone with a foreign property sale, an inheritance or accumulated savings
abroad should check. Note the test is any single month-end, not the year-end
balance.

## Electing the flat tax

The 19% flat rate for foreign employees is elected through the employer at the
year-end settlement, or on the May return. It can be chosen or not chosen each
year, so it is worth recomputing annually rather than settling on it once.

## Access

Hometax needs a joint certificate or simple authentication, both of which
require a Korean phone number and either a resident registration number or alien
registration number. Set this up before February rather than during it.

## Penalties

Late filing: 20% of the tax due, or 40% where deliberate. Understatement: 10%,
rising to 40% for fraudulent reporting. Late payment: 0.022% per day, roughly 8%
a year. Voluntary amendment before the NTS acts reduces the underreporting
penalty substantially, on a sliding scale by how soon it is filed.
