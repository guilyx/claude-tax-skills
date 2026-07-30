---
name: czechia-tax-calculation
description: Calculate Czech income tax, social and health insurance, and net pay, including the lump-sum expense regimes for the self-employed. Use this whenever someone asks what they will take home in Czechia, how a Prague or Brno offer compares, what an OSVČ pays, whether paušální daň is worth it, how the 23% higher rate works, or how the three-year time test exempts investment gains — including when they only mention the finanční úřad or a živnostenský list.
---

# Czech income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Czechia.

## Run the engine

```bash
python -m taxcalc calc CZ --employment 1200000
python -m taxcalc calc CZ --self-employment 1800000
python -m taxcalc info CZ
```

## Two rates, and the threshold moves every year

15% up to 36 times the average wage (1,676,052 CZK for 2025) and 23% above. The
threshold is indexed to the average wage, so it changes annually — always state
which year's figure you are using.

Health insurance has **no ceiling** while social insurance is capped at 48 times
the average wage, so the marginal wedge falls partway up the income scale but
never disappears.

## The self-employed regimes are where the real money is

An OSVČ has three broadly different positions:

- **Lump-sum expenses (paušální výdaje)**: deduct a fixed 40%, 60% or 80% of
  revenue depending on the activity, with **no receipts required** and no
  bookkeeping. For most consultants and tradespeople this beats tracking real
  costs, and it is the default choice.
- **Paušální daň**: one fixed monthly payment covering income tax, social and
  health insurance, with **no return to file at all**. Available up to 2m CZK of
  revenue with conditions. Extremely simple, and usually cheapest for
  higher-earning freelancers with few expenses.
- **Real expenses**: only worth it where costs genuinely exceed the lump-sum
  percentage.

Contribution bases for the self-employed are also being raised in steps — 55% of
profit for social insurance in 2025, rising toward 60% — so figures from a couple
of years ago understate the cost.

## The three-year time test

Securities held more than three years, or shares in a company held more than
five, are exempt from income tax. From 2025 this exemption is **capped at 40m
CZK of proceeds per year** — a change that only affects large disposals but is
new and worth flagging.

Separately, annual securities sales under 100,000 CZK are exempt regardless of
holding period.

Together these make ordinary long-term investing effectively tax free in
Czechia, which is unusual within the EU.

## Most employees never file

With a single employer and a signed annual declaration (the růžové prohlášení),
payroll settles everything. See the reporting skill for what triggers a return.

## What the engine leaves out

Both lump-sum regimes, the fact that the 23% rate technically applies to gross
income rather than taxable income, and the spouse and disability credits.
