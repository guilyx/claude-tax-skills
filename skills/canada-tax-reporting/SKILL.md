---
name: canada-tax-reporting
description: Handle Canadian tax filing — T1 deadlines, the slips and schedules required, T1135 foreign property reporting, RRSP deadlines, instalments, and CRA penalties. Use this whenever someone asks when Canadian taxes are due, what forms or slips they need, whether they must file with no income, how to report foreign property or income, what happens if they file late, how Quebec filing differs, or how to claim benefits like the Canada Child Benefit or GST credit.
---

# Canadian tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Canada.

## Get the calendar

```bash
python -m taxcalc deadlines CA
```

## File even with no income

Benefits are delivered through the tax system and are only paid to people who
file: the Canada Child Benefit, the GST/HST credit, provincial credits and the
Canada Workers Benefit all require a return. A student or a stay-at-home parent
with zero income should still file. This is the most commonly missed piece of
practical Canadian tax advice.

## Deadlines

| Date | What |
| --- | --- |
| 2 March 2026 | RRSP contribution deadline for the 2025 tax year |
| 30 April 2026 | T1 filing and payment for 2025 |
| 15 June 2026 | Filing deadline if you or your spouse are self-employed |
| 15 Mar / Jun / Sep / Dec | Instalments where required |

The self-employed extension is a trap: the **filing** deadline moves to 15 June
but the **payment** deadline stays at 30 April. Interest runs on anything unpaid
from 1 May. Always state both dates together.

## T1135: separately penalised, frequently missed

Anyone whose foreign property cost more than 100,000 CAD at any time in the year
must file form T1135. This includes foreign bank accounts, foreign shares held
in a non-registered account, and foreign rental property. It excludes personal
use property and anything in an RRSP or TFSA.

The penalty is 25 per day, minimum 100 and maximum 2,500 — charged even when no
tax is owed and the income was fully reported. Raise it whenever someone
mentions assets outside Canada.

## Slips

Most slips are visible in CRA My Account and auto-fill into certified software,
which is the easiest way to avoid missing one. T4 employment, T4A other income,
T5 investment income, T3 trust income, T2202 tuition, plus RRSP receipts. Note
that slips issued late — especially T3s in late March — are a common cause of
having to amend a return filed early.

## Quebec

Two returns: the federal T1 to CRA and the TP-1 to Revenu Québec, with
different forms and separate payments, though the deadlines align.

## Penalties

5% of the balance owing plus 1% per month up to 12 months; 10% plus 2% per month
up to 20 months for a repeat offence within three years. Interest compounds
daily at the prescribed rate. The Voluntary Disclosures Program can relieve
penalties and part of the interest for someone coming forward before the CRA
contacts them — worth raising for anyone with unfiled years.
