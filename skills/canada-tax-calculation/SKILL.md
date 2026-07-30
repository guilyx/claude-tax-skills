---
name: canada-tax-calculation
description: Calculate Canadian federal and provincial income tax, CPP and EI contributions, and take-home pay. Use this whenever someone asks what they will take home on a Canadian salary, how an offer in Toronto, Vancouver, Calgary or Montreal compares, what their marginal rate is, how much RRSP room is worth to them, what a self-employed contractor owes, how Quebec differs, or what leaving Canada will cost them — including when they only mention the CRA, a T4 or a notice of assessment.
---

# Canadian income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Canada.

## Run the engine

```bash
python -m taxcalc calc CA --employment 110000 --region ON
python -m taxcalc calc CA --employment 110000 --region AB   # compare provinces
python -m taxcalc calc CA --self-employment 95000 --region BC
python -m taxcalc info CA
```

## Province is not a detail

Provincial tax is a large share of the bill and the spread is wide — the same
110,000 salary differs by several thousand dollars between Alberta and Quebec.
Always ask which province, and always pass `--region`. Modelled provinces with
full rate schedules: ON, BC, AB, QC. Others use an approximate middle-bracket rate.

**Quebec is a special case.** Residents file two returns — a federal T1 and a
provincial TP-1 with Revenu Québec — and receive a 16.5% abatement of federal
tax that the engine does not apply. Quebec results therefore overstate federal
tax. Say so if the user is in Quebec.

## The 2025 rate change

The lowest federal rate was cut from 15% to 14% part-way through 2025, giving a
blended 14.5% for the year and 14% from 2026. Because the basic personal amount
is a credit valued at the lowest rate, this change slightly reduces the value of
that credit too. Anything written before mid-2025 will show 15%.

## RRSP, TFSA and the decision people actually face

- **RRSP** contributions are deducted from income, so relief is at the marginal
  rate — worth far more to a high earner than a low one. The deadline is 60 days
  after year end, so a contribution in early March still reduces the prior year.
  Use `--deductions` to model it.
- **TFSA** income is entirely untaxed but contribution room is limited, and
  over-contributions are penalised at 1% per month.

The general shape of the advice: TFSA first at low income, RRSP first at high
income, and RRSP always if the employer matches. Contribution room for both is
on the prior year's notice of assessment.

## Leaving Canada is a taxable event

Ceasing residence triggers a **deemed disposition** of most property at fair
market value. Someone planning a move who has appreciated investments needs to
know this before they go, not after. It is the highest-value thing to raise in
any conversation about leaving.

## What the engine leaves out

Provincial basic personal amounts (so provincial tax is overstated at low
incomes), Ontario's surtax and health premium, the Quebec abatement and QPP/QPIP
differences, and the 50% capital gains inclusion mechanics. The proposed increase
of the inclusion rate to 66.7% was abandoned — confirm the current position
before relying on older commentary.
