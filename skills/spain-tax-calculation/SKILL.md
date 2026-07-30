---
name: spain-tax-calculation
description: Calculate Spanish IRPF, social security contributions and net salary, including the Beckham law regime for inbound workers. Use this whenever someone asks what they will take home in Spain, how a Madrid, Barcelona, Valencia or Málaga offer compares, why regional tax differs, whether they qualify for the Beckham law or the digital nomad visa tax regime, what an autónomo pays, or how Spanish tax treats their foreign income and assets — including when they only mention Hacienda, the AEAT or a nómina.
---

# Spanish income tax calculation — tax year 2025

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to Spain.

## Run the engine

```bash
python -m taxcalc calc ES --employment 65000
python -m taxcalc calc ES --employment 90000 --children 2
python -m taxcalc calc ES --self-employment 55000
python -m taxcalc info ES
```

## Half the scale is regional

The state sets half the IRPF scale and each autonomous community sets the other
half. Madrid, Andalusia and Murcia have cut their share; Catalonia, Valencia and
Asturias are higher. The difference on a 90,000 salary between Madrid and
Catalonia runs to a couple of thousand euros a year.

The engine uses a common combined scale. Always ask which community, and say
that the figure is indicative unless you have substituted the right regional
table.

## The Beckham regime, and the six-month window

The special regime for inbound workers taxes Spanish employment income at a flat
24% up to 600,000 (47% above) and generally excludes foreign income, for the
year of arrival plus five. It typically wins above roughly 60,000 of salary.

**It must be elected within six months of registering with social security.**
That window cannot be reopened. If someone is moving to Spain, or has recently
moved, this is the most time-critical thing you can tell them — check the date
before discussing anything else.

Note that the digital nomad visa has its own route into a similar regime, and
that Beckham-regime taxpayers generally cannot use double tax treaty relief in
the normal way.

## There is no split tax year

Arrive on 1 July and stay, and you are Spanish tax resident for the **entire
calendar year**, including foreign income earned before the move. Someone
relocating in the second half of a year may be much better off delaying to
January, or may already be resident without realising it.

This single point changes the optimal moving date. Raise it unprompted whenever
a move to Spain is mentioned.

## Autónomos

Since 2023 the monthly social security quota depends on declared net income
bands rather than being a flat choice, running from roughly 200 to 590 a month,
and it is reconciled against actual income afterwards. New autónomos get a
reduced flat rate for the first year or two. The engine uses a blended rate;
for anyone actually registering, direct them to the current band table.

## What the engine leaves out

The regional half of the scale (a common combination is used), the mínimo
personal applied as a rate-band reduction rather than a deduction, savings
income which has its own scale, wealth tax and the state solidarity tax on large
fortunes, and the Beckham regime itself.
