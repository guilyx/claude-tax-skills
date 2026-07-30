# Changelog

Notable changes to this project. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Because this project is mostly data, the entries that matter most are tax
parameter updates. Record the country and tax year for each one so a reader can
tell at a glance whether the figures they are relying on have moved.

## [Unreleased]

### Added

- Personal income tax engine (`taxcalc`) covering progressive brackets, flat
  rates, piecewise-polynomial formula schedules, capped and floored social
  contributions, surcharges, tapered allowances, refundable and non-refundable
  credits, and income splitting for joint filers.
- Tax year 2025 parameters for 30 countries, with residence tests, filing
  calendars, forms, penalties, known traps and official source URLs.
- 60 agent skills — one calculation and one reporting skill per country.
- Shared references covering calculation and reporting workflow, residence and
  cross-border analysis, and disclaimers.
- CLI: `list`, `calc`, `compare`, `info`, `deadlines`, `validate`.
- Test suite including property tests that run against every country: totals
  reconcile, net income never falls as gross rises, tax never exceeds income,
  zero income owes nothing, and the documentation fields the skills quote are
  present.
- `tools/check_freshness.py` and a quarterly workflow that fails when country
  files fall more than a year behind.
- Repository scaffolding: ruff lint and format, pre-commit hooks, packaging
  metadata, issue and pull request templates, Dependabot, and a CI matrix
  across Python 3.9–3.13.

### Fixed

Bugs caught by the property tests while assembling the dataset:

- German formula schedule returned negative tax — the Horner evaluation was
  missing its constant term.
- UK additional-rate threshold was £112,570 instead of £125,140; because the
  personal allowance is fully withdrawn at that point, the taxable-income
  threshold equals the total-income figure.
- Flat-amount contributions (Denmark's ATP, Japan's national pension) were
  charged against zero income, producing a negative net.
- Brazil applied both the simplified 20% discount and deductible INSS, which
  are mutually exclusive under Brazilian rules.
