# Technical & Organisational Measures (TOM) — GDPR Art. 32

> **Template.** The Art. 32 "appropriate technical and organisational measures" that secure the
> processing — the concrete mitigations the [DPIA](README.md) §5 risks point at. Fill the
> **Where implemented** cell with a real pointer (file · ADR · CI gate) and set the **Status**;
> an `active` DPIA risk whose mitigation cell is empty is a gap to close. Kept current by the
> [`dpia-officer`](../../skills/dpia-officer/SKILL.md) skill.
>
> **Status legend:** ✅ implemented & verified · 🟢 implemented · 🟠 partial / verify at go-live ·
> 🔴 gap · ⏳ planned (milestone). **[DPO/LEGAL INPUT NEEDED]** marks a legal determination.

## A. Confidentiality — access control (Art. 5(1)(f), 32(1)(b))

| # | Measure | GDPR ref | Where implemented | Status |
|---|---|---|---|---|
| A1 | **Authentication required** for all endpoints exposing personal data | 32(1)(b) | <auth config · ADR> | 🔴 |
| A2 | **Authorization / least-privilege** — each actor reaches only the data it needs | 5(1)(c), 32(1)(b) | <authz rules · ADR> | 🔴 |
| A3 | **Role/attribute-based access** with documented roles | 32(1)(b) | <identity provider · roles> | 🔴 |
| A4 | **Secrets management** — no credentials in the repo (gitleaks / vault) | 32(1)(b) | <secret-scanning · .gitignore> | 🟠 |

## B. Integrity (Art. 5(1)(f), 32(1)(b))

| # | Measure | GDPR ref | Where implemented | Status |
|---|---|---|---|---|
| B1 | **Single controlled write path** — no direct data-store writes bypassing validation | 5(1)(f) | <architecture invariant> | 🔴 |
| B2 | **Data-minimisation surface** — only the necessary data categories are accepted/stored | 5(1)(c) | <schema / allow-list> | 🔴 |
| B3 | **Audit / provenance** of access & change | 5(2), 30 | <audit log / capability> | 🔴 |

## C. Availability & resilience (Art. 32(1)(b), (c))

| # | Measure | GDPR ref | Where implemented | Status |
|---|---|---|---|---|
| C1 | **Backup / restore (disaster recovery)** | 32(1)(c) | <backup policy> | 🔴 |
| C2 | **Monitoring / alerting** on the processing systems | 32(1)(b) | <monitoring stack> | 🔴 |

## D. Pseudonymisation, transport & storage (Art. 32(1)(a))

| # | Measure | GDPR ref | Where implemented | Status |
|---|---|---|---|---|
| D1 | **Encryption in transit** (TLS) | 32(1)(a) | <TLS config> | 🔴 |
| D2 | **Encryption at rest** | 32(1)(a) | <storage encryption> | 🔴 |
| D3 | **Pseudonymisation / minimisation** where the purpose allows | 32(1)(a), 25 | <pseudonymisation approach> | 🔴 |
| D4 | **Retention & erasure** — data deleted when no longer needed | 5(1)(e), 17 | <retention/deletion job> | 🔴 |

## E. Logging (Art. 5(1)(f), 32(1)(b))

| # | Measure | GDPR ref | Where implemented | Status |
|---|---|---|---|---|
| E1 | **Log minimisation** — no personal data / PII in application logs or error bodies | 5(1)(c), 32 | <logging policy> | 🔴 |

## F. Data-subject rights & process (Art. 12–22, 33–34)

| # | Measure | GDPR ref | Where implemented | Status |
|---|---|---|---|---|
| F1 | **Subject-access / rectification / erasure** process | 12–17 | <rights process> | 🔴 |
| F2 | **Breach-notification** process (72 h) | 33–34 | <incident/CVD process> | 🔴 |
| F3 | **Processing agreements** with processors; transfer safeguards | 28, Ch. V | <DPA register> | 🔴 [DPO] |

## G. Governance (Art. 5(2), 24, 30)

| # | Measure | GDPR ref | Where implemented | Status |
|---|---|---|---|---|
| G1 | **Record of processing activities (RoPA)** | 30 | <RoPA> | 🔴 [DPO] |
| G2 | **Data-protection-by-design & by-default** embedded in the process | 25 | this DPIA + the design ADRs | 🟠 |

## H. Open prerequisites (must close before real-data go-live)
- <list the 🔴/🟠 rows that gate go-live, cross-referenced from the DPIA §8 checklist>
