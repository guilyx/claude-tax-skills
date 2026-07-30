---
name: singapore-tax-calculation
description: Calculate Singapore income tax, CPF contributions and take-home pay, distinguishing citizens and PRs from foreigners on work passes. Use this whenever someone asks what they will take home in Singapore, how a Singapore offer compares with Hong Kong, London or the US, what CPF costs them, whether foreign income is taxed, what an Employment Pass holder pays, how the two-year concession works, or how a Singapore package compares — including when they only mention IRAS or a Year of Assessment.
---

# Singapore income tax calculation — Year of Assessment 2026 (2025 income)

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Singapore.

## Run the engine

```bash
python -m taxcalc calc SG --employment 180000
python -m taxcalc info SG
```

## CPF is the first question, and it changes everything

The engine applies CPF at the full 20% employee rate. That is correct for
**citizens and permanent residents** and wrong for **foreigners on Employment or
S Passes, who contribute nothing**.

For an EP holder, either set employment income and ignore the CPF line, or note
that the "total burden" figure overstates their position substantially. A
citizen and a foreigner on the same 180,000 salary have very different take-home
pay, and comparing them without saying which is which is misleading.

CPF is also not a tax — it is the employee's own money in a retirement, housing
and medical account. In international comparisons it belongs with pension
contributions, not with income tax.

## Foreign income is generally not taxed

Singapore taxes income accrued in or derived from Singapore. **Foreign-sourced
income received by individuals is generally exempt**, and there is no capital
gains tax.

Combined, these are what actually make Singapore attractive — not the headline
rates, which are unremarkable in the middle brackets and reach 24% at the top.
Someone comparing headline rates with Hong Kong or Dubai is looking at the wrong
number.

## The two-year administrative concession

A stay spanning two calendar years totalling at least 183 days can be treated as
tax resident for both years. This matters enormously for someone arriving late in
a year: without it, they are a non-resident taxed at a flat 15% on employment
income with no reliefs; with it, they get resident rates and reliefs.

A three-year concession applies to stays spanning three calendar years. Anyone
arriving in the second half of a year should know which applies.

## Reliefs are capped at 80,000

Personal reliefs in total — earned income, spouse, child, parent, course fees,
CPF cash top-ups and SRS — cannot exceed 80,000. Beyond that, further
contributions give no relief.

The **Supplementary Retirement Scheme** is one of the few real deductions
available to foreigners: 35,700 a year for foreigners, 15,300 for citizens and
PRs. Worth raising with any higher-earning EP holder.

## What the engine leaves out

CPF age-banding (rates fall from 55), the non-resident 15% flat computation,
reliefs beyond earned income relief, and the fact that CPF applies only to
ordinary and additional wage components up to their respective ceilings.
