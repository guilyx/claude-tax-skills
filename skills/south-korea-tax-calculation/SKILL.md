---
name: south-korea-tax-calculation
description: Calculate Korean income tax, the 10% local income tax, national pension and health insurance, plus net pay — including the 19% flat rate election for foreign employees. Use this whenever someone asks what they will take home in Korea, how a Seoul offer compares, whether the foreign worker flat tax is better, what the five-year rule means for foreign income, how severance pay is taxed, what year-end settlement involves, or how a Korean offer compares — including when they only mention the NTS, Hometax or yeonmal jeongsan.
---

# Korean income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to South Korea.

## Run the engine

```bash
python -m taxcalc calc KR --employment 80000000
python -m taxcalc calc KR --employment 150000000
python -m taxcalc info KR
```

## Always compute the flat tax alternative

Foreign employees may elect a **flat 19%** (20.9% including local income tax) on
gross employment income, for up to 20 years from first starting work in Korea.
The election ignores all deductions, credits and exemptions.

It wins at high salaries and loses at moderate ones, and the crossover depends
on the individual's deductions — typically somewhere around 120–150m KRW. Never
assume either way. Compute the ordinary result with the engine, then compare
against 20.9% of gross, and present both.

## Local income tax is a surcharge on the tax, not the income

A flat 10% **of the income tax itself**, not of income. The engine applies it.
People reading the bracket table alone will understate their liability by
roughly a tenth.

## Year-end settlement is where deductions actually happen

**Yeonmal jeongsan** in February reconciles the year through the employer.
Employees with a single employer file nothing in May. The Hometax simplified
service pulls most receipts automatically — card spending, insurance, medical,
education, and pension contributions.

What it does not pull, and what foreign residents most often miss:

- **Housing costs** — monthly rent credit, and jeonse loan principal repayments
- **Donations** made outside the tracked system
- Anything paid in cash without a receipt tied to the resident registration number

The credit card deduction is the reason Koreans pay for everything by card:
spending above 25% of salary generates an income deduction, and cash without a
receipt generates nothing.

## The five-year rule on foreign income

A foreign resident who has had a domicile in Korea for **five years or less in
the last ten** is taxed on foreign-source income only where it is paid in or
remitted to Korea. Past that, worldwide income is taxable.

The same shape as Japan's rule, and with the same consequence: the timing of
foreign asset disposals matters, and the five-year date is worth knowing.

## Severance is taxed separately and lightly

Retirement income uses its own schedule with service-length adjustments, not
ordinary rates. Someone comparing a Korean package should count it as real value
— it is a statutory entitlement of roughly one month's salary per year of service.

## What the engine leaves out

The flat tax election, child, pension savings, medical and education credits,
and the employment income deduction is approximated — results below about 45m
KRW overstate the tax.
