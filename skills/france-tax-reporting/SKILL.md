---
name: france-tax-reporting
description: Handle French tax return filing — the déclaration des revenus, form 2042 and its annexes, the staggered May and June deadlines by département, declaring foreign bank accounts on form 3916, and DGFiP penalties. Use this whenever someone asks when the French tax declaration is due, which forms they need, whether they must file even with no tax to pay, how to declare foreign income or a foreign account, what happens if they file late, or how to set up their impots.gouv.fr space.
---

# French tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to France.

## Get the calendar

```bash
python -m taxcalc deadlines FR
```

## Everyone files, including people who owe nothing

Unlike Germany, the UK or Japan, France expects an annual declaration from every
fiscal household resident in France, even where tax is fully withheld and even
where nothing is owed. The avis d'imposition it produces is also the document
banks, landlords and administrations ask for, so filing has practical value
beyond the tax itself.

## Deadlines are staggered by département

The exact dates are published each April, but the pattern is stable:

| Group | Approximate deadline |
| --- | --- |
| Départements 01–19 and non-residents | Late May |
| Départements 20–54 | Early June |
| Départements 55–976 | Early June, a few days later |
| Paper filers (where still permitted) | Mid-May |

Always give the pattern and tell the user to confirm their own date on
impots.gouv.fr rather than asserting a specific day.

The avis d'imposition arrives in late summer, and any balance is due in
September.

## Form 3916: the one that costs the most to forget

Every foreign bank account, foreign life insurance policy and foreign crypto
account held at any point during the year must be declared on form 3916,
**whether or not it produced income and whether or not it has any money in it**.
The penalty is 1,500 per account per year, rising to 10,000 for accounts in
non-cooperative states, and it is charged independently of any tax.

This catches nearly every foreigner living in France who kept a home-country
current account or a Revolut or Wise balance. Raise it unprompted.

## Forms

2042 is the main return. Add 2042-C for complementary items, 2042-C-PRO for
self-employed and rental micro-regimes, 2044 for rental income under the régime
réel, 2047 for foreign income, 2074 for securities gains, and 3916 for foreign
accounts. Run `python -m taxcalc deadlines FR` for the list.

## Check the pre-filled figures

The return arrives pre-filled from employer and bank data. It is usually right
for salary and wrong or incomplete for anything else — foreign income, rental
income, childcare and donations all need adding. Correcting a pre-filled figure
is normal and does not trigger scrutiny.

## Penalties

10% increase for late filing, rising to 40% if still unfiled 30 days after
formal notice, and 80% where undisclosed activity is found. Late payment adds
10% plus 0.20% per month. A correction filed spontaneously before any enquiry
attracts reduced interest — the télécorrection service reopens after the
deadline for exactly this purpose.
