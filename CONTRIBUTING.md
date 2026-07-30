# Contributing

The most valuable contribution to this repository is keeping the numbers right.
Rates, thresholds and ceilings change every year in every country, and a stale
figure is the failure mode that matters.

## Updating a country for a new tax year

Almost always a JSON edit and nothing else:

1. Open `data/countries/<iso2>.json`.
2. Update `tax_year`, the brackets, contribution ceilings, allowances and
   credits from the URL in `sources`.
3. Update `reporting.deadlines` — the dates shift with the year.
4. Run the checks:

```bash
python -m taxcalc validate
python -m taxcalc calc <ISO2> --employment 80000
python -m pytest tests/ -q
```

The validator catches bracket ordering, rates entered as percentages instead of
decimals, a missing open-ended top band, and schedules that produce negative or
decreasing tax. Eyeball the calculation output too — the effective and marginal
rates should look plausible for that country.

If a change makes a country's `warnings` stale, update them. Those warnings are
printed with every result and are how users know what the model leaves out.

## Adding a country

1. Copy the closest existing file. A progressive-brackets country with a
   municipal rate is close to `fi.json`; a flat-plus-surcharge country is close
   to `no.json`; a country with no income tax is close to `ae.json`.
2. Fill in every top-level block. `country`, `iso2`, `tax_year`, `currency`,
   `income_tax`, `reporting` and `sources` are required; the tests also require
   `residency.test` and `quirks`, because a country without them produces
   answers with no way to check them.
3. Create both skill directories — `skills/<name>-tax-calculation/SKILL.md` and
   `skills/<name>-tax-reporting/SKILL.md` — and add their names to the `skills`
   block in the JSON. The tests fail if a country references a skill that does
   not exist, or if a skill exists with no country behind it.
4. Run the suite. The per-country property tests will run against the new file
   automatically.

See [`docs/data-schema.md`](docs/data-schema.md) for every field the engine
understands.

## Writing a skill

Skills are short on purpose. The shared method lives in `references/`; a skill
covers what is *different* about that country.

What belongs in a skill:

- The elections and deadlines that are easy to miss and impossible to fix late
- What the engine gets wrong for this country, and what to do instead
- The question the user is probably actually asking (regime choice for Italian
  and Polish freelancers, employment versus company in Brazil, flat tax election
  in Korea)
- Facts that are commonly out of date in guidance found elsewhere

What does not:

- Rate tables — those live in the JSON and are printed by the engine
- Generic workflow — that lives in `references/`
- Hedging. Say what is true, note the limits once, and move on

The frontmatter `description` is the only thing seen when deciding whether to
load the skill. Write it around the phrases people actually use, including city
names, portal names and local terminology, not just the word "tax". The tests
enforce a minimum length because a thin description means the skill never fires.

## Adding an engine feature

Add country-specific logic to the data, not to `taxcalc/`. The engine should
only grow when a country has a genuinely new *shape* — as happened for Germany's
formula schedule, Scotland replacing the UK schedule, and France's per-child
splitting.

When adding a shape:

- Put the primitive in `schedules.py` and unit-test it with an invented example
  in `tests/test_schedules.py`, not with a real country
- Wire it into `engine.py` in the existing pipeline order
- Extend `validate.py` if the new shape has a way of being silently wrong

## Style

Explain why, not just what. Someone reading a country file or a skill six months
from now should be able to tell whether a number is still right and what it was
meant to capture.
