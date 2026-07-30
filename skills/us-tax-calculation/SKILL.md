---
name: us-tax-calculation
description: Calculate US federal and state income tax, FICA payroll tax, and take-home pay for employees, contractors, and Americans living abroad. Use this whenever someone asks what they will actually take home on a US salary, how a job offer in a particular state compares, what their effective or marginal rate is, how much self-employment tax a 1099 contractor owes, what a bonus or RSU vest will cost them, or how the foreign earned income exclusion affects an expat — including when they name a city or state rather than saying "US tax", and including when they ask about withholding, W-4 allowances, or quarterly estimated payments.
---

# US federal and state income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to the United States.

## Run the engine

```bash
python -m taxcalc calc US --employment 150000 --status single --region CA
python -m taxcalc calc US --employment 220000 --status married_joint --children 2
python -m taxcalc calc US --self-employment 120000 --status single   # 1099 contractor
python -m taxcalc info US
```

## Establish these before computing

- **Filing status** — `single`, `married_joint`, `married_separate`,
  `head_of_household`. This changes the brackets, the standard deduction and the
  additional Medicare threshold. Never assume; a wrong status is the single
  largest source of error in a US estimate.
- **State** — pass `--region`. Nine states levy no tax on wage income (TX, FL,
  WA, NV, TN, NH, WY, SD, AK). California and New York are progressive and the
  flat rate in the data is a high-bracket approximation, so for those two, treat
  the state figure as indicative and compute properly if the number matters.
- **W-2 or 1099** — a contractor pays both halves of FICA (15.3% up to the wage
  base) and gets no employer match. Use `--self-employment`, and mention that
  half of SECA is deductible and that the QBI deduction may apply.
- **Citizenship** — a US citizen abroad still files. See below.

## What is specific to the US

- **Worldwide taxation of citizens and green card holders.** This is the fact
  that surprises people most. Someone moving to Dubai or Singapore does not stop
  filing. The foreign earned income exclusion (130,000 for 2025) and the foreign
  tax credit usually eliminate the tax, but never the return, and never the FBAR.
- **State residency is decided separately from federal.** California and New
  York pursue departing residents on domicile grounds. Someone "moving to
  Texas" who keeps a California home and family has not necessarily left.
- **RSUs and bonuses are supplementally withheld at 22%** up to 1m, which is
  below the marginal rate of most people who receive them. The shortfall shows
  up as a bill in April. Raise this whenever equity comp comes up — it is the
  most common unpleasant surprise in US tax.
- **Estimated tax is quarterly** for income without withholding. Underpayment
  penalties accrue even if the return is filed and paid on time in April.

## What the engine leaves out

The alternative minimum tax, the 3.8% net investment income tax, the qualified
business income deduction, itemised deductions, and the child tax credit's
refundable portion mechanics. State tax is a single approximate rate. Say so if
any of these are material.

## Worked example

A single filer on 150,000 in Texas: taxable income is 134,250 after the 15,750
standard deduction, giving 25,199 of federal tax, plus 11,475 of FICA. Take-home
is about 113,300, an effective federal rate of 16.8% and a total burden of 24.5%.
The marginal rate on the next dollar is 24% federal plus 1.45% Medicare.

Note how far the effective rate sits below the marginal rate. Users frequently
believe a raise into the "24% bracket" taxes all their income at 24%; showing
both numbers side by side is usually the most useful thing in the answer.
