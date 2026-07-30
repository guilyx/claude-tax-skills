---
name: saudi-arabia-tax-calculation
description: Work out the Saudi tax position — no personal income tax on salary, 20% income tax on non-GCC business profits, Zakat, GOSI contributions and 15% VAT. Use this whenever someone asks about take-home pay in Riyadh, Jeddah or NEOM, whether Saudi Arabia is tax free, what a non-Saudi consultant or business owner pays, how Zakat differs from income tax, what withholding tax applies to payments abroad, or how a Saudi package compares with a taxed country.
---

# Saudi Arabia tax position — 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Saudi Arabia.

## Run the engine

```bash
python -m taxcalc calc SA --employment 600000
python -m taxcalc info SA
```

The engine returns zero for employment income, which is correct. Expatriate
employees pay no income tax and no social security beyond employer-paid
occupational hazards cover.

## The split system for business

Saudi Arabia taxes businesses in two ways at once, by ownership:

- **Non-GCC ownership share** — 20% income tax on the attributable profit
- **Saudi and GCC ownership share** — Zakat at 2.5% of the Zakat base

A mixed-ownership company computes both. A non-Saudi individual carrying on
business in the Kingdom is subject to the 20% income tax on that business
income, and the engine does not compute this.

## Withholding tax is the common compliance failure

Payments to non-residents attract withholding at 5% to 20% depending on the
nature of the payment — 5% on most services and dividends, 15% on royalties and
payments to related parties, 20% on management fees. It is due within the first
ten days of the following month.

Foreign businesses and Saudi entities paying overseas suppliers miss this
routinely, and ZATCA assesses it against the payer, not the recipient. If
someone describes paying an overseas consultant or licensor from Saudi Arabia,
this is worth raising.

## The honest comparison

- **15% VAT** is high for the region and a real cost of living.
- **Housing, schooling and healthcare** are typically employer-provided or paid
  privately. The value of the package matters more than the salary line.
- **No pension accrual** for expatriates, who are outside GOSI's pension
  elements. Years worked build no retirement entitlement anywhere.
- **End-of-service benefit** under the labour law functions as deferred pay.
- **Real Estate Transaction Tax** of 5% applies on property transfers instead of
  VAT.

## GOSI

Saudi nationals contribute to the full scheme — 11.75% employee for those
joining from July 2024 under the reformed rules, phasing upward, with the rate
depending on when the employee first joined. Expatriates are covered only for
occupational hazards at 2%, paid entirely by the employer.

## US citizens

As everywhere, US citizens and green card holders remain taxable on worldwide
income and must file, regardless of Saudi Arabia levying nothing. The foreign
earned income exclusion and housing exclusion usually eliminate the tax on
salary but never the return or the FBAR.
