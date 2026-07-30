## What this changes

<!-- One or two sentences. If this updates tax parameters, name the country and tax year. -->

## Type of change

- [ ] Tax parameter update (rates, thresholds, deadlines for a new year)
- [ ] New country
- [ ] Skill content
- [ ] Engine or tooling
- [ ] Documentation

## For tax parameter changes

<!-- Delete this section if it does not apply. -->

- **Country / tax year:**
- **Official source consulted:** <!-- the URL from the file's `sources`, or a new one -->
- [ ] `warnings` in the country file still describe what the model actually omits
- [ ] `reporting.deadlines` updated for the new year

## Checks

- [ ] `python -m taxcalc validate` passes
- [ ] `python -m pytest tests/ -q` passes
- [ ] `ruff check .` passes
- [ ] Spot-checked a calculation and the effective and marginal rates look plausible

## Notes for the reviewer

<!-- Anything you were unsure about, or figures worth a second pair of eyes. -->
