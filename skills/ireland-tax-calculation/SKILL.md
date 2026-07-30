---
name: ireland-tax-calculation
description: Calculate Irish income tax, USC, PRSI and net pay from gross. Use this whenever someone asks what they will take home on an Irish salary, how a Dublin, Cork or Galway offer compares, what their marginal rate is, how tax credits and the standard rate band work for a married couple, what a sole trader or contractor owes, how the remittance basis works for non-domiciled residents, or whether an Irish offer is competitive — including when they only mention Revenue, myAccount or a payslip.
---

# Irish income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Ireland.

## Run the engine

```bash
python -m taxcalc calc IE --employment 70000
python -m taxcalc calc IE --employment 110000 --status married_joint
python -m taxcalc calc IE --self-employment 85000
python -m taxcalc info IE
```

## Three separate charges

Irish pay is reduced by income tax (20% then 40%), USC (0.5% to 8% on gross,
with its own bands), and PRSI (4.1%). USC applies to income that income tax
reliefs have already sheltered, including pension contributions, which is why
pension relief in Ireland is worth less than the headline marginal rate suggests.

Separating the three is usually the most useful part of the answer, because
payslips show them separately and people conflate them.

## Credits and the band: the married-couple decision

Ireland relieves tax through **credits** rather than allowances, and both credits
and the standard rate band can be allocated between spouses. The one-income
couple band is 53,000; a two-income couple can raise it to 88,000, but only up
to the lower earner's income.

The practical consequence: where one spouse earns much more, transferring the
unused portion of the band and the personal credit to the higher earner saves
real money, and it is not always done automatically. Raise it whenever a couple
is mentioned. Note that the **PAYE credit cannot be transferred** and is lost if
a spouse has no employment income.

## Ireland kept the remittance basis

Non-domiciled residents are taxed on foreign income and gains only to the extent
remitted to Ireland. The UK abolished its equivalent in April 2025, which has
made Ireland substantially more attractive for internationally mobile people —
this is a genuinely current and relevant point for anyone comparing the two.

Domicile is not the same as residence and is hard to shed; someone born and
raised in Ireland is Irish-domiciled regardless of where they live.

## Ordinary residence catches people leaving

Acquired after three consecutive years of Irish residence and retained for three
years after departure. Someone who leaves Ireland can remain liable on certain
income for years. Raise it for anyone planning to move away.

## What the engine leaves out

The two-income married band increase (model each spouse separately as single
where that is more accurate), PRSI weekly thresholds and the tapered credit for
low earners, medical expense relief at 20%, the rent tax credit, and pension
relief which is age-banded from 15% to 40% of earnings.
