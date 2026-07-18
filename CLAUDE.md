# Risk Management Template — Claude Code Context

@AGENTS.md

> Project context, repository map, conventions, branching/release rules, architecture invariants, and the
> vendor-neutral skills catalog are in the `AGENTS.md` imported above (canonical — also applies to Codex,
> Cursor, Gemini, Copilot). This file supplements **only** Claude-Code-specific working instructions.

## Working with Claude Code

- Skills are auto-discovered via `.claude/skills/` (symlinks into `skills/` — edit `skills/` only):
  `apply-risk-management` (this repo's own), plus the shared FGDH toolkit `arc42-generator`,
  `docs-auditor`, `release-manager`, `branching-strategist`, `dependency-scanner`, `security-scanner`,
  `security-reviewer`, `template-updater`, `grilling`, `grill-me`.
- **Architecture docs** live at `docs/arc42/` (arc42 v9, one file per section, §11 pre-wired to the risk
  register). Change them via `arc42-generator`, using `docs-auditor` as the quality gate — never break
  the arc42 ↔ `RISK_MANAGEMENT.md` touchpoints, and keep the harm-risk register separate.
- **GitHub ↔ GitLab parity:** any change to one platform's templates/labels/CI must be mirrored on the
  other (see `docs/GITLAB.md`). Keep the "additive / idempotent / inert-until-configured" contract.
- This repo tracks the shared `arc42-project-template` (`.arc42-template.json` stamp); the monthly
  `template-sync-check` workflow flags newer template releases and `template-updater` reconciles them,
  preserving this repo's risk-management / conformance / GitLab specialization.
- Do **not** add release-please/SemVer without a decision — this repo keeps its tag-based SBOM model.
