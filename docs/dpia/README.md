# Data Protection Impact Assessment (DPIA) — <product>

> **Template — living artifact (GDPR Art. 35).** A DPIA is required where processing is *likely to
> result in a high risk* to the rights and freedoms of natural persons (Art. 35(1)), in particular
> for large-scale processing of special-category data such as **health data** (Art. 9, Art. 35(3)).
> Fill this per project **before you process real personal data**; keep it in step with the system
> via the [`dpia-officer`](../../skills/dpia-officer/SKILL.md) skill. Legal determinations (lawful
> basis, necessity/proportionality, residual-risk acceptance, sign-off) are **[DPO/LEGAL INPUT
> NEEDED]** — this template does not decide them. **Synthetic-only data is out of scope.**

## 0. Document control

| Field | Value |
|---|---|
| Version | 0.1 (draft — not a go-live sign-off) |
| Last updated | <YYYY-MM-DD> |
| Owner (author) | <name / role> |
| Data controller | <legal entity> [DPO/LEGAL INPUT NEEDED] |
| DPO consulted | <name / date, or "not yet"> (Art. 35(2)) |
| Status | draft · **not** cleared for real-data processing |

## 1. Is a DPIA required? (screening — Art. 35(1), (3))

Record the screening decision. Triggers that make a DPIA likely-mandatory (Art. 35(3) + EDPB
guidance): systematic & extensive evaluation/profiling; large-scale special-category (e.g. health)
data; systematic monitoring. State which apply.

- Processes personal data? <yes/no> · Special-category (health) data? <yes/no>
- Screening conclusion: <DPIA required / not required — rationale> [DPO/LEGAL INPUT NEEDED]

## 2. Description of the processing (Art. 35(7)(a))

### 2.1 Nature
<What the system does with personal data — collect, store, display, transmit, analyse; who the
processing actors are (services, skills/agents, operators).>

### 2.2 Scope — data categories
<List each personal-data category processed and its sensitivity (identifiers, contact, health/
clinical, credentials, logs). Keep this the data-minimisation surface — only what is needed.>

| Data category | Special-category? | Purpose | Retention |
|---|---|---|---|
| <e.g. name, contact> | no | <…> | <…> |
| <e.g. clinical/health data> | yes (Art. 9) | <…> | <…> |

### 2.3 Context, purposes, lawful basis
<Purpose(s) of processing; lawful basis under Art. 6 (and the Art. 9(2) condition for health data).>
Lawful basis: <…> [DPO/LEGAL INPUT NEEDED]

### 2.4 Data flows (high-level)
<Where personal data enters, is stored, moves, and leaves — a simple flow. Note each hand-off.>

### 2.5 Recipients, retention, transfers
<Recipients / processors; retention & deletion; any transfer to a third country (Ch. V) and its
safeguard.> Transfers: <none / …> [DPO/LEGAL INPUT NEEDED]

## 3. Consultation (Art. 35(9))
<Where appropriate, the views of data subjects or their representatives.>

## 4. Necessity & proportionality (Art. 35(7)(b))
<Is the processing necessary and proportionate to the purpose? Data-minimisation, accuracy, storage
limitation, transparency, and how data-subject rights (Art. 12–22) are supported.>
Assessment: <…> [DPO/LEGAL INPUT NEEDED]

## 5. Risk assessment (Art. 35(7)(c))

Risks to the **rights and freedoms** of data subjects (not project risk — that is the delivery
register; not safety — that is the harm-risk register). Score likelihood × severity per your policy.

| # | Risk to data subjects | Likelihood | Severity | Mitigation (→ TOM) | Residual |
|---|---|---|---|---|---|
| R1 | <e.g. unauthorised access to health data> | <L> | <S> | TOM A-rows | <…> [DPO] |
| R2 | <e.g. personal data leaked via logs> | <L> | <S> | TOM (log minimisation) | <…> [DPO] |
| R3 | <e.g. excessive retention / no erasure> | <L> | <S> | TOM (retention) | <…> [DPO] |

## 6. Measures to reduce risk (Art. 35(7)(d))
The technical & organisational measures live in the register:
[`technical-organisational-measures.md`](technical-organisational-measures.md) (GDPR Art. 32). Each
risk above links the control rows that mitigate it; each control links where it is implemented.

## 7. DPO advice, residual risk & sign-off (Art. 35(2), Art. 36)
<The DPO's advice; the residual risk after measures; whether prior consultation with the supervisory
authority is needed (Art. 36, if residual high risk remains). **The go-live sign-off gate.**>

| Role | Name | Decision | Date |
|---|---|---|---|
| DPO | <…> | advised / prior-consultation-needed | <…> [DPO/LEGAL INPUT NEEDED] |
| Controller | <…> | cleared for real data / held | <…> [DPO/LEGAL INPUT NEEDED] |

## 8. Pre-go-live checklist (engineering ↔ DPO)
Concrete gates that must be closed before real personal data is processed:

- [ ] All §5 risks have an implemented mitigation or a DPO-accepted residual
- [ ] Encryption in transit and at rest in place (TOM D-rows)
- [ ] Retention & erasure implemented; subject-rights process defined (Art. 12–22)
- [ ] Breach-notification process defined (Art. 33–34)
- [ ] Recipients/processors under a processing agreement (Art. 28); transfers safeguarded (Ch. V)
- [ ] §7 DPO advice recorded and controller sign-off obtained → then bump to v1.0

## 9. Review log & change triggers
Append one row per evaluation (the [`dpia-officer`](../../skills/dpia-officer/SKILL.md) skill does
this automatically after each data-surface change):

| Date | Version | Change | By |
|---|---|---|---|
| <YYYY-MM-DD> | 0.1 | Initial draft from template | <author> |
