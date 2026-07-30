---
name: brazil-tax-reporting
description: Handle Brazilian tax filing — the March to May annual declaration, carnê-leão monthly payments, the asset schedule, the exit declaration on leaving Brazil, and Receita Federal penalties. Use this whenever someone asks when the Brazilian tax return is due, whether they must file, how to declare foreign income or assets, what happens when they leave Brazil, how to pay a DARF, or what the penalties are for filing late.
---

# Brazilian tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Brazil.

## Get the calendar

```bash
python -m taxcalc deadlines BR
```

## The declaration is a wealth statement as well as an income return

Alongside income, you list **every asset and right held at 31 December with its
acquisition cost** — property, vehicles, bank balances, shares, crypto, holdings
abroad. Balances are carried forward year to year, and Receita Federal
cross-checks the change in net worth against declared income.

An unexplained increase in assets relative to income is the classic trigger for
falling into the *malha fina* review queue. Keeping the asset schedule accurate
and consistent from year to year matters as much as reporting the income.

## Deadlines

| Date | What |
| --- | --- |
| 15 March – 30 May 2026 | Annual declaration (DIRPF) for 2025 |
| 30 May 2026 | First or single instalment; up to eight instalments with interest |
| Last working day of the following month | Carnê-leão for income from individuals or abroad |
| Last working day of the following month | Capital gains tax on disposals (DARF 4600) |
| Last day of February | Exit declaration for those who left in the prior year |

Note the two monthly obligations. Capital gains are paid the month after the
sale, not at the annual filing — someone who sold a property in March and plans
to deal with it in May has already missed the payment.

## Leaving Brazil: the most expensive mistake in this file

Departure requires two filings:

- **Comunicação de Saída Definitiva** — notification, filed from the date of
  departure until the end of February of the following year
- **Declaração de Saída Definitiva** — the exit return itself, covering the
  period of residence

Without them you remain a Brazilian tax resident **indefinitely**, liable to
declare worldwide income and to file every year. People discover this years
later, typically when trying to regularise a CPF or repatriate money, and by
then there are multiple years of returns and penalties.

Anyone who has left Brazil, or is planning to, should be asked whether they
filed the exit declaration.

## Who must file

Taxable income above roughly R$33,888, exempt income above R$200,000, assets
above R$800,000 at year end, any capital gain, or any stock exchange trading.
The asset threshold catches people with no income at all.

## Penalties

Late filing: 1% of the tax due per month, minimum R$165.74, maximum 20%.
Late payment: 0.33% per day up to 20%, plus SELIC interest. Omitted income: 75%
of the tax, 150% where fraud is found. Carnê-leão penalties and interest run
from each **monthly** due date, which is why a year of unpaid carnê-leão costs
far more than a single late annual return.
