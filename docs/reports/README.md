# Skill-run reports

Analysis-skill runs persist their result here as **`<skill-name>-<YYYY-MM-DD>.md`** so everyone can read
them — not only whoever ran the skill.

## The convention

- **Filename:** `docs/reports/<skill-name>-<date>.md`; for different scopes on the same day append a slug:
  `<skill-name>-<date>-<scope>.md`.
- **Provenance header (first block):** the audited commit (`git rev-parse --short HEAD`), date, scope,
  method (which skills/subagents ran), and a pointer to the previous report if any.
- **Immutable snapshots:** a report is never edited after its day; a re-run creates a NEW dated file.
- **Write scope:** for read-only analysis skills (e.g. [`docs-auditor`](../../skills/docs-auditor/SKILL.md)),
  the dated report is the ONLY repository write — findings and fixes stay proposals the human applies.
- **Delivery:** like any change — via a PR into `main`, never a direct push.

Living, curated documents — the arc42 docs (`docs/arc42/`), the ADRs (`docs/adr/`), `docs/RISK_MANAGEMENT.md` —
are **not** reports: skills draft input for them here, and humans merge the accepted parts.
[`arc42-generator`](../../skills/arc42-generator/SKILL.md) is the exception that writes the arc42 docs
directly, using `docs-auditor`'s report as its quality gate.
