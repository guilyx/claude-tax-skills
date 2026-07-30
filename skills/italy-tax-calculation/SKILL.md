---
name: italy-tax-calculation
description: Calculate Italian IRPEF, regional and municipal surcharges, INPS contributions and net salary, including the regime forfettario for freelancers and the impatriate regime for inbound workers. Use this whenever someone asks what they will take home in Italy, how a Milan, Rome, Turin or Bologna offer compares, what a partita IVA holder pays, whether the flat tax for new residents applies, or how the impatriate regime works — including when they only mention the Agenzia delle Entrate, a busta paga or a codice fiscale.
---

# Italian income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Italy.

## Run the engine

```bash
python -m taxcalc calc IT --employment 55000 --region LOM
python -m taxcalc calc IT --employment 90000 --region LAZ
python -m taxcalc info IT
```

## Three layers of income tax

IRPEF at 23/35/43% since the 2024 reform, plus a regional surcharge of 1.23% to
3.33% and a municipal surcharge up to 0.9%. Both local surcharges are based on
where you were resident on **1 January**, and the spread between Lombardy and
Lazio or Campania is close to two percentage points. Pass `--region`.

## The regime forfettario is the biggest single decision in Italian tax

A self-employed person with revenue up to 85,000 can elect a **15% substitute
tax** — 5% for the first five years — charged on a fixed percentage of revenue
(typically 78% for professionals), replacing IRPEF and both local surcharges
entirely. Real expenses are not deductible, and INPS contributions are.

For a consultant on 60,000 of revenue the difference against the ordinary regime
is enormous. Whenever someone describes freelancing in Italy, this is the
question worth answering first — before any calculation of the ordinary regime.

Conditions to check: no employment income above 30,000 in the prior year, no
control of a company in a related activity, and not predominantly invoicing a
current or recent employer.

## The impatriate regime was cut back in 2024

The version that applies depends on when you moved. The current regime exempts
**50%** of employment income up to 600,000 for five years, with conditions on
qualifying skills and a commitment to remain resident. The earlier version
exempted 70% (90% in the south) with much looser conditions.

Guidance describing 70% or 90% relief is not necessarily wrong — it may just be
about the old regime. Establish the date of the move before answering.

Separately, high-net-worth new residents can elect a **flat 200,000 per year**
substitute tax on all foreign income, which is the relevant option at very high
wealth.

## Residence changed in 2024

The test is now: registered in the population register, **or** domiciled in Italy
(where personal and family relationships are centred), **or** physically present,
for more than 183 days. The shift toward personal and family ties over formal
registration matters for people who deregistered but left family behind.

## What the engine leaves out

The regime forfettario, the impatriate regime, the true three-range formula for
the employment income credit, IMU property tax, and IVIE and IVAFE on foreign
property and financial assets.
