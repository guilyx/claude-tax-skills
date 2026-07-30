---
name: netherlands-tax-reporting
description: Handle Dutch tax return filing — the aangifte inkomstenbelasting, the 1 May deadline, DigiD access, the M-formulier for migration years, provisional assessments, and Belastingdienst penalties. Use this whenever someone asks when the Dutch tax return is due, whether they need to file, how to file the year they arrived in or left the Netherlands, what a voorlopige aanslag is, how to get a DigiD, or what happens if they file late.
---

# Dutch tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to the Netherlands.

## Get the calendar

```bash
python -m taxcalc deadlines NL
```

## Deadlines

| Date | What |
| --- | --- |
| 1 March 2026 | Return opens; pre-filled data available |
| 1 April 2026 | File by here and the Belastingdienst aims to reply before 1 July |
| 1 May 2026 | Standard deadline for the 2025 return |
| 1 July 2026 | Extended deadline if requested before 1 May |
| 1 May 2027 | Collective arrangement deadline via a tax adviser |

Requesting an extension takes two minutes online and is granted automatically.
Mention it to anyone who will not make 1 May.

## The M-formulier: the year you arrive or leave

If someone became or stopped being a Dutch resident during the year, the normal
return does not apply — the M-formulier does. It is longer, it used to be
paper-only, and it frequently produces a substantial refund because the tax
credits are calculated for a full year against part-year income.

Anyone who moved to or from the Netherlands mid-year should be told about this
specifically. It is easy to miss and it is usually money in their pocket.

## Filing when you do not have to is often worth it

Filing is compulsory only if you receive an aangiftebrief or owe more than the
threshold. But voluntary filing is common and frequently produces a refund,
especially where there were mortgage interest payments, study costs, healthcare
costs above the threshold, deductible gifts, or a partial working year.

## The voorlopige aanslag

A provisional assessment spreads a refund or a payment across the year in monthly
instalments rather than settling it all afterwards. Homeowners with mortgage
interest relief use it to receive the benefit monthly. Anyone with significant
untaxed income uses it to avoid a lump-sum bill. Worth raising in both cases.

## Access

Everything runs through DigiD, and getting one requires a BSN and a postal
activation code sent to a Dutch address — which takes days and cannot be
short-circuited. Tell new arrivals to start this early; it blocks almost every
other administrative task in the country too.

## Penalties

A verzuimboete of up to 385 for a first late filing, more for repeats.
Belastingrente accrues from 1 July following the tax year. Deliberate
misstatement can reach 100% of the underpaid tax. The Belastingdienst is
generally reasonable about genuine errors corrected voluntarily.
