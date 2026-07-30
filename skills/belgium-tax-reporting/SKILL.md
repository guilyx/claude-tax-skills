---
name: belgium-tax-reporting
description: Handle Belgian tax filing — the June and July deadlines, Tax-on-web, the simplified proposed assessment, declaring foreign accounts to the National Bank, advance payments for the self-employed, and SPF Finances penalties. Use this whenever someone asks when the Belgian tax return is due, how to file with itsme or an eID reader, what a proposition de déclaration simplifiée means, how to declare a foreign account or foreign property, or what happens if they file late.
---

# Belgian tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Belgium.

## Get the calendar

```bash
python -m taxcalc deadlines BE
```

## Deadlines

| Date | What |
| --- | --- |
| 30 June 2026 | Paper return for income year 2025 |
| 15 July 2026 | Online return via Tax-on-web |
| Mid-October 2026 | Extended online deadline for returns with self-employment or foreign income |
| 10 Apr / Jul / Oct / 20 Dec | Advance payments for the self-employed |

The extended October deadline applies automatically to returns containing
professional income from self-employment or foreign income — it is not something
you have to request.

## The simplified proposed assessment

Many taxpayers receive a **proposition de déclaration simplifiée** rather than a
blank return. It becomes final unless corrected, which is convenient and also
dangerous: it is generated from third-party data and does not know about your
deductible childcare, pension savings, service vouchers or foreign income.

Tell people to check it rather than ignore it. Correcting it is a normal
procedure with its own deadline printed on the document.

## Foreign accounts get declared twice

- On the **tax return**, ticking the box and naming the country
- Separately to the **Central Point of Contact at the National Bank of Belgium**,
  a one-off registration per account

Both are required. The National Bank registration is a distinct obligation that
people who have correctly completed their tax return still miss. Foreign life
insurance policies and foreign property must also be declared, and since 2021
foreign property is assigned a deemed cadastral income.

## Advance payments matter for the self-employed

An indépendant who makes no advance payments incurs a tax increase of around 9%
on the amount due. Making them quarterly avoids this entirely, and the earlier
quarters attract larger credits. Anyone newly self-employed should be told to
start advance payments in their first profitable year rather than discovering
the surcharge afterwards.

## Access

Tax-on-web needs itsme (a phone app) or a card reader with an eID. itsme is far
easier and is worth setting up before the deadline rather than during it.

## Penalties

Administrative fines of 50 to 1,250 for late filing, plus an ex officio
assessment on estimated income — which shifts the burden of proof onto you.
Tax increases of 10% to 200% for understatement depending on intent and
repetition. Interest at the statutory rate on late payment.
