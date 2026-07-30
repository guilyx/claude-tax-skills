---
name: us-tax-reporting
description: Prepare US tax filing — Form 1040 deadlines, which schedules and forms apply, FBAR and FATCA foreign account reporting, extensions, quarterly estimated payments, and late-filing penalties. Use this whenever someone asks when their US taxes are due, what forms they need, whether they have to file at all, how to file from abroad, what happens if they missed a deadline or have unfiled returns, what an extension actually buys them, or whether their foreign bank account needs reporting — including for expats, contractors, and anyone who mentions the IRS.
---

# US tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to the United States.

## Get the calendar

```bash
python -m taxcalc deadlines US
python -m taxcalc deadlines US --json
```

## The deadline that actually applies

- **15 April 2026** for the 2025 return and, critically, for payment.
- **15 June 2026** automatic for citizens and residents living abroad. This is a
  filing extension only — interest runs from 15 April.
- **15 October 2026** if Form 4868 was filed. Again, filing only.

Form 4868 does not extend the time to pay. Say this explicitly every time an
extension comes up; the belief that it does is widespread and costs people the
0.5%-per-month failure-to-pay penalty plus interest.

## Foreign accounts: the part that catches people

Two separate obligations, both independent of whether any tax is owed:

- **FBAR (FinCEN 114)** — triggered by aggregate foreign account balances
  exceeding 10,000 at any moment in the year. Filed with FinCEN, not the IRS.
  Due 15 April, automatically extended to 15 October. Penalties reach 10,000 per
  non-wilful violation and far more if wilful.
- **Form 8938 (FATCA)** — higher thresholds, varies by filing status and whether
  you live abroad, filed with the return.

Someone with a foreign account can owe zero tax and still face five figures of
penalties. Raise this unprompted whenever the person mentions living abroad or
holding a foreign account.

## If they are behind

There are established routes back into compliance, and saying so is more useful
than warning them. The Streamlined Filing Compliance Procedures cover
non-wilful failures for taxpayers abroad, typically three years of returns and
six years of FBARs, often with no penalty. For domestic taxpayers, filing the
delinquent returns and requesting first-time abatement of penalties works in
many cases. Do not tell someone their situation is hopeless — it rarely is.

## Forms

Run `python -m taxcalc deadlines US` for the full list. The usual set: 1040 plus
Schedule 1 for adjustments, Schedule C and SE for contractors, Schedule D and
Form 8949 for investments, Form 2555 or 1116 for expats, Form 8938 and FinCEN 114
for foreign assets.

## Estimated tax

Due 15 April, 15 June, 15 September and 15 January. Safe harbour: pay 100% of
last year's tax (110% if AGI exceeded 150,000) or 90% of this year's, and the
underpayment penalty does not apply regardless of what you finally owe. This is
the single most useful thing to tell a new contractor.
