---
name: czechia-tax-reporting
description: Handle Czech tax filing — whether a return is needed at all, the April, May and July deadlines, the MOJE daně portal, OSVČ insurance summaries, and penalties. Use this whenever someone asks when the Czech tax return is due, whether their employer settles it for them, what an OSVČ must file, how the data box (datová schránka) affects filing, or what happens if they file late.
---

# Czech tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Czechia.

## Get the calendar

```bash
python -m taxcalc deadlines CZ
```

## First: does the employer settle it?

An employee with a **single employer at a time** who signs the annual
declaration can request the employer's annual payroll settlement (roční
zúčtování) by **15 February**, and files nothing.

A return is required where:

- Two or more employers paid concurrently
- Self-employment income exceeded 50,000 CZK
- Other income exceeded 20,000 CZK
- Income fell into the 23% band
- You have a data box, which changes the filing method (see below)

## Deadlines, and the electronic bonus

| Date | What |
| --- | --- |
| 15 February 2026 | Ask the employer for the payroll settlement instead of filing |
| 1 April 2026 | Paper return for 2025 |
| 1 May 2026 | Electronic return — a full extra month |
| 1 July 2026 | Return filed by a registered tax adviser |
| Within 8 days of filing | Social and health insurance summaries (Přehled) for the self-employed |

Filing electronically buys a month automatically. Using an adviser buys three.

There is also a **five working day grace period** after each deadline during
which no penalty applies — useful to know, though not something to rely on.

## Data boxes changed who must file electronically

Since 2023 every self-employed person and every company has a data box
(datová schránka) created automatically, and having one makes **electronic
filing mandatory**. A paper return from someone with a data box is treated as
defective. Many sole traders acquired one without realising.

## The OSVČ has three filings, not one

The tax return, the social insurance summary (ČSSZ) and the health insurance
summary (to their health insurer) are three separate documents with three
separate recipients, all due within eight days of the tax return. Missing the
insurance summaries is common and separately penalised.

## Penalties

0.05% of assessed tax per day, capped at 5% or 300,000 CZK, with no penalty
inside the five-day grace window. Interest on late payment at the Czech National
Bank repo rate plus 8 percentage points. Penalties below 1,000 CZK are not
collected at all, which covers many small delays.
