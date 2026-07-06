# Prompt: Set up risk management on an existing GitHub project (human-in-the-loop)

> The agent-executable, gate-approved setup prompt this template is derived from. Use it to
> retrofit risk management onto an EXISTING repository: paste everything below the line into
> an agent with `gh` CLI + repo write access, fill in the **Inputs** block, and keep the
> default `MODE = dry-run` until you have reviewed each gate. For a NEW project, prefer
> creating the repo from this template (see the README).

---

## Role

You are setting up a complete, GitHub-native risk-management system on an **existing** repository for a software development project. You operate under a strict **human-in-the-loop execution contract** (below). Work **idempotently**: inspect what exists before proposing anything, never delete or overwrite existing content, prefer additive changes. Use the `gh` CLI and the GitHub GraphQL/REST API.

## Execution contract (read first — overrides everything below)

1. **Two modes.** `MODE = dry-run` (default) or `MODE = apply`. In **dry-run you make ZERO mutations** — no labels, issues, files, boards, workflows, or settings changes. You only read and produce proposals.
2. **Gates are hard stops.** At each gate you present the proposed changeset, then **end your turn and wait**. Do not continue to the next phase in the same turn. Proceed only when the user replies with the exact approval token for that gate (e.g. `APPROVE GATE 1`). Any other reply — including "looks good", questions, or edits — is **not** approval; respond and re-present, do not execute.
3. **Ambiguity = stop.** If a reply is unclear, if an input is missing, or if an API call needs a scope/permission you lack, stop and ask. Never work around a missing permission.
4. **Even in apply mode, gates still apply.** `MODE = apply` authorizes mutation *only past gates that have been individually approved*. It is not blanket consent.
5. **Highest-blast-radius steps are quarantined.** Anything touching security settings, branch protection, org-level features, or GitHub Actions with write scopes lives behind its **own** gate (Gate 3) and is never bundled with additive changes.
6. **Show diffs, not intentions.** Every proposal shows the concrete artifact — exact label names/colors, the full template YAML, the field/view schema, file contents, workflow YAML — not a summary of what you'll "generally" do.

### Gate map

- **Gate 0 — Plan approval.** After pre-flight inspection. Token: `APPROVE PLAN`.
- **Gate 1 — Register scaffolding.** Labels, issue form, method doc, RISKS.md. Additive, reversible. Token: `APPROVE GATE 1`.
- **Gate 2 — Projects v2 board.** Board, fields, views, auto-add automation. Token: `APPROVE GATE 2`.
- **Gate 3 — Automation & security (quarantined).** Actions workflows, Dependabot/code-scanning/secret-scanning, dependency review, branch protection. Token: `APPROVE GATE 3`.
- **Gate 4 — Example risk & verification.** Creating the demo issue and triaging it. Token: `APPROVE GATE 4`.

At every gate also offer: `SKIP` (this phase), `EDIT <changes>` (revise the proposal and re-present), or `ABORT` (stop entirely).

## Inputs (fill these in)

- `REPO`: <owner/repo>
- `PROJECT_OWNER`: <org or user that owns the Projects v2 board>
- `MODE`: `dry-run` (default) | `apply`
- `REGISTER_MODE`: `issues` (live register in Issues + Projects v2 — recommended) | `in-repo` (RISKS.md as source of truth) | `both`
- `RISK_FOCUS`: `delivery` (scope/schedule/dependencies/tech-debt) | `security` (supply-chain/vuln) | `both`
- `ENABLE_AUTOMATION`: `yes` | `no`
- `SCALE`: 1–5 likelihood × 1–5 impact (default)

If `REPO` or `PROJECT_OWNER` is missing, stop and ask before anything else.

## Phase 0 — Pre-flight and plan (→ Gate 0)

1. Confirm `gh auth status` and that the token can write issues, labels, and Projects v2 (`project` scope). Report exactly which scopes are present and which are missing.
2. Read the repo: existing labels (`gh label list`), issue templates under `.github/ISSUE_TEMPLATE/`, any existing `RISK*.md`, existing Projects v2 boards under `PROJECT_OWNER`, and current state of Dependabot / code scanning / secret scanning / branch protection.
3. Produce a **written plan**: resolved inputs, every artifact you intend to create per phase, collisions detected (label/template/board that already exists → will skip), and anything requiring manual action.
4. **GATE 0 — present the plan, end turn, wait for `APPROVE PLAN`.**

## Phase 1 — Register scaffolding (→ Gate 1)

Propose (then, once approved, create idempotently):

**Labels** (skip existing, don't recolor):
- `risk` (`#B60205`); lifecycle `risk:open`, `risk:mitigated`, `risk:accepted`, `risk:closed`; severity `risk:sev-critical|high|medium|low`.
- Category labels per `RISK_FOCUS`:
  - delivery: `risk-cat:schedule|scope|dependency|tech-debt|resource`
  - security: `risk-cat:supply-chain|vulnerability|secret|compliance`

**Issue form** `.github/ISSUE_TEMPLATE/risk.yml` (GitHub issue form, not legacy markdown), auto-applying `risk` + `risk:open`, capturing: title; description (required); category (dropdown); likelihood 1–5 with anchors; impact 1–5 with anchors; owner (handle); trigger/early-warning signs; mitigation actions (required); contingency plan; affected issues/milestones/PRs. Extend `config.yml` additively.

**Method doc** `docs/RISK_MANAGEMENT.md`: purpose/scope; the 5×5 scale with explicit anchors per level; Score→Severity bands and the response rule per band (Critical ≥15 = act now + named owner + review each sprint; High 10–14; Medium 5–9 = monitor; Low <5 = accept/log); lifecycle (raise → triage → review → close); roles; sprint-review cadence walking the Matrix view; how automated detectors feed the register; links to board and template.

**If `REGISTER_MODE` includes `in-repo`:** `RISKS.md` table (ID, Title, Category, L, I, Score, Severity, Owner, Status, Mitigation, Link) with a note that changes go via PR + CODEOWNERS sign-off.

Present all file contents and the label list in full. **GATE 1 — wait for `APPROVE GATE 1`.**

## Phase 2 — Projects v2 board (→ Gate 2)

Propose a board **"Risk Register"** under `PROJECT_OWNER` (skip if it exists) with fields: `Likelihood` (1–5 single-select), `Impact` (1–5), `Score` (number, 1–25 — set at triage since v2 has no computed fields), `Severity` (Critical/High/Medium/Low single-select), `Risk Status` (Open/Mitigating/Mitigated/Accepted/Closed), `Category`, `Owner`, `Review date`.

Views: **Matrix** (board grouped by Impact, Likelihood secondary sort, open risks — the 5×5 grid); **By severity** (table, Score desc); **By owner**; **Review queue** (Review date ≤ today OR status Open). Plus built-in automation to auto-add `risk`-labeled issues.

Present the full field/view schema. **GATE 2 — wait for `APPROVE GATE 2`.**

## Phase 3 — Automation & security — QUARANTINED (→ Gate 3, only if `ENABLE_AUTOMATION = yes`)

Present each item as an explicit diff and list which require org/admin rights you may not have:
- Security detectors: ensure Dependabot, CodeQL code scanning, secret scanning are enabled — or print the exact settings path for the user to toggle if you lack rights. Never assume you can flip org-level features.
- `.github/dependency-review.yml` + dependency-review action on PRs.
- `.github/workflows/risk-automation.yml`: add `risk`-labeled issues to the board; open/comment a `risk` + `risk-cat:vulnerability` issue on **critical/high** Dependabot or code-scanning alerts with a back-link; optional weekly Critical/High summary.
- Minimal permissions (`contents: read`, `issues: write`, `security-events: read`; project scope via PAT/GitHub App only if org policy requires — flag this, don't silently add secrets).
- **Branch protection: propose only, never apply without its own explicit confirmation inside this gate.**

**GATE 3 — wait for `APPROVE GATE 3`.** This gate is never auto-approved by `MODE = apply`.

## Phase 4 — Example risk & verification (→ Gate 4)

Propose to: open one example risk via the form, triage it on the board (set L/I/Score/Severity/Status) so the full flow is visible, then re-list labels/template/fields/views to confirm.

**GATE 4 — wait for `APPROVE GATE 4`**, then execute and produce the final report: what was created, what was skipped (already existed), what needs manual action (org security features, GitHub App install), and the URLs of the board, method doc, and example issue.

## Constraints

- Dry-run by default; mutate only in `apply` mode past an individually approved gate.
- Idempotent and additive; never clobber existing labels, templates, boards, or files.
- No force-push, no deleting issues, no changing branch protection or security/org settings without explicit in-gate confirmation.
- Stay inside `REPO` and the named board; never touch other repos.
- If a call needs a scope you lack, stop and name the exact setting to grant.
