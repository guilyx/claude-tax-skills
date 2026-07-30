# Security

## Reporting a vulnerability

Report suspected vulnerabilities through GitHub's private vulnerability
reporting on this repository (Security → Report a vulnerability). Please do not
open a public issue for anything exploitable.

Expect an acknowledgement within a week.

## Threat model

This project is a JSON dataset plus a pure-Python engine with **no runtime
dependencies** and no network access. It reads data files, does arithmetic and
prints text. The realistic concerns are narrow:

- **Untrusted country files.** `TAXCALC_DATA_DIR` lets a caller point the loader
  at a different directory. Files there are parsed with `json.loads` and never
  evaluated, so a malicious file can produce wrong numbers but not code
  execution. Do not point it at a directory you do not control.
- **Supply chain.** Pinned GitHub Actions and dev tooling are updated monthly by
  Dependabot. The published package itself has no dependencies to compromise.

## What is not a vulnerability

An incorrect tax rate, threshold or deadline is a **data correction**, not a
security issue — please open a [Tax data correction][data] issue instead. The
parameters are a best-effort snapshot and are documented as such; see
[`references/disclaimers.md`](references/disclaimers.md).

[data]: https://github.com/guilyx/claude-tax-skills/issues/new?template=tax-data-correction.yml
