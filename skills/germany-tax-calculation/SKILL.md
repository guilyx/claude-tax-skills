---
name: germany-tax-calculation
description: Calculate German income tax (Einkommensteuer), solidarity surcharge, church tax and social insurance contributions to work out net pay from gross. Use this whenever someone asks about German take-home pay, brutto versus netto, what they will earn in Berlin, Munich, Hamburg or Frankfurt, how tax classes (Steuerklasse) affect their payslip, what a Freiberufler or GmbH director owes, whether a German offer is competitive, or how marriage changes their tax — including when they only mention the Finanzamt, ELSTER or a Lohnabrechnung.
---

# German income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Germany.

## Run the engine

```bash
python -m taxcalc calc DE --employment 85000
python -m taxcalc calc DE --employment 140000 --status married_joint
python -m taxcalc calc DE --self-employment 90000
python -m taxcalc info DE
```

## Establish these before computing

- **Married or not.** The Splittingverfahren halves the income before applying
  the scale and then doubles the tax, which is worth thousands where one spouse
  earns much more. Use `--status married_joint`.
- **Church member or not.** Church tax is 8–9% *of the income tax*, not of
  income — roughly 1,500 a year on an 85,000 salary. The engine excludes it.
  Ask, because it is large and people forget it exists.
- **Statutory or private health insurance.** The engine models the statutory
  scheme (gesetzlich). Privately insured taxpayers pay an age- and
  health-related premium instead, which is often cheaper for high earners and
  much more expensive later in life. Above the 73,800 threshold this is a live
  choice and the calculation changes materially.
- **Children.** Germany applies whichever is better of Kindergeld or the
  Kinderfreibetrag automatically (Günstigerprüfung); the engine does neither.

## Tax classes change the payslip, not the year

Steuerklassen I–VI set monthly withholding. A married couple in III/V sees a
very different pair of payslips from IV/IV, but the annual assessment is
identical. When someone asks "which tax class should we choose", the honest
answer is that it affects cash flow through the year and wage-replacement
benefits (Elterngeld, Arbeitslosengeld) which are calculated on net pay — not
the final bill. That framing is usually what they actually need.

## The rate formula, and why the marginal wedge is interesting

Germany has no brackets. EStG §32a defines a continuous polynomial, so the
marginal rate rises smoothly from 14% to 42%. Combined with contribution
ceilings, the marginal wedge does something unusual: it **falls** between the
health ceiling (66,150) and the pension ceiling (96,600), then falls again above
96,600, before the solidarity surcharge starts biting. The engine measures this
numerically. It is worth showing when someone is negotiating a raise.

## Other specifics

- **Progressionsvorbehalt**: tax-free foreign income and benefits such as
  Elterngeld or Kurzarbeitergeld raise the rate applied to your German income.
- **Solidarity surcharge** only applies above roughly 19,950 of assessed tax, so
  most people no longer pay it.
- **Werbungskosten**: the flat 1,230 allowance is often beaten by real costs —
  commuting at 0.30/km (0.38 beyond 20 km), home office, professional training,
  and a move for work are all deductible.

## What the engine leaves out

Church tax, private health insurance premiums, Kindergeld/Kinderfreibetrag, the
solidarity surcharge transition band, and Riester/Rürup relief.
