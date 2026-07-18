# Harm-risk management — method (ISO 14971)

How this project identifies, evaluates, controls, and tracks risks of **harm** —
following **ISO 14971:2019** (*Medical devices — Application of risk management to
medical devices*, Ed. 3) with the guidance of **ISO/TR 24971:2020**. The harm-risk
register lives in **GitHub Issues** (label `harm-risk`) on the separate **Harm Risk
File** board.

This register is **deliberately separate** from the delivery-risk register
([`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md)): patient-harm risk is never conflated with
schedule/scope risk, is scored on different scales (severity of harm, not project
impact), and follows the 14971 control hierarchy instead of mitigate/accept/watch. A
delivery risk may *reference* a harm risk (and vice versa); they are never merged.

> **Scope note.** Kept live even while the product is not qualified as MDSW
> ([ADR-0001](adr/0001-mdsw-qualification.md)): a harm-risk file is near-impossible to
> reconstruct retroactively, and health software benefits from it regardless
> (IEC 82304-1, IEC 81001-5-1 perspective). This template is **not** a claim of
> regulatory compliance — completeness of the risk management file is the (future)
> manufacturer's obligation ([`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md)).

## 1. Risk management plan (fill per project — 14971 §4.4)

| Plan element | This project |
|---|---|
| Scope of these activities | <product + life-cycle phases covered> |
| Responsibilities & authorities | <who owns the file; who may accept residual risk> |
| Criteria for risk acceptability | the S×P acceptability matrix in §4 (adapt it consciously, **before** scoring) |
| Verification activities | the two verifications per control (§6) |
| Production & post-production information | detector feed per §8 + user feedback channel |

## 2. The 14971 chain — what a harm-risk issue captures

`hazard → foreseeable sequence of events → hazardous situation → harm`

- **Hazard** — potential source of harm (e.g. *wrong-patient data displayed*).
- **Sequence of events** — how normal use, misuse, or failure gets there.
- **Hazardous situation** — people exposed to the hazard.
- **Harm** — injury/damage to health (physical or psychological), including harm from
  wrong or delayed clinical decisions based on the software.

The [harm-risk issue form](../.github/ISSUE_TEMPLATE/harm-risk.yml) enforces this chain.

## 3. Scoring — severity × probability

**Severity of harm (S)** — example anchors, calibrate per product:

| S | Anchor |
|---|---|
| 1 | Negligible — inconvenience, no health effect |
| 2 | Minor — temporary impairment, no intervention needed |
| 3 | Serious — impairment requiring professional intervention |
| 4 | Critical — permanent impairment or life-threatening injury |
| 5 | Catastrophic — patient death |

**Probability (P)** — of the harm occurring. Score it either as a single P (1 = remote …
5 = frequent) or decomposed per ISO/TR 24971 as **P1 × P2**:
P1 = probability of the hazardous situation occurring; P2 = probability that the
hazardous situation leads to harm. Record P1/P2 in the issue when known — for software,
P1 is often the only estimable part (a software failure's probability is convention-
ally set to 1 when it cannot be estimated; then S and P2 carry the evaluation).

## 4. Acceptability matrix (example — adopt consciously)

| P \ S | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 5 | investigate | reduce | reduce | reduce | reduce |
| 4 | acceptable | investigate | reduce | reduce | reduce |
| 3 | acceptable | investigate | investigate | reduce | reduce |
| 2 | acceptable | acceptable | investigate | investigate | reduce |
| 1 | acceptable | acceptable | acceptable | investigate | investigate |

`reduce` = risk control required; `investigate` = control if practicable, justify if
not; `acceptable` = document and monitor. Acceptance of any risk with S ≥ 4 is the
project lead's call, recorded in the issue.

## 5. Risk control — hierarchy is mandatory (14971 §7.1, in this order)

1. **Inherently safe design and manufacture** — remove the hazard or reduce S/P by
   design (e.g. make wrong-patient display impossible by construction).
2. **Protective measures** — in the product or its environment (validation checks,
   confirmation steps, monitoring, alarms).
3. **Information for safety** — instructions, warnings, training. Weakest tier; never
   the first resort.

Each control states its tier in the issue. Controls that change the architecture are
recorded as ADRs and appear in [arc42 §11](arc42/11_technical_risks.md).

## 6. Verification — twice per control (14971 §7.2)

1. **Implementation verified** — the control exists in the released product (link the
   PR/test).
2. **Effectiveness verified** — the control actually reduces the risk (test, analysis,
   or usability evaluation per IEC 62366-1 where the control depends on user action).

Track via the board field `Control verification: None → Implemented → Verified
effective`.

## 7. Residual risk, benefit–risk, lifecycle

After controls: re-score (residual S/P), evaluate against §4. If still not acceptable
and further control is not practicable, a documented **benefit–risk analysis**
(14971 §7.4) decides — recorded in the issue, accepted by the project lead
(`harm-risk:residual-accepted`). Review the **overall** residual risk of all harm risks
together before each release (14971 §8).

Lifecycle labels: `harm-risk:open` → (controls in progress = board status `Controlling`)
→ `harm-risk:controlled` → `harm-risk:residual-accepted` (only via benefit–risk) →
`harm-risk:closed`. Every state change is an issue comment.

## 8. Production & post-production feed (14971 §10)

Automated detectors feed this register the same way they feed the delivery register: a
security alert on a SOUP component with potential safety impact prompts a linked
`harm-risk` issue (see [`SOUP.md`](SOUP.md) and the risk-automation workflow). User
feedback and incident reports from pilot/production use are triaged into this register.

## 9. Example entry (obviously artificial)

> **Hazard:** questionnaire score displayed for the wrong patient. **Sequence:** two
> records open in adjacent tabs; stale component state renders patient A's score in
> patient B's view. **Hazardous situation:** clinician reads the wrong score during
> triage of `Max Mustermann-Testpatient`. **Harm:** delayed escalation of care (S 3).
> **P:** P1 2 × P2 3 → P 2–3. **Controls:** (1) inherent — patient context bound
> immutably per view, re-fetch on focus (tier 1, ADR-linked); (2) protective — patient
> banner with name/DOB on every clinical view (tier 2). **Verification:** unit +
> characterization tests (implemented); usability walkthrough (effectiveness).
> **Residual:** S 3 × P 1 — acceptable per §4.

## 10. Where things live

- **Register:** Issues labelled `harm-risk` · board **Harm Risk File** — fields:
  Severity, Probability, Residual severity, Residual probability, Risk Status, Hazard
  category, Control verification, Owner, Review date
  ([`scripts/setup-harm-risk-board.sh`](../scripts/setup-harm-risk-board.sh)).
- **Issue form:** [`.github/ISSUE_TEMPLATE/harm-risk.yml`](../.github/ISSUE_TEMPLATE/harm-risk.yml)
  · labels: [`.github/conformance-labels.json`](../.github/conformance-labels.json)
  (`scripts/setup-labels.sh <owner>/<repo> .github/conformance-labels.json`).
- **Method:** this document · delivery risks: [`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md)
  · standards context: [`standards/CONFORMANCE.md`](standards/CONFORMANCE.md).
- **On GitLab:** `.gitlab/issue_templates/Harm Risk.md` + scoped `harm-risk::*` labels +
  board lists — mapping in [`GITLAB.md`](GITLAB.md).
