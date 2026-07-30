---
name: norway-tax-calculation
description: Calculate Norwegian income tax — the 22% ordinary income tax, trinnskatt bracket tax, national insurance and net salary — plus wealth tax and the 25% PAYE scheme for new arrivals. Use this whenever someone asks what they will take home in Norway, how an Oslo, Bergen, Stavanger or Trondheim offer compares, what the wealth tax costs them, whether the simplified PAYE scheme is better, what the exit tax means, or how a Norwegian offer compares — including when they only mention Skatteetaten or a skattekort.
---

# Norwegian income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Norway.

## Run the engine

```bash
python -m taxcalc calc NO --employment 750000
python -m taxcalc calc NO --employment 1200000
python -m taxcalc info NO
```

## Two taxes on two different bases

This is the structural quirk that makes Norway confusing:

- **Ordinary income tax at 22%** is charged on income **after** the minimum
  deduction and personal allowance.
- **Trinnskatt** (1.7% to 17.5%) is charged on **gross personal income before
  any deductions**.

So deductions only reduce part of your bill. A pension contribution or a
mortgage interest deduction saves 22%, not the headline marginal rate. Anyone
reasoning about Norwegian deductions from a marginal-rate intuition will get it
wrong, and pointing this out is usually the most useful thing in the answer.

## The 25% PAYE scheme for new arrivals

New foreign workers are placed on a simplified flat 25% scheme (including
national insurance) by default in their first year. It requires no return at all.

It is simple, but it allows **no deductions**. For anyone with mortgage interest,
a long commute, or a spouse and children abroad, the ordinary system is usually
cheaper. The choice can be revisited — someone can opt out of the scheme and
file ordinarily. This is worth raising with any new arrival, because the default
is not the optimum for most people who own property.

## Wealth tax is not a footnote

Roughly 1% on net worldwide assets above 1.76m NOK, rising to 1.1% above 20.7m.
It applies to unlisted shares and foreign property, and for someone with
substantial savings it can exceed their income tax. It is not in the engine.

Norway's wealth tax is also the reason for genuine high-net-worth emigration in
recent years, and for the **exit tax** on unrealised gains when tax residence
ends. Anyone with appreciated assets planning to leave needs to know about this
before they go.

## Other specifics

- **Skattekort**: the deduction card sets withholding and can be adjusted at any
  time during the year. Someone whose income changes should update it rather than
  wait for the assessment.
- **Tax lists are public** — income, wealth and tax paid are searchable by anyone
  logged in with an ID, and the taxpayer can see who looked them up.
- **The pre-filled return is deemed submitted if you do nothing**, which means
  unclaimed deductions are silently lost rather than flagged.

## What the engine leaves out

Wealth tax, the 25% PAYE scheme, the trygdeavgift phase-in just above the
threshold, and the shielding deduction on share income.
