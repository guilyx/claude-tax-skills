---
name: finland-tax-calculation
description: Calculate Finnish state and municipal income tax, TyEL and health insurance contributions, and net pay, including the 32% key employee regime. Use this whenever someone asks what they will take home in Finland, how a Helsinki, Espoo, Tampere or Oulu offer compares, what a tax card (verokortti) rate should be, what YEL means for an entrepreneur, whether the foreign key employee flat tax applies, or how a Finnish offer compares — including when they only mention Vero, OmaVero or a veroprosentti.
---

# Finnish income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Finland.

## Run the engine

```bash
python -m taxcalc calc FI --employment 55000 --region HEL
python -m taxcalc calc FI --employment 90000 --region TAM
python -m taxcalc info FI
```

## Municipal rates fell by twelve points in 2023

When healthcare funding moved to the wellbeing services counties, municipal
rates dropped by roughly 12 percentage points and the state scale absorbed the
difference. Municipal tax now averages about 7.5%.

Any comparison with pre-2023 figures, or any source quoting a Finnish municipal
rate around 20%, is out of date. Say so if the user is working from older
material — the totals are similar but the components look completely different.

## The tax card is what people actually ask about

Finns think in terms of their **veroprosentti** — the withholding percentage on
the tax card. Two rates apply: a base rate up to an estimated annual income
limit, and a higher additional rate above it.

The practical advice: update the card in OmaVero whenever income changes. Going
over the income limit means the additional rate applies to everything beyond it,
which produces a noticeably smaller payslip. A new card takes effect
immediately and can be issued any number of times a year.

## The deemed acquisition cost rule

When selling an asset, you may deduct **20% of the sale price** as cost instead
of the actual acquisition cost — or **40%** if held over ten years — with no
documentation at all. For long-held assets this frequently beats the real cost
and removes any need to find old paperwork.

This is unusually generous and widely underused. Raise it whenever a disposal
comes up. Sales totalling under 1,000 in a year are exempt entirely.

## YEL sets your pension, not just your tax

Self-employed contributions are charged on a **declared YEL income** figure
rather than actual profit. That declared figure also determines future pension,
sickness allowance and parental allowance. Setting it low to save contributions
quietly reduces every benefit for years afterwards, and the Finnish Centre for
Pensions has been actively raising under-declared figures. This is the most
consequential decision a Finnish entrepreneur makes.

## Other specifics

- **Capital income** is taxed separately at 30%, rising to 34% above 30,000.
- **Church tax** of 1% to 2.25% applies to members of the Lutheran or Orthodox
  church and is collected with income tax. Not in the engine.
- **Foreign key employees** can elect a 32% flat tax on Finnish salary for up to
  48 months, which wins at high salaries.

## What the engine leaves out

The earned income deduction and basic deduction, which means results at low
incomes overstate the tax. Church tax and the key employee regime are excluded.
