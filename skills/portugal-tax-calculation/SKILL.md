---
name: portugal-tax-calculation
description: Calculate Portuguese IRS, social security and net income, including IRS Jovem for young workers and the IFICI regime that replaced NHR. Use this whenever someone asks what they will take home in Portugal, how a Lisbon or Porto offer compares, whether the non-habitual resident regime still exists, what the D7 or digital nomad visa means for tax, what a recibos verdes freelancer pays, or how Portugal taxes foreign pensions and remote income — including when they only mention Finanças, a NIF or the Portal das Finanças.
---

# Portuguese income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Portugal.

## Run the engine

```bash
python -m taxcalc calc PT --employment 45000
python -m taxcalc calc PT --employment 80000 --status married_joint --children 1
python -m taxcalc info PT
```

## NHR is closed. Be precise about what replaced it

The non-habitual resident regime is **closed to new arrivals**. Its replacement,
IFICI, is much narrower: a 20% flat rate on Portuguese employment income from a
qualifying highly skilled activity, plus exemption on most foreign income, for
ten years — but only for people in scientific research, innovation, qualifying
startups and specified industrial roles.

The practical consequence: **retirees and ordinary remote workers no longer
qualify for anything special.** A great deal of guidance still online assumes
NHR is available, and people are making relocation decisions on it. Correcting
this is often the most valuable thing in the answer.

Nine bands reaching 48%, plus a solidarity surcharge above 80,000, make ordinary
Portuguese tax comparatively heavy — the country's reputation for low tax came
almost entirely from NHR.

## IRS Jovem is generous and widely missed

Workers up to 35 in the first ten years of employment income get a large
exemption that tapers over the period, starting at 100% of employment income up
to a ceiling in year one. For a young professional this is worth far more than
most planning. Ask about age whenever the person could plausibly qualify.

## Deductions depend on what you did during the year

Health, education, housing and general family expenses only generate deductions
if the invoice was issued with your **NIF at the point of sale** and validated
in the e-fatura system. This cannot be reconstructed in April. Anyone living in
Portugal should be told to give their NIF for every purchase and to check
e-fatura before the late-February validation deadline.

## Married couples choose each year

Joint or separate taxation is elected annually. Joint filing divides income by
two before applying the scale, so it helps when incomes are very unequal and
does nothing when they are similar. Model both with and without
`--status married_joint`.

## Freelancers

The simplified regime taxes a fixed percentage of revenue (75% for most
professional services) with no need to document expenses, available below
200,000 of revenue. Social security is 21.4% charged on 70% of services income —
roughly 15% effective — and is recalculated quarterly from declared income
rather than annually.

## What the engine leaves out

IRS Jovem, IFICI, e-fatura expense deductions, and the reduced rates for Madeira
and the Azores.
