---
name: poland-tax-reporting
description: Handle Polish tax filing — Twój e-PIT, the 30 April deadline, which PIT form applies, monthly advances for the self-employed, czynny żal voluntary disclosure, and penalties. Use this whenever someone asks when the Polish tax return is due, which PIT form they need, how Twój e-PIT works, how to report capital gains or crypto, how to declare foreign income, or what happens if they file late.
---

# Polish tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Poland.

## Get the calendar

```bash
python -m taxcalc deadlines PL
```

## Twój e-PIT accepts itself

The pre-filled return appears on 15 February and, for employees, is **accepted
automatically at the deadline** if not touched. That is convenient, but it uses
only the data the tax office holds — it will not include reliefs you have to
claim, deductible IKZE pension contributions, or joint filing with a spouse
unless you elect it.

| Date | What |
| --- | --- |
| 15 February 2026 | Twój e-PIT opens for 2025 |
| 28 February 2026 | Employers issue PIT-11 |
| 30 April 2026 | Filing and payment deadline for PIT-36, PIT-37 and PIT-38 |
| 31 January 2026 | PIT-28 for lump-sum (ryczałt) taxpayers |
| 20th of each month | Advance income tax for the self-employed |

Note that PIT-28 is due in **January**, three months before everything else.
Ryczałt taxpayers miss this regularly.

## Which form

- **PIT-37** — employees and others whose income went through a withholding agent
- **PIT-36** — business income taxed on the scale, and foreign income
- **PIT-36L** — business income under the 19% flat tax
- **PIT-38** — securities, crypto and other capital gains
- **PIT-28** — lump sum on registered revenue

Capital gains are **not** withheld at source in Poland. Brokers issue a PIT-8C
but deduct nothing, so anyone who sold shares or crypto has a self-assessed
liability due 30 April that they may not be expecting. Crypto losses can only be
carried against crypto income.

## Czynny żal

Poland's active regret procedure lets you disclose a failure — a late filing, an
unreported source — before the authorities detect it, and it generally avoids
fiscal penal liability entirely. It must be filed voluntarily and before
detection, and the outstanding tax must be paid.

For anyone who has realised they missed something, this is the answer. It is
routine, it works, and it is much cheaper than waiting.

## Foreign income

Poland applies either exemption with progression or proportional credit
depending on the treaty, and the abolition relief (ulga abolicyjna) that used to
neutralise the difference is now capped. Anyone with foreign employment income
should file PIT-36 with the ZG annex rather than assuming a treaty exemption
means nothing to report.

## Penalties

Late filing is a fiscal offence, with fines set in daily rates tied to the
minimum wage. Late payment carries statutory interest of roughly 14.5% a year.
Czynny żal is the standard route out of the penalty, though not the interest.
