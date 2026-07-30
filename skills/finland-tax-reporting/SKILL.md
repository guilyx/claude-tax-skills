---
name: finland-tax-reporting
description: Handle Finnish tax filing — the pre-completed return, personal deadlines in May, MyTax (OmaVero), tax cards, and Vero penalties. Use this whenever someone asks when the Finnish tax return is due, whether they need to do anything, how to correct the pre-completed return, how to change their tax card, how to report foreign income or securities, or what happens if they miss the deadline.
---

# Finnish tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Finland.

## Get the calendar

```bash
python -m taxcalc deadlines FI
```

## Your deadline is printed on your own return

Finland does not have one filing date. The pre-completed return is published in
March with **one of three dates in May** printed on it, assigned per taxpayer.
Never quote a single national date — tell the user to read the date on their own
return or check OmaVero.

| Date | What |
| --- | --- |
| March 2026 | Pre-completed return published in MyTax |
| One of three dates in May 2026 | Correction deadline, personal to you |
| 1 April 2026 | Deadline for the self-employed and business operators |
| August and October | Residual tax instalment dates |

If the pre-completed return is correct, you do nothing and it stands.

## What needs adding

The pre-completed return covers Finnish salary, benefits and Finnish investment
income. It does not cover:

- **Foreign securities**, including holdings with non-Finnish brokers
- **Foreign income and foreign tax paid**
- **Rental income** details beyond what was reported
- **Commuting costs** above the 750 threshold, and work-related expenses
- **Household deduction (kotitalousvähennys)** for domestic help, care and
  renovation work — a substantial deduction that must be claimed

## The tax card is a year-round tool

Unlike the return, the verokortti can and should be updated whenever income
changes. It is done in MyTax in a few minutes and takes effect at once. Someone
who is over-withholding all year and waiting for a refund is lending the state
money; someone under-withholding faces residual tax with interest.

## Foreign account reporting

Finland receives automatic exchange of information and pre-fills some foreign
data, but the obligation to report foreign income rests with the taxpayer.
Anyone with accounts or investments abroad should check what did and did not
appear on the pre-completed return rather than assuming it is complete.

## Penalties

A late-filing penalty of 50 for individuals. A punitive tax increase of 2% to
10% of the added income where income was negligently omitted. Late payment
interest at the reference rate plus 7 percentage points. Vero is comparatively
mild about honest errors corrected promptly, and MyTax allows corrections after
the deadline with a smaller penalty than a discovered omission.
