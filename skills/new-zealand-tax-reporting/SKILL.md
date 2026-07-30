---
name: new-zealand-tax-reporting
description: Handle New Zealand tax filing — automatic income tax assessments, when an IR3 is required, the 7 July deadline and the tax agent extension, provisional tax, and IRD penalties. Use this whenever someone asks when their New Zealand tax return is due, whether they need to file at all, how the automatic assessment works, how to report foreign income or a property sale, what provisional tax means, or what happens if they file late.
---

# New Zealand tax reporting and filing — 2025-26 tax year

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to New Zealand.

## Get the calendar

```bash
python -m taxcalc deadlines NZ
```

## Most people get an automatic assessment and file nothing

Inland Revenue receives payday-filed employer data and issues an **automatic
income tax assessment** in May or June to anyone whose income was all
PAYE-taxed. If it shows a refund, it is paid without any action.

An **IR3 return** is required where there is business or rental income, foreign
income, income without PAYE deducted, or FIF income.

| Date | What |
| --- | --- |
| May–July 2026 | Automatic assessments issued |
| 7 July 2026 | IR3 for the year ended 31 March 2026 |
| 31 March 2027 | Extended deadline if linked to a tax agent |
| 7 February 2027 | Terminal tax (7 April with a tax agent) |
| 28 Aug / 15 Jan / 7 May | Provisional tax instalments |

Check the automatic assessment rather than ignoring it — it does not know about
donation credits, and it can be wrong where someone was on the wrong tax code.

## Tax codes and the secondary income problem

Someone with two jobs uses a secondary tax code on the second, which withholds
at a flat rate that is frequently wrong in either direction. The automatic
assessment squares it up, but a large bill at year end usually traces back to
this. Anyone with multiple income sources should check their codes in myIR
during the year.

## Provisional tax

Once residual income tax exceeds 5,000, provisional tax applies for the
following year in three instalments. The standard option uses last year's tax
plus 5%, which underpays a growing business. The accounting income method (AIM)
computes from actual results and avoids use-of-money interest — worth mentioning
to anyone with volatile income.

## Foreign income and FIF

Nothing foreign is pre-populated. Anyone with overseas investments, a foreign
pension, or overseas rental income files an IR3 and computes FIF income
themselves. The comparative value or fair dividend rate methods give different
answers and can be chosen — but not switched arbitrarily year to year.

## Penalties

Late filing: 50 to 500 depending on net income. Late payment: 1% immediately, a
further 4% after seven days, then use-of-money interest compounding. Shortfall
penalties run from 20% for lack of reasonable care to 150% for evasion, and are
reduced substantially for voluntary disclosure made before an audit begins.
