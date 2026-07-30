---
name: hong-kong-tax-calculation
description: Calculate Hong Kong salaries tax under both the progressive and standard rate computations, plus MPF and net pay. Use this whenever someone asks what they will take home in Hong Kong, how a Hong Kong offer compares with Singapore, London or New York, why there is no tax withheld from their salary, what the 60-day rule means, how income for work done outside Hong Kong is treated, or how the territorial source basis works — including when they only mention the IRD or a BIR60.
---

# Hong Kong salaries tax calculation — year of assessment 2025/26

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Hong Kong.

## Run the engine

```bash
python -m taxcalc calc HK --employment 900000
python -m taxcalc calc HK --employment 1200000 --children 2
python -m taxcalc info HK
```

## You pay the lower of two computations

The Inland Revenue Department charges whichever is less:

- **Progressive**: 2/6/10/14/17% on net chargeable income, *after* the 132,000
  basic allowance and any other allowances
- **Standard rate**: 15% on net income *before* allowances, and 16% on the part
  above 5,000,000

The engine only applies the progressive computation. The standard rate wins at
high income — roughly above 2.2m for a single person with only the basic
allowance. Above that, check the standard rate figure manually and use the
lower one.

## Nothing is withheld from your salary

There is no PAYE. You receive an assessment and pay in two instalments, in
January and April. In your first year of working in Hong Kong this means:

1. No tax comes out of your pay all year, so take-home feels very high
2. The first bill covers the year just ended **plus provisional tax for the
   current year**, so it is close to double a normal year's tax

New arrivals routinely spend the money and then face a bill of a third of a
year's salary. Raise this whenever someone starts work in Hong Kong — setting
money aside monthly is the practical advice.

## Territorial source

Hong Kong taxes income arising in or derived from Hong Kong. Income from
services rendered **entirely outside** Hong Kong is not chargeable, and a
visitor present 60 days or fewer in the year of assessment is exempt on services
performed here.

Time apportionment is available where an employment is non-Hong Kong sourced and
services are split between locations. This requires keeping day records — worth
mentioning to anyone travelling regularly for work.

## What is not taxed at all

No capital gains tax, no tax on dividends or interest, no VAT or sales tax, no
estate duty. The headline salaries tax rates therefore understate how light the
overall position is by a wide margin — this is the real comparison point against
Singapore, not the rate tables.

## Deductions worth knowing

Home loan interest up to 100,000 a year for 20 years of assessment, MPF
contributions up to 18,000, approved charitable donations, elderly residential
care expenses, and voluntary health insurance premiums.

## What the engine leaves out

The standard rate computation, joint assessment and personal assessment
elections for married couples, and the one-off rate reductions announced in most
years' Budget.
