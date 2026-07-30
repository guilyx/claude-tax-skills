---
name: uae-tax-reporting
description: Handle UAE tax compliance — corporate tax registration and filing for individuals in business, VAT returns, Tax Residency Certificates, and EmaraTax deadlines and penalties. Use this whenever someone asks whether they need to file anything in the UAE, how a freelancer or sole trader registers for corporate tax, when the corporate tax return is due, how to get a tax residency certificate, what the VAT obligations are, or what the penalties are for missing registration.
---

# UAE tax reporting and compliance — 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to the United Arab Emirates.

## Get the calendar

```bash
python -m taxcalc deadlines AE
```

## Employees file nothing

There is no personal income tax return in the UAE. A salaried employee has no
filing obligation of any kind. Say this plainly rather than hedging — it is the
answer to most questions.

## Individuals in business do have obligations

A natural person carrying on a business with turnover above **1,000,000 AED** in
a calendar year must:

| Obligation | Timing |
| --- | --- |
| Register for corporate tax on EmaraTax | By 31 March of the following year |
| File the corporate tax return | Within 9 months of the end of the tax period |
| Pay the tax | Same deadline as the return |

Late registration alone is a **10,000 AED penalty**, charged even where no tax
is ultimately due. Late returns run at 500 per month for the first year and
1,000 per month thereafter.

Registration is the trap: someone crossing the turnover threshold has an
obligation even before they have any tax to pay.

## VAT

Registration is mandatory above 375,000 AED of taxable supplies and voluntary
above 187,500. Returns are quarterly for most businesses, due 28 days after the
period ends. Separate penalties apply to late registration, late filing and late
payment.

## Tax Residency Certificate

Applied for through the FTA portal. For an individual under domestic rules you
need 183 days of presence, or 90 days with UAE nationality, residency or a
permanent home plus a job or business. Supporting evidence: Emirates ID,
residence visa, an entry-and-exit report from ICP or GDRFA, a tenancy contract
or title deed, six months of UAE bank statements, and a salary certificate.

Two versions exist — one for domestic purposes and one for a specific treaty
partner. Ask which country will receive it, because the treaty version names it.

## Other filings

Economic substance reporting and ultimate beneficial owner filings apply to
certain entities, and e-invoicing requirements are being phased in. These are
entity obligations rather than individual ones, but a freelancer operating
through a company is caught by them.

## What to tell someone who has just crossed the threshold

Register first — the 10,000 penalty is for registration, not for the tax.
Then work out the tax period, which for a natural person is the calendar year.
Small business relief may be available below 3,000,000 AED of revenue, which
treats the business as having no taxable income, but it still requires
registration and a return.
