# Risk management — method

How this project identifies, scores, tracks, and retires risks. The register lives in
**GitHub Issues** (label `risk`) and is worked on the **Risk Register** Projects v2 board;
this document is the method behind it.

## 1. Purpose & scope

Catch what threatens the project's delivery, quality, security, or compliance **early**,
make the exposure visible and owned, and force a conscious decision (mitigate / accept /
watch) instead of silent drift. In scope: anything with an uncertain outcome that would
matter — schedule, scope, dependencies, technical debt, people/resources, supply chain,
vulnerabilities, secrets, compliance. Out of scope: routine bugs and tasks (use normal
issues) — a risk is about *potential* future impact, not a defect that already occurred.
Also out of scope: risks of **harm** (safety) — they follow ISO 14971 in the separate
harm-risk register ([`HARM_RISK.md`](HARM_RISK.md)); a delivery risk may reference a
harm risk, they are never merged.

## 2. Raising a risk

Open an issue with the **Risk** form (it applies `risk` + `risk:open` automatically).
Describe the risk as *cause → uncertain event → consequence*, pick a category, propose
likelihood and impact, name an owner if known, and — required — state at least one
mitigation action. Anyone can raise a risk; triage happens on the board.

## 3. Scoring — 5×5 likelihood × impact

**Likelihood** (that the event materializes within the planning horizon):

| L | Anchor |
|---|---|
| 1 | Rare — no concrete indication; would surprise us (< ~10 %) |
| 2 | Unlikely — conceivable, no current signals (~10–30 %) |
| 3 | Possible — credible path exists; early signals plausible (~30–60 %) |
| 4 | Likely — signals already visible; expected without countermeasures (~60–85 %) |
| 5 | Almost certain — happening or imminent (> ~85 %) |

**Impact** (if it materializes):

| I | Anchor |
|---|---|
| 1 | Negligible — absorbed inside a normal iteration; no external visibility |
| 2 | Minor — days of rework or small scope trim; internally visible |
| 3 | Moderate — milestone slips or meaningful scope loss; stakeholder-visible |
| 4 | Major — deliverable/deadline at risk; external commitments affected |
| 5 | Critical — project goals, funding, legal, or safety in question |

**Score = L × I** (1–25), set at triage (Projects v2 has no computed fields).

## 4. Severity bands & response rules

| Severity | Score | Response rule |
|---|---|---|
| **Critical** | ≥ 15 | Act **now**: named owner, mitigation in progress, reviewed **every sprint**; escalation to project lead |
| **High** | 10–14 | Mitigation planned and scheduled; owner named; reviewed every sprint |
| **Medium** | 5–9 | Monitor: watch triggers, revisit at the regular review; mitigate opportunistically |
| **Low** | < 5 | Accept & log; re-check only when triggers fire or context changes |

Apply the matching `risk:sev-*` label and set the board's `Severity` field at triage.

## 5. Lifecycle

`raise → triage → (mitigate | accept | watch) → review → close`

- **Open** (`risk:open`): raised, awaiting or under triage.
- **Mitigating**: actions underway (board `Risk Status: Mitigating`).
- **Mitigated** (`risk:mitigated`): exposure reduced to an accepted level; keep watching triggers.
- **Accepted** (`risk:accepted`): consciously not mitigating — record why and who accepted.
- **Closed** (`risk:closed`): no longer applicable or fully retired; close the issue.

Every state change is an issue comment (one line is enough: what changed, why, by whom).

## 6. Roles

- **Raiser** — anyone; describes the risk and proposes scores.
- **Owner** — accountable for mitigation progress and honest status; every Critical/High
  risk has exactly one named owner.
- **Project lead / maintainer** — chairs the review, arbitrates scores, accepts risks
  (acceptance of a Critical risk is the lead's call, recorded in the issue).

## 7. Review cadence

Walk the board's **Matrix view** at the regular planning/steering meeting (sprint or
bi-weekly): new risks triaged, Critical/High progress checked, stale scores challenged,
triggers reviewed, closed risks celebrated. The **Review queue** view (review date reached
or still open) is the working list; set the next `Review date` before leaving the meeting.

## 8. Automated detectors → register

Security tooling **feeds** the register, it never replaces judgment: a critical/high
Dependabot or code-scanning alert may open (or comment on) a `risk` + `risk-cat:vulnerability`
issue with a back-link (see `.github/workflows/risk-automation.yml`, optional). Triage such
issues like any raised risk — score, own, decide.

## 9. Mitigation lives in code AND documentation

Risk mitigation is rarely just a task ticked off — it is a **design decision, an
implementation, a requirement, or a documented concept**. The architecture documentation
([arc42 v9](architecture/README.md)) is therefore part of the risk apparatus:

- **[§11 Risks and Technical Debts](architecture/11_technical_risks.md)** holds the
  architecture-level view of the register: only architecturally significant risks/debt,
  each linking its register issue and its mitigation's home section. Scores, owners, and
  status stay in the register — no duplication.
- **[§9 Architecture Decisions](architecture/09_architecture_decisions.md)**: a decision
  taken to reduce a risk cites the risk issue in its rationale; the issue links back.
- **[§4 Solution Strategy](architecture/04_solution_strategy.md)** and
  **[§8 Cross-cutting Concepts](architecture/08_concepts.md)**: where strategy- and
  concept-level mitigations (e.g. security concepts) are written down.
- **[§10 Quality Requirements](architecture/10_quality_requirements.md)**: quality
  scenarios pin a mitigation down as a testable expectation, guarding against regression.

Rule of thumb at triage: if the chosen mitigation changes *how the system is built*,
record it in the architecture docs and cross-link both ways — closing the issue must not
erase the knowledge.

## 10. Where things live

- **Register**: GitHub Issues labelled `risk` · board **Risk Register** (Projects v2) —
  fields: Likelihood, Impact, Score, Severity, Risk Status, Category, Owner, Review date.
- **Method**: this document.
- **Architecture documentation**: [`architecture/`](architecture/README.md) (arc42 v9,
  per-section files; §11 = architecture-level risk view).
- **Issue form**: `.github/ISSUE_TEMPLATE/risk.yml`.
- Optional in-repo register: [`../RISKS.md`](../RISKS.md) (changes via PR + CODEOWNERS).
- **On GitLab:** same register, platform equivalents per [`GITLAB.md`](GITLAB.md) —
  scoped labels (`risk::open`), issue-board lists, Score as issue weight.
