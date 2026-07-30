---
name: uae-tax-calculation
description: Work out UAE tax position — no personal income tax on salary, but 9% corporate tax for individuals carrying on a business, plus what a move to the UAE actually costs once the former home country is accounted for. Use this whenever someone asks about take-home pay in Dubai or Abu Dhabi, whether the UAE is really tax free, what a freelancer or consultant with a licence owes, how corporate tax applies to sole traders, whether a free zone company helps, or how a UAE package compares with a taxed country.
---

# UAE tax position — 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to the United Arab Emirates.

## Run the engine

```bash
python -m taxcalc calc AE --employment 500000
python -m taxcalc info AE
```

The engine returns zero income tax and zero employee social security for
expatriate employees. That is correct, and the interesting part of the answer is
everything around it.

## Salary is untaxed. Business income may not be

The distinction that matters:

- **Employment income** — no tax, no social security for expatriates, no return.
- **Business income** — an individual carrying on a business or business
  activity with turnover above **1,000,000 AED** in a calendar year is within
  corporate tax at 9% on profits above 375,000, must register, and must file.

A freelancer or consultant with a trade licence billing above that threshold is
therefore a taxpayer, even operating alone. Personal investment income, real
estate income held personally, and salary stay outside it.

Free zone companies can qualify for 0% on qualifying income, but the conditions
around substance and qualifying activities are specific and not automatic.

## The honest comparison

Someone comparing a Dubai package with a European one should account for:

- **Housing, schooling and healthcare** are typically paid privately and are a
  large share of the real cost. An AED 500,000 package with school fees for two
  children is not equivalent to the same figure without.
- **End-of-service gratuity** accrues under the labour law and functions as
  deferred pay. New savings schemes are replacing it in some emirates.
- **No pension accrual.** Years in the UAE build no state pension anywhere,
  which is a real long-term cost that never appears in a take-home comparison.
- **5% VAT** on most goods and services.

## The part people get wrong is leaving, not arriving

Moving to the UAE does not end tax liability in the country left behind. What
matters is whether residence there was properly terminated under **that
country's** rules — the available-home tests in Germany and Switzerland, the
ordinary residence rule in Ireland, the exit declaration in Brazil, the
Statutory Residence Test in the UK.

And **US citizens and green card holders remain fully taxable** on worldwide
income wherever they live. A US citizen in Dubai still files, still reports
foreign accounts on an FBAR, and pays US tax on investment income the UAE does
not touch.

## Tax Residency Certificate

Other countries will ask for evidence, and physical presence alone is not it. A
TRC from the Federal Tax Authority requires 183 days supported by entry and exit
records, a tenancy contract and bank statements. Apply early — it takes time and
is often needed to stop the former country taxing you.
