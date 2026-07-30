---
name: australia-tax-reporting
description: Handle Australian tax return lodgment — the 31 October deadline, the tax agent extension to 15 May, myTax and prefilled income statements, what deductions need substantiation, BAS and PAYG instalments, and ATO penalties. Use this whenever someone asks when their Australian tax return is due, how to lodge, what they can claim, whether they need a tax agent, what happens if they lodge late or have several years outstanding, or how to handle GST and BAS as a sole trader.
---

# Australian tax reporting and lodgment — 2025-26 income year

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Australia.

## Get the calendar

```bash
python -m taxcalc deadlines AU
```

## Deadlines, and the extension that is worth knowing about

| Date | What |
| --- | --- |
| 14 July 2026 | Employers finalise Single Touch Payroll; income statements become "tax ready" |
| 31 October 2026 | Lodgment deadline if you lodge yourself |
| 15 May 2027 | Deadline if you lodge through a registered tax agent |

The agent extension is substantial — over six months — but it only applies if
you are **on the agent's client list before 31 October**. Someone who engages an
agent in November has already missed it. This is worth raising in October.

Do not lodge before mid-July. Pre-fill data is incomplete until employers,
banks and health funds report, and lodging early is the main cause of having to
amend.

## Deductions and substantiation

Work-related deductions are generous in Australia relative to most countries,
but the ATO data-matches heavily and publishes a focus area each year. The
practical rules:

- Under 300 of total work expenses: no receipts needed, but you must have
  actually incurred them and be able to explain the claim.
- Car expenses: cents-per-kilometre up to 5,000 km, or a logbook kept for 12
  continuous weeks.
- Working from home: the fixed rate per hour requires a record of hours actually
  worked from home for the whole year — a diary kept from July, not reconstructed
  in October.
- Clothing: only occupation-specific, protective or logo-branded uniforms.
  Conventional clothing is never deductible however strictly the employer requires it.

## Sole traders

An ABN sole trader lodges the individual return with a business schedule — not
a separate return. GST registration is compulsory above 75,000 of turnover, and
BAS is then lodged quarterly. PAYG instalments start once the ATO assesses
enough business income, and they are based on the prior year, so a growing
business systematically underpays and gets a bill.

## If they are behind

The ATO's position on multiple outstanding years is more constructive than
people fear. Lodging voluntarily before being contacted generally means
failure-to-lodge penalties are remitted, and payment plans are routinely
available online for debts under 200,000. Someone with several unlodged years
should be told to lodge them all rather than to keep avoiding it.

## Penalties

One penalty unit per 28 days late, up to five units. Shortfall penalties run
from 25% for failure to take reasonable care to 75% for intentional disregard.
General interest charge compounds daily.
