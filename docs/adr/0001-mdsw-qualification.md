# 0001 — Medical device software (MDSW) qualification

- **Status:** accepted — **living**, re-evaluated at the triggers below (this ADR is never
  "done"; it records the *current* qualification decision)
- **Date:** <YYYY-MM-DD of the latest evaluation>
- **Deciders:** <project lead, regulatory-affairs contact if available>
- **Linked risks:** <register issue tracking the qualification/regulatory risk, if raised>

> **Template note.** This ADR ships with the conformance-readiness layer (see
> [`docs/standards/CONFORMANCE.md`](../standards/CONFORMANCE.md)). Replace the
> placeholders with your project's facts at first triage; keep the trigger list. It
> presumes the strategy *design for conformance, defer certification*: the software is
> developed in a research project, market placement after project end is intended, and
> the manufacturer (in the MDR sense) is **TBD** — resolved by the dissemination /
> exploitation plan.

## Context and problem statement

Software is a medical device when it meets the definition in **Regulation (EU) 2017/745
(MDR), Art. 2(1)** — independent of where it runs or how it is distributed. Whether *this*
product qualifies as medical device software (MDSW) determines whether the
"activated iff MDSW" tier of the [conformance index](../standards/CONFORMANCE.md)
(IEC 62304, ISO 14971, IEC 62366-1, IEC 82304-1, …) becomes binding, and how it would be
classified (**MDR Annex VIII, Rule 11**). Qualification is **not static**: it can flip as
features move from displaying/organizing data toward influencing clinical decisions.
The authoritative decision aid is **MDCG 2019-11 rev. 1 (June 2025)** — *Guidance on
qualification and classification of software in Regulation (EU) 2017/745 (MDR) and
Regulation (EU) 2017/746 (IVDR)* — which since rev. 1 also covers AI-based software,
modular software, and the interplay with EHR systems under the EHDS.

## Current decision

<State the current qualification, e.g.:>

The product is currently **not qualified as MDSW**: it <displays / stores / transmits /
performs simple search on> data without performing an action on data beyond storage,
archival, communication, simple search, or lossless compression (MDCG 2019-11 decision
steps), and its intended purpose is <…>, not a medical purpose in the sense of MDR
Art. 2(1).

Consequences of *this* answer while it holds:

- The "activated iff MDSW" tier in the conformance index stays **dormant**; the
  conformance-ready artifacts (harm-risk register, SOUP inventory, SBOM, traceability)
  are still maintained, because they are cheap to keep live and near-impossible to
  reconstruct later.
- **Regulation (EU) 2024/2847 (Cyber Resilience Act)** then applies to a commercial
  market placement instead (products with digital elements; main obligations from
  **2027-12-11**) — MDR-covered devices are excluded from the CRA, non-devices are not.
  See the *watch* tier of the conformance index (incl. EHDS obligations for EHR systems
  from **2029-03-26**).

## Considered options

1. Qualify now as MDSW and develop under full IEC 62304 from day one — rejected: no
   manufacturer exists yet; the organizational QMS (ISO 13485) cannot be meaningfully
   operated by a research project and would be discarded/re-established at transfer.
2. Ignore qualification until transfer — rejected: the design history, risk file, SOUP
   and traceability evidence cannot be reconstructed retroactively at acceptable cost.
3. **Design for conformance, defer certification** (chosen): keep qualification under
   living review, maintain the transferable evidence, defer manufacturer-only
   obligations. See [`docs/CONFORMANCE_TRANSFER.md`](../CONFORMANCE_TRANSFER.md).

## Re-evaluation triggers

Re-evaluate this ADR (and record the result here) **before merging** any feature that:

- provides **clinical decision support** — recommends, prioritizes, or filters
  diagnostic/therapeutic options;
- **alerts or alarms on clinical values** (thresholds, deterioration detection);
- computes **risk scores**, staging, dosing, or other patient-specific clinical
  calculations;
- drives or adapts a **care plan / pathway logic** in a way that influences treatment;
- adds **AI/ML components** whose output is used for decisions with diagnostic or
  therapeutic purposes (also triggers the AI-Act row of the conformance index; walk
  **MDCG 2025-6 / AIB 2025-1** — the MDR↔AI-Act interplay guidance — alongside
  MDCG 2019-11 rev. 1);
- turns the product into (or embeds it in) an **EHR system** for priority-category data
  (EHDS row);
- changes the **intended purpose** statement, target users, or claims in any published
  material.

Procedure: raise a `risk` issue referencing this ADR → walk MDCG 2019-11 rev. 1 decision
steps → update *Current decision* (+ date, deciders) → if the answer flips to **yes**,
activate the MDSW tier in [`CONFORMANCE.md`](../standards/CONFORMANCE.md) and classify per
**MDR Annex VIII Rule 11**: decision-support / diagnostic-or-therapeutic software is
**class IIa** by default, **IIb** if it may cause serious deterioration of health or a
surgical intervention, **III** if it may cause death or an irreversible deterioration of
health; software intended to monitor physiological processes is **IIa**, **IIb** where it is for
monitoring **vital** physiological parameters whose variations could result in immediate danger to
the patient; **all other** software is **class I**. Record
the resulting **device class** — which is *distinct* from the IEC 62304 **software safety
class** (A/B/C) decided in [ADR-0002](0002-software-safety-classification.md). Then
evaluate the German **DiGA** fast-track (§ 33a SGB V / DiGAV; requires MDSW class I or IIa)
if reimbursement in Germany is a goal.

The PR template asks the trigger question on every pull request; `CODEOWNERS` (once
owners are set) forces human review of changes to this file.

## Consequences

- Good: qualification drift is caught at the feature gate, not at transfer; the evidence
  the future manufacturer needs accrues continuously.
- Bad / accepted: a small per-PR review burden; the answer "not MDSW" must be defensible
  at every point in time, not just at release.
