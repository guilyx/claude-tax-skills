---
name: japan-tax-calculation
description: Calculate Japanese national income tax, inhabitant tax, the reconstruction surtax and social insurance, plus net pay. Use this whenever someone asks what they will take home in Japan, how a Tokyo or Osaka offer compares, why their second-year tax jumped, what the five-year non-permanent resident rule means for foreign income, what furusato nozei is worth, how a foreign pension or investment is taxed, or how a Japanese offer compares — including when they only mention the NTA, gensen choshu hyo or juminzei.
---

# Japanese income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Japan.

## Run the engine

```bash
python -m taxcalc calc JP --employment 8000000
python -m taxcalc calc JP --employment 15000000
python -m taxcalc info JP
```

## Inhabitant tax arrives a year late

Juminzei is a flat 10% billed the **following June** for the calendar year just
ended. Three consequences that come up constantly:

1. **Year one in Japan feels cheap.** There is no inhabitant tax at all, because
   you were not resident on the assessment date. People budget from their first
   year's take-home and are then surprised.
2. **Year two costs more** for the same salary, by roughly 10% of income.
3. **Leaving Japan generates a bill after you have gone.** Appoint a tax agent
   (nozei kanrinin) before departure, or arrange a lump-sum deduction from final
   pay. This is the most important thing to tell anyone leaving.

## The five-year cliff

A **non-permanent resident** — a foreign national resident five years or less
within the last ten — is taxed on Japanese income plus only the foreign income
paid in or remitted to Japan. After five years, worldwide income becomes fully
taxable, including foreign capital gains and investment income.

This makes the timing of asset sales genuinely decisive. Someone approaching
five years with appreciated foreign holdings should know the date, because
selling before it and after it are very different outcomes.

An **exit tax** also applies to residents holding ¥100m or more of financial
assets who have been resident more than five of the last ten years.

## Furusato nozei is close to free money

You redirect part of your inhabitant tax to a municipality of your choice and
receive local goods in return, at a net cost of ¥2,000. The limit depends on
income and family circumstances. It is not a loophole; it is government policy,
widely used, and most foreign residents have never heard of it.

## Most employees never file

The employer's **year-end adjustment (nenmatsu chosei)** in December settles the
liability. A final return is required above ¥20,000,000 of salary, with side
income over ¥200,000, with two or more employers, or to claim medical expense,
donation or first-year housing loan deductions.

## Other specifics

- **NISA** gives a permanent exemption on investment income within generous
  annual limits, and is the default retail investing account.
- **Listed securities** are otherwise taxed at 20.315%, usually withheld inside
  a tokutei kouza account so no filing is needed.
- **Dependants abroad** can be claimed but require documentation and remittance
  evidence since the rules tightened.

## What the engine leaves out

Spouse, dependant and insurance deductions, which reduce most households' real
bill; the per-capita inhabitant tax levy of about ¥5,000; and the employment
income deduction is a close approximation of a tiered formula.
