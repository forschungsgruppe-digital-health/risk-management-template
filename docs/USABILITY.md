# Usability engineering — method (IEC 62366-1)

How this project analyses, specifies, and evaluates the **use-related safety** of its user
interface — following **IEC 62366-1:2015** (*Medical devices — Part 1: Application of usability
engineering to medical devices*, Ed. 1.0; with A1:2020). Usability engineering is the safety
counterpart to security risk management ([`SECURITY_RISK.md`](SECURITY_RISK.md)): it finds and
reduces the **use errors** that can lead to harm, and it feeds the ISO 14971 harm-risk register
([`HARM_RISK.md`](HARM_RISK.md)) — it is **not** a separate safety register.

> **Scope note.** Kept live even while the product is not qualified as medical-device software
> (MDSW) ([ADR-0001](adr/0001-mdsw-qualification.md)): use-related hazards are near-impossible to
> reconstruct retroactively, and any health software benefits from an honest use-error analysis.
> This is **not** a claim of conformity — completeness (and the summative validation, §5.9) is the
> future manufacturer's obligation ([`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md)).
> **Copyright:** clause titles are cited for navigation; no tables, figures, or substantial text of
> the standard are reproduced — consult the licensed standard for the normative wording.

## 1. Why use errors are a safety concern

A **use error** (IEC 62366-1 §3.21) is a user action, or lack of action, that leads to a result
different from what the manufacturer intended or the user expected — including being unable to
finish a task. It is not a device malfunction and not an unexpected physiological response. The
chain to harm mirrors ISO 14971:

`task → use error → hazard-related use scenario → hazardous situation → harm`

Because a use error can expose a patient to a hazard just as a component failure can, IEC 62366-1
plugs **into** the ISO 14971 process: the hazardous situations it surfaces are evaluated and
controlled in the harm-risk register, and the effectiveness of a use-related control is verified
by usability evaluation (the §6 "effectiveness" verification of [`HARM_RISK.md`](HARM_RISK.md)).

## 2. The IEC 62366-1 process — mapped to this repo

The standard's usability engineering process (§5) runs these steps; each maps to a living
artifact here. The **usability engineering file** (§4.2) is the collected record — for this repo,
this document + the `use-scenario` issues + the linked harm-risks + the design decisions (ADRs).

| IEC 62366-1 step | What it means | Where it lives here |
|---|---|---|
| §5.1 Prepare **use specification** | intended users, use environments, intended use / operational context | §3 below; the intended purpose in [ADR-0001](adr/0001-mdsw-qualification.md) |
| §5.2 Identify **UI characteristics related to safety** + potential **use errors** | which parts of the interface, if misused, could contribute to harm | §4 below; per feature at design time |
| §5.3 Identify known/foreseeable **hazards & hazardous situations** | the use-related hazards those errors lead to | fed into [`HARM_RISK.md`](HARM_RISK.md) as `hazard-cat:usability` harm-risks |
| §5.4 Identify & describe **hazard-related use scenarios** | the concrete task+error+context that reaches a hazardous situation | the [`use-scenario` form](../.github/ISSUE_TEMPLATE/use-scenario.yml) (label `use-scenario`) |
| §5.5 **Select** hazard-related use scenarios for **summative** evaluation | which scenarios the final validation must cover | a field on the `use-scenario` issue (deferred execution, see §6) |
| §5.6 Establish **UI specification** | the interface requirements that control the use errors | `requirement` issues ([`TRACEABILITY.md`](TRACEABILITY.md)) + arc42 §5/§8 |
| §5.7 Establish **UI evaluation plan** (5.7.2 formative / 5.7.3 summative) | how the interface will be evaluated | §6 below |
| §5.8 Design + implement + **formative** evaluation | iterative, exploratory testing during design | §6 below; findings loop back as `use-scenario`/harm-risk updates |
| §5.9 **Summative** evaluation (validation of safe use) | final objective evidence of safe use | **deferred-to-manufacturer** ([`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md)) |
| §5.10 **User interface of unknown provenance (UOUP)** | reused UI you did not develop under this process | §7 below |

## 3. Use specification (§5.1)

Fill per project — the honest baseline the whole analysis rests on:

| Element | This project |
|---|---|
| Intended users (profiles: role, training, expertise, impairments) | <e.g. clinicians; patients as lay users; …> |
| Use environment(s) | <e.g. ward, home, variable lighting/noise, interruptions> |
| Operational / clinical context of use | <what tasks, on what data, with what consequences> |
| Intended medical indication & patient population | from the intended purpose ([ADR-0001](adr/0001-mdsw-qualification.md)) |

Lay users (patients) and professional users have different error profiles — analyse each user
profile separately where they use the same function.

## 4. UI characteristics related to safety & potential use errors (§5.2)

For each user-facing function that could contribute to harm, record the safety-related interface
characteristic and the **potential use errors** (slips, mistakes, an unnoticed state, an
uncompletable task). A useful prompt list: data-entry fields, patient/context selection, alarms
and their acknowledgement, dosing or scoring displays, confirmation steps, and anything where the
user could act on **stale, wrong-patient, or misread** information. IEC 62366-1 **Annex B** lists
example hazardous situations related to usability — work it the way ISO/TR 24971 Annex A is worked
for hazards generally.

## 5. From use error to harm-risk (§5.3–§5.4)

A potential use error that could reach a hazardous situation is documented as a **hazard-related
use scenario** on the [`use-scenario` form](../.github/ISSUE_TEMPLATE/use-scenario.yml), which
captures: the task, the user profile & environment, the use error, the resulting hazardous
situation, and the harm. The scenario then **links to a `harm-risk` issue** (category
`hazard-cat:usability`) where it is scored and controlled under the ISO 14971 hierarchy — for a
use-related risk, the control tiers are:

1. **Inherently safe UI design** — make the error impossible or harmless by construction (e.g.
   bind patient context immutably per view; disable an unsafe action in an unsafe state).
2. **Protective measures** — in the UI or its environment (confirmation for irreversible actions,
   a persistent patient banner, alarms — mind alarm fatigue, a new risk from the control per
   ISO 14971 §7.5).
3. **Information for safety** — labels, warnings, instructions, training (weakest; flag
   `disclose-in-ifu` so it reaches the accompanying information / instructions-for-use).

## 6. Evaluation — formative now, summative deferred (§5.7–§5.9)

- **Formative evaluation (§5.7.2, §5.8)** — exploratory user-interface testing **during design**
  to find and fix use errors early; run iteratively. Record findings as `use-scenario`/`harm-risk`
  updates and, where a control depends on the user acting correctly, as the **effectiveness**
  verification of that harm-risk control (the §6 "effectiveness verified" step of
  [`HARM_RISK.md`](HARM_RISK.md)). Formative notes live per project (link them from the issue).
- **Summative evaluation (§5.7.3, §5.9)** — the **final validation** that the interface can be used
  safely, over the scenarios selected in §5.5. This is **deferred-to-manufacturer** (execution
  needs a production-equivalent build and representative users); pre-stage its **inputs** here (the
  selected scenarios, user profiles, use environments) so it is not reconstructed later.

## 7. User interface of unknown provenance — UOUP (§5.10 / Annex C)

A user interface (or UI component) you reuse but did not develop under this process is a **UOUP** —
the usability analogue of SOUP ([`SOUP.md`](SOUP.md)). Treat it like SOUP: identify it, state what
safe-use behaviour you rely on, review available post-production/known-use-problem information, and
carry any use-related hazard it introduces into the harm-risk register. Note UOUP components
alongside their code dependency in [`soup.yaml`](../soup.yaml) (a comment or a `ui: true` marker) or
in the `use-scenario` issue.

## 8. Tailoring (§4.3)

Scale the effort to the use-related risk: a lay-facing function that displays clinical scores earns
more scenarios and formative rounds than an internal admin screen. Record the tailoring rationale
(what you analysed lightly and why) — an auditor accepts a scaled effort, not an unexplained gap.

## 9. Where things live

- **Method:** this document · **use-related-risk register:** the `harm-risk` issues with
  `hazard-cat:usability` ([`HARM_RISK.md`](HARM_RISK.md)).
- **Hazard-related use scenarios:** [`.github/ISSUE_TEMPLATE/use-scenario.yml`](../.github/ISSUE_TEMPLATE/use-scenario.yml)
  (label `use-scenario`; GitLab: `.gitlab/issue_templates/Use Scenario.md`).
- **UI specification:** `requirement` issues + [`TRACEABILITY.md`](TRACEABILITY.md); design in arc42 §5/§8.
- **Standards context:** [`standards/CONFORMANCE.md`](standards/CONFORMANCE.md) (IEC 62366-1 row);
  summative transfer in [`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md).
- **Day-to-day situations:** [`RECIPES.md`](RECIPES.md).
