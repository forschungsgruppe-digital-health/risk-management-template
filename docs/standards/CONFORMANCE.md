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

Standard editions below were verified 2026-07; ISO/IEC/IEC-standards are available via
the official catalogues (iso.org, webstore.iec.ch), EU law via the stable ELI links.

## 1. Engineering process & quality (active now)

| Standard | Edition | Role | Status | Evidenced in |
|---|---|---|---|---|
| ISO/IEC/IEEE 16085 — *Systems and software engineering — Life cycle processes — Risk management* | 2021 | frame for the risk process (both registers) | active | [`docs/RISK_MANAGEMENT.md`](../RISK_MANAGEMENT.md), [`docs/HARM_RISK.md`](../HARM_RISK.md) |
| ISO/IEC/IEEE 42010 — *Software, systems and enterprise — Architecture description* | 2022 | architecture-description frame; arc42 is the concrete template | active | [`docs/architecture/`](../architecture/README.md) (arc42 v9) |
| ISO/IEC/IEEE 29148 — *Systems and software engineering — Life cycle processes — Requirements engineering* | 2018 | requirement quality + the `requirement` issue convention | active | [`docs/TRACEABILITY.md`](../TRACEABILITY.md) |
| ISO/IEC 25010 — *SQuaRE — Product quality model* | **2023** (2011 withdrawn; quality-in-use now ISO/IEC 25019:2023) | quality vocabulary for arc42 §1/§10 | active | [`docs/architecture/10_quality_requirements.md`](../architecture/10_quality_requirements.md) |
| ISO/IEC/IEEE 12207 — *Software life cycle processes* | 2017 | life-cycle frame (software) | active (reference) | this index |
| ISO/IEC/IEEE 15288 — *System life cycle processes* | **2023** (replaced 2015) | life-cycle frame (system) | active (reference) | this index |

## 2. Security & privacy baseline (active now)

| Standard / Regulation | Edition | Role | Status | Evidenced in |
|---|---|---|---|---|
| [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | in force | lawful processing, DPIA where required | active | project-specific DPIA docs (add per project) |
| ISO/IEC 27001 — *Information security management systems — Requirements* | 2022 | ISMS reference frame | active (reference) | this index |
| ISO 27799 — *Health informatics — Information security management in health using ISO/IEC 27002* | 2016 — **caveat:** still based on ISO/IEC 27002:2013 controls; map to 27002:2022 numbering when using both | health-sector ISM guidance | active (reference) | this index |
| IEC 81001-5-1 — *Health software and health IT systems safety, effectiveness and security — Part 5-1: Security — Activities in the product life cycle* | 2021 | secure development lifecycle for **health software regardless of MDSW status**; designed to plug into IEC 62304; FDA-recognized, referenced in German TI context | active | SBOM workflow, [`docs/SOUP.md`](../SOUP.md), vulnerability→register automation |

## 3. Conditional — German healthcare telematics infrastructure (iff the product integrates with TI/ePA)

| Specification | Version | Role | Status | Evidenced in |
|---|---|---|---|---|
| gematik specifications (ISiK — *Informationstechnische Systeme im Krankenhaus*; ePA) — [fachportal.gematik.de](https://fachportal.gematik.de) | use current published stage | FHIR-based interoperability with hospital systems / ePA | conditional | project-specific interface docs |
| BSI TR-03161 — *Anforderungen an Anwendungen im Gesundheitswesen* (Part 1: mobile, Part 2: web, Part 3: backend) | current version at evaluation | security requirements for health applications | conditional | project-specific security concept |
| BSI C5 — *Cloud Computing Compliance Criteria Catalogue* | 2020 | cloud-operation attestation frame | conditional (cloud operation) | deployment docs |

## 4. Activated iff MDSW = yes (ADR-0001)

| Standard / Regulation | Edition | Role | Status | Evidence prepared in |
|---|---|---|---|---|
| [Regulation (EU) 2017/745 (MDR)](https://eur-lex.europa.eu/eli/reg/2017/745/oj) | in force | qualification (Art. 2(1)) + classification (**Annex VIII Rule 11**) + GSPR Annex I | iff MDSW | [ADR-0001](../adr/0001-mdsw-qualification.md) |
| MDCG 2019-11 **rev. 1 (June 2025)** — *Guidance on qualification and classification of software — MDR/IVDR* ([MDCG guidance list](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en)) | rev. 1 covers AI-based software, modules, EHR/EHDS interplay | the decision aid ADR-0001 walks | active (drives the living ADR) | [ADR-0001](../adr/0001-mdsw-qualification.md) |
| MDCG 2020-1 — *Guidance on clinical evaluation (MDR) / performance evaluation (IVDR) of medical device software* | 2020 | clinical-evaluation frame for MDSW | iff MDSW (execution deferred-to-manufacturer) | — |
| IEC 62304 — *Medical device software — Software life cycle processes* | 2006 + A1:2015 (Ed. 1.1) — **Ed. 2 in final approval, publication expected from 2026-08**; Ed. 1.1 remains state of the art until published and harmonized | software life cycle; SOUP (§8.1.2, §5.3.3–5.3.4, §7.1.2–7.1.3); safety classes A/B/C (§4.3) | iff MDSW — evidence kept live | [`docs/SOUP.md`](../SOUP.md), [`soup.yaml`](../../soup.yaml), [`docs/TRACEABILITY.md`](../TRACEABILITY.md) |
| ISO 14971 — *Medical devices — Application of risk management to medical devices* | 2019 (Ed. 3) | harm-risk management process | iff MDSW — **register kept live now** | [`docs/HARM_RISK.md`](../HARM_RISK.md), harm-risk board |
| ISO/TR 24971 — *Guidance on the application of ISO 14971* | 2020 | scoring guidance (incl. P1×P2 decomposition) | companion to the above | [`docs/HARM_RISK.md`](../HARM_RISK.md) |
| IEC 62366-1 — *Application of usability engineering to medical devices* | 2015 + A1:2020 | usability engineering file; **summative validation deferred-to-manufacturer** | iff MDSW | formative-evaluation notes per project |
| IEC 82304-1 — *Health software — Part 1: General requirements for product safety* | 2016 | product-level safety requirements for standalone health software | iff MDSW | — |
| IEC 80001-1 — *Application of risk management for IT-networks incorporating medical devices* | 2021 (Ed. 2) | operator-side network risk (deployment into clinical IT) | iff MDSW (operator-facing) | deployment docs |
| ISO 13485 — *Medical devices — Quality management systems — Requirements for regulatory purposes* | 2016 (EN version incl. A11:2021) | the manufacturer's QMS | **deferred-to-manufacturer** — organizational, not a repo artifact | [`docs/CONFORMANCE_TRANSFER.md`](../CONFORMANCE_TRANSFER.md) |

## 5. Watch — EU horizontal product law (applicability window approaching)

| Regulation | Key dates | Applies | Status |
|---|---|---|---|
| [Regulation (EU) 2024/2847 — Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) | in force 2024-12-10; **vulnerability-reporting obligations 2026-09-11**; main obligations **2027-12-11** | to commercial placement of products with digital elements — **iff the product is *not* MDR-covered** (MDR/IVDR devices are excluded); a post-project market placement lands inside its window | watch |
| [Regulation (EU) 2024/1689 — AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | staged: GPAI 2025-08-02; Annex-III high-risk 2026-08-02; Art. 6(1) product-linked high-risk 2027-08-02 | iff AI components are added; MDSW + third-party conformity assessment ⇒ high-risk via Art. 6(1) | watch (trigger listed in ADR-0001) |
| [Regulation (EU) 2025/327 — European Health Data Space](https://eur-lex.europa.eu/eli/reg/2025/327/oj) | in force 2025-03-26; general application 2027-03-26; **EHR-system obligations (priority category 1: patient summary, ePrescription/eDispensation) 2029-03-26** | iff the product is or embeds an **EHR system** processing priority-category data → self-assessed conformity, technical documentation, EU declaration | watch |
| DiGA fast-track (Germany) — § 33a SGB V, DiGAV (BfArM) | available now | optional reimbursement pathway; **requires** MDSW class I/IIa | optional (evaluated at ADR-0001 flip) |

## Maintenance

- Re-check `watch` rows and the IEC 62304 Ed. 2 note at the regular risk review
  ([`RISK_MANAGEMENT.md`](../RISK_MANAGEMENT.md) §7); regulatory drift is a
  `risk-cat:compliance` register entry.
- Any edit to this file and to ADR-0001 should be human-reviewed (`CODEOWNERS` entry
  provided, set owners per project).
- Column "Evidenced in" must point at living repo artifacts — an empty cell in an
  `active` row is a gap to raise as a risk.
