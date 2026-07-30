# Country data schema

Every file in `data/countries/` describes one country for one tax year. The
engine understands only the fields below; anything else is carried through
untouched and can be read by a skill.

Money amounts are **annual**, in the country's own currency. Rates are
**decimals** — `0.42`, never `42`. The validator rejects anything outside 0–1,
because a percentage entered by mistake is silently catastrophic.

## Top level

| Field | Required | Purpose |
| --- | --- | --- |
| `country`, `iso2`, `tax_year`, `currency` | yes | identity |
| `skills` | yes (by tests) | `{calculation, reporting}` skill directory names |
| `residency` | yes (by tests) | residence tests, worldwide income position, special regimes |
| `headline` | no | short summary strings shown by `taxcalc info` |
| `income_tax` | yes | the national schedule |
| `standard_deduction` | no | employment expense or standard deduction |
| `personal_allowance` | no | personal and family allowances |
| `social_security` | no | employee, employer and self-employed contributions |
| `surcharges` | no | levies charged on tax, taxable income or gross income |
| `credits` | no | amounts deducted from tax rather than income |
| `local_tax` | no | a single municipal or regional rate |
| `regions` | no | named sub-national schedules or rates |
| `capital_gains` | no | descriptive strings, not computed |
| `quirks` | yes (by tests) | the country-specific traps skills quote |
| `reporting` | yes | filing calendar, forms, penalties |
| `sources` | yes | official URLs for verification |
| `warnings` | no | what the model leaves out, printed with every result |

## Schedules

A schedule turns taxable income into tax. Four `type` values:

```jsonc
// progressive - up_to is the cumulative threshold where the band ends,
// as printed in published rate tables. The last band must be open-ended.
{"type": "progressive", "brackets": [
  {"up_to": 12450, "rate": 0.19},
  {"up_to": null,  "rate": 0.47}
]}

// flat
{"type": "flat", "rate": 0.22}

// none - the country levies no tax at this layer
{"type": "none"}

// piecewise_polynomial - a continuous formula (Germany's EStG §32a).
// tax = poly((x - offset) / divisor) + constant, coeffs highest power first.
// Include the constant term: [0.42, 0] is 0.42y, [0.42] is the constant 0.42.
{"type": "piecewise_polynomial", "zones": [
  {"up_to": 12096, "coeffs": [], "constant": 0},
  {"up_to": null, "offset": 0, "divisor": 1, "coeffs": [0.45, 0], "constant": -19246.67}
]}
```

### Filing statuses

Where a country publishes different tables per status, nest them:

```jsonc
"income_tax": {
  "type": "progressive",
  "default_filing_status": "single",
  "by_filing_status": {
    "single":        {"brackets": [...]},
    "married_joint": {"brackets": [...]}
  }
}
```

The keys the CLI passes are `single`, `married_joint`, `married_separate`,
`head_of_household`, `single_parent`. An unknown status falls back to
`default_filing_status`.

### Income splitting

```jsonc
"by_filing_status": {"married_joint": {"income_splitting_factor": 2}},
"income_splitting_per_child": 0.5
```

Income is divided by the number of shares, the schedule applied, then the tax
multiplied back up. Used by Germany, France, Portugal, Luxembourg and Switzerland.

## Deductions and allowances

```jsonc
"standard_deduction": {
  "name": "Abattement de 10%",
  "amount": 504,        // floor
  "rate": 0.10,         // percentage of employment income; the larger of the two wins
  "cap": 14426,
  "taper": {"threshold": 100000, "rate": 0.5, "floor": 0}
}

"personal_allowance": {
  "amount": 12570,
  "per_child": 2400,
  "per_dependant": 1500,
  "taper": {"threshold": 100000, "rate": 0.5, "floor": 0}
}
```

A `taper` withdraws the amount above a threshold at `rate` per unit of income,
never below `floor`. This is what produces the UK's 60% band and the Dutch
credit phase-outs.

## Social security

```jsonc
"social_security": {
  "employee": [{
    "name": "National Insurance Class 1",
    "rate": 0.08,
    "floor": 12570,
    "floor_mode": "reduce_base",   // or "exempt_below" (default)
    "ceiling": 50270,
    "max_amount": 5000,
    "deductible": false,           // does it reduce taxable income?
    "note": "..."
  }],
  "employer": [...],
  "self_employed": [...]
}
```

`floor_mode` matters: `exempt_below` charges nothing under the floor and the
full base above it; `reduce_base` charges only the excess. Band-shaped
contributions combine a `reduce_base` floor with a ceiling.

A fixed annual amount uses `{"type": "fixed", "amount": 1136}`.

Employer lines are reported for total-cost-of-employment but never affect the
employee's result.

## Surcharges

```jsonc
"surcharges": [{
  "name": "Solidaritätszuschlag",
  "base": "tax",                 // "tax" | "taxable_income" | "gross_income"
  "rate": 0.055,
  "threshold": 19950,
  "above_threshold_only": false, // false: charge the whole base once past the threshold
  "schedule": {...}              // optional, instead of a flat rate
}]
```

## Credits

```jsonc
"credits": [{
  "name": "Child tax credit",
  "amount": 600,
  "per_child": 2200,
  "per_dependant": 0,
  "rate": 0.09,          // percentage of gross income
  "cap": 45000,
  "refundable": false,   // non-refundable credits stop at zero tax
  "filing_status": "married_joint",
  "taper": {...}
}]
```

Non-refundable credits are applied first against available tax; refundable ones
can push the liability below zero.

## Regional tax

Two mechanisms:

```jsonc
// a single rate applied to taxable income, overridable with --local-rate
"local_tax": {"name": "Kommunalskatt", "default_rate": 0.3241, "extra_allowance": 0}

// named regions: either a full schedule, or a rate
"default_region": "ON",
"regions": {
  "ON":  {"name": "Ontario", "schedule": {"type": "progressive", "brackets": [...]}},
  "ZH":  {"name": "Zurich", "rate": 0.14},
  "SCT": {"name": "Scotland", "replaces_national": true, "schedule": {...}}
}
```

`replaces_national` swaps out the national schedule instead of adding to it —
Scotland is the only current user.

## Reporting

```jsonc
"reporting": {
  "tax_year_end": "5 April",
  "authority": "HM Revenue and Customs (HMRC)",
  "portal": "https://...",
  "who_must_file": "...",
  "deadlines": [{"date": "31 January 2027", "what": "...", "note": "..."}],
  "forms": [{"id": "SA100", "name": "..."}],
  "documents_to_collect": ["..."],
  "penalties": {"late_filing": "...", "late_payment": "..."}
}
```

The tests require `authority`, `tax_year_end`, at least three `deadlines`,
`penalties` and `who_must_file`, because the reporting skills quote all of them.

## Computation order

```
gross income
  − deductible social security contributions
  − standard deduction
  − personal allowance (after taper)
  − user deductions
= taxable income
  → national schedule (with splitting)
  + regional schedule or local rate
  + surcharges
  − credits
= total income tax
net = gross − employee social security − total income tax
```

The marginal wedge is measured by recomputing at gross + 100, so contribution
ceilings, allowance tapers and surcharge thresholds are all reflected in it.
