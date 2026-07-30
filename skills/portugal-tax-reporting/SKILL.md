---
name: portugal-tax-reporting
description: Handle Portuguese tax filing — the Modelo 3 window from 1 April to 30 June, the anexos required, e-fatura invoice validation in February, declaring foreign income and accounts on Anexo J, and Finanças penalties. Use this whenever someone asks when the Portuguese IRS declaration is due, which anexos they need, how to validate e-fatura invoices, how to declare foreign income or a foreign bank account, how to get a NIF, or what happens if they file late.
---

# Portuguese tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Portugal.

## Get the calendar

```bash
python -m taxcalc deadlines PT
```

## The calendar starts in February, not April

| Date | What |
| --- | --- |
| 15 February 2026 | Confirm household composition and dependants in the portal |
| 25 February 2026 | Validate pending e-fatura invoices |
| 15 March 2026 | Check the deduction totals Finanças has computed, and complain if wrong |
| 1 April – 30 June 2026 | File Modelo 3 for 2025 |
| 31 August 2026 | Payment of any balance |

The February and March steps are the ones people miss, and they are the ones
that cannot be fixed later. Deductions for health, education, housing and general
family expenses are computed by Finanças from validated invoices; an invoice that
was never validated simply does not count.

Unlike most countries, the filing window is the **same for every kind of income**
— employment, business, foreign, capital gains. There is no separate later
deadline for the self-employed.

## Anexos

Anexo A employment and pensions, Anexo B simplified self-employment, Anexo C
organised accounts, Anexo G capital gains, Anexo H deductions and benefits,
Anexo J foreign income. Run `python -m taxcalc deadlines PT` for the list.

**Anexo J** is required from every resident with any foreign income, and foreign
bank account IBANs must be reported even where the account produced nothing.
This catches almost every foreign resident in Portugal.

## Getting set up

A NIF is needed before almost anything else — renting, banking, utilities. Non-EU
residents historically needed a fiscal representative to obtain one, though the
rules have eased for EU residents and those with a Portuguese address. Portal
das Finanças access uses the NIF plus a password sent by post, which takes a
week or two; start early.

## Payments on account

Business and professional income attracts payments on account in July, September
and December, based on the prior year. A first-year freelancer avoids them and
then meets them all at once in year two.

## Penalties

Late filing: 150 to 3,750. Late payment: 30% to 100% of the tax due plus interest
of roughly 4% a year. Specific penalties apply for failing to report foreign
account IBANs. Filing voluntarily before Finanças raises an assessment keeps you
at the bottom of these ranges.
