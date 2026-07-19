# Applying this template to an EXISTING repository

Three ways in, by decreasing automation. All are **additive**: nothing existing is
overwritten; collisions are skipped or merged per the rules below. The steps below are
GitHub-worded (`gh`, Projects v2, Actions); applying to a **GitLab** repo uses the same
file sets plus the GitLab twins (`.gitlab/`, `*-gitlab.sh` scripts, `.gitlab-ci.yml`) —
mapping in [`GITLAB.md`](GITLAB.md).

| Path | When |
|---|---|
| **A. Agent skill** ([`skills/apply-risk-management/SKILL.md`](../skills/apply-risk-management/SKILL.md)) | you use Claude Code / Codex / Cursor or another agent that reads Agent Skills — the skill inventories your repo and previews the full changeset via a throwaway scratch clone (`MODE = plan`, the zero-mutation default), then applies what you approve (`MODE = apply`) |
| **B. Gated prompts** ([`SETUP_PROMPT.md`](SETUP_PROMPT.md), then [`CONFORMANCE_EXTENSION_PROMPT.md`](CONFORMANCE_EXTENSION_PROMPT.md)) | you want an agent but with explicit per-gate approval tokens (dry-run by default) |
| **C. Manual copy** (below) | no agent — plain `git` + `gh` |

## C. Manual path

```bash
# 1. Fetch the template next to your repo (shallow, throwaway)
gh repo clone <owner>/risk-management-template /tmp/rmt -- --depth 1
cd <your-repo>

# 2. Base layer (delivery-risk register) — cp -n never overwrites existing files
mkdir -p docs scripts .github/ISSUE_TEMPLATE .github/workflows
cp -n /tmp/rmt/docs/RISK_MANAGEMENT.md docs/
cp -n /tmp/rmt/RISKS.md .                                # optional in-repo register
cp -n /tmp/rmt/.github/ISSUE_TEMPLATE/risk.yml .github/ISSUE_TEMPLATE/
cp -n /tmp/rmt/.github/risk-labels.json .github/
cp -n /tmp/rmt/scripts/setup-labels.sh /tmp/rmt/scripts/setup-project-board.sh scripts/
cp -n /tmp/rmt/.github/workflows/risk-automation.yml .github/workflows/  # ships inert

# 3. Conformance layer (optional — MDR/62304 readiness, see docs/standards/CONFORMANCE.md)
mkdir -p docs/standards docs/adr
cp -n /tmp/rmt/docs/standards/*.md docs/standards/       # CONFORMANCE + GSPR-CHECKLIST + IEC-62304-COVERAGE
cp -rn /tmp/rmt/docs/adr/. docs/adr/                     # ('/.': portable on GNU+BSD) renumber 0001–0003 to your next free numbers + fix cross-links
cp -n /tmp/rmt/docs/HARM_RISK.md /tmp/rmt/docs/HARM_RISK_REPORT.md /tmp/rmt/docs/SOUP.md \
      /tmp/rmt/docs/TRACEABILITY.md /tmp/rmt/docs/CONFORMANCE_TRANSFER.md docs/
cp -n /tmp/rmt/soup.yaml .
cp -n /tmp/rmt/.github/ISSUE_TEMPLATE/harm-risk.yml /tmp/rmt/.github/ISSUE_TEMPLATE/requirement.yml .github/ISSUE_TEMPLATE/
cp -n /tmp/rmt/.github/conformance-labels.json .github/
cp -n /tmp/rmt/scripts/setup-harm-risk-board.sh /tmp/rmt/scripts/traceability-matrix.sh scripts/
cp -n /tmp/rmt/.github/workflows/sbom.yml .github/workflows/
cp -n /tmp/rmt/.github/dependabot.yml .github/             # MERGE by hand if one exists (ADR-0003)
cp -n /tmp/rmt/renovate.json .                             # MERGE by hand if one exists (GitLab-image bumps)
cp -n /tmp/rmt/.github/pull_request_template.md .github/   # MERGE by hand if one exists
cp -n /tmp/rmt/.github/CODEOWNERS .github/                 # MERGE by hand if one exists

# 4. Architecture docs (arc42 v9.0, §11 risk-wired) — optional
mkdir -p docs/arc42 && cp -rn /tmp/rmt/docs/arc42/. docs/arc42/

# 5. Activate (idempotent)
./scripts/setup-labels.sh <owner>/<your-repo>
./scripts/setup-labels.sh <owner>/<your-repo> .github/conformance-labels.json
./scripts/setup-project-board.sh <owner>
./scripts/setup-harm-risk-board.sh <owner>
```

Then: set the repo variable `RISK_PROJECT_URL` (activates the inert automation), fill in
[ADR-0001](adr/0001-mdsw-qualification.md) **and** the safety-classification
[ADR-0002](adr/0002-software-safety-classification.md) (both renumbered to your scheme) and
the plan table in [`HARM_RISK.md`](HARM_RISK.md) §1, replace the example entry in
`soup.yaml`, set owners in `.github/CODEOWNERS`, and link `docs/RISK_MANAGEMENT.md` from
your README.

## Collision rules (all paths)

| You already have | Rule |
|---|---|
| labels with the same names | `setup-labels.sh` skips them (never recolors/deletes) |
| an issue-template `config.yml` | keep yours; the forms coexist with other templates |
| `docs/adr/` with numbered ADRs | keep your numbering + template; add the template's **three** ADRs (qualification, safety classification, supply-chain pinning) under your **next free numbers** and fix the links to them |
| a PR template | **merge**: append the *Traceability* + *Conformance gate* sections |
| `CODEOWNERS` | **merge**: append the conformance-critical entries |
| CI workflows named `risk-automation.yml`/`sbom.yml` | do **not** overwrite — wire the equivalent steps into yours per [`CONFORMANCE_EXTENSION_PROMPT.md`](CONFORMANCE_EXTENSION_PROMPT.md) Phase E3 |
| architecture docs | keep yours; optionally adopt only [§11's register hook](arc42/11_technical_risks.md) |
| a `Risk Register` / `Harm Risk File` board | the board scripts detect by title and skip creation, then only add missing fields |

## Verify (any path)

- [ ] `risk` + `harm-risk` + `requirement` issue forms selectable under *New issue*
- [ ] both label sets exist (`gh label list | grep -E '^(risk|harm-risk|hazard-cat|requirement|soup|disclose-in-ifu)'`)
- [ ] boards exist with their fields; views added per the scripts' printed recipes
- [ ] a test `risk` issue lands on the board (auto-add or `RISK_PROJECT_URL` + workflow)
- [ ] ADR-0001 reflects **your** product's qualification answer, with a real date
- [ ] ADR-0002 records **your** software safety classification (or its "N/A while not MDSW" default)
- [ ] `docs/standards/` carries GSPR-CHECKLIST.md + IEC-62304-COVERAGE.md; `docs/HARM_RISK_REPORT.md` present as the §9 release-review stub
- [ ] `.github/dependabot.yml` + `renovate.json` present (or consciously skipped/merged — ADR-0003)
- [ ] `soup.yaml` example replaced; SBOM workflow runs on `workflow_dispatch`
