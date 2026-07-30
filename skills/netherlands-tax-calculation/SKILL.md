---
name: netherlands-tax-calculation
description: Calculate Dutch income tax across the three boxes, national insurance, heffingskortingen and net salary from gross. Use this whenever someone asks about Dutch take-home pay, bruto versus netto, what they will earn in Amsterdam, Rotterdam, Eindhoven or Utrecht, how the 30% ruling affects their salary, what box 3 wealth tax costs them, how a ZZP freelancer is taxed, or whether a Dutch offer is competitive — including when they only mention the Belastingdienst or a jaaropgaaf.
---

# Dutch income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to the Netherlands.

## Run the engine

```bash
python -m taxcalc calc NL --employment 75000
python -m taxcalc calc NL --employment 120000
python -m taxcalc info NL
```

## Social security is inside the rate, not next to it

The first two box 1 rates (35.82% and 37.48%) already include 27.65% of national
insurance contributions. The engine therefore shows zero employee social
security for the Netherlands — that is correct, not a bug, but it makes raw
cross-country comparisons of the "social security" column misleading. Say so
when comparing the Netherlands with anywhere else.

## The 30% ruling changes everything, and it has been trimmed

If the user qualifies, a portion of salary is paid free of tax. The regime has
been repeatedly cut back and **the version that applies depends on when your
first working day was**, not on the current year's rules. Do not assume the
historic "30% for five years". Establish the start date, then apply the right
version, and note the cap at the WNT norm (roughly 233,000).

The engine does not apply it. Reduce gross by the exempt portion before running
the calculation, and say that is what you did.

## The credits are why the real marginal rate is higher than it looks

The algemene heffingskorting withdraws at 6.337% from 28,406, and the
arbeidskorting at 6.51% from 43,071. Both taper at once in the middle of the
income range, so the true marginal rate between roughly 43,000 and 76,000 sits
near 50% despite a headline rate of 37.48%. The engine measures this
numerically; it is usually the most surprising and useful number in the answer.

## Box 3 is a wealth tax, not a capital gains tax

There is no capital gains tax on ordinary investments. Instead, box 3 taxes a
**deemed return** on net assets above the 57,684 exemption, measured on 1 January.
A loss-making year still produces tax. The Supreme Court has forced a route to be
taxed on actual return where that is lower, and the regime is being rebuilt —
flag that this area is unsettled rather than quoting a figure with confidence.

The engine does not compute box 3. It depends on asset composition on a single
date, not on income.

## Other specifics

- **Fiscal partners** may freely allocate certain shared items — mortgage
  interest, box 3 assets, some deductions — between their two returns. Choosing
  the higher earner for deductions and the lower for box 3 is a real and widely
  missed saving.
- **Mortgage interest relief** is capped at a 37.48% benefit even for top-rate
  taxpayers, and is offset by the eigenwoningforfait deemed rental value.
- **ZZP freelancers** get the zelfstandigenaftrek, which is being phased down
  each year, plus the MKB-winstvrijstelling. Neither is in the engine.
