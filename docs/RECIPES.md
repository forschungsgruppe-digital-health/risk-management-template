# Risk-management recipes — typical situations, step by step

Cookbook for the day-to-day: what to do **when X happens**, using the register mechanics
this template ships. Recipes operationalize the methods — they add **no new rules**; on
conflict, [`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md) / [`HARM_RISK.md`](HARM_RISK.md) win.
Adapt freely per project (guidance, not mandate). Labels are written GitHub-style
(`risk:open`); on GitLab read them scoped (`risk::open`, [`GITLAB.md`](GITLAB.md)).
Recipes marked **(conformance layer)** assume the optional MDR/62304/14971 layer.

## 1. You spot a risk

**When:** anything with an uncertain outcome that would matter — schedule, scope,
dependency, tech debt, security, compliance.
**Steps:** Open a **Risk** issue (form auto-labels `risk` + `risk:open`) · describe it as
*cause → uncertain event → consequence* · propose L and I (anchors:
RISK_MANAGEMENT.md §3) · name an owner if known · state a mitigation — *"none known yet —
to be proposed at triage"* is a valid answer.
**Done when:** the issue exists and appears on the **Risk Register** board (auto-add or
next triage). Scoring is *proposed*; triage decides (§2 below).

## 2. Triage & scoring at the review

**When:** each new risk, at the regular review (RISK_MANAGEMENT.md §7).
**Steps:** Challenge L×I together · set `Score = L × I` and the board's Severity field ·
apply the `risk-sev:*` label · per the band's response rule (§4): Critical/High get a
**named owner** + scheduled mitigation; Medium gets watch-triggers; Low is accepted &
logged · set the next `Review date`.
**Done when:** every new risk has Score, severity, owner (Critical/High), review date —
and its mitigation decision is one of *mitigate / accept / watch*, recorded in the issue.

## 3. A dependency alert (CVE) arrives

**When:** Dependabot / Trivy flags a critical or high vulnerability.
**Steps:** If the automation is enabled it opens/comments a `risk` + `risk-cat:vulnerability`
issue — treat it as recipe 2 (detectors feed, never decide) · check whether the component
is inventoried in [`soup.yaml`](../soup.yaml) — if yes **(conformance layer)**: record the
evaluation as a **SOUP anomaly** issue (§7.1.3 record) and update the entry's `anomalies:` ·
ask the safety question: *can it contribute to a hazardous situation?* If yes/unclear →
recipe 5.
**Done when:** the vulnerability is a scored register entry with a decision; the SOUP
record and (if safety-relevant) a linked harm-risk exist.

## 4. A pilot user / clinician reports something odd **(conformance layer)**

**When:** feedback, complaint, incident, monitoring alert from pilot or production use.
**Steps:** Capture it via the **Field feedback / incident** form (label `field-feedback`;
ISO 14971 §10 intake — synthetic identifiers only, never real patient data) · at triage,
route it: possible patient impact → recipe 5 (harm-risk) · project impact → recipe 1
(risk) · SOUP behaviour → recipe 3 · plain defect → normal bug. Link the created issue
back. External security reports use [`SECURITY.md`](../SECURITY.md) (CVD), not this form.
**Done when:** the intake issue links its routing decision; it never substitutes for the
register entry.

## 5. A possible patient-harm hazard is identified **(conformance layer)**

**When:** anything that could injure or damage health — including wrong/delayed clinical
decisions caused by the software.
**Steps:** Open a **Harm risk** issue (labels `harm-risk` + `harm-risk:open`) — *never* a
delivery risk (harm ≠ delivery, HARM_RISK.md) · fill the 14971 chain: hazard → sequence →
hazardous situation → harm · score S and P (§3; software convention: P1 = 1 worst case,
S + P2 carry the evaluation) · judge against the acceptability matrix (§4) · plan controls
in the **mandatory hierarchy order** (§5): inherently safe design → protective measures →
information for safety.
**Done when:** the chain is complete, S×P judged, controls planned per tier (or honestly
"to be determined at evaluation"), and the issue is on the **Harm Risk File** board.

## 6. Choosing & verifying risk controls **(conformance layer)**

**When:** implementing the controls of recipe 5.
**Steps:** Prefer the highest feasible tier; architectural controls become **ADRs** and
appear in arc42 §11 · answer the required §7.5 field: *does any control introduce or shift
a hazard?* ("none identified" + rationale is valid) — net-new hazards run recipe 5 again ·
verify **twice** per control (§6): implemented (link PR/test) and effective (test,
analysis, or usability evaluation) · track via the board's `Control verification` field ·
tier-3 controls that rely on telling the user something get the `disclose-in-ifu` label.
**Done when:** every control is verified twice, the §7.5 answer is recorded, §7.6
completeness is confirmed — then `harm-risk:controlled`.

## 7. Accepting a residual risk

**When:** after controls (harm) or when consciously not mitigating (delivery).
**Steps — delivery:** record *why* and *who accepted* in the issue → `risk:accepted`
(acceptance of a Critical risk is the lead's call, §6).
**Steps — harm (conformance layer):** re-score residual S×P (form dropdowns mirror the
board) · judge against §4 — remember the MDR **AFAP** note: if MDSW, "acceptable" does not
skip the control hierarchy, and "not practicable" needs a non-economic justification · if
still above acceptability: a documented **benefit–risk analysis** (§7), accepted by the
project lead → `harm-risk:residual-accepted`.
**Done when:** the acceptance, its rationale, and the acceptor are in the issue — and (harm)
the residual feeds the next release's overall review (recipe 9).

## 8. A risk materialized

**When:** the uncertain event actually happened.
**Steps:** Execute the contingency plan from the issue (or improvise and record it) · the
event itself is now an incident/bug — open it and link both ways · close the risk
(`risk:closed`) with a one-line post-mortem: did triggers fire? was L honest? · ask what
*new* risks the event revealed → recipe 1 · **(conformance layer)** if patients were or
could have been affected → recipe 4/5 immediately.
**Done when:** incident handled in its own issue, risk closed with lessons, follow-up
risks raised.

## 9. Preparing a release **(conformance layer)**

**When:** before any release/tag.
**Steps:** Review the **overall** residual risk of all harm-risks together (HARM_RISK.md
§7; 14971 §8) — the whole picture, not each risk alone · record the review in
[`HARM_RISK_REPORT.md`](HARM_RISK_REPORT.md) (§9: plan executed / overall residual
acceptable / §10 feed in place + sign-off) · confirm `soup.yaml` matches the shipped
versions — the release's **SBOM** is the cross-check · the release automatically attaches
the SBOM + the **register exports** (evidence snapshots) · walk open `disclose-in-ifu`
items into the accompanying information.
**Done when:** the report is signed, exports attached, SOUP reconciled.

## 10. The periodic review meeting

**When:** sprint/bi-weekly (RISK_MANAGEMENT.md §7).
**Steps:** Walk the board's **Matrix view**: new risks (recipe 2), Critical/High progress,
stale scores challenged, triggers reviewed, closed risks celebrated · work the **Review
queue** view; set next review dates · **(conformance layer)** also: harm-risk board
(uncontrolled items), pending SOUP anomalies and field feedback, and the `watch` tier of
[`standards/CONFORMANCE.md`](standards/CONFORMANCE.md) (regulatory drift → a
`risk-cat:compliance` entry).
**Done when:** the review-queue view is empty of overdue items.

## 11. A feature might change the product's regulatory status **(conformance layer)**

**When:** the PR template's trigger question fires — clinical decision support, alarms on
clinical values, risk scores, care-plan logic, AI/ML for clinical decisions, EHR
embedding, intended-purpose changes.
**Steps:** **Before merging**, raise a `risk` issue referencing [ADR-0001](adr/0001-mdsw-qualification.md)
· walk MDCG 2019-11 rev. 1 (AI/ML: also MDCG 2025-6) · update ADR-0001's *Current
decision* (+ date, deciders) · if it flips to MDSW: activate the conformance tier, classify
per Rule 11, and bind the software safety class ([ADR-0002](adr/0002-software-safety-classification.md)).
**Done when:** ADR-0001 reflects the post-feature answer — "unchanged" is a valid,
recorded outcome.

## 12. A SOUP component version bump **(conformance layer)**

**When:** any inventoried dependency moves (Dependabot/Renovate PR or manual).
**Steps:** Before merge: re-check the new version's published anomaly/errata list (not
just CVEs) — findings become **SOUP anomaly** issues · re-confirm the relied-upon
functional/performance requirements still hold (SOUP.md) · update the `soup.yaml` entry's
version.
**Done when:** the bump PR links the check (or states "no relevant anomalies"), and
`soup.yaml` matches what ships.

## 13. Handing over to the future manufacturer **(conformance layer)**

**When:** transfer/market-placement approaches.
**Steps:** run the checklist in [`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md) —
board+issue exports, SOUP↔SBOM reconciliation, traceability matrix, the ADR-0001 walk,
the §9 reports, and the watch-tier due-date conversation.
**Done when:** that checklist says so.
