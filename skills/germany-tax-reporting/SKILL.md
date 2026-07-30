---
name: germany-tax-reporting
description: Handle German tax return filing — whether a Steuererklärung is mandatory or voluntary, ELSTER, the Anlage forms, the 31 July deadline and the four-year voluntary window, and Finanzamt penalties. Use this whenever someone asks if they must file a German tax return, when it is due, which Anlage forms they need, how to use ELSTER, whether filing late is a problem, how to claim a refund for previous years, or what they can deduct — including for freelancers, expats and people who have left Germany.
---

# German tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Germany.

## Get the calendar

```bash
python -m taxcalc deadlines DE
```

## Mandatory or voluntary — this is the first question

Filing is **mandatory** if any of these apply:

- Tax class combination III/V, or IV with a factor
- More than one employer in the year (tax class VI on a second job)
- Wage replacement benefits over 410: Elterngeld, Kurzarbeitergeld,
  Arbeitslosengeld, Krankengeld
- Side income over 410 not subject to wage tax
- Self-employed or freelance income
- A Freibetrag was entered on the Lohnsteuerkarte during the year

Otherwise it is **voluntary** — and worth doing. The average refund is around
1,000, and the voluntary window is four years, so someone in 2026 can still file
for 2022, 2023, 2024 and 2025. Anyone who worked only part of a year, moved for
work, or had large commuting costs is very likely owed money.

This asymmetry matters: the mandatory deadline is 31 July, but a voluntary filer
has years and no late penalty at all. Establishing which category someone is in
changes the entire answer.

## Deadlines

| Date | What |
| --- | --- |
| 31 July 2026 | 2025 return if filing yourself (mandatory cases) |
| 30 April 2027 | 2025 return if a Steuerberater or Lohnsteuerhilfeverein files |
| 31 December 2029 | Last date for a voluntary 2025 return |

Using a tax adviser genuinely buys nine months. Mention it when someone is close
to the deadline and panicking.

## The Anlage system

The main form (ESt 1 A / Hauptvordruck) is short; the substance is in annexes:
Anlage N employment, Anlage S freelance, Anlage G trade, Anlage KAP investments,
Anlage V rental, Anlage AUS foreign income, Anlage Vorsorgeaufwand insurance,
Anlage Kind per child. Run `python -m taxcalc deadlines DE` for the full list.

ELSTER is free and pre-fills most employment data from the Lohnsteuerbescheinigung
your employer already transmitted. Commercial tools are easier but the underlying
data is the same.

## Deductions people miss

Commuting (Entfernungspauschale), the home office flat rate, professional
training, work equipment, a work-related move, union and professional fees,
double household costs during a relocation, childcare, and Handwerkerleistungen
(20% of the labour element of tradesman invoices, up to 1,200 off the tax).

## Penalties

Verspätungszuschlag of 0.25% of assessed tax per month, minimum 25 per month;
Säumniszuschlag of 1% per month on unpaid amounts; interest at 0.15% per month
from 15 months after year end. Note that interest runs **both ways** — a slow
assessment in your favour earns interest too.
