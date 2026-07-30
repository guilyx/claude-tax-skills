---
name: uk-tax-reporting
description: Handle UK Self Assessment — whether a return is required at all, the 31 January deadline, SA100 and its supplementary pages, payments on account, registering with HMRC, capital gains reporting on property within 60 days, and late-filing penalties. Use this whenever someone asks if they need to file a UK tax return, when it is due, what happens if they missed 31 January, how to register as self-employed, what a payment on account is, or how to report a property sale or foreign income to HMRC.
---

# UK Self Assessment reporting — tax year 2025/26

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to the United Kingdom.

## Get the calendar

```bash
python -m taxcalc deadlines GB
```

## First question: do they need to file?

Most UK employees never file — PAYE settles everything. A return is required if
any of these apply:

- Self-employed with turnover above 1,000
- A partner in a partnership
- Untaxed income: rental, foreign, significant savings or dividends
- Capital gains above the 3,000 annual exempt amount
- Total income above 150,000
- Liable to the High Income Child Benefit Charge (60,000–80,000)
- HMRC has issued a notice to file — once issued, the obligation exists even if
  no tax is due, and it must be formally withdrawn to be cancelled

Someone who has been filing out of habit but no longer meets any trigger can ask
HMRC to withdraw the notice. That is often the most useful answer.

## The dates that matter

| Date | What |
| --- | --- |
| 5 October 2026 | Register for Self Assessment for 2025/26 |
| 31 October 2026 | Paper return |
| 31 January 2027 | Online return, balancing payment, and first payment on account |
| 31 July 2027 | Second payment on account |
| 60 days from completion | UK residential property capital gains return and payment |

The 60-day property deadline is separate from the annual return and is missed
constantly. Raise it whenever a property sale is mentioned.

## Payments on account

The first year of self-employment produces a bill of roughly 150% of the tax
due: the balancing payment for the year just ended plus 50% on account for the
next. Nobody expects this. Explain it before it happens rather than after, and
mention that a claim to reduce payments on account is available if income has
genuinely fallen — with interest charged if the reduction proves too optimistic.

## Penalties, and how to deal with them

- 100 immediately at 31 January, even with no tax owing
- 10 per day from three months, up to 900
- 5% of the tax or 300 (whichever is greater) at six and twelve months
- Separate late payment penalties of 5% at 30 days, six months and twelve months

Reasonable excuse appeals succeed more often than people expect, and HMRC
publishes what it accepts. If someone is late, the useful advice is: file
immediately to stop the daily penalties accruing, pay what they can, and appeal
if there is a genuine reason.

## Forms

SA100 plus the pages that apply: SA102 employment, SA103 self-employment,
SA105 UK property, SA106 foreign, SA108 capital gains, SA109 residence. Run
`python -m taxcalc deadlines GB` for the full list with the employer-issued
documents (P60, P45, P11D).
