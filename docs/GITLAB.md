# Using this template on GitLab

Everything in this repo works on GitLab too — the register mechanics are the same
(issues + labels + a board + method docs); only the platform plumbing differs. This page
is the mapping. GitHub artifacts live under `.github/` + `scripts/setup-*.sh` (gh CLI);
their GitLab counterparts live under `.gitlab/` + `scripts/*-gitlab.sh` (glab CLI) +
`.gitlab-ci.yml`. Verified against GitLab 17.x docs; tier caveats are marked — the
free tier suffices for the whole base workflow.

## Equivalence table

| Concern | GitHub | GitLab |
|---|---|---|
| Get the template | *Use this template* / `gh repo create --template` | no template button: **Import project → Repository by URL** (or `git clone --mirror` + push); GitLab groups can also mark a project as a [custom project template](https://docs.gitlab.com/ee/user/group/custom_project_templates.html) (Premium) |
| Raising a risk | issue **form** `.github/ISSUE_TEMPLATE/risk.yml` | **description template** [`.gitlab/issue_templates/Risk.md`](../.gitlab/issue_templates/Risk.md) — markdown sections instead of form fields; the embedded [quick actions](https://docs.gitlab.com/ee/user/project/quick_actions.html) (`/label …`) auto-apply the labels on creation |
| Harm risk (ISO 14971) | `.github/ISSUE_TEMPLATE/harm-risk.yml` | [`.gitlab/issue_templates/Harm Risk.md`](../.gitlab/issue_templates/Harm%20Risk.md) |
| Labels | flat names with `:` (e.g. `risk:open`), created by `scripts/setup-labels.sh` (gh) | **scoped labels** `risk::open` etc., created by [`scripts/setup-labels-gitlab.sh`](../scripts/setup-labels-gitlab.sh) (glab) — the script maps `x:y` → `x::y`. Scoped labels are mutually exclusive per scope, which *enforces* the lifecycle/severity single-value rule the GitHub flavor only documents |
| Score | Projects v2 number field | issue **weight** (`/weight <n>`) — set Score = L×I at triage |
| Board | Projects v2 board + custom fields (`scripts/setup-project-board.sh`) | **issue board** with label lists per lifecycle label ([`scripts/setup-boards-gitlab.sh`](../scripts/setup-boards-gitlab.sh)). Free tier = one board per project (delivery + harm lists side by side); separate *Risk Register* / *Harm Risk File* boards need Premium (multiple boards) — the script degrades gracefully and prints the manual recipe |
| Matrix/severity views | Projects v2 views (manual recipe) | board filtered by `risk::sev-*` labels, or the issue list grouped by label; save as [board scopes] on Premium |
| PR template + gate | `.github/pull_request_template.md` | [`.gitlab/merge_request_templates/Default.md`](../.gitlab/merge_request_templates/Default.md) |
| CODEOWNERS | `.github/CODEOWNERS` | [`.gitlab/CODEOWNERS`](../.gitlab/CODEOWNERS) (GitLab reads root, `docs/`, or `.gitlab/` — **not** `.github/`); enforcement via protected-branch "Code owner approval" (Premium) |
| CI: SBOM per release | `.github/workflows/sbom.yml` (release asset) | `sbom` job in [`.gitlab-ci.yml`](../.gitlab-ci.yml) — Syft, CycloneDX, runs on tags (job artifact; attach to a release with `release-cli` if you use GitLab releases) |
| CI: vulnerability → register | Dependabot alerts → `risk-automation.yml` | guarded `vuln-to-register` job in `.gitlab-ci.yml`: scheduled Trivy scan opens deduped `risk` + `risk-cat::vulnerability` issues. **Inert until** `RISK_AUTOMATION_ENABLED=1` **and** `RISK_AUTOMATION_TOKEN` (project access token with `api` scope) are set — the same inert-until-configured contract as the GitHub workflow. (GitLab's built-in Dependency Scanning is Ultimate; the Trivy job is the tier-independent equivalent) |
| Auto-add to board | Projects v2 auto-add workflow | not needed: label lists pull labelled issues onto the board automatically |

## Setup on GitLab (mirrors the README's GitHub steps)

```bash
# 0. Import the template (GitLab has no template button)
#    GitLab UI: New project → Import project → Repository by URL → this repo's URL
#    or, keeping full history, from a local clone:
git clone --mirror <this-repo-url> rmt.git && cd rmt.git
git push --mirror git@<your-gitlab-host>:<group>/<name>.git

# 1. Labels (scoped; idempotent; needs glab authenticated against your instance)
./scripts/setup-labels-gitlab.sh <group>/<name>
./scripts/setup-labels-gitlab.sh <group>/<name> .github/conformance-labels.json

# 2. Board lists (label lists on the default board; idempotent)
./scripts/setup-boards-gitlab.sh <group>/<name>

# 3. Templates are picked up automatically from .gitlab/ (issue + MR templates).
# 4. Optional automation: set CI/CD variables RISK_AUTOMATION_ENABLED=1 and
#    RISK_AUTOMATION_TOKEN (project access token, api scope) + a pipeline schedule.
```

## Label-name mapping (canonical ↔ GitLab)

The method docs use the canonical flat names (`risk:open`); on GitLab they materialize as
scoped labels (`risk::open`). Both spellings mean the same state — when a doc says "apply
`risk:sev-high`", on GitLab that is `risk::sev-high`. Plain labels without a colon
(`risk`, `harm-risk`, `requirement`, `soup-anomaly`) are identical on both platforms.
One caveat: scoped-label *display* (mutual exclusivity, two-tone chips) is a Premium
feature on gitlab.com but **works on self-managed Free** for exclusivity semantics since
16.x — on instances where it doesn't, the labels still work as plain labels.

## What stays identical

The method is platform-free: `docs/RISK_MANAGEMENT.md`, `docs/HARM_RISK.md`, the 5×5
scoring, the conformance layer (`docs/standards/`, ADRs, SOUP/`soup.yaml`,
`docs/TRACEABILITY.md`, arc42) and `RISKS.md` need no changes. `scripts/traceability-matrix.sh`
is gh-based; on GitLab use the MR list per requirement label (`glab mr list --label requirement`)
or adapt the script — noted in `docs/TRACEABILITY.md`.
