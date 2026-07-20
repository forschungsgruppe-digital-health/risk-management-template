# AGENTS.md — Risk Management Template

Operational context for AI coding agents (OpenAI Codex, Cursor, GitHub Copilot, Gemini CLI, and others
that read the open [AGENTS.md](https://agentskills.io) standard). This file is self-contained and
**canonical**: Claude Code reads `CLAUDE.md`, which imports this file via `@AGENTS.md`. On conflict, this
file wins.

## Project

- **Project:** a **template repository** for platform-native, lightweight **risk management** on any
  software project — a risk register as **issues + labels + a board**, a **5×5 likelihood × impact**
  method with severity bands + response rules, and optional security automation. Everything is
  **additive, idempotent, and reviewable**.
- **Platforms:** **GitHub-first** (issue forms, Projects v2, Actions) **with GitLab equivalents**
  (description/MR templates, scoped labels, issue-board lists, GitLab CI — functional parity on Free;
  a few enforcement conveniences are Premium) — see `docs/GITLAB.md`.
- **Conformance-readiness layer (optional):** capture-now/defer-certification for software that may be
  placed on the market later (MDR / IEC 62304 / ISO 14971 / CRA / EHDS); standards editions are dated and
  verified (see `docs/standards/CONFORMANCE.md`).

## Repository map

- `docs/arc42/` — arc42 v9.0 architecture documentation, one file per section; **§11 pre-wired to the
  risk register** (risk mitigation lives in code *and* docs). Vendors the unmodified arc42 with-help
  edition under `docs/arc42/arc42-reference/` (CC BY-SA).
- `docs/adr/` — Architecture Decision Records (MADR-style; the ADR ↔ arc42 §9/§11 link is a core feature).
- `docs/RISK_MANAGEMENT.md` · `RISKS.md` — the method + the optional in-repo register;
  `docs/RECIPES.md` — the situation cookbook (13 recipes; operationalizes the methods, adds no rules).
- `docs/HARM_RISK.md` — the **harm-risk** register (ISO 14971 style), **kept separate from the delivery
  register**; `docs/HARM_RISK_REPORT.md` — the §9 per-release review record.
- `docs/SOUP.md` · `soup.yaml` — Software of Unknown Provenance (IEC 62304);
  `docs/standards/GSPR-CHECKLIST.md` + `IEC-62304-COVERAGE.md` — Annex-I checklist + clause coverage map.
- `docs/SECURITY_RISK.md` · `SECURITY.md` — security-risk method (MDCG 2019-16, coupled to the harm
  register, no third register) + CVD-policy stub.
- `docs/TRACEABILITY.md`, `docs/CONFORMANCE_*`, `docs/standards/` — conformance apparatus.
- `docs/SETUP_PROMPT.md`, `docs/APPLY_TO_EXISTING_REPO.md` — retrofit an existing repo (prompt or skill).
- `.github/` (issue forms: risk, harm-risk, requirement, soup-anomaly, field-feedback + `config.yml`;
  labels; `risk-automation.yml`, `sbom.yml`, `register-export.yml`, `dependabot.yml`) · `renovate.json`
  · `.gitlab/` + `.gitlab-ci.yml` (GitLab twins) · `scripts/` (idempotent `gh`/`glab` setup;
  board scripts take `[owner/repo]` to link the project).
- `skills/` — agent skills (see catalog); `AGENTS.md` is canonical, wired via `.claude/.codex` symlinks.

## Conventions

- **Additive, idempotent, reviewable.** Nothing mutates a repo behind the user's back; scripts skip what
  exists; automation ships **inert until configured**.
- **GitHub ↔ GitLab parity.** A change to one platform's templates/labels/CI **must be mirrored** on the
  other (the mapping is in `docs/GITLAB.md`).
- **arc42 wired to the register.** Keep the §11 / §9 / §4 / §8 / §10 ↔ `RISK_MANAGEMENT.md` touchpoints
  intact; the harm-risk register stays separate from the delivery register.
- **Conformance editions are dated.** When touching `docs/standards/` or the conformance docs, keep the
  edition/date claims accurate (they were verified 2026-07).
- **Language:** English. **Diagrams:** Mermaid, no colors.

## Branching & releases

- `main` is the trunk. Changes are small, additive, and reviewable. The SBOM job builds on **tags**
  (CycloneDX via Syft); there is no release-please/SemVer automation here — this repo keeps its
  tag-and-SBOM release model (do **not** add release-please without a decision).

## Architecture invariants (do not violate)

- The arc42 docs live at `docs/arc42/` and stay **pre-wired to the risk register**; ADRs at `docs/adr/`.
- **Harm-risk register ≠ delivery-risk register** — never merge them.
- GitHub and GitLab config stay in parity.
- Conformance standard editions/dates stay accurate and sourced.

## Hard boundaries (NEVER do these)

- NEVER commit secrets. NEVER put real/sensitive data in the repo — this is a template; use obviously
  synthetic examples.
- NEVER weaken the "additive / idempotent / inert-until-configured" contract of the scripts and workflows.

## Agent capabilities (skills) — vendor-neutral catalog

The portable form is **Agent Skills** (`skills/<name>/SKILL.md`, [agentskills.io](https://agentskills.io)).
`skills/` is the single source of truth; see [`skills/SKILLS_SETUP.md`](skills/SKILLS_SETUP.md).

- **`apply-risk-management`** — this repo's own skill: retrofit risk management onto an existing repo
  (inventory → proposed diff → additive apply). *Outbound* (applies this template to others).
- **`mdr-audit-readiness`** — this repo's own skill and the **verification counterpart** to the above:
  a read-only "mock audit" of the risk-management documentation through an MDR/CE Notified-Body auditor's
  lens (verified ISO 14971 / IEC 62304 / 62366-1 / 81001-5-1 / MDR Annex I clauses), classifying gaps,
  drifts, and errors with the real major/minor/observation taxonomy — and separating a *documented*
  deferral (not a finding) from a *silent* gap → dated `docs/reports/` scorecard. `apply` sets the file
  up; this measures how far it is from auditable. Never issues a conformity verdict.
- **`dpia-officer`** — this repo's own skill (generic canonical; a repo may specialise it): the
  **privacy** track. A human-in-the-loop watchdog that keeps the living Data Protection Impact
  Assessment (GDPR Art. 35) + the Art. 32 technical-and-organisational-measures register (`docs/dpia/`)
  in step with data-protection-relevant change; consults before recording anything legal-impacting;
  never fabricates legal determinations ([DPO/LEGAL INPUT NEEDED]). Sits alongside the ISO 14971
  harm-risk + IEC 81001-5-1 security tracks.
- **Shared FGDH toolkit** (kept identical across repos; single source = the `arc42-project-template`):
  - **`arc42-generator`** — generate/consolidate the arc42 docs (`docs/arc42/`), novice+expert, via `docs-auditor`.
  - **`docs-auditor`** — audit all docs (complete/consistent/error-free/understandable/usable) + fixes; read-only.
  - **`release-manager`** / **`branching-strategist`** — set up CI release management / a branching strategy (wizards).
  - **`dependency-scanner`** / **`security-scanner`** — set up CI dependency-CVE / security review (wizards; GitHub-first — mirror to GitLab per `docs/GITLAB.md`).
  - **`security-reviewer`** — read-only STRIDE + checklist + scanner-triage review → dated `docs/reports/` report.
  - **`template-updater`** — reconcile this repo's shared tooling with the latest `arc42-project-template` release (preserving this repo's specialization); *inbound*, paired with `.arc42-template.json` + the `template-sync-check` notifier.
  - **`grilling`** / **`grill-me`** — a relentless interview to stress-test a plan/decision.

Beyond the skills, the conformance layer ships a **Risk Management File generator** —
`scripts/build-risk-management-file.py` + the `risk-management-file` CI job (GitHub + GitLab) —
which compiles the scattered risk records into ONE ISO 14971 §4.5/§9 hand-to-auditor document per
release ([ADR-0004](docs/adr/0004-risk-management-file-deliverable.md), [guide](docs/RISK_MANAGEMENT_FILE.md)).
Run [`mdr-audit-readiness`](skills/mdr-audit-readiness/SKILL.md) before a release so its Annex J carries
an honest self-assessment.

**How each tool accesses them:** Claude Code via `.claude/skills/`; Codex/Cursor/Gemini via `.codex/skills/`
(symlinks → `skills/`); anything else reads this catalog and performs the skill inline.

## Notes for non-Claude agents

- Treat **`AGENTS.md` as canonical**. If your tool lacks a native skills primitive, open the relevant
  `skills/<name>/SKILL.md` and follow it inline.
