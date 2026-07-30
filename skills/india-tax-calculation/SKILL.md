---
name: india-tax-calculation
description: Calculate Indian income tax under the new and old regimes, including surcharge, cess, EPF and take-home pay. Use this whenever someone asks what they will take home on an Indian salary, whether the new or old tax regime is better for them, how HRA and 80C deductions compare with the new regime's lower rates, what an NRI or RNOR pays, how capital gains on shares or property are taxed, what advance tax they owe, or how an Indian offer compares — including when they only mention the IT department, Form 16 or a CTC breakup.
---

# Indian income tax calculation — FY 2025-26 (AY 2026-27)

Read `references/calculation-workflow.md` for the general method. This file
covers what is specific to India.

## Run the engine

```bash
python -m taxcalc calc IN --employment 1800000
python -m taxcalc calc IN --employment 3500000
python -m taxcalc info IN
```

The engine implements the **new regime**, which is the default since 2023-24.

## New regime or old: the question behind most Indian tax questions

- **New regime** (default): slabs from 4 lakh, nil tax up to ₹12,00,000 after the
  section 87A rebate, standard deduction ₹75,000, and almost no other deductions.
- **Old regime** (elective, via Form 10-IEA): higher rates but HRA exemption,
  section 80C up to ₹1,50,000, 80D health insurance, home loan interest up to
  ₹2,00,000, and the rest.

The old regime typically wins where someone has a home loan, pays substantial
rent in a metro, and uses the full 80C. The new regime wins for most people
without those. Salaried taxpayers can switch **each year**; those with business
income can opt out only once.

Whenever an Indian salary question comes up, compute both rather than assuming.

## CTC is not salary

Indian offers are quoted as cost to company, which includes the employer's EPF
contribution, gratuity provision and often insurance premiums. Take-home from a
₹20,00,000 CTC is substantially less than ₹20,00,000 minus tax.

Ask for the salary structure — basic, HRA, special allowance — because HRA
exemption under the old regime depends on the basic component, and EPF is
charged on basic rather than total pay. The engine applies EPF to a proxy
ceiling; in practice it is 12% of basic, typically 40–50% of CTC.

## Surcharge and cess

The engine adds the 4% health and education cess but leaves surcharge at zero so
it is visible without double-counting. Apply manually:

- 10% of tax above ₹50,00,000
- 15% above ₹1,00,00,000
- 25% above ₹2,00,00,000 (capped at 25% under the new regime)

**Marginal relief** limits the surcharge so that the increase in tax cannot
exceed the increase in income above the threshold. Just above each threshold
this matters.

## Residency: three statuses, not two

Resident and Ordinarily Resident (worldwide income), **RNOR** (foreign income not
taxed), and Non-Resident (Indian-source only). RNOR is a transitional status
that returning NRIs hold for two to three years, and it is a genuine window for
repatriating foreign assets before worldwide taxation begins.

## Other specifics

- **Financial year 1 April to 31 March**, reported in the following
  "assessment year". Do not mix the two labels.
- **LRS remittances** above ₹10,00,000 a year attract 20% tax collected at
  source, creditable but a real cash flow cost.
- **Capital gains** changed in July 2024: 20% short-term and 12.5% long-term on
  listed equity, with a ₹1,25,000 annual exemption.

## What the engine leaves out

The old regime entirely, surcharge and marginal relief, and the fact that EPF is
charged on basic pay rather than gross.
