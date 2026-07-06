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
| [`.github/ISSUE_TEMPLATE/risk.yml`](.github/ISSUE_TEMPLATE/risk.yml) | Issue form for raising a risk (auto-labels `risk` + `risk:open`) |
| [`RISKS.md`](RISKS.md) | Optional in-repo register (source of truth via PR + CODEOWNERS, if you prefer files over boards) |
| [`.github/risk-labels.json`](.github/risk-labels.json) | Label set: `risk`, lifecycle, severity, delivery + security categories |
| [`scripts/setup-labels.sh`](scripts/setup-labels.sh) | Idempotent label creation (`gh` CLI; skips existing, never recolors) |
| [`scripts/setup-project-board.sh`](scripts/setup-project-board.sh) | Creates the **Risk Register** Projects v2 board + custom fields (`gh project`); prints the manual view recipe |
| [`.github/workflows/risk-automation.yml`](.github/workflows/risk-automation.yml) | Optional automation: auto-add `risk` issues to the board, open a risk issue for critical/high Dependabot alerts — **inert until configured** |
| [`docs/SETUP_PROMPT.md`](docs/SETUP_PROMPT.md) | The original agent-executable, gate-approved setup prompt (dry-run by default) — use it to retrofit an *existing* repo instead of templating |

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

Either copy the artifacts you want (everything is additive), or run the gated setup prompt
in [`docs/SETUP_PROMPT.md`](docs/SETUP_PROMPT.md) with an agent — it inspects what exists,
proposes diffs, and waits for your explicit approval at every gate.

## Principles

- **Additive & idempotent** — nothing overwrites or deletes existing labels, templates,
  boards, or files.
- **Human-gated** — the register lives where reviews happen (issues/PRs); automation only
  *feeds* it, never decides.
- **Right-sized** — a 5×5 matrix, four severity bands, one board. No tooling ceremony.

## License / reuse

Add your organization's license before publishing anything from a repo created off this
template. The template itself carries no license file by design — licensing is a per-project
decision.
