---
name: austria-tax-reporting
description: Handle Austrian tax filing — when a return is mandatory versus voluntary, the April and June deadlines, FinanzOnline, forms E1 and L1, the five-year window for employee assessments, and Finanzamt penalties. Use this whenever someone asks when the Austrian tax return is due, whether they need to file, how to claim a refund for earlier years, what an Arbeitnehmerveranlagung is, how to register for FinanzOnline, or what happens if they file late.
---

# Austrian tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Austria.

## Get the calendar

```bash
python -m taxcalc deadlines AT
```

## Mandatory or voluntary

Filing is **mandatory** where:

- Self-employment or other non-payroll income exceeds 730 and total income
  exceeds 12,816
- Two or more employments ran simultaneously during the year
- Certain allowances (Freibetragsbescheid, Alleinverdienerabsetzbetrag,
  Pendlerpauschale) were applied in payroll and the conditions were not met for
  the full year

Otherwise it is **voluntary**, and the voluntary route — the
Arbeitnehmerveranlagung — is open for **five years**. Someone in 2026 can still
file for 2021 through 2025.

There is also an automatic assessment (antragslose Arbeitnehmerveranlagung): if
you have not filed by mid-year and the Finanzamt's data shows a refund is due, it
issues one unprompted. That is convenient but only uses data it already holds —
it never includes deductions you would have had to claim.

## Deadlines

| Date | What |
| --- | --- |
| 30 April 2026 | Paper return for 2025 |
| 30 June 2026 | FinanzOnline electronic return for 2025 |
| 31 March 2027 | If represented by a Steuerberater |
| 31 December 2030 | Last date for a voluntary assessment for 2025 |

## Forms

E1 is the full income tax return; L1 is the employee assessment, with L1k for
child-related items including the Familienbonus Plus and L1i for international
circumstances. E1a covers business income. Run `python -m taxcalc deadlines AT`
for the list.

Employers transmit the Lohnzettel (L16) electronically, so employment data is
already with the Finanzamt — most voluntary filings are a matter of adding
deductions to figures that are already there.

## What is worth claiming

Work equipment and professional literature, further education and retraining,
commuting beyond the standard allowance, double household costs during a
relocation, church contributions up to 600, donations to registered
organisations, childcare, and extraordinary burdens such as medical costs and
disability-related expenses.

## Penalties

Verspätungszuschlag of up to 10% of assessed tax for late filing;
Säumniszuschlag of 2% for late payment with further 1% charges at three and six
months; Anspruchszinsen from 1 October of the following year. Note that a
voluntary assessment carries **no late penalty at all**, because there was no
obligation to file — worth saying to anyone anxious about filing five years at once.
