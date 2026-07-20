# IEC 62304 process-area coverage (design-for-conformance map)

Which IEC 62304:2006+A1:2015 clauses this repo keeps evidence for **now**, which are
**deferred** to the future manufacturer, and which are **not yet in scope** — so the line
between "deferred on purpose" and "silently missing" is explicit. This binds only if the
product qualifies as MDSW ([ADR-0001](../adr/0001-mdsw-qualification.md)); the **software
safety class** ([ADR-0002](../adr/0002-software-safety-classification.md)) sets how much
rigour each clause needs (class A < B < C). Clause numbers verified against the licensed
standard (2026-07).

| Clause | Area | Status | Where / note |
|---|---|---|---|
| §4.3 | Software safety classification | **covered** | [ADR-0002](../adr/0002-software-safety-classification.md) — risk-based A/B/C, per software item |
| §5.1 | Software development planning | not-yet | a class-B/C project adds a software development plan; §5.1.1(c) traceability is modelled in [`TRACEABILITY.md`](../TRACEABILITY.md) |
| §5.2 | Software requirements analysis | partial | `requirement`-labelled issues ([`TRACEABILITY.md`](../TRACEABILITY.md)) capture requirements; a formal SRS is deferred |
| §5.3 | Software architectural design | partial | arc42 §5 building-block view; the SOUP boundary in [`SOUP.md`](../SOUP.md) (§5.3.3–5.3.4; §5.3.5 segregation is architectural, not SOUP) |
| §5.4 | Software detailed design | not-yet | class C only; not maintained at template stage |
| §5.5 | Software unit implementation (& verification) | partial | code review + unit tests are project practice; formal unit-verification records deferred |
| §5.6 | Software integration & integration testing | not-yet | project CI; formal integration records deferred |
| §5.7 | Software system testing | partial | project test suite; formal system-test records deferred |
| §5.8 | Software release | partial | SBOM per release ([`sbom.yml`](../../.github/workflows/sbom.yml)); formal release records + anomaly list at release deferred |
| §6 | Software maintenance process | not-yet | a maintenance plan + SOUP change-evaluation on version bump is a follow-up |
| §7 | Software risk-management process | **covered** | [`HARM_RISK.md`](../HARM_RISK.md) (ISO 14971); §7.1.3 SOUP anomalies in [`SOUP.md`](../SOUP.md); §7.3 traceability |
| §8 | Software configuration management | partial | Git + the SBOM give configuration identification; a formal CM plan is deferred |
| §8.1.2 | SOUP identification | **covered** | [`soup.yaml`](../../soup.yaml) + [`SOUP.md`](../SOUP.md) |
| §9 | Software problem-resolution process | partial | GitHub Issues + the register; a formal problem-resolution procedure is a follow-up |

**Legend:** *covered* = live evidence in this repo · *partial* = a base exists, formal
62304 records are added at the MDSW flip · *not-yet* = deliberately out of scope until then
(**not** a silent omission). Manufacturer-organizational items (ISO 13485 QMS, CE, clinical
evaluation, summative usability, PMS) live in
[`CONFORMANCE_TRANSFER.md`](../CONFORMANCE_TRANSFER.md), not here.

> AMD1:2015 retitled §5.5 to "Software unit implementation" (verification folded into
> subclauses) and §5.8 to "Software release for utilization at a system level" — scope
> unchanged.
