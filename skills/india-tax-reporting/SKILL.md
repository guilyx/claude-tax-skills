---
name: india-tax-reporting
description: Handle Indian tax filing — which ITR form applies, the 31 July deadline, Form 16, Form 26AS and the Annual Information Statement, advance tax instalments, Schedule FA foreign asset reporting, and penalties. Use this whenever someone asks when the Indian tax return is due, which ITR to file, whether they must file at all, how to reconcile Form 26AS, how to report foreign assets or an ESOP, how to opt out of the new regime, or what happens if they file late.
---

# Indian tax reporting and filing — FY 2025-26 (AY 2026-27)

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to India.

## Get the calendar

```bash
python -m taxcalc deadlines IN
```

## Reconcile against AIS and 26AS before filing anything

The Annual Information Statement and Form 26AS show what the department already
knows: salary, tax deducted at source, interest, dividends, securities
transactions, property purchases, large cash deposits, foreign remittances.

Almost every notice issued to an ordinary taxpayer traces back to a mismatch
between the return and these statements. Downloading both and reconciling first
is the single most effective thing anyone can do. Where the AIS is wrong — it
often is, especially for joint accounts and sold-and-rebought securities — there
is a feedback mechanism to dispute the entry rather than silently ignoring it.

## Deadlines

| Date | What |
| --- | --- |
| 15 June 2026 | Employers issue Form 16 for FY 2025-26 |
| 31 July 2026 | Return for individuals not subject to audit |
| 31 October 2026 | Return where a tax audit applies |
| 31 December 2026 | Belated or revised return, with a late fee |
| 15 Jun / 15 Sep / 15 Dec / 15 Mar | Advance tax at 15%, 45%, 75%, 100% cumulative |

The 31 July deadline has been extended in several recent years, but planning
around an extension that has not been announced is unwise.

## Which ITR

- **ITR-1 (Sahaj)** — salary, one house property, other income, total up to ₹50 lakh
- **ITR-2** — capital gains, more than one property, **or any foreign asset**
- **ITR-3** — business or professional income
- **ITR-4 (Sugam)** — presumptive income under 44AD, 44ADA or 44AE

Holding any foreign asset — including unvested foreign ESOPs or a foreign bank
account — pushes you out of ITR-1 into ITR-2 regardless of income.

## Schedule FA and the Black Money Act

Every foreign asset, account and financial interest must be disclosed in
Schedule FA. The penalty under the Black Money Act is **₹10,00,000 per year**
for non-disclosure, regardless of the value of the asset or whether any income
arose.

This catches returning NRIs with dormant overseas accounts and employees with
foreign parent-company stock. It is the most disproportionate penalty in Indian
tax and it is being actively enforced — raise it whenever anything foreign is
mentioned.

## Opting out of the new regime

Form 10-IEA must be filed **before** the return, by the due date. Salaried
taxpayers can switch each year; taxpayers with business income can opt out once
and back once, and then are locked in. Missing the form means the new regime
applies whether or not it is better.

## Penalties

Late filing fee of ₹5,000 under section 234F, ₹1,000 where total income is
₹5,00,000 or less. Interest of 1% a month under 234A for late filing and 234B
and 234C for advance tax shortfalls. Underreporting penalties of 50% of the tax,
200% where misreported. The updated return (ITR-U) allows correction for
several years afterwards on payment of additional tax — a useful route for
someone who has realised an omission.
