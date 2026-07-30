---
name: france-tax-calculation
description: Calculate French income tax (impôt sur le revenu), CSG/CRDS social levies and cotisations to work out net salary from gross. Use this whenever someone asks about French take-home pay, salaire brut versus net, what they will earn in Paris, Lyon or Bordeaux, how the quotient familial and parts fiscales work for a couple or family, what a freelancer or micro-entrepreneur owes, how the prélèvement à la source rate is set, or whether a French offer is competitive — including when they only mention the fisc, URSSAF or impots.gouv.fr.
---

# French income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to France.

## Run the engine

```bash
python -m taxcalc calc FR --employment 60000
python -m taxcalc calc FR --employment 95000 --status married_joint --children 2
python -m taxcalc calc FR --self-employment 70000
python -m taxcalc info FR
```

## The household is the taxpayer, not the person

France taxes the **foyer fiscal**. Income is divided by the number of parts,
the scale is applied to that share, and the result is multiplied back up:

- 1 part single, 2 parts married or PACSed
- half a part per child for the first two, a full part from the third
- 1.5 parts for a single parent

This is why a French family's effective rate can be dramatically lower than a
single person's on identical income. The engine applies parts via
`--status` and `--children`. The benefit per half-part is capped at roughly
1,791, which the engine does not apply, so results for high-income households
with several children understate the tax slightly.

## Three different levies, and only one is income tax

Gross salary is reduced by cotisations sociales (pension, health, unemployment),
then CSG at 9.2% and CRDS at 0.5% on 98.25% of gross. Only 6.8 points of CSG are
deductible. Then income tax applies. When someone says "French tax is 45%" they
are usually conflating these; separating them is the most useful thing you can do.

CSG/CRDS are not always treated as creditable income taxes under treaties. For
US taxpayers this was litigated for years and the position has shifted — flag
it rather than asserting a conclusion.

## Withholding versus filing

Tax is withheld at source (prélèvement à la source), but the rate comes from the
return filed a year earlier. A big pay rise means under-withholding until the
rate updates — you can update it yourself in the impots.gouv.fr space, which is
worth mentioning to anyone whose income has just changed.

## Freelancers: the regime choice dominates everything

A micro-entrepreneur pays a flat percentage of *revenue* (about 22% social
contributions for services, plus optional versement libératoire of 2.2% income
tax) with no expense deduction, available up to 77,700 of revenue for services.
The régime réel deducts real expenses but carries much higher contributions
(~45%). Which is better depends almost entirely on the expense ratio. If someone
describes freelancing in France, this choice is the question worth answering.

## Other specifics

- **Flat tax (PFU)** of 30% on investment income — 12.8% tax plus 17.2% social
  levies — or elect the progressive scale for the whole household for the year.
- **Contribution exceptionnelle sur les hauts revenus**: 3% above 250,000 and 4%
  above 500,000 (doubled thresholds for couples). The engine applies this.
- **Frais réels**: the automatic 10% deduction is capped at 14,426; long commutes
  and professional costs can beat it.

## What the engine leaves out

The half-part cap, the décote for low tax amounts, and employer-specific
contribution rates. Treat the social security lines as a close approximation.
