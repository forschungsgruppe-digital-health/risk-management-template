# Traceability — requirement → design → implementation → test

The linking model that makes the chain reconstructable **from the project forge** — the
issues, PRs, and their cross-references, **not** a bare `git clone`: at MDR transfer the
Issues + Projects boards must be exported alongside the git history (see
[`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md)). Lightweight now, and the backbone of
IEC 62304 §5.1.1(c)/§7.3 evidence if the product qualifies as
MDSW (class B/C makes this granularity mandatory; see
[`standards/CONFORMANCE.md`](standards/CONFORMANCE.md)). Requirement quality follows
ISO/IEC/IEEE 29148:2018 (singular, verifiable, unambiguous).

## The model

| Link | Convention |
|---|---|
| **Requirement** | issue raised with the [Requirement form](../.github/ISSUE_TEMPLATE/requirement.yml) (label `requirement`); ID = the issue number (cite as `REQ-<n>`); acceptance criteria in the issue body |
| Requirement → **design** | the issue links the ADR / arc42 section that realizes it ([`docs/adr/`](adr/README.md), [`docs/arc42/`](arc42/README.md)) |
| Requirement → **implementation** | the implementing PR declares `Closes #<n>` (GitHub keyword — creates the cross-reference) |
| Implementation → **test** | the PR that closes a requirement contains (or links) the verifying tests; name tests so the requirement is findable (e.g. `REQ-42` in the test name or a `Verifies: #42` line in the PR body) |
| Requirement ↔ **risk** | a requirement mitigating a registered risk links the `risk`/`harm-risk` issue and vice versa |
| **SOUP** → requirement | a `soup.yaml` entry names the requirement its use is justified by (`req:` field) — closing the IEC 62304 §5.3.3 / §7.1.3 loop |
| **risk control** → test | a harm-risk control's *effectiveness* verification (§7.2) links its test/PR inside the issue; a delivery-risk mitigation likewise |

One requirement per issue — bundles break the chain.

## Reconstruction & advisory check

[`scripts/traceability-matrix.sh <owner>/<repo>`](../scripts/traceability-matrix.sh)
(gh-based; on GitLab query MRs per requirement label instead — see
[`GITLAB.md`](GITLAB.md)) emits a Markdown matrix: requirement → cross-referenced PRs → whether those PRs touch
test files — flagging requirements with **no linked test** (⚠). It is **advisory** (always
exits 0): at template stage the gap list is review input, not a merge blocker. Projects
that reach class-B/C ambitions wire it into CI as a warning first, then a gate.
The script traces **requirement → PR → test** only; the **SOUP → requirement** edge lives
in `soup.yaml` (`req:`) and the **control → test** edge inside each harm-risk issue — query
those directly (or extend the script) when a full class-C matrix is needed.

## PR-side duties

The [pull-request template](../.github/pull_request_template.md) asks for the linked
requirement/risk issues and the verifying tests on every PR — filling it *is* the
traceability work; nothing else to maintain.
