---
name: denmark-tax-calculation
description: Calculate Danish income tax — AM-bidrag, municipal tax, bottom and top bracket tax — and net pay, including the 27% researcher and expat scheme. Use this whenever someone asks what they will take home in Denmark, how a Copenhagen or Aarhus offer compares, why Danish tax is described as the highest in the world, whether the 27% expat scheme applies, what the tax ceiling means, or how a Danish offer compares — including when they only mention SKAT, forskudsopgørelse or årsopgørelse.
---

# Danish income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Denmark.

## Run the engine

```bash
python -m taxcalc calc DK --employment 600000 --region KBH
python -m taxcalc calc DK --employment 900000 --region AAR
python -m taxcalc info DK
```

## Four layers, and the order matters

1. **AM-bidrag** at 8% comes off gross first and is deductible against everything
   else. It is a labour market contribution, but functionally it is a flat tax.
2. **Municipal tax** at roughly 25.1% on average — the largest single component.
3. **Bottom-bracket tax** at 12.01%.
4. **Top-bracket tax** at 15% above roughly 611,800 of personal income.

The **tax ceiling** caps the combined municipal, bottom and top rate at 52.07%,
but AM-bidrag and church tax sit outside it. That is how the often-quoted
"55.9% marginal rate" arises. The engine does not enforce the ceiling, so very
high incomes are marginally overstated.

## The 27% scheme, and the salary condition that must hold every month

Qualifying researchers and highly paid employees can be taxed at 27% plus
AM-bidrag — an effective 32.84% — for up to seven years, with no deductions.

The minimum salary requirement is checked **monthly**, and a single month below
the threshold can disqualify the entire arrangement retroactively. Unpaid leave,
a period of part-time work, or a salary sacrifice arrangement can all break it.
Anyone on the scheme should know this; the consequence is a large retroactive
bill at ordinary rates.

Researchers approved under the alternative route are exempt from the salary
requirement.

## Church tax is opt-out, not opt-in

Roughly 0.7% is charged automatically to members of the Danish National Church,
and membership is inherited. Someone who has never actively joined may still be
paying it. It is excluded from the engine.

## The forskudsopgørelse is where the real work happens

The preliminary income assessment, published each November, drives your monthly
withholding for the following year. Updating it when circumstances change — a
new job, a mortgage, a move abroad — is how Danes avoid a large March bill. When
someone asks about a Danish tax problem, the fix is very often to update this
rather than to do anything with the annual return.

## What the engine leaves out

The 52.07% tax ceiling, church tax, the 27% expat scheme, and the personal
allowance is applied as a deduction rather than Denmark's actual credit
mechanism.
