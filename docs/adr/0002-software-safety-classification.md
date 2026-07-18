# 0002 — Software safety classification (IEC 62304 §4.3)

- **Status:** accepted — **living**, re-evaluated together with
  [ADR-0001](0001-mdsw-qualification.md) and at the triggers below
- **Date:** <YYYY-MM-DD of the latest evaluation>
- **Deciders:** <project lead, regulatory-affairs contact if available>
- **Linked risks:** <register issue tracking the classification/regulatory risk, if raised>

> **Template note.** Ships with the conformance-readiness layer. Fill the placeholders at
> first triage; keep the mechanism. This is the **IEC 62304 software safety class**
> (A/B/C) — **distinct** from the MDR **Annex VIII Rule 11 device class** (I/IIa/IIb/III)
> decided in [ADR-0001](0001-mdsw-qualification.md). A product has *both*; they answer
> different questions (the patient-harm potential of a software item vs the market-access
> risk class of the device) and must never be conflated.

## Context and problem statement

IEC 62304 §4.3 requires each software system — and, since A1:2015, each software **item** —
to be assigned a **safety class** that sets the rigour of the required life-cycle
activities and documentation:

- **Class A** — the software system cannot contribute to a hazardous situation, **or** it
  can but the resulting risk — after taking into account risk-control measures *external*
  to the software — is not unacceptable.
- **Class B** — the software system can contribute to a hazardous situation with
  unacceptable residual risk (after external risk control), and the possible resulting
  **harm is non-serious injury**.
- **Class C** — as Class B, but the possible resulting **harm is death or serious injury**.

These are the **AMD1:2015 (Ed. 1.1) risk-based definitions** (§4.3 + Figure 3): since the
amendment, Class A no longer means "no injury is possible" — the class depends on the
*residual* risk after risk-control measures **external** to the software item.

The class drives how much of §5 (development), §7 (risk management) and §8 (configuration
management) applies and how fine the traceability must be — class **B/C** make the
requirement → design → test → SOUP granularity in
[`../TRACEABILITY.md`](../TRACEABILITY.md) mandatory. Per A1:2015 the class may be assigned
**per item**: a hazard-relevant item can be class B/C while the remainder is A, *if* the
segregation is justified. The class only **binds** once the product is MDSW
([ADR-0001](0001-mdsw-qualification.md)); it is recorded now because the harm-analysis
rationale behind it is near-impossible to reconstruct later.

## Current decision

<State the current class, e.g.:>

While the product is **not qualified as MDSW** ([ADR-0001](0001-mdsw-qualification.md)),
IEC 62304 does not bind and **no formal safety class is assigned** (record as
*N/A — not MDSW*). The provisional working assumption, should qualification flip, is
**Class <A|B|C>**, because <the software can / cannot contribute to a hazardous situation
that could lead to (serious) injury — reference the harm-risk file
[`../HARM_RISK.md`](../HARM_RISK.md)>. Item-level decomposition (§4.3, A1:2015):
<none yet | items X/Y provisionally class B/C, segregated from the class-A remainder —
justify the segregation>.

## Considered options

1. Assign the highest plausible class (C) pre-emptively — rejected: over-constrains a
   research build with documentation rigour that has no manufacturer to satisfy yet.
2. Leave the class entirely unrecorded until MDSW qualification — rejected: the
   harm-analysis rationale for the class is exactly the near-impossible-to-reconstruct
   evidence this layer exists to preserve.
3. **Record a provisional class + item decomposition now, binding on the ADR-0001 flip**
   (chosen): cheap to keep live, and it makes the traceability/SOUP rigour requirements
   explicit rather than implied.

## Consequences

- Good: the §4.3 class has a home and a rationale trail; the class-B/C traceability/SOUP
  granularity requirements are traceable to a decision, not folklore; the software safety
  class is never confused with the MDR device class.
- Bad / accepted: a provisional class must be revisited whenever the harm-risk picture,
  the architecture (segregation), or the qualification changes.

## Re-evaluation triggers (living ADR)

Re-evaluate (and record here) whenever:

- [ADR-0001](0001-mdsw-qualification.md) qualification changes — a flip to MDSW **binds**
  this class;
- a new or changed **harm-risk** ([`../HARM_RISK.md`](../HARM_RISK.md)) alters the
  worst-case harm the software can contribute to (may raise/lower a class);
- architecture changes alter the **segregation** that justifies an item-level class split.
