---
name: sweden-tax-calculation
description: Calculate Swedish municipal and state income tax, the jobbskatteavdrag credit and net salary. Use this whenever someone asks what they will take home in Sweden, how a Stockholm, Gothenburg, Malmö or Uppsala offer compares, where the state tax threshold bites, what an ISK account saves them, what SINK means for a temporary worker, what expert tax relief is worth, or how a Swedish offer compares with elsewhere — including when they only mention Skatteverket or a lönespecifikation.
---

# Swedish income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Sweden.

## Run the engine

```bash
python -m taxcalc calc SE --employment 600000 --region STO
python -m taxcalc calc SE --employment 800000 --region GOT
python -m taxcalc info SE
```

## Municipal tax does most of the work

Most Swedish income tax is municipal — roughly 32.4% on average, but ranging
from about 29% in Österåker to 35.3% in Dorotea. Ask where they live and pass
`--region`; a six-point spread is larger than most people expect within one
country.

State tax of 20% only applies **above 625,800** of taxable income. Below that
threshold the marginal rate is essentially the municipal rate; above it, it
jumps to roughly 52%. This threshold is the single most important number in
Swedish salary negotiation and is why compensation above it often shifts toward
pension contributions and benefits.

## The 7% pension fee that nobody actually pays

The allmän pensionsavgift of 7% appears on payslips but is offset in full by a
matching tax credit for almost everyone. The engine shows it as a contribution,
so the "employee social security" line overstates the real cost. Say so —
otherwise Sweden looks worse in comparisons than it is.

## ISK is the account choice that matters

The investeringssparkonto replaces capital gains tax with a small annual charge
on the account value. For long-term investors in rising markets this is
dramatically cheaper than the 30% capital gains rate, and it removes the need to
track acquisition costs at all. For someone likely to make losses, or holding
cash, it is worse. Whenever investing in Sweden comes up, this is the practical
question.

## Regimes for people arriving

- **SINK**: non-residents working temporarily in Sweden can elect a 25% flat
  withholding with no deductions and no return to file. Simple, and usually
  better than the ordinary system for short stays.
- **Expert tax relief**: 25% of remuneration exempt for up to seven years for
  qualifying key personnel and researchers, or for anyone above a monthly salary
  threshold. It must be applied for within three months of starting work — a
  hard deadline that is easy to miss during a relocation.

## What the engine leaves out

The grundavdrag and jobbskatteavdrag are both formula-driven and approximated
here, so results in the 200,000–500,000 range are the least precise. Church fee
of roughly 1% for members of the Church of Sweden is excluded, as is the 25%
employer contribution on pension provisions.
