---
name: luxembourg-tax-reporting
description: Handle Luxembourg tax filing — who must file, the 31 December deadline, Modèle 100 and the décompte annuel, MyGuichet access, tax class changes, and ACD penalties. Use this whenever someone asks when the Luxembourg tax return is due, whether they need to file, how a cross-border commuter files, what a décompte annuel is, how to request resident treatment, or what happens if they file late.
---

# Luxembourg tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Luxembourg.

## Get the calendar

```bash
python -m taxcalc deadlines LU
```

## The deadline is unusually generous

**31 December 2026** for the 2025 tax year — a full extra year. Luxembourg is
the most relaxed deadline among the countries covered here, and the same date
applies to the simplified décompte annuel.

That generosity has a downside: people forget entirely. Someone who has not
filed for several years may still be within time for some of them.

## Two routes: Modèle 100 or décompte annuel

- **Modèle 100** — the full return. Required where income exceeds 100,000, where
  there were multiple employers, where there is non-employment income above
  thresholds, or where you want deductions that payroll did not apply.
- **Décompte annuel (Modèle 163)** — a simplified payroll adjustment for
  straightforward employees. Faster, but it only reconciles withholding; it
  cannot carry most deductions.

If someone has deductible interest, insurance premiums, pension contributions or
childcare costs, the full return is worth the extra effort.

## Cross-border commuters

Non-residents working in Luxembourg file here for Luxembourg-source employment
income, and separately in their country of residence for worldwide income with
treaty relief. Two filings, not one.

The request to be **assimilated to a resident** — which restores tax class 2 and
allows deductions — is made on the return itself, and requires meeting the 90%
income threshold (50% for Belgian residents). It is elective each year, so it can
be tested and reconsidered.

## Changing tax class or rate during the year

Form 166 requests a change to the tax card (fiche de retenue) — after a
marriage, a birth, a change in the spouse's income, or to enter a deduction
(Freibetrag) that reduces monthly withholding rather than waiting for a refund.
For most people this is more useful than anything on the return.

## Access

MyGuichet with LuxTrust or an eID. The matricule (13-digit national identifier)
is needed throughout.

## Penalties

A surcharge of up to 10% of the tax due for late filing, 0.6% per month for late
payment, and a taxation d'office — an assessment on estimated income — where no
return is filed at all. Objections to an assessment must be lodged within
**three months** of the bulletin d'impôt, which is a short window and easy to miss.
