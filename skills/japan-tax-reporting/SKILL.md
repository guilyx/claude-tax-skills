---
name: japan-tax-reporting
description: Handle Japanese tax filing — the kakutei shinkoku window from 16 February to 15 March, the year-end adjustment, e-Tax, inhabitant tax billing, overseas asset reporting, and NTA penalties. Use this whenever someone asks when the Japanese tax return is due, whether they need to file at all, what nenmatsu chosei is, how to claim medical or furusato nozei deductions, what to do about tax when leaving Japan, or what happens if they file late.
---

# Japanese tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Japan.

## Get the calendar

```bash
python -m taxcalc deadlines JP
```

## Most employees file nothing

The year-end adjustment (**nenmatsu chosei**) in December settles the liability
through payroll. In November the employer circulates declaration forms for
dependants, insurance premiums and housing loans — completing these correctly is
what most people need to do, and it is the moment when deductions are actually
claimed.

A **final return (kakutei shinkoku)** is required where:

- Salary exceeds ¥20,000,000
- Side income exceeds ¥200,000
- There were two or more employers
- You want medical expense, donation, or first-year housing loan deductions
- You have foreign income taxable in Japan

| Date | What |
| --- | --- |
| November–December 2025 | Year-end adjustment forms |
| 16 February – 15 March 2026 | Final return for 2025 |
| 15 March 2026 | Payment, or first instalment |
| June 2026 | Inhabitant tax bills issued for 2025 income |

## Leaving Japan

Two separate things must be handled:

- **Inhabitant tax** for the year just ended and the current year will be billed
  after you leave. Appoint a **tax agent (nozei kanrinin)** with the local ward
  office before departure, or arrange a lump-sum deduction from final salary.
- **A departure return** may be required if you leave mid-year with income to
  report, filed before departure or by the tax agent afterwards.

Someone who leaves without doing either can find an unpaid bill blocking a
future visa. This is the highest-value thing to raise with anyone departing.

## Overseas asset reporting

Residents holding more than ¥50,000,000 of overseas assets at 31 December must
file an overseas assets report by 15 March. There is a separate reporting
requirement for assets and liabilities where income exceeds ¥20,000,000.
Penalties for omission are lighter than in Europe but the reporting itself is
mandatory.

## The two documents that matter

- **Gensen choshu hyo** — the withholding statement from each employer. Without
  it, nothing can be filed or verified. It is issued in January or on leaving.
- **My Number card** — needed for e-Tax and increasingly for everything else.
  The NTA's return preparation corner works in a browser and produces a filing
  that can be submitted electronically or printed and posted.

## Penalties

Additional tax of 15% to 20% for late filing, reduced to 5% where the return is
filed voluntarily before the NTA acts. Understatement penalties of 10% to 15%,
rising to 35–40% where there was concealment. Delinquent tax on late payment at
roughly 2.4% to 8.7% a year depending on how long.
