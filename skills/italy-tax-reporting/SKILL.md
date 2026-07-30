---
name: italy-tax-reporting
description: Handle Italian tax filing — Modello 730 versus Modello Redditi PF, the September and October deadlines, Quadro RW foreign asset monitoring, F24 payments, and Agenzia delle Entrate penalties. Use this whenever someone asks when the Italian tax return is due, which model they should use, whether they must file at all, how to report foreign accounts or property, what ravvedimento operoso means, or how to access the precompilata.
---

# Italian tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Italy.

## Get the calendar

```bash
python -m taxcalc deadlines IT
```

## Which return: 730 or Redditi PF

- **Modello 730** — for employees and pensioners. Its advantage is that the
  refund or charge flows straight through **payroll**, usually in July, rather
  than requiring a payment or waiting for a refund. It is largely pre-filled.
- **Modello Redditi PF** — for everyone else: partita IVA holders, people with
  foreign income or assets, and anyone the 730 cannot accommodate.

Recent years have widened what the 730 can handle, including some foreign
income. If someone is an employee, start by checking whether the 730 works,
because the payroll settlement is a genuine convenience.

## Deadlines

| Date | What |
| --- | --- |
| 30 June 2026 | Balance for 2025 and first advance for 2026 |
| 30 September 2026 | Modello 730 |
| 31 October 2026 | Modello Redditi PF |
| 30 November 2026 | Second advance payment for 2026 |

Note that **payment comes before filing** for Redditi PF filers — the balance is
due 30 June but the return is not due until 31 October. Estimating and paying on
time while finalising the return later is normal.

## Quadro RW

Foreign accounts, property, crypto and investments must be declared in Quadro
RW, which serves double duty: it is both the monitoring declaration and where
IVIE (0.76% on foreign property) and IVAFE (0.2% on foreign financial assets)
are computed.

Penalties run from 3% to 15% of the undeclared assets, doubled for blacklisted
jurisdictions — assessed on the **asset value**, not on any income. This is the
single most expensive Italian filing failure for foreigners.

## Ravvedimento operoso

Italy's voluntary correction regime scales the penalty down according to how
quickly you fix the error — a fraction of the standard penalty if corrected
within 30 days, rising with delay but still far below the full amount for years
afterwards. Anyone who realises they have made a mistake should be told about
this immediately; the cost of correcting rises with time but never approaches
the cost of being found out.

## The precompilata

Agenzia delle Entrate prepares a pre-filled return from employer, healthcare,
insurance and mortgage data. Accepting it unchanged removes the risk of
documentary checks on the pre-filled items, which is a real benefit — but it
also means accepting figures that may be incomplete. Access needs SPID, CIE or CNS.

## Penalties

Late filing: 120% to 240% of the tax due, minimum 250 where no tax is owed.
Late payment: 25% of the unpaid amount, heavily reduced under ravvedimento.
