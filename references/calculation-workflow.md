# Calculation workflow

Every country's calculation skill follows this shape. The country skill supplies
the local judgment; this file supplies the method, so the country files can stay
short and stay focused on what is actually different about that country.

## 1. Establish the facts before computing anything

A tax number computed from the wrong facts is worse than no number, because it
looks finished. Before running anything, you need:

| Fact | Why it changes the answer |
| --- | --- |
| Tax residence | Decides whether worldwide or only local income is taxed |
| Tax year | Several countries do not use the calendar year (UK, AU, NZ, IN, JP local, HK) |
| Gross income and its type | Employment, self-employment and investment income are taxed differently everywhere |
| Filing status and household | Joint filing, splitting and family quotients can move the result by 20%+ |
| Region | State, province, canton, municipality or autonomous community |
| Special regimes | Inbound-expat regimes exist in most European countries and are usually elective and time-limited |

If a fact is missing and it would materially change the answer, ask. If it would
not, state your assumption in one line and carry on — stopping to ask about
something that does not matter wastes the user's time.

## 2. Run the engine, do not do arithmetic in prose

```bash
python -m taxcalc calc DE --employment 85000 --status married_joint --children 2
python -m taxcalc calc US --employment 150000 --status single --region CA --json
python -m taxcalc info PT          # residence rules, headline figures, known traps
python -m taxcalc compare 90000 --countries DE,FR,NL,CH
```

Mental arithmetic across five brackets, a contribution ceiling and a tapered
allowance is exactly the kind of task where a plausible-looking wrong answer is
easy to produce and hard to spot. The engine is deterministic and its output is
auditable line by line. Use `--json` when you need to compute something further
from the result, and `--markdown` when you are dropping a table into a document.

Useful flags: `--self-employment`, `--other-income`, `--region`, `--local-rate`,
`--children`, `--dependants`, `--deductions` (extra deductible amounts),
`--credits` (extra non-refundable credits).

## 3. Read the warnings the engine prints

Every country file carries a `warnings` list describing what the model leaves
out — church tax, wealth tax, a special regime, an approximated deduction. These
are printed under NOTES AND LIMITATIONS. If a warning is material to this user's
situation, say so in your answer rather than letting the number stand unqualified.

## 4. Sanity-check before presenting

- Does the effective rate look plausible for that country and income level?
- Is the marginal wedge sensible? A figure above 70% usually means a tapered
  allowance or a credit cliff — worth explaining, since it often changes what
  the user should do next.
- Does net income reconcile: gross − employee social security − income tax?

## 5. Present the result

Structure that works for almost every request:

1. **The number**, with the currency and tax year stated
2. **How it breaks down** — the engine's table, trimmed to what matters
3. **What moves it** — the two or three levers that actually apply to this
   person (pension contributions, a regime election, a filing status choice)
4. **What this does not cover** — the relevant warnings, briefly
5. **The disclaimer** (see `references/disclaimers.md`)

Give the number first. Someone who asked what they will take home should not
have to read three paragraphs of caveats to find it.

## Multi-country comparisons

Use `compare`, and be careful about three things:

- **No FX conversion is applied.** Amounts are in local currency. Compare rates,
  or convert explicitly and say what rate you used.
- **Social security is not comparable.** Singapore's CPF and New Zealand's
  KiwiSaver are the user's own savings; Australia's superannuation is an
  employer cost; the Netherlands folds contributions into the income tax rate.
  A raw "total burden" column flatters and penalises the wrong countries.
- **Cost of living and what you get for the tax** are outside the model
  entirely. A 0% country with private schooling and healthcare is not obviously
  cheaper than a 40% one.
