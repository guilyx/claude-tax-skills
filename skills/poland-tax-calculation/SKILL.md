---
name: poland-tax-calculation
description: Calculate Polish PIT, ZUS social contributions and the non-deductible health contribution, plus net pay. Use this whenever someone asks what they will take home in Poland, how a Warsaw, Kraków, Wrocław or Gdańsk offer compares, whether a B2B contract beats an employment contract, what the under-26 exemption is worth, which self-employment tax regime to choose, or how a Polish offer compares — including when they only mention ZUS, a umowa o pracę or a PIT-11.
---

# Polish income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Poland.

## Run the engine

```bash
python -m taxcalc calc PL --employment 180000
python -m taxcalc calc PL --self-employment 300000
python -m taxcalc info PL
```

## The health contribution is the hidden 9%

Since 2022 the 9% health contribution is charged on income **and is not
deductible from tax**. It sits on top of income tax and on top of the other ZUS
contributions, so the real marginal burden on employment income is well above
the headline 12% or 32%.

Anyone reasoning from the two-band scale alone will substantially underestimate
Polish tax. Showing income tax, social contributions and health separately is
the most useful structure for the answer.

## B2B versus employment: the question Polish professionals actually ask

A large share of Polish IT and professional work is done through self-employment
(B2B) rather than an employment contract, because the tax difference is enormous:

- **Employment (umowa o pracę)**: progressive 12%/32%, full ZUS, 9%
  non-deductible health, plus employer contributions of ~20%.
- **B2B with the 19% flat tax**: flat rate regardless of income, ZUS at a fixed
  monthly amount unrelated to profit, health at 4.9%.
- **B2B with ryczałt** (lump sum on revenue): 2% to 17% of *revenue* with no
  expense deduction — 12% for most IT services, 8.5% for many others.

For a developer on 300,000 PLN a year the gap between employment and ryczałt can
exceed 50,000 PLN. The trade-offs are real too: no paid leave, no notice period,
weaker credit standing, and the fixed ZUS is punishing at low income.

Whenever someone describes Polish professional work, this comparison is likely
the question underneath.

## The under-26 exemption

Employment and mandate-contract income is exempt from income tax up to 85,528 a
year for anyone under 26. Social and health contributions still apply. For a
young professional this is worth several thousand zloty and is applied
automatically unless waived.

## Other specifics

- **Joint filing with a spouse** effectively doubles the first bracket, valuable
  where incomes are unequal.
- **Ulga na powrót** exempts up to 85,528 a year for four years for people moving
  their tax residence to Poland after living abroad — including returning Poles.
- **Pension and disability contributions are capped** at 260,190, so the marginal
  wedge falls above that; health is uncapped.

## What the engine leaves out

The three self-employment regimes, the under-26 and return reliefs, and the
regime-specific health contribution bases. The abolished middle-class relief
appears in older guidance and no longer exists.
