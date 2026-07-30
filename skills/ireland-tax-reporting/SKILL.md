---
name: ireland-tax-reporting
description: Handle Irish tax filing — Form 11 versus Form 12, the 31 October deadline and the ROS extension, preliminary tax, Statements of Liability for PAYE workers, capital gains payment dates, and Revenue penalties. Use this whenever someone asks when Irish taxes are due, whether they need to file a return, how to claim a refund for previous years, what preliminary tax means, how to register for ROS or myAccount, or what happens if they file late.
---

# Irish tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Ireland.

## Get the calendar

```bash
python -m taxcalc deadlines IE
```

## Two very different systems, and most people are in the easy one

- **PAYE-only taxpayers** do not file a return. They request a **Statement of
  Liability** through myAccount, which reconciles the year. This is where you
  claim medical expenses, the rent tax credit, remote working relief and tuition
  fees — and claims can be made for the **previous four years**, so someone who
  has never claimed can often recover a meaningful sum immediately.
- **Self-assessed taxpayers** — the self-employed, proprietary directors,
  landlords, and anyone with substantial non-PAYE income — file **Form 11**
  through ROS.

Establishing which category someone is in should be the first move. Telling a
PAYE worker to file a Form 11 sends them somewhere they do not need to go.

## Deadlines

| Date | What |
| --- | --- |
| 31 October 2026 | Form 11 for 2025, plus preliminary tax for 2026 |
| Mid-November 2026 | Extended date if both filing and paying through ROS |
| 15 December 2026 | CGT on disposals January–November 2026 |
| 31 January 2027 | CGT on December 2026 disposals |
| Any time within 4 years | PAYE refund claims for earlier years |

## Preliminary tax is the part that surprises people

The 31 October payment covers **both** the balance for the year just ended and
preliminary tax for the current year. A first-year sole trader therefore faces
roughly double. The safe harbour is 100% of the prior year's liability or 90% of
the current year's — paying 100% of last year is the simple, safe choice.

## Capital gains are paid before the return

CGT on disposals is due in December of the **same year** as the disposal, months
before the return that reports it. Someone who sold shares in March and plans to
deal with it "at tax time" has already missed the payment date. Raise this
whenever a disposal is mentioned.

## Penalties

A 5% surcharge if filed within two months of the deadline, 10% after, capped at
63,485. Interest of roughly 8% a year on late payment. Revenue operates a
self-correction window and a qualifying disclosure regime that substantially
reduce penalties for someone who comes forward first.
