---
name: luxembourg-tax-calculation
description: Calculate Luxembourg income tax, the employment fund surcharge, social contributions and net pay, including tax classes and cross-border commuter treatment. Use this whenever someone asks what they will take home in Luxembourg, how a Luxembourg offer compares with Belgium, France or Germany, what tax class 1, 1a or 2 means, how commuting from across the border is taxed, whether the impatriate regime applies, or how the six-month rule exempts investment gains — including when they only mention the ACD or a fiche de retenue.
---

# Luxembourg income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Luxembourg.

## Run the engine

```bash
python -m taxcalc calc LU --employment 90000
python -m taxcalc calc LU --employment 150000 --status married_joint
python -m taxcalc info LU
```

## Tax class is the first question

- **Class 1** — single taxpayers
- **Class 1a** — single parents, and taxpayers aged 65 or over. Lower than
  class 1, and **not modelled by the engine**, so results for these taxpayers
  are overstated.
- **Class 2** — jointly taxed married and partnered couples, with income split
  between the spouses. Substantially lower.

Since 2018, married non-residents default to class 1 rather than class 2. They
can request assimilation to resident treatment, which restores class 2 and
allows deductions — but only if at least 90% of household income is taxable in
Luxembourg (or 50% for Belgian residents). Whether it helps depends entirely on
the spouse's income, so it needs computing both ways rather than assuming.

## Cross-border commuters

A large share of Luxembourg's workforce lives in Belgium, France or Germany.
Two consequences worth raising:

- **Workdays spent outside Luxembourg** can become taxable in the country of
  residence beyond tolerance thresholds — 34 days for Belgium and Germany, 34
  for France. Remote working from home eats into this quickly, and exceeding it
  splits the salary between two tax systems.
- **Social security stays in Luxembourg** provided less than 25% of activity is
  performed in the country of residence, under EU rules. The teleworking
  framework agreement raised this to 49.9% for cross-border remote work, but it
  must be applied for.

Anyone commuting into Luxembourg and working from home should know both numbers.

## The employment fund surcharge

7% of the tax itself, rising to 9% at higher incomes. This is why the effective
top marginal rate is about 45.8% rather than 42%. The engine applies 7%; switch
to 9% manually for taxable income above roughly 150,000 (class 1) or 300,000
(class 2).

## The six-month rule on capital gains

Gains on securities held **more than six months** are exempt entirely, unless
you hold a substantial participation above 10%. Gains within six months are
speculative and taxed at ordinary rates.

Six months is short by international standards, and it makes Luxembourg unusually
favourable for medium-term investors. Worth raising whenever investment is
mentioned.

## What the engine leaves out

Class 1a, the 23-bracket statutory scale (approximated), the 9% surcharge tier,
the impatriate regime for inbound employees, and the various small deductions
Luxembourg allows — loan interest, life insurance premiums, private pension
contributions and childcare — which together are worth more than in most systems.
