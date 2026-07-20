# Standards & regulatory conformance index

Which standards and regulations this project works against, in which role, and where the
evidence lives in the repo. Strategy: **design for conformance, defer certification** —
the product is developed in a research project, market placement after project end is
intended, the manufacturer (MDR sense) is TBD; qualification as medical-device software
is a **living decision** ([ADR-0001](../adr/0001-mdsw-qualification.md)).

**Status values** — `active`: applied now, evidence in this repo · `conditional`: applies
only if the stated condition holds · `iff MDSW`: becomes binding only if ADR-0001 flips
to "is MDSW" · `deferred-to-manufacturer`: an obligation of the future market-placing
manufacturer, not a repo artifact · `watch`: applicability window or final shape still
approaching — re-check at the review cadence.

Standard editions below were verified 2026-07 against the official catalogues (iso.org,
webstore.iec.ch) and EU law via the stable ELI links. Horizontal-law application dates
(CRA; AI Act — incl. the 2026 *Digital Omnibus* deferrals; EHDS) and the IEC 62304 Ed. 2
timeline are moving targets — re-check them at the review cadence.

## 1. Engineering process & quality (active now)

| Standard | Edition | Role | Status | Evidenced in |
|---|---|---|---|---|
| ISO/IEC/IEEE 16085 — *Systems and software engineering — Life cycle processes — Risk management* | 2021 | frame for the risk process (both registers) | active | [`docs/RISK_MANAGEMENT.md`](../RISK_MANAGEMENT.md), [`docs/HARM_RISK.md`](../HARM_RISK.md) |
| ISO/IEC/IEEE 42010 — *Software, systems and enterprise — Architecture description* | 2022 | architecture-description frame; arc42 is the concrete template | active | [`docs/arc42/`](../arc42/README.md) (arc42 v9.0) |
| ISO/IEC/IEEE 29148 — *Systems and software engineering — Life cycle processes — Requirements engineering* | 2018 | requirement quality + the `requirement` issue convention | active | [`docs/TRACEABILITY.md`](../TRACEABILITY.md) |
| ISO/IEC 25010 — *SQuaRE — Product quality model* | **2023** (2011 withdrawn; quality-in-use now ISO/IEC 25019:2023) | quality vocabulary for arc42 §1/§10 | active | [`docs/arc42/10_quality_requirements.md`](../arc42/10_quality_requirements.md) |
| ISO/IEC/IEEE 12207 — *Software life cycle processes* | 2017 | life-cycle frame (software) | active (reference) | this index |
| ISO/IEC/IEEE 15288 — *System life cycle processes* | **2023** (replaced 2015) | life-cycle frame (system) | active (reference) | this index |

## 2. Security & privacy baseline (active now)

| Standard / Regulation | Edition | Role | Status | Evidenced in |
|---|---|---|---|---|
| [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | in force | lawful processing; DPIA (Art. 35) where high-risk (e.g. health data); Art. 32 measures | active — **method live; fill before real-data processing** (per project) | [`docs/dpia/`](../dpia/README.md) (living DPIA + Art. 32 TOM register), the [`dpia-officer`](https://github.com/forschungsgruppe-digital-health/risk-management-template/blob/main/skills/dpia-officer/SKILL.md) skill |
| ISO/IEC 27001 — *Information security management systems — Requirements* | 2022 | ISMS reference frame | active (reference) | this index |
| ISO 27799 — *Health informatics — Information security controls in health based on ISO/IEC 27002* | **2025** (third ed., 2025-12; based on ISO/IEC 27002:2022; cancels and replaces 27799:2016 and ISO/TS 14441:2013) | health-sector ISM guidance | active (reference) | this index |
| IEC 81001-5-1 — *Health software and health IT systems safety, effectiveness and security — Part 5-1: Security — Activities in the product life cycle* | 2021 | secure development lifecycle for **health software regardless of MDSW status**; designed to plug into IEC 62304; FDA-recognized, referenced in German TI context | active | [`docs/SECURITY_RISK.md`](../SECURITY_RISK.md), [`SECURITY.md`](../../SECURITY.md) (CVD), SBOM workflow, [`docs/SOUP.md`](../SOUP.md), vulnerability→register automation |

## 3. Conditional — German healthcare telematics infrastructure (iff the product integrates with TI/ePA)

| Specification | Version | Role | Status | Evidenced in |
|---|---|---|---|---|
| gematik specifications (ISiK — *Informationstechnische Systeme im Krankenhaus*; ePA) — [fachportal.gematik.de](https://fachportal.gematik.de) | use current published stage | FHIR-based interoperability with hospital systems / ePA | conditional | project-specific interface docs |
| BSI TR-03161 — *Anforderungen an Anwendungen im Gesundheitswesen* (Part 1: mobile, Part 2: web, Part 3: backend) | current version at evaluation | security requirements for health applications | conditional | project-specific security concept |
| BSI C5 — *Cloud Computing Compliance Criteria Catalogue* | 2020 | cloud-operation attestation frame | conditional (cloud operation) | deployment docs |

## 4. Activated iff MDSW = yes (ADR-0001)

| Standard / Regulation | Edition | Role | Status | Evidence prepared in |
|---|---|---|---|---|
| [Regulation (EU) 2017/745 (MDR)](https://eur-lex.europa.eu/eli/reg/2017/745/oj) | in force | qualification (Art. 2(1)) + classification (**Annex VIII Rule 11**) + GSPR Annex I ([checklist](GSPR-CHECKLIST.md)) | iff MDSW | [ADR-0001](../adr/0001-mdsw-qualification.md) |
| MDCG 2019-11 **rev. 1 (17 June 2025)** — *Guidance on qualification and classification of software — MDR/IVDR* ([direct PDF](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf)) | rev. 1 covers AI-based software, modules, EHR/EHDS interplay | the decision aid ADR-0001 walks | active (drives the living ADR) | [ADR-0001](../adr/0001-mdsw-qualification.md) |
| MDCG 2020-1 — *Guidance on clinical evaluation (MDR) / performance evaluation (IVDR) of medical device software* | 2020 (March) | clinical-evaluation frame for MDSW | iff MDSW (execution deferred-to-manufacturer) | — |
| MDCG 2019-16 — *Guidance on cybersecurity for medical devices* | rev. 1 (July 2020) | operationalizes the Annex I §17 cybersecurity GSPR; complements IEC 81001-5-1 | iff MDSW — **security-RM method kept live now** | [`docs/SECURITY_RISK.md`](../SECURITY_RISK.md), [`SECURITY.md`](../../SECURITY.md), SBOM workflow, [`docs/SOUP.md`](../SOUP.md), vulnerability→register automation |
| IEC 62304 — *Medical device software — Software life cycle processes* | 2006 + A1:2015 (Ed. 1.1) — **Ed. 2 at Committee Draft stage; IEC forecast publication ~2028 (date uncertain — monitor)**; Ed. 1.1 remains state of the art until then | software life cycle; SOUP (§8.1.2, §5.3.3–5.3.4, §7.1.3); software safety classes A/B/C (§4.3 → [ADR-0002](../adr/0002-software-safety-classification.md)) | iff MDSW — evidence kept live | [`docs/SOUP.md`](../SOUP.md), [`soup.yaml`](../../soup.yaml), [`docs/TRACEABILITY.md`](../TRACEABILITY.md), [ADR-0002](../adr/0002-software-safety-classification.md), [§-coverage map](IEC-62304-COVERAGE.md) |
| ISO 14971 — *Medical devices — Application of risk management to medical devices* | 2019 (Ed. 3); harmonized EU edition **EN ISO 14971:2019+A11:2021** (Annex ZA — the MDR "as far as possible" reconciliation, see [`HARM_RISK.md`](../HARM_RISK.md) §4) | harm-risk management process | iff MDSW — **register kept live now** | [`docs/HARM_RISK.md`](../HARM_RISK.md), harm-risk board, [§9 report](../HARM_RISK_REPORT.md) |
| ISO/TR 24971 — *Guidance on the application of ISO 14971* | 2020 | scoring guidance (incl. P1×P2 decomposition) | companion to the above | [`docs/HARM_RISK.md`](../HARM_RISK.md) |
| IEC 62366-1 — *Application of usability engineering to medical devices* | 2015 + A1:2020 | usability engineering file; **summative validation deferred-to-manufacturer** | iff MDSW — **method kept live now** | [`docs/USABILITY.md`](../USABILITY.md), the [`use-scenario`](../../.github/ISSUE_TEMPLATE/use-scenario.yml) form, `hazard-cat:usability` harm-risks; formative notes per project |
| ISO 81001-1 — *Health software and health IT systems safety, effectiveness and security — Part 1: Principles and concepts* | 2021 | the foundational vocabulary + the safety/effectiveness/security "key properties" triad the other health-software standards build on | active (reference — foundational) | [`docs/learning/risk-management-primer.md`](../learning/risk-management-primer.md), [`docs/SECURITY_RISK.md`](../SECURITY_RISK.md) |
| IEC 82304-1 — *Health software — Part 1: General requirements for product safety* | 2016 | product-level safety **and security** requirements for standalone health software (points to IEC 62304 for the life cycle, ISO 14971 for risk management) | iff MDSW | — |
| IEC 80001-1 — *Application of risk management for IT-networks incorporating medical devices — Part 1: Safety, effectiveness and security in the implementation and use of connected medical devices or connected health software* | 2021 (Ed. 2) | operator-side network risk (deployment into clinical IT) | iff MDSW (operator-facing) | deployment docs |
| ISO 13485 — *Medical devices — Quality management systems — Requirements for regulatory purposes* | 2016 (EN version incl. A11:2021) | the manufacturer's QMS | **deferred-to-manufacturer** — organizational, not a repo artifact | [`docs/CONFORMANCE_TRANSFER.md`](../CONFORMANCE_TRANSFER.md) |
| ISO 20417 — *Medical devices — Information to be supplied by the manufacturer* | 2026 (Ed. 2; supersedes 2021) | labelling / IFU content requirements (design-side) | iff MDSW | project labelling/IFU docs |
| EN ISO 15223-1 — *Medical devices — Symbols to be used with information to be supplied by the manufacturer — Part 1: General requirements* | 2021 (4th ed.) | label/IFU symbols (design-side) | iff MDSW | project labelling/IFU docs |

## 5. Watch — EU horizontal product law (applicability window approaching)

| Regulation | Key dates | Applies | Status |
|---|---|---|---|
| [Regulation (EU) 2024/2847 — Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) | in force 2024-12-10; **vulnerability-reporting obligations 2026-09-11**; main obligations **2027-12-11** | to commercial placement of products with digital elements — **iff the product is *not* MDR-covered** (MDR/IVDR devices are excluded); a post-project market placement lands inside its window | watch |
| [Regulation (EU) 2024/1689 — AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | staged: GPAI 2025-08-02; Annex-III high-risk **2026-08-02**; Art. 6(1) product-linked high-risk **2027-08-02** — these are the *enacted, still-operative* dates. The 2026 *Digital Omnibus* (signed 8 Jul 2026, **awaiting OJ publication — not yet in force**) will defer them to **2027-12-02** and **2028-08-02** respectively once published | iff AI components are added; MDSW + third-party conformity assessment ⇒ high-risk via Art. 6(1) | watch (trigger listed in ADR-0001) |
| [Regulation (EU) 2025/327 — European Health Data Space](https://eur-lex.europa.eu/eli/reg/2025/327/oj) | in force 2025-03-26; general application 2027-03-26; **EHR-system obligations (priority category 1: patient summary, ePrescription/eDispensation) 2029-03-26** | iff the product is or embeds an **EHR system** processing priority-category data → self-assessed conformity, technical documentation, EU declaration | watch |
| DiGA fast-track (Germany) — § 33a SGB V, DiGAV (BfArM) | available now | optional reimbursement pathway; **requires** MDSW class I/IIa | optional (evaluated at ADR-0001 flip) |
| **MDR/IVDR amendment — COM(2025) 1023** (*Simplification Package*, proposal adopted 2025-12-16; ordinary legislative procedure ongoing) | not yet law | may alter software classification (Rule 11), certificate validity, conformity-assessment routes, and the AI-Act interplay — re-walk [ADR-0001](../adr/0001-mdsw-qualification.md) when it lands | watch |
| MDCG 2025-6 / AIB 2025-1 — *Interplay between the MDR/IVDR and the AI Act* (June 2025) | published | the operative decision aid for the ADR-0001 **AI/ML trigger** (MDAI qualification, combined conformity assessment) | watch (cited from ADR-0001) |
| MDCG 2025-4 — *Guidance on MDSW apps distributed via online platforms* (2025) | published | applies iff the product is distributed as an app via online platforms/app stores | conditional |

## Maintenance

- Re-check `watch` rows and the IEC 62304 Ed. 2 note at the regular risk review
  ([`RISK_MANAGEMENT.md`](../RISK_MANAGEMENT.md) §7); regulatory drift is a
  `risk-cat:compliance` register entry.
- Any edit to this file and to ADR-0001 should be human-reviewed (`CODEOWNERS` entry
  provided, set owners per project).
- Column "Evidenced in" must point at living repo artifacts — an empty cell in an
  `active` row is a gap to raise as a risk.
