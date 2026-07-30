---
name: singapore-tax-reporting
description: Handle Singapore tax filing — the 18 April e-filing deadline, Form B1 and B, the Auto-Inclusion Scheme, tax clearance (IR21) before leaving Singapore, and IRAS penalties. Use this whenever someone asks when Singapore taxes are due, whether they need to file, how the Year of Assessment works, what tax clearance means when leaving a job or the country, how to pay by GIRO, or what happens if they file late.
---

# Singapore tax reporting and filing — Year of Assessment 2026

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Singapore.

## Get the calendar

```bash
python -m taxcalc deadlines SG
```

## Year of Assessment, not tax year

YA 2026 assesses income earned in calendar 2025. Singaporeans speak in YAs and
foreigners speak in tax years, and the two are always one apart. State which you
mean every time — this single ambiguity causes more confusion than anything else
in Singapore tax conversation.

| Date | What |
| --- | --- |
| 1 March 2026 | Employers submit income under the Auto-Inclusion Scheme |
| 15 April 2026 | Paper filing deadline |
| 18 April 2026 | E-filing deadline |
| Within 30 days of the Notice of Assessment | Payment, or start a GIRO plan |

GIRO spreads the payment across up to twelve interest-free instalments. Most
people should use it; it is set up once and rolls forward.

## Tax clearance is the one that traps people

Before a **foreign employee** leaves Singapore or changes employer, the employer
must file **Form IR21** at least one month in advance and **withhold all monies
due** until IRAS issues clearance.

Consequences worth explaining:

- The final salary is held back, sometimes for weeks
- Clearance covers tax on income up to the departure date, assessed immediately
  rather than in the following April
- Leaving without clearance creates a liability that follows the employee and
  can prevent re-entry on a future pass

Anyone changing jobs or leaving Singapore should plan cash flow around this.

## Who files

Anyone who receives a filing notification, anyone with annual income above
22,000, and anyone with self-employment income of any amount. Employees of
companies in the Auto-Inclusion Scheme have salary data pre-filled and often
only need to check and confirm.

The No-Filing Service goes further — some taxpayers receive a direct notice of
assessment and file nothing at all.

## Records

The self-employed must keep business records for **five years**, and IRAS
enforces this. Donations to Institutions of a Public Character are deductible at
**250%** of the amount given, which is unusually generous and worth raising.

## Penalties

Late filing: a fine up to 1,000, plus an estimated assessment which must be paid
even if disputed. Late payment: a 5% penalty and 1% per month up to an additional
12%. Understatement: up to 200% of the tax undercharged, or 400% where there was
intent to evade. IRAS operates a voluntary disclosure programme with substantially
reduced penalties for someone who comes forward before an audit.
