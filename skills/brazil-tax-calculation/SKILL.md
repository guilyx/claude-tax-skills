---
name: brazil-tax-calculation
description: Calculate Brazilian IRPF, INSS contributions and net pay, including carnê-leão for foreign or individual-sourced income and the pejotização company route. Use this whenever someone asks what they will take home in Brazil, how a São Paulo or Rio offer compares, why Brazilian professionals invoice through a company, what a PJ or MEI pays, how a foreign salary is taxed for a resident in Brazil, or how the offshore investment rules work — including when they only mention the Receita Federal, CPF or holerite.
---

# Brazilian income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Brazil.

## Run the engine

```bash
python -m taxcalc calc BR --employment 180000
python -m taxcalc calc BR --self-employment 250000
python -m taxcalc info BR
```

## The top rate arrives early

27.5% applies above roughly R$55,976 of annual taxable income — low by
international standards. Combined with employee INSS, the marginal wedge on a
professional salary reaches its maximum quickly and stays there.

## Which is why so much work is done through a company

**Pejotização** — invoicing through a company rather than being employed — is
widespread among Brazilian professionals because the arithmetic is stark:

- **CLT employment**: up to 27.5% IRPF plus INSS, and employer costs of roughly
  70% of salary on top
- **Simples Nacional or Lucro Presumido company**: effective tax on service
  revenue often in the 6–16% range, and **dividends distributed to the owner are
  currently exempt** in the hands of the individual

The trade-offs are real: no paid holiday, no 13th salary, no FGTS, no notice
period, and the arrangement can be recharacterised as employment by the labour
courts where subordination exists. Note also that dividend exemption has been
under active reform discussion — treat it as current but not permanent.

Whenever someone describes Brazilian professional work, this comparison is
usually what they are really asking about.

## Carnê-leão: a monthly obligation, not an annual one

Income received **from individuals or from abroad** — rent from a private
tenant, fees from foreign clients, a foreign salary — is self-assessed and paid
**monthly**, by the last working day of the following month. Interest and
penalties run from each monthly due date, not from the annual return.

This catches remote workers who are Brazilian tax residents earning from
overseas employers. They frequently assume they can settle everything in April
and arrive with a year of accrued interest. Raise it whenever foreign income is
mentioned.

## The simplified discount is a choice made once

Either the 20% simplified discount (capped at R$16,754.34) **or** itemised
deductions including dependants, education and medical costs — not both. Medical
expenses are uncapped, so households with significant healthcare costs usually
itemise; almost everyone else takes the simplified route.

## Offshore income is now taxed annually

Since 2024, income from offshore financial investments and controlled foreign
companies is taxed at 15% **each year whether or not it is distributed**. The
old deferral through foreign holding structures is gone. Anyone with an
offshore structure set up before 2024 should be told the position changed.

## What the engine leaves out

The company route entirely, municipal ISS for the self-employed, and the
mutually exclusive nature of the simplified discount and dependant deductions —
do not add both.
