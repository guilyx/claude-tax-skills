---
name: switzerland-tax-reporting
description: Handle Swiss tax return filing — cantonal deadlines and extensions, whether a source-taxed employee must file, the Steuererklärung documents, provisional instalments, and penalties. Use this whenever someone asks when the Swiss tax return is due, whether they need to file at all on a B permit, how to get an extension, what documents the canton wants, how to request an ordinary assessment instead of Quellensteuer, or what happens if they file late.
---

# Swiss tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Switzerland.

## Get the calendar

```bash
python -m taxcalc deadlines CH
```

## There is no national deadline

Each canton sets its own. The common pattern is **31 March** following the tax
year (Zurich, Geneva), with Vaud around 15 March and others in between. Always
say which canton the date applies to, and tell the user to confirm on the
cantonal tax administration's own site.

**Extensions are routine.** Most cantons grant them online, often to September
or November, sometimes free and sometimes for a nominal fee. Nobody should miss
a Swiss deadline; the extension takes a few minutes. This is genuinely different
from most countries and is worth stating plainly.

## Who must file

- Swiss citizens and C-permit holders: always.
- B-permit holders taxed at source: only if income exceeds roughly 120,000, or
  they have other income or assets above cantonal thresholds — **or** if they
  request an ordinary assessment.

## The 31 March request that cannot be made late

A source-taxed employee who wants deductions (pillar 3a, pillar 2 buy-in,
childcare, commuting, debt interest) must request a subsequent ordinary
assessment by **31 March following the tax year**. This deadline is strict, it
is separate from the filing deadline, and once passed the year is closed.

Once requested, the choice applies for all subsequent years too, and it cannot be
withdrawn. Mention both halves — it is not automatically a good idea for someone
with no deductions, since it means filing every year thereafter.

## Documents

The Lohnausweis (salary certificate) is the central document; everything else
supports deductions. Year-end statements for every bank account including foreign
ones, pillar 2 and 3a certificates, health insurance premiums, mortgage interest
and the property tax value, and receipts for professional expenses and further
education. Run `python -m taxcalc deadlines CH` for the list.

Note that the return doubles as a **wealth declaration** — you list assets, not
just income. People arriving from countries without wealth tax are routinely
surprised by this.

## Moving cantons

Tax residence for the whole year is generally where you lived on 31 December.
Someone moving from Geneva to Zug in November is taxed by Zug for that year,
which can be worth planning around.

## Penalties

A reminder first, then an assessment on estimated income plus a fine. Cantonal
default interest applies to late payment. For undeclared income the usual
outcome is the evaded tax plus a penalty of the same amount again — but
Switzerland allows one **penalty-free voluntary disclosure per lifetime**, which
is the single most useful thing to tell someone with an undeclared foreign account.
