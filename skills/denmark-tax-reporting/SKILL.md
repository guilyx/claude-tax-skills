---
name: denmark-tax-reporting
description: Handle Danish tax filing — the automatic årsopgørelse, the 1 May correction deadline, what SKAT does not know about, the forskudsopgørelse, and penalties. Use this whenever someone asks when the Danish tax return is due, whether they need to file at all, how to correct the annual statement, how to report foreign income or property, how to get a CPR number and MitID, or what happens if they get it wrong.
---

# Danish tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Denmark.

## Get the calendar

```bash
python -m taxcalc deadlines DK
```

## There is no return to file, only a statement to check

The årsopgørelse is generated automatically in mid-March from data SKAT already
holds. Most people have nothing to do. The obligation is to **correct** it where
it is wrong.

| Date | What |
| --- | --- |
| Mid-March 2026 | Årsopgørelse for 2025 available in TastSelv |
| 1 May 2026 | Correction deadline for most individuals |
| 1 July 2026 | Deadline where there is foreign income or self-employment |
| November 2025 | Forskudsopgørelse for the following year published |
| 1 July 2026 | Residual tax paid by here carries a lower interest surcharge |

## What SKAT does not know

The statement is accurate for Danish salary, Danish bank interest, Danish
mortgage interest and Danish share income. It knows nothing about:

- **Foreign income, foreign pensions and foreign property** — including property
  you own abroad, which affects Danish property value tax
- **Foreign shares and accounts**, including holdings with non-Danish brokers
- **Commuting distance** (befordringsfradrag), which is generous over long
  distances and must be entered
- **Union fees and A-kasse contributions**, which are usually reported but worth
  verifying

Anyone who moved to Denmark or has any connection abroad needs to actively
correct the statement. Simply accepting it is how people end up with an
under-declaration they did not intend.

## The interest asymmetry on residual tax

Underpaid tax carries a non-deductible surcharge, and it is **higher after 1
July**. Paying voluntarily before that date costs materially less. Anyone who
knows they owe should be told to pay early rather than wait for the demand.

## Getting set up

CPR number then MitID. Without both, nothing in Danish public administration is
accessible. Foreign workers need to register with International Citizen Service
on arrival; the sequence takes time and blocks bank accounts and salary payment.

## Penalties

An estimated assessment (taksation) plus a fee of about 200 where information is
not provided. Penalties from one to two times the evaded tax for
under-reporting, with criminal liability above thresholds. SKAT distinguishes
sharply between errors corrected voluntarily and those it discovers.
