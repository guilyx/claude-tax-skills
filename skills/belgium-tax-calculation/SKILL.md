---
name: belgium-tax-calculation
description: Calculate Belgian personal income tax, municipal surcharges, ONSS social security and net pay. Use this whenever someone asks what they will take home in Belgium, how a Brussels, Antwerp, Ghent or Leuven offer compares, why Belgian tax is so high, how company cars and meal vouchers change the package, what an indépendant pays, or whether the expat regime applies to them — including when they only mention the SPF Finances, Tax-on-web or a fiche 281.10.
---

# Belgian income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Belgium.

## Run the engine

```bash
python -m taxcalc calc BE --employment 70000
python -m taxcalc calc BE --employment 55000 --children 2
python -m taxcalc calc BE --self-employment 80000
python -m taxcalc info BE
```

## Belgium reaches its top rate at a strikingly low income

The 50% bracket starts below 50,000 of taxable income, and social security has
**no ceiling**. The combined marginal wedge therefore hits its maximum early and
stays there, which is why Belgian gross-to-net ratios look worse than
neighbouring countries at every level above modest salaries.

Add the municipal surcharge — 7% to 9% *of the tax*, based on where you were
registered on 1 January — and the effective rate on a normal professional salary
approaches 45%.

## Which is why the package matters more than the salary

Because cash is taxed so heavily, Belgian employers structure compensation
around benefits that are not:

- **Company car** with a favourable benefit-in-kind valuation, plus a fuel card
- **Meal vouchers** (up to 8 per working day, largely untaxed)
- **Eco-cheques**, mobile phone and internet allowances
- **Group insurance** (occupational pension) taxed lightly on payout
- **Warrant or bonus plans** structured to avoid social security

When someone compares a Belgian offer with one elsewhere, comparing gross
salaries alone will mislead them badly. Ask what is in the package.

## The BIRTI inbound regime

The special tax regime for inbound taxpayers allows up to **30% of gross
remuneration, capped at 90,000**, to be paid as a tax-free and
social-security-free reimbursement of costs proper to the employer. There are
conditions — a minimum gross salary of 75,000, recruitment from abroad, and not
having been Belgian tax resident recently — and it runs for five years,
extendable to eight.

The engine does not apply it. If it applies, reduce gross by the exempt portion
before calculating.

## Couples

Married and legally cohabiting partners file jointly. The **marital quotient**
transfers up to 30% of the higher earner's professional income (capped) to a
spouse with little or no income, which is a real saving in single-income
households. Not modelled by the engine.

## What the engine leaves out

The marital quotient, the detailed child allowance scale (which rises steeply
with each child), the BIRTI regime, and benefit-in-kind valuations. The
municipal surcharge is set to a typical 7.5% — substitute the actual commune rate.
