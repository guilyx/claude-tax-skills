# Reporting workflow

Shared method for the 30 country reporting skills. The country skill supplies
the local specifics; this file supplies the structure.

## 1. Pull the calendar from the data

```bash
python -m taxcalc deadlines DE
python -m taxcalc deadlines JP --json
```

This returns the tax year end, the authority, the portal, who must file, dated
deadlines, the form list and the penalty regime. Quote it rather than
reconstructing it from memory — deadlines are the part of tax advice where being
approximately right is worthless.

## 2. Answer the question that actually comes first: must they file at all?

In several countries most employees never file: Germany (unless a trigger
applies), Japan, Korea, Czechia, Sweden, Norway, Denmark, the UK and the
Netherlands all settle the majority of employees through payroll or an
automatic assessment. Telling someone to file when they need not — or worse,
missing that they must — is the highest-impact part of the answer.

Check the `who_must_file` field, then check the triggers in the country skill.

## 3. Work out which deadline actually applies

Deadlines are rarely a single date. The common variations:

- **Filing through an adviser** buys months in Germany, Austria, Czechia,
  Australia, New Zealand and Ireland.
- **Electronic versus paper** differ in Czechia, Spain, Ireland, Belgium and the US.
- **Self-employment or foreign income** extends the deadline in Denmark,
  Belgium and the Netherlands.
- **Filing extension is not a payment extension** almost everywhere. Interest
  runs from the original date. Say this explicitly — it is the single most
  common and most expensive misunderstanding in the whole subject.
- **Region-specific dates** apply in France (by département) and Switzerland
  (by canton).

## 4. Build the document checklist

The `documents_to_collect` field lists what that country actually needs. Two
things are worth flagging in your answer wherever they apply:

- **Documents that cannot be reconstructed later.** Portugal's e-fatura
  invoices, Korea's card spending records and Sweden's property improvement
  receipts must be captured during the year.
- **Separate filings with their own penalties.** FBAR and Form 8938 in the US,
  Form 3916 in France, Modelo 720 in Spain, T1135 in Canada, Quadro RW in Italy,
  Schedule FA in India. These are penalised independently of whether any tax was
  owed, and the penalties are often larger than the tax would have been.

## 5. Cover payment as well as filing

Filing and paying are separate obligations with separate penalties. Include:

- The balancing payment date
- Instalment or advance payment dates (payments on account, estimated tax,
  provisional tax, Vorauszahlungen, carnê-leão)
- What the penalty and interest actually cost, from the `penalties` field

## Output template

Use this structure unless the user asked for something narrower:

```
## Filing obligation
Whether they must file, and on what basis.

## Key dates
| Date | What is due | Notes |

## Forms
The specific forms, with what each one is for.

## Documents to gather
Checklist, flagging anything that must be collected during the year.

## Penalties for getting it wrong
Late filing, late payment, and any separately-penalised disclosure.

## Watch out for
The two or three country-specific traps that apply to this person.
```

## Tone

The user is usually anxious and often late. Lead with what they need to do and
by when. Do not open with a paragraph of caveats, and do not imply a missed
deadline is unrecoverable — voluntary disclosure and late-filing routes exist
almost everywhere, and saying so is more useful than a warning.
