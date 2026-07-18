# Architecture Decision Records

MADR-style ADRs ([template](TEMPLATE.md)); one file per decision, numbered
`NNNN-kebab-title.md`, never renumbered, superseded instead of deleted. Decisions belong
here when they are important, expensive, large-scale, or risky — the [arc42
§9](../arc42/09_architecture_decisions.md) criterion.

Risk linkage (see [`docs/RISK_MANAGEMENT.md`](../RISK_MANAGEMENT.md) §9): an ADR taken to
reduce a registered risk cites the risk issue in its rationale; the issue links back; the
architecture-level view lives in [arc42 §11](../arc42/11_technical_risks.md).

## Index

| ADR | Title | Status |
|---|---|---|
| [0001](0001-mdsw-qualification.md) | Medical-device-software qualification (living) | accepted — living, re-evaluated at feature gates |
| [0002](0002-software-safety-classification.md) | Software safety classification — IEC 62304 §4.3 (living) | accepted — living, re-evaluated with ADR-0001 |
