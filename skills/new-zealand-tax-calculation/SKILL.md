---
name: new-zealand-tax-calculation
description: Calculate New Zealand income tax, ACC levies, KiwiSaver and take-home pay, including the foreign investment fund rules that catch migrants. Use this whenever someone asks what they will take home in New Zealand, how an Auckland, Wellington or Christchurch offer compares, what their marginal rate is, whether New Zealand really has no capital gains tax, how foreign shares are taxed, what the transitional resident exemption gives them, or how an NZ offer compares — including when they only mention IRD or myIR.
---

# New Zealand income tax calculation — 2025-26 tax year

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to New Zealand.

## Run the engine

```bash
python -m taxcalc calc NZ --employment 110000
python -m taxcalc calc NZ --self-employment 130000
python -m taxcalc info NZ
```

## The tax year ends 31 March

Not 31 December, and not 30 June like Australia. Confirm which year is meant.

## Foreign shares are taxed even if you never sell

This is the single biggest surprise for people moving to New Zealand. Under the
**foreign investment fund (FIF) rules**, holdings in foreign shares costing more
than 50,000 NZD are taxed annually on a **deemed 5% return** — whether or not
they paid a dividend and whether or not you sold anything.

Someone arriving with an ETF portfolio, a foreign pension outside the exempt
categories, or accumulated employer stock will face annual tax on assets that
generate no cash. Australian-listed shares meeting conditions and some other
categories are exempt, and the rules were revised for new migrants in 2025.

Raise this unprompted with anyone relocating to New Zealand with investments. It
frequently changes what they should hold, and the decision is best made before
arriving.

## The transitional resident exemption

New migrants and returning New Zealanders who have been away ten years get a
**four-year exemption on most foreign income**, including FIF income. It applies
automatically but is lost if you or your partner claim Working for Families.

The four years is the window in which to restructure foreign holdings. Anyone
arriving should know when their exemption ends, because the FIF liability starts
the day after.

## No capital gains tax, with edges

There is no general CGT. But:

- The **bright-line test** taxes residential property sold within two years of
  acquisition (reduced from ten years in July 2024), with a main home exclusion.
- The **intention test** taxes gains on anything acquired with the purpose of
  resale, regardless of holding period — this catches active traders.
- FIF rules tax foreign shares annually, as above.

## KiwiSaver is savings, not tax

The 3% employee contribution reduces take-home pay but remains the employee's
money. Employer contributions are taxed at your marginal rate (ESCT), so the
headline 3% match is worth less than it appears. When comparing offers
internationally, treat it as deferred pay rather than a deduction.

## What the engine leaves out

FIF income, student loan repayments (12% above the threshold), Working for
Families tax credits, and the independent earner tax credit.
