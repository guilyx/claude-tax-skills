---
name: switzerland-tax-calculation
description: Calculate Swiss federal, cantonal and communal income tax, AHV and pension contributions, and net salary. Use this whenever someone asks what they will take home in Switzerland, how Zurich, Geneva, Zug, Basel, Lausanne or Lucerne compare, why Swiss tax varies so much by location, what Quellensteuer means on their payslip, how pillar 2 and 3a contributions reduce their tax, or whether a Swiss offer is as good as it looks — including when they only mention a canton or commune by name.
---

# Swiss income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Switzerland.

## Run the engine

```bash
python -m taxcalc calc CH --employment 140000 --region ZH
python -m taxcalc calc CH --employment 140000 --region ZG   # compare cantons
python -m taxcalc calc CH --employment 180000 --status married_joint --region GE
python -m taxcalc info CH
```

## Location dominates the answer

Tax is levied at three levels — federal, cantonal and communal — and the federal
part is the smallest. The same 140,000 salary can differ by more than 10,000
francs a year between Zug and Geneva, and by thousands between communes inside
the same canton.

**Always ask which canton and, ideally, which commune.** An answer that does not
name a location is not a Swiss tax answer. The cantonal rates in the data are
single approximate effective rates; for anything consequential, direct the user
to the official federal calculator at swisstaxcalculator.estv.admin.ch, which
handles real cantonal schedules and communal multipliers.

## Quellensteuer: most foreigners are taxed at source

Foreign nationals without a C permit have tax withheld through payroll at a
cantonal tariff. Two things follow:

- Above roughly 120,000 of income you are required to file an ordinary return
  anyway, and the withholding becomes a payment on account.
- Below that threshold you can **request** an ordinary assessment, which is
  worthwhile if you have significant deductions — pillar 3a, pillar 2 buy-ins,
  childcare, or a long commute. The request has a deadline of 31 March following
  the tax year and cannot be made late.

Raise this with anyone on a B permit. It is frequently money left on the table.

## Pillar 2 buy-ins are the largest available lever

Voluntary purchases into the occupational pension are **fully deductible** from
taxable income, with no annual cap beyond your accumulated gap. For a high
earner in a high-tax canton this is the single most effective planning move
available, and the buy-in capacity is stated on the annual pension certificate.
Pillar 3a is smaller but simpler — 7,258 for employees in 2025.

## Wealth tax is real

Cantons tax worldwide net assets annually, typically 0.1% to 1%. It is not in
the engine. For someone with substantial savings this can exceed their income
tax, and it is the main reason the "low tax Switzerland" picture is incomplete.
On the other side, **private capital gains on securities are entirely tax free**,
which is unusually generous.

## What the engine leaves out

Real cantonal and communal rate schedules (approximated by a flat rate), wealth
tax, church tax, the true married-couple federal scale, and the age-banding of
BVG contributions from 7% up to 18%.
