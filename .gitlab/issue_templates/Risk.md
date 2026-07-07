<!-- Risk register entry (delivery risk). Method: docs/RISK_MANAGEMENT.md.
     Harm/safety risks use the "Harm Risk" template instead (docs/HARM_RISK.md).
     The quick actions at the bottom apply the labels on creation — leave them in. -->

## Risk (cause → uncertain event → consequence)

<!-- REQUIRED. e.g. "Because the upstream API has no SLA (cause), it may be
     unavailable during the pilot (event), blocking the demo scenario (consequence)." -->

## Category

<!-- pick ONE and adjust the /label quick action below accordingly:
     schedule | scope | dependency | tech-debt | resource |
     supply-chain | vulnerability | secret | compliance -->

## Likelihood (1–5)

<!-- 1 rare (<~10%) · 2 unlikely · 3 possible · 4 likely · 5 almost certain
     (anchors: docs/RISK_MANAGEMENT.md §3) -->

## Impact (1–5)

<!-- 1 negligible · 2 minor · 3 moderate · 4 major · 5 critical -->

## Proposed owner

## Triggers / early-warning signals

## Mitigation action(s) — REQUIRED (at least one)

## Contingency (if it materializes anyway)

## Affected (deliverables, milestones, components)

<!-- Score = L×I is set at triage as the issue WEIGHT (/weight <n>).
     Severity label (risk::sev-*) is applied at triage per §4. -->

/label ~"risk" ~"risk::open"
