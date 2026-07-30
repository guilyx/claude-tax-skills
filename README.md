# claude-tax-skills

Agent skills for personal income tax calculation and reporting across the
30 countries people most often work in — two skills per country, backed by a
deterministic calculation engine rather than by the model doing arithmetic in
prose.

```
60 skills  =  30 countries  ×  { calculation, reporting }
```

## Why it is built this way

A tax answer that is confidently wrong is worse than no answer. Bracket
arithmetic across a tapered allowance, a contribution ceiling and a surcharge is
exactly the kind of task that produces plausible-looking mistakes, so the
numbers do not come from the model:

- **`data/countries/*.json`** — one file per country holding rates, thresholds,
  contribution rules, residence tests, filing calendars and known traps.
- **`taxcalc/`** — a small engine that knows the handful of *shapes* tax systems
  come in and nothing about any specific country. Every country runs through the
  same pipeline, so results are comparable and one reviewer can audit all thirty.
- **`skills/`** — the judgment the data cannot hold: which regime election has a
  deadline, what the engine gets wrong here, what to ask before answering.

Each skill file stays short and country-specific. The shared method lives in
`references/`, so a skill covers what is *different* about that country instead
of repeating a generic workflow thirty times.

## Quick start

```bash
python -m taxcalc list                                     # the 30 countries
python -m taxcalc calc DE --employment 85000               # a full breakdown
python -m taxcalc calc US --employment 150000 --region CA --status married_joint
python -m taxcalc compare 90000 --countries DE,FR,NL,CH,SG
python -m taxcalc info PT                                  # residence rules and traps
python -m taxcalc deadlines JP                             # filing calendar
python -m taxcalc validate                                 # check the data files
```

No dependencies beyond the Python standard library (3.9+). `pytest` is only
needed to run the tests.

Example:

```
$ python -m taxcalc calc DE --employment 85000
==============================================================
Germany - personal tax estimate, tax year 2025
==============================================================

INCOME
  Employment income                              85,000.00 EUR
  Gross income                                   85,000.00 EUR

DEDUCTIONS AND ALLOWANCES
  Deductible social security contributions       14,751.53 EUR
  Arbeitnehmer-Pauschbetrag                       1,230.00 EUR
  Taxable income                                 69,018.48 EUR
...
  Effective income tax rate                             21.27%
  Effective total burden                                39.92%
  Marginal rate on next 100                             48.69%
```

## Coverage

| Region | Countries |
| --- | --- |
| North America | United States, Canada |
| UK & Ireland | United Kingdom (incl. Scotland), Ireland |
| Western Europe | Germany, France, Netherlands, Belgium, Luxembourg, Switzerland, Austria |
| Southern Europe | Spain, Portugal, Italy |
| Nordics | Sweden, Norway, Denmark, Finland |
| Central Europe | Poland, Czechia |
| Asia-Pacific | Japan, South Korea, Singapore, Hong Kong SAR, India, Australia, New Zealand |
| Middle East | United Arab Emirates, Saudi Arabia |
| Latin America | Brazil |

Sub-national detail is modelled where it materially changes the answer: US
states, Canadian provinces, Swiss cantons, Italian and Spanish regions, Nordic
and Japanese municipalities, and Scottish income tax bands.

## Using the skills

The repository ships `.claude/skills` as a symlink to `skills/`, so the skills
are available to Claude Code when working inside this repository. To install
them globally:

```bash
for skill in skills/*/; do
  ln -s "$(pwd)/$skill" ~/.claude/skills/"$(basename "$skill")"
done
```

Skills are named `<country>-tax-calculation` and `<country>-tax-reporting`, and
their descriptions are written to fire on the questions people actually ask —
"what will I take home in Berlin", "when is my Self Assessment due", "is the
Beckham law worth it" — rather than only on the word "tax".

## What is modelled, and what is not

**Modelled:** personal income tax on employment and self-employment income,
national and sub-national schedules, social security with ceilings and floors,
surcharges, tapered allowances, refundable and non-refundable credits, income
splitting for joint filers, and the marginal wedge measured numerically.

**Not modelled:** wealth, inheritance, property and consumption taxes; corporate
tax; treaty relief and foreign tax credits; withholding schedules; and most
itemised deductions. Country-specific gaps are listed in each file's `warnings`
and printed with every calculation.

## Accuracy and honesty about it

The parameters are a best-effort snapshot of **tax year 2025**, assembled from
public sources and not reviewed by a tax authority or a professional. Every
country file carries `sources` with official URLs, and every skill is written to
point at them when the stakes are real.

`python -m taxcalc validate` checks structure and behaviour — bracket ordering,
rates entered as decimals, an open-ended top band, and that each schedule
produces non-negative, non-decreasing tax across a range of incomes. It cannot
tell you whether 42% is this year's correct rate. That is what the source URLs
are for.

This is not tax advice. See [`references/disclaimers.md`](references/disclaimers.md).

## Repository layout

```
data/countries/*.json     30 country parameter files
taxcalc/                  the engine
  schedules.py            bracket, flat, formula and contribution primitives
  engine.py               the shared computation pipeline
  loader.py               country lookup
  report.py               human-readable output
  validate.py             structural and behavioural checks
  cli.py                  list / calc / compare / info / deadlines / validate
skills/<name>/SKILL.md    60 skills
references/               shared method: workflows, residence, disclaimers
tests/                    631 tests
tools/check_freshness.py  flags country files that have fallen behind
docs/                     data schema and contribution notes
```

## Development

```bash
pip install -e ".[dev]"      # pytest + ruff
pre-commit install           # optional, runs the checks below on commit

python -m pytest tests/ -q   # tests
python -m taxcalc validate   # country data structure and behaviour
ruff check . && ruff format --check .
python tools/check_freshness.py   # how far behind the tax years are
```

CI runs the same checks across Python 3.9–3.13, and a quarterly workflow fails
when any country file falls more than a year behind the calendar year — stale
rates are the failure mode that produces confident wrong answers.

## Tests

```bash
pip install pytest && python -m pytest tests/ -q
```

The suite includes property tests that run against **every** country: net income
reconciles with its components, earning more never leaves you with less, tax
never exceeds income, and every country carries the sources, residence test and
filing calendar the skills quote. Adding a country with a mis-transcribed
threshold fails these rather than silently producing wrong answers.

## Contributing

Rates change every year. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to
update a country or add a new one — in most cases it is a JSON edit and nothing
else.

## Licence

MIT. See [`LICENSE`](LICENSE).
