<!-- Harm risk (ISO 14971) — risks of HARM only (injury/damage to health, incl. wrong or
     delayed clinical decisions caused by the software). Delivery risks use the "Risk"
     template. Method: docs/HARM_RISK.md. Quick actions at the bottom apply the labels. -->

## Hazard

<!-- REQUIRED. Potential source of harm, e.g. "questionnaire score displayed for the
     wrong patient". -->

## Foreseeable sequence of events

<!-- REQUIRED. How normal use, reasonably foreseeable misuse, or a failure leads to the
     hazardous situation. -->

## Hazardous situation

<!-- REQUIRED. Who is exposed to the hazard, and in what circumstances. -->

## Harm

<!-- REQUIRED. The injury or damage to health that can result. -->

## Hazard category

<!-- pick ONE and adjust the /label quick action below:
     data-integrity | availability | confidentiality |
     clinical-misinterpretation | interoperability | usability -->

## Severity of harm S (1–5)

<!-- 1 negligible · 2 minor · 3 serious · 4 critical · 5 catastrophic
     (anchors: docs/HARM_RISK.md §3) -->

## Probability of harm P (1–5) — optionally decomposed P1 × P2

<!-- P1 = probability of the hazardous situation; P2 = probability it leads to harm. -->

## Risk control measure(s) — state the hierarchy tier per measure (14971 §7.1 order)

<!-- 1 inherently safe design → 2 protective measures → 3 information for safety, e.g.
     1. (tier 1) bind patient context immutably per view — ADR-xxxx
     2. (tier 2) patient banner with name/DOB on every clinical view -->

## Residual risk evaluation

<!-- Re-scored S × P after controls, judged against the acceptability matrix (§4). -->

## Verification plan (TWO per control — implemented + effective, §6)

## Benefit–risk note (only if residual risk stays above acceptability)

## Design element / ADR / requirement the control lives in

## Proposed owner

/label ~"harm-risk" ~"harm-risk::open"
