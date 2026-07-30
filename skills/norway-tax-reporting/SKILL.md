---
name: norway-tax-reporting
description: Handle Norwegian tax filing — the pre-filled skattemelding, the 30 April deadline, what is not pre-filled, adjusting the skattekort, additional advance payments, and Skatteetaten penalties. Use this whenever someone asks when the Norwegian tax return is due, whether they need to do anything at all, how to claim deductions, how to report foreign income or a foreign mortgage, how to get a D-number or electronic ID, or what happens if they file late.
---

# Norwegian tax reporting and filing — tax year 2025

Read `references/reporting-workflow.md` for the general method. This file covers
what is specific to Norway.

## Get the calendar

```bash
python -m taxcalc deadlines NO
```

## Doing nothing is a valid filing — and that is the risk

The pre-filled skattemelding is published in mid-March and is **deemed submitted
at the deadline if you do not touch it**. There is no late penalty for someone
who simply accepts it.

That convenience is also the trap: deductions you never claimed are not flagged,
they are just lost. The return is only as good as the third-party data behind it.

| Date | What |
| --- | --- |
| Mid-March 2026 | Pre-filled return published |
| 30 April 2026 | Corrections deadline for individuals |
| 31 May 2026 | Deadline for the self-employed, and to request an extension to 30 June |
| By 31 May 2026 | Additional advance payment to avoid interest on underpayments |
| June–October 2026 | Assessments issued in batches; refunds follow |

## What is not pre-filled

- **Foreign mortgage interest** — Norwegian mortgages appear automatically,
  foreign ones do not. This is a significant deduction for anyone who kept
  property abroad.
- **Commuting, home-away-from-home costs and travel** for those who qualify,
  including visits home for workers with family abroad.
- **Foreign income, foreign property and foreign accounts**, along with the
  foreign tax paid for credit relief.
- **Valuations of unlisted shares and foreign property** for wealth tax.

## The skattekort matters more than the return

Withholding is set by the tax deduction card, which is issued in December based
on estimated income. Anyone whose income has changed should update it in the
portal — otherwise they either lend the state money interest-free all year or
face an underpayment with interest. This is a more useful action than anything
to do with the return itself.

## Getting set up

A fødselsnummer or D-number plus an electronic ID (MinID, BankID) is required
for everything. Foreign workers frequently arrive on a D-number, which works but
limits some services.

## Penalties

An enforcement fine (tvangsmulkt) of roughly 1,277 per day up to about 63,850
for failing to submit where submission is required. Additional tax of 20% for
incorrect information, rising to 40–60% where intentional. Norway operates a
voluntary disclosure route that waives the additional tax for someone coming
forward before being contacted.
