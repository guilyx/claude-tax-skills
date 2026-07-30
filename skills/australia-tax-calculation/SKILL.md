---
name: australia-tax-calculation
description: Calculate Australian income tax, the Medicare levy and surcharge, superannuation and take-home pay. Use this whenever someone asks what they will take home on an Australian salary, how a Sydney, Melbourne, Brisbane or Perth offer compares, what their marginal rate is, whether they should get private health insurance to avoid the surcharge, how HECS/HELP repayments work, what a sole trader or ABN contractor owes, or how salary sacrificing into super changes things — including when they only mention the ATO or myGov.
---

# Australian income tax calculation — 2025-26 income year

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Australia.

## Run the engine

```bash
python -m taxcalc calc AU --employment 120000
python -m taxcalc calc AU --self-employment 95000
python -m taxcalc info AU
```

## The tax year ends 30 June

Not 31 December. Confirm which year the user means before quoting anything —
this is the most common confusion for anyone arriving from Europe or North
America, and it also means mid-year arrivals get a full year's tax-free
threshold against part-year income.

## The Medicare levy surcharge is a decision, not just a tax

Above roughly 101,000 (single) or 202,000 (family), someone without eligible
private hospital cover pays a surcharge of 1% to 1.5% of taxable income. A basic
hospital policy usually costs **less than the surcharge it avoids**. For someone
on 120,000 the surcharge is 1,200 a year against a policy costing perhaps 1,000.

The engine applies the surcharge by default. If the user has private hospital
cover, subtract it — and if they do not, tell them the arithmetic, because it is
one of the few places where buying something saves money outright.

## Superannuation is not a tax

The 12% employer superannuation guarantee (from 1 July 2025) is shown as an
employer cost. It is the employee's money, preserved until retirement. When
comparing an Australian package with an offer elsewhere, count it as deferred
compensation rather than as a deduction — and check whether the advertised
salary is "package including super" or "plus super", because the difference is
12%.

Salary sacrificing into super is taxed at 15% inside the fund against marginal
rates up to 47%, up to the 30,000 concessional cap. For anyone in the 37% or 45%
bracket this is the largest available lever.

## HECS/HELP

Student loan repayments are collected through the tax system at up to 10% of
repayment income, which adds back reportable fringe benefits and salary-sacrificed
super. The engine does not include them. For a graduate on 90,000 this is
several thousand dollars a year, so raise it whenever someone studied in
Australia.

## Foreign residents

No tax-free threshold and 30% from the first dollar, plus no Medicare levy.
Working holiday makers have their own scale. If someone is on a temporary visa,
establish residency status before computing anything — the difference at 60,000
of income is around 5,500.

## What the engine leaves out

HECS/HELP repayments, the Medicare levy phase-in range and family thresholds,
franking credits, the low income superannuation tax offset, and Division 293
tax on super contributions for those earning above 250,000.
