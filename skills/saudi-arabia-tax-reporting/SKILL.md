---
name: saudi-arabia-tax-reporting
description: Handle Saudi tax compliance — ZATCA registration and filing for businesses, VAT returns, monthly withholding tax returns, e-invoicing (FATOORA), Zakat certificates and penalties. Use this whenever someone asks what they need to file in Saudi Arabia, whether an employee files anything, when the corporate or Zakat return is due, how VAT reporting works, what e-invoicing requires, or what the penalties are for late filing.
---

# Saudi tax reporting and compliance — 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Saudi Arabia.

## Get the calendar

```bash
python -m taxcalc deadlines SA
```

## Employees file nothing

There is no personal income tax return. An employee — Saudi or expatriate — has
no annual filing obligation. Everything below concerns businesses and
individuals carrying on business.

## The filing calendar

| Obligation | Deadline |
| --- | --- |
| Annual income tax or Zakat return | 120 days after the financial year end |
| VAT return | Monthly if annual supplies exceed 40m SAR, otherwise quarterly |
| Withholding tax return | First 10 days of the month following payment |
| GOSI contributions | Monthly |

The 120-day rule means a 31 December year end gives a 30 April deadline.

## The Zakat and tax certificate gates everything else

ZATCA issues a certificate on filing and payment, and it is required to renew
commercial licences, obtain government contracts, receive payments from
government entities, and complete many administrative processes. A business that
falls behind on filing finds itself unable to operate long before any penalty is
assessed.

This makes Saudi compliance unusually self-enforcing, and it is the practical
reason to file on time rather than the penalty schedule.

## E-invoicing

FATOORA phase one (generation) applies to all VAT-registered businesses. Phase
two (integration with ZATCA's platform) is being rolled out in waves by revenue
band, with each wave notified individually at least six months ahead. Invoices
must be generated in a compliant format with a QR code and, in phase two,
cleared through ZATCA before issue for B2B transactions.

Non-compliant invoicing carries its own fixed penalties, separate from VAT.

## Transfer pricing

Entities above the revenue threshold file a transfer pricing disclosure form
with the annual return, plus local and master files where thresholds are met.
Related-party transactions with foreign affiliates are a standard audit focus.

## Penalties

- Late filing: 1% of revenue for every 30 days of delay, capped at 20% of the
  tax due
- Late payment: 1% of the unpaid tax for every 30 days
- VAT: 5% to 25% of the tax due, plus fixed penalties for e-invoicing breaches
- Understatement: up to 25% of the difference

ZATCA has run several penalty amnesty and instalment initiatives in recent
years. If someone is behind, checking whether an initiative is currently open is
worth doing before assuming the full schedule applies.
