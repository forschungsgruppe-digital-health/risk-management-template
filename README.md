# Risk Management Template

A **template repository** for standing up lightweight, platform-native risk management
on any software project: a risk register as **issues + labels + a board**, a **5×5
likelihood × impact** method, severity-banded response rules, and optional security
automation — all additive, idempotent, and reviewable. GitHub-first (issue forms,
Projects v2, Actions), **with GitLab equivalents** (description templates, scoped
labels, issue-board lists, GitLab CI — functional parity on Free; a few enforcement
conveniences are Premium) — see [`docs/GITLAB.md`](docs/GITLAB.md).

> **See it applied:** [`risk-management-template-example`](https://github.com/forschungsgruppe-digital-health/risk-management-template-example)
> is a browsable child repo — the applied artifact set, filled synthetic register entries
> (risk / harm-risk / requirement), and the two linked Projects v2 boards.

Derived from a gated, human-in-the-loop setup prompt (see
[`docs/SETUP_PROMPT.md`](docs/SETUP_PROMPT.md)): nothing here mutates a repository behind
your back; the scripts are idempotent and skip what already exists. Shipped automation
has three disclosed activation models — **risk-automation** is inert until you set its
repo variable/token; **sbom** + **register-export** run only on your own release/tag
events; **template-sync-check** opens a monthly advisory issue (opt out via the
`TEMPLATE_SYNC_OPTOUT=1` variable or by deleting the workflow). Nothing blocks a merge or
changes code on its own.

## What's inside

| Artifact | Purpose |
|---|---|
| [`docs/RISK_MANAGEMENT.md`](docs/RISK_MANAGEMENT.md) | The method: 5×5 scale with anchors, Score→Severity bands, response rules, lifecycle, roles, review cadence |
| [`docs/RECIPES.md`](docs/RECIPES.md) | Novice-friendly cookbook — 13 step-by-step recipes with worked examples + common mistakes for typical situations (raise/triage a risk, CVE arrives, field feedback, harm hazard, controls, residual acceptance, risk materialized, release prep, review meeting, qualification trigger, SOUP bump, handover) |
| [`docs/learning/risk-management-primer.md`](docs/learning/risk-management-primer.md) (+ [DE](docs/learning/risk-management-primer.de.md)) | Standards-grounded novice **primer/lecture** on risk management (general + MDR): concepts, the ISO 14971 process, software/usability/security, MDR GSPRs — every claim clause-cited; examples point at this + the example repo |
| [`docs/arc42/`](docs/arc42/README.md) | [arc42 v9.0](https://arc42.org) architecture documentation, one file per section — §11 pre-wired to the register (risk mitigation lives in code **and** documentation); unmodified with-help edition vendored as reference |
| [`.github/ISSUE_TEMPLATE/risk.yml`](.github/ISSUE_TEMPLATE/risk.yml) | Issue form for raising a risk (auto-labels `risk` + `risk:open`) |
| [`RISKS.md`](RISKS.md) | Optional in-repo register (source of truth via PR + CODEOWNERS, if you prefer files over boards) |
| [`.github/risk-labels.json`](.github/risk-labels.json) | Label set: `risk`, lifecycle, severity, delivery + security categories |
| [`scripts/setup-labels.sh`](scripts/setup-labels.sh) | Idempotent label creation (`gh` CLI; skips existing, never recolors) |
| [`scripts/setup-project-board.sh`](scripts/setup-project-board.sh) | Creates the **Risk Register** Projects v2 board + custom fields (`gh project`); prints the manual view recipe |
| [`.github/workflows/risk-automation.yml`](.github/workflows/risk-automation.yml) | Optional automation: auto-add `risk` issues to the board, open a risk issue for critical/high Dependabot alerts — **inert until configured** |
| [`docs/SETUP_PROMPT.md`](docs/SETUP_PROMPT.md) | The original agent-executable, gate-approved setup prompt (dry-run by default) — use it to retrofit an *existing* repo instead of templating |
| [`docs/APPLY_TO_EXISTING_REPO.md`](docs/APPLY_TO_EXISTING_REPO.md) | How to apply the template to an **existing** repo: agent skill, gated prompts, or manual copy — with collision rules and a verify checklist |
| [`docs/GITLAB.md`](docs/GITLAB.md) | **GitLab support**: the full GitHub ↔ GitLab mapping + [`.gitlab/`](.gitlab/) issue/MR templates & CODEOWNERS, [scoped-label](scripts/setup-labels-gitlab.sh) + [board-list](scripts/setup-boards-gitlab.sh) scripts (glab), and the inert-until-configured [`.gitlab-ci.yml`](.gitlab-ci.yml) (SBOM on tags, scheduled Trivy→register) |
| [`skills/apply-risk-management/`](skills/apply-risk-management/SKILL.md) | Portable [Agent Skill](https://agentskills.io) that performs that retrofit (inventory → proposed diff → additive apply) |
| [`skills/mdr-audit-readiness/`](skills/mdr-audit-readiness/SKILL.md) | Its **verification counterpart**: a read-only "mock audit" of the risk-management docs from an MDR/CE Notified-Body lens (verified 14971/62304/62366-1/81001-5-1/MDR clauses) → dated `docs/reports/` scorecard of gaps, drifts & errors, with the major/minor/observation taxonomy. Deferral ≠ omission; never a conformity verdict |

### Conformance-readiness layer (optional)

For software that may be **placed on the market after the project** (research → product):
capture now what is near-impossible to reconstruct later, defer certification to the
future manufacturer — *design for conformance, defer certification*. Standards editions
verified 2026-07.

| Artifact | Purpose |
|---|---|
| [`docs/standards/CONFORMANCE.md`](docs/standards/CONFORMANCE.md) | Tiered standards & regulatory index (active / conditional / iff-MDSW / deferred / watch) with verified editions — incl. MDR + MDCG 2019-11 rev. 1, IEC 62304 (+ Ed. 2 timeline), CRA, AI Act, EHDS |
| [`docs/adr/`](docs/adr/README.md) | MADR-style ADR mechanism + three living/template ADRs: [0001 MDSW qualification](docs/adr/0001-mdsw-qualification.md) (feature-gate re-evaluation triggers), [0002 software safety classification](docs/adr/0002-software-safety-classification.md) (IEC 62304 §4.3), [0003 supply-chain pinning](docs/adr/0003-supply-chain-pinning.md) |
| [`docs/HARM_RISK.md`](docs/HARM_RISK.md) | ISO 14971 harm-risk method — separate register: [`harm-risk.yml`](.github/ISSUE_TEMPLATE/harm-risk.yml) form (§5–§8 chain incl. §7.5/§7.6/disclosure), [labels](.github/conformance-labels.json), [board script](scripts/setup-harm-risk-board.sh) |
| [`docs/HARM_RISK_REPORT.md`](docs/HARM_RISK_REPORT.md) | ISO 14971 §9 risk-management-report stub — the per-release review record (three §9 conclusions + sign-off) |
| [`docs/USABILITY.md`](docs/USABILITY.md) + [`use-scenario.yml`](.github/ISSUE_TEMPLATE/use-scenario.yml) | IEC 62366-1 usability-engineering method (use specification, hazard-related use scenarios, formative eval; summative deferred) — feeds the harm-risk register via `hazard-cat:usability`; not a separate register |
| [`docs/dpia/`](docs/dpia/README.md) + [`dpia-officer` skill](skills/dpia-officer/SKILL.md) | **Privacy track** — living Data Protection Impact Assessment (GDPR Art. 35) + Art. 32 technical-and-organisational-measures register, kept current by a human-in-the-loop watchdog skill; never fabricates legal determinations |
| [`docs/standards/GSPR-CHECKLIST.md`](docs/standards/GSPR-CHECKLIST.md) + [`IEC-62304-COVERAGE.md`](docs/standards/IEC-62304-COVERAGE.md) | MDR Annex I software-GSPR checklist (evidence-mapped) + clause-level 62304 process-coverage map (covered/partial/not-yet) |
| [`docs/SOUP.md`](docs/SOUP.md) + [`soup.yaml`](soup.yaml) | IEC 62304 SOUP inventory (identification, relied-upon requirements, known-anomaly impact assessments) |
| [`.github/workflows/sbom.yml`](.github/workflows/sbom.yml) | Per-release SBOM (Syft, CycloneDX default) attached as release asset — inert until a release is published |
| [`.github/workflows/register-export.yml`](.github/workflows/register-export.yml) | Per-release JSON snapshot of both risk registers attached as release assets (the ISO 14971 §9 "risk management file state" evidence) — inert until a release |
| [`scripts/build-risk-management-file.py`](scripts/build-risk-management-file.py) + [`risk-management-file.yml`](.github/workflows/risk-management-file.yml) | **Single hand-to-auditor Risk Management File** (ISO 14971 §4.5/§9): compiles the scattered records into ONE ISO 14971-ordered document (PDF/DOCX/HTML) via pandoc, per release — deliverable attached to the release, Markdown master archived in-repo. Asserts no conformity; placeholders show through. [Guide](docs/RISK_MANAGEMENT_FILE.md) · [ADR-0004](docs/adr/0004-risk-management-file-deliverable.md) |
| [`docs/SECURITY_RISK.md`](docs/SECURITY_RISK.md) + [`SECURITY.md`](SECURITY.md) | Security-risk-management method (MDCG 2019-16 parallel process, safety↔security coupling rules) + CVD-policy stub (CRA Annex I Part II readiness) |
| [`.github/dependabot.yml`](.github/dependabot.yml) + [`renovate.json`](renovate.json) | Keep the pinned CI generators current (Dependabot: GitHub Actions; Renovate: GitLab-CI images) — [ADR-0003](docs/adr/0003-supply-chain-pinning.md) |
| [`docs/TRACEABILITY.md`](docs/TRACEABILITY.md) | Requirement → design → PR → test linking model ([`requirement.yml`](.github/ISSUE_TEMPLATE/requirement.yml) form as anchor), reconstructable from the project forge; [advisory matrix script](scripts/traceability-matrix.sh) |
| [`docs/CONFORMANCE_TRANSFER.md`](docs/CONFORMANCE_TRANSFER.md) | What transfers to the future manufacturer vs what stays manufacturer-side (QMS, CE, clinical evaluation); DCO/IP hygiene; handover checklist |
| [`.github/pull_request_template.md`](.github/pull_request_template.md) + [`CODEOWNERS`](.github/CODEOWNERS) | The per-PR qualification-trigger gate + human review of conformance-critical files |
| [`docs/CONFORMANCE_EXTENSION_PROMPT.md`](docs/CONFORMANCE_EXTENSION_PROMPT.md) | Gated agent prompt to retrofit this layer onto an existing risk-managed repo |

## Agent toolkit

Agent context is canonical in [`AGENTS.md`](AGENTS.md) (Claude Code reads it via [`CLAUDE.md`](CLAUDE.md),
which imports `@AGENTS.md`). Beyond this
repo's own [`apply-risk-management`](skills/apply-risk-management/SKILL.md) skill, it now carries the
**shared FGDH agent toolkit** from the
[`arc42-project-template`](https://github.com/forschungsgruppe-digital-health/arc42-project-template) —
`arc42-generator`, `docs-auditor`, `release-manager`, `branching-strategist`, `dependency-scanner`,
`security-scanner`, `security-reviewer`, `template-updater`, `grilling`/`grill-me` (see
[`skills/SKILLS_SETUP.md`](skills/SKILLS_SETUP.md)). This repo **tracks that template** via
[`.arc42-template.json`](.arc42-template.json): the monthly `template-sync-check` workflow flags newer
releases and the `template-updater` skill reconciles the shared tooling while preserving this repo's
risk-management, conformance, and GitLab specialization.

## Using this template

### For a NEW project

1. **Create your repo from this template**: GitHub → *Use this template*, or
   ```bash
   gh repo create <owner>/<name> --template <owner>/risk-management-template --private
   ```
2. **Create the labels** (idempotent):
   ```bash
   ./scripts/setup-labels.sh <owner>/<name>
   ```
3. **Create the board** (Projects v2 + fields; the second argument links it to your repo;
   views are added manually — the script prints the recipe):
   ```bash
   ./scripts/setup-project-board.sh <owner> <owner>/<name>
   ```
4. Optionally **enable the automation**: set the repository variable `RISK_PROJECT_URL` to
   the board URL and enable the `risk-automation` workflow. It stays a no-op without it.
5. Read [`docs/RISK_MANAGEMENT.md`](docs/RISK_MANAGEMENT.md) with your team; agree on owners
   and the review cadence; raise the first risks via the issue form.

### On GitLab

No template button there — import the repo (**New project → Import → Repository by URL**),
then run the `*-gitlab.sh` twins of the setup scripts. The register semantics are
identical; labels materialize as **scoped labels** (`risk::open`), Score = issue weight.
Full mapping + tier notes: [`docs/GITLAB.md`](docs/GITLAB.md).

### For an EXISTING project

See **[`docs/APPLY_TO_EXISTING_REPO.md`](docs/APPLY_TO_EXISTING_REPO.md)** — three paths:
the [`apply-risk-management` skill](skills/apply-risk-management/SKILL.md) (agent
inventories your repo, proposes the diff, applies additively), the gated prompts
([`SETUP_PROMPT.md`](docs/SETUP_PROMPT.md) →
[`CONFORMANCE_EXTENSION_PROMPT.md`](docs/CONFORMANCE_EXTENSION_PROMPT.md), dry-run by
default), or the manual `cp -n` copy path — all with the same collision rules and verify
checklist.

## Principles

- **Additive & idempotent** — nothing overwrites or deletes existing labels, templates,
  boards, or files.
- **Human-gated** — the register lives where reviews happen (issues/PRs); automation only
  *feeds* it, never decides.
- **Right-sized** — a 5×5 matrix, four severity bands, one board. No tooling ceremony.
- **Mitigation is code + documentation** — architecturally significant mitigations are
  recorded in the arc42 docs (§11 ↔ register, decisions in §9), not just closed as issues.
- **Design for conformance, defer certification** — keep the evidence live
  (harm-risk file, SOUP, SBOM, traceability, qualification history) that a future
  manufacturer cannot reconstruct; defer the organizational QMS apparatus to them.
- **Harm ≠ delivery** — patient-safety risk (ISO 14971) and project risk live in
  separate registers with separate scales; they reference, never merge.

## License / reuse

Add your organization's license before publishing anything from a repo created off this
template. The template itself carries no top-level license file by design — licensing is a
per-project decision — with one exception: [`docs/arc42/`](docs/arc42/README.md)
derives from the [arc42 template](https://github.com/arc42/arc42-template) and remains
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (attribution + changes
documented there; the architecture *content you write* into it is yours).
