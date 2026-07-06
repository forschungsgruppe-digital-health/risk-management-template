# Risk Management Template

A **GitHub template repository** for standing up lightweight, GitHub-native risk management
on any software project: a risk register as **Issues + a Projects v2 board**, a **5×5
likelihood × impact** method, severity-banded response rules, and optional security
automation — all additive, idempotent, and reviewable.

Derived from a gated, human-in-the-loop setup prompt (see
[`docs/SETUP_PROMPT.md`](docs/SETUP_PROMPT.md)): nothing here mutates a repository behind
your back; the scripts are idempotent and skip what already exists, and the automation
workflow ships **inert until you configure it**.

## What's inside

| Artifact | Purpose |
|---|---|
| [`docs/RISK_MANAGEMENT.md`](docs/RISK_MANAGEMENT.md) | The method: 5×5 scale with anchors, Score→Severity bands, response rules, lifecycle, roles, review cadence |
| [`docs/architecture/`](docs/architecture/README.md) | [arc42 v9](https://arc42.org) architecture documentation, one file per section — §11 pre-wired to the register (risk mitigation lives in code **and** documentation); unmodified with-help edition vendored as reference |
| [`.github/ISSUE_TEMPLATE/risk.yml`](.github/ISSUE_TEMPLATE/risk.yml) | Issue form for raising a risk (auto-labels `risk` + `risk:open`) |
| [`RISKS.md`](RISKS.md) | Optional in-repo register (source of truth via PR + CODEOWNERS, if you prefer files over boards) |
| [`.github/risk-labels.json`](.github/risk-labels.json) | Label set: `risk`, lifecycle, severity, delivery + security categories |
| [`scripts/setup-labels.sh`](scripts/setup-labels.sh) | Idempotent label creation (`gh` CLI; skips existing, never recolors) |
| [`scripts/setup-project-board.sh`](scripts/setup-project-board.sh) | Creates the **Risk Register** Projects v2 board + custom fields (`gh project`); prints the manual view recipe |
| [`.github/workflows/risk-automation.yml`](.github/workflows/risk-automation.yml) | Optional automation: auto-add `risk` issues to the board, open a risk issue for critical/high Dependabot alerts — **inert until configured** |
| [`docs/SETUP_PROMPT.md`](docs/SETUP_PROMPT.md) | The original agent-executable, gate-approved setup prompt (dry-run by default) — use it to retrofit an *existing* repo instead of templating |
| [`docs/APPLY_TO_EXISTING_REPO.md`](docs/APPLY_TO_EXISTING_REPO.md) | How to apply the template to an **existing** repo: agent skill, gated prompts, or manual copy — with collision rules and a verify checklist |
| [`skills/apply-risk-management/`](skills/apply-risk-management/SKILL.md) | Portable [Agent Skill](https://agentskills.io) that performs that retrofit (inventory → proposed diff → additive apply) |

### Conformance-readiness layer (optional)

For software that may be **placed on the market after the project** (research → product):
capture now what is near-impossible to reconstruct later, defer certification to the
future manufacturer — *design for conformance, defer certification*. Standards editions
verified 2026-07.

| Artifact | Purpose |
|---|---|
| [`docs/standards/CONFORMANCE.md`](docs/standards/CONFORMANCE.md) | Tiered standards & regulatory index (active / conditional / iff-MDSW / deferred / watch) with verified editions — incl. MDR + MDCG 2019-11 rev. 1, IEC 62304 (+ Ed. 2 timeline), CRA, AI Act, EHDS |
| [`docs/adr/`](docs/adr/README.md) | MADR-style ADR mechanism + [ADR-0001](docs/adr/0001-mdsw-qualification.md): the **living** medical-device-software qualification decision with feature-gate re-evaluation triggers |
| [`docs/HARM_RISK.md`](docs/HARM_RISK.md) | ISO 14971 harm-risk method — separate register: [`harm-risk.yml`](.github/ISSUE_TEMPLATE/harm-risk.yml) form, [labels](.github/conformance-labels.json), [board script](scripts/setup-harm-risk-board.sh) |
| [`docs/SOUP.md`](docs/SOUP.md) + [`soup.yaml`](soup.yaml) | IEC 62304 SOUP inventory (identification, relied-upon requirements, known-anomaly impact assessments) |
| [`.github/workflows/sbom.yml`](.github/workflows/sbom.yml) | Per-release SBOM (Syft, CycloneDX default) attached as release asset — inert until a release is published |
| [`docs/TRACEABILITY.md`](docs/TRACEABILITY.md) | Requirement → design → PR → test linking model, reconstructable from Git; [advisory matrix script](scripts/traceability-matrix.sh) |
| [`docs/CONFORMANCE_TRANSFER.md`](docs/CONFORMANCE_TRANSFER.md) | What transfers to the future manufacturer vs what stays manufacturer-side (QMS, CE, clinical evaluation); DCO/IP hygiene; handover checklist |
| [`.github/pull_request_template.md`](.github/pull_request_template.md) + [`CODEOWNERS`](.github/CODEOWNERS) | The per-PR qualification-trigger gate + human review of conformance-critical files |
| [`docs/CONFORMANCE_EXTENSION_PROMPT.md`](docs/CONFORMANCE_EXTENSION_PROMPT.md) | Gated agent prompt to retrofit this layer onto an existing risk-managed repo |

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
3. **Create the board** (Projects v2 + fields; views are added manually — the script prints
   the recipe):
   ```bash
   ./scripts/setup-project-board.sh <owner>
   ```
4. Optionally **enable the automation**: set the repository variable `RISK_PROJECT_URL` to
   the board URL and enable the `risk-automation` workflow. It stays a no-op without it.
5. Read [`docs/RISK_MANAGEMENT.md`](docs/RISK_MANAGEMENT.md) with your team; agree on owners
   and the review cadence; raise the first risks via the issue form.

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
per-project decision — with one exception: [`docs/architecture/`](docs/architecture/README.md)
derives from the [arc42 template](https://github.com/arc42/arc42-template) and remains
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (attribution + changes
documented there; the architecture *content you write* into it is yours).
