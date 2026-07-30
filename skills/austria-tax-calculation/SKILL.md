---
name: austria-tax-calculation
description: Calculate Austrian income tax, social insurance and net pay, including the favourable treatment of the 13th and 14th salaries. Use this whenever someone asks what they will take home in Austria, how a Vienna, Graz, Salzburg or Linz offer compares, why Austrian payslips show 14 payments, what the Familienbonus Plus is worth, what a Neue Selbständige pays, or whether an Austrian offer is competitive — including when they only mention the Finanzamt, FinanzOnline or a Lohnzettel.
---

# Austrian income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Austria.

## Run the engine

```bash
python -m taxcalc calc AT --employment 65000
python -m taxcalc calc AT --employment 95000 --children 2
python -m taxcalc info AT
```

## Fourteen salaries, and two of them are barely taxed

Austrian employment contracts almost always pay 14 monthly salaries — the
Urlaubsgeld in summer and Weihnachtsgeld at year end. Within the annual sixth
(Jahressechstel), these two are taxed at just **6%** instead of the marginal
rate.

This matters twice over:

1. **The engine does not apply it**, so its figure overstates tax for anyone on
   a 14-salary contract. Real annual take-home is meaningfully higher.
2. **Job offers are quoted differently.** An Austrian offer of "65,000" may mean
   14 × 4,643 while a German offer of "65,000" means 12 × 5,417. Comparing the
   annual figures is fine; comparing monthly figures is not.

Always ask whether the quoted salary is for 12 or 14 payments.

## The Familienbonus Plus is a credit, not an allowance

2,000 per child under 18 and 700 thereafter, deducted from tax rather than
income. Because it is a credit, it is worth exactly the same to a low earner and
a high earner — unusual, and the opposite of how child relief works in Germany.
It can be split between parents or claimed wholly by one, and the optimum
depends on whether both have enough tax to absorb it.

## Most people do not have to file, and most should anyway

The Arbeitnehmerveranlagung (employee assessment) is voluntary in most cases and
can be filed for **five prior years**. It reliably produces a refund for anyone
who worked part of a year, changed jobs, has commuting costs, or paid for
professional training. Someone who has never filed can often claim five years at
once.

## Other specifics

- **Pendlerpauschale**: a commuting allowance that is generous where public
  transport is unreasonable, claimed through payroll or the annual assessment.
- **No wealth tax and no inheritance tax**, which is unusual for a high-tax
  European country and materially changes long-term planning.
- **Capital income** is taxed separately at 27.5% (25% on bank interest), not at
  scale rates.
- **Neue Selbständige** pay SVS contributions of roughly 27%, with a mandatory
  minimum base that hits low-income years hard.

## What the engine leaves out

The 6% rate on the 13th and 14th salaries, church contribution relief (up to
600), the Pendlerpauschale, and the split of blue- and white-collar contribution
rates.
