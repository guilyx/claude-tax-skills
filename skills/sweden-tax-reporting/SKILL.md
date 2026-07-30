---
name: sweden-tax-reporting
description: Handle Swedish tax filing — the pre-filled inkomstdeklaration, the 2 May deadline, approving by app or SMS, K4 and K5 schedules for securities and property sales, ROT and RUT deductions, and Skatteverket penalties. Use this whenever someone asks when the Swedish tax return is due, how to approve it, what they need to add manually, how to report a property or share sale, how to get a personnummer or BankID for filing, or what happens if they file late.
---

# Swedish tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Sweden.

## Get the calendar

```bash
python -m taxcalc deadlines SE
```

## Filing is genuinely easy, with two exceptions

The return arrives pre-filled in early March with salary, benefits, interest,
dividends and most Swedish securities sales already entered. If nothing needs
changing it can be approved by app, SMS or phone in under a minute.

| Date | What |
| --- | --- |
| Early March 2026 | Pre-filled return available digitally |
| Early April 2026 | Approve unchanged by here for the earliest refund, usually paid in April |
| 2 May 2026 | Filing deadline for 2025 |
| 12 February 2026 | Extra payment deadline to avoid interest on large underpayments |

The two things that are **not** pre-filled and must be added:

- **Property sales (K5/K6)** — the sale price is reported but the deductible
  costs are not. Renovation and improvement expenditure over the years of
  ownership can be substantial, and receipts must have been kept. This is where
  Swedish taxpayers most often overpay.
- **Foreign securities and foreign income** — nothing from a non-Swedish broker
  or employer appears automatically.

## ROT and RUT

Deductions for home renovation (ROT) and household services (RUT) are normally
applied by the contractor at the point of invoice, so they appear as a discount
rather than something you claim. Check the return reflects the right amount —
the annual cap is per person, and exceeding it results in a claw-back.

## Getting set up

Everything depends on a personnummer and BankID. A newly arrived worker without
a personnummer receives a coordination number instead, which limits access.
BankID requires a Swedish bank account, which requires a personnummer — a
sequence that takes weeks and is worth starting immediately on arrival.

## The tax lists

Sweden publishes assessed income publicly. This surprises new arrivals and is
worth mentioning matter-of-factly if the subject of privacy comes up.

## Penalties

Förseningsavgift of 1,250, rising in stages to 3,750 for continued delay.
Skattetillägg of 40% of the underpaid tax for incorrect information, 20% for
capital income — but it is not charged where the error was in information
Skatteverket already held, which covers most pre-filled items. Interest applies
to underpayments above 30,000 from February.
