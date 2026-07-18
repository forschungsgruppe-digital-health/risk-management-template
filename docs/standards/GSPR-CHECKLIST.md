# GSPR conformity checklist (MDR Annex I) — <product>

> **Template.** MDR Annex I **General Safety and Performance Requirements (GSPR)**. Binds
> only if the product is MDSW ([ADR-0001](../adr/0001-mdsw-qualification.md)). This lists
> the GSPRs most relevant to standalone **software**; a full device needs the *entire*
> Annex I. For MDSW the manufacturer must produce a complete GSPR checklist as part of the
> technical documentation — this repo pre-stages the *software-side* evidence so it is not
> reconstructed later. **Numbering paraphrases MDR Annex I — confirm each item verbatim
> against the [OJ text](https://eur-lex.europa.eu/eli/reg/2017/745/oj) per product.**
> Determinations ("applicable?", "met?") are **[NEEDS RA INPUT]** — not decided by this
> template.

## Chapter I — General requirements

| GSPR | Requirement (paraphrase) | Applicable? | Evidence / where in repo | Met? |
|---|---|---|---|---|
| 1 | Safe & effective; risks acceptable weighed against benefit; no unacceptable compromise of clinical condition/safety | [RA] | intended purpose ([ADR-0001](../adr/0001-mdsw-qualification.md)); benefit-risk ([HARM_RISK_REPORT](../HARM_RISK_REPORT.md) §9) | [RA] |
| 2 | Reduce risks as far as possible without adversely affecting the benefit-risk ratio | [RA] | [HARM_RISK.md](../HARM_RISK.md) (ISO 14971) | [RA] |
| 3 | A risk-management **system** — plan → analysis → control → review, continuously updated | [RA] | HARM_RISK.md §1–§10; HARM_RISK_REPORT.md | [RA] |
| 4 | Risk-control measures in the safety priority order (inherently safe design → protective → information for safety) | [RA] | HARM_RISK.md §5 (14971 §7.1) | [RA] |
| 5 | Reduce risks related to **use error** (ergonomics, intended users & environment) | [RA] | usability (IEC 62366-1); `hazard-cat:usability` | [RA] |
| 8 | All known & foreseeable risks and undesirable side-effects minimised & acceptable vs benefit | [RA] | overall residual risk (HARM_RISK.md §8; HARM_RISK_REPORT.md) | [RA] |

## Chapter II — Design & manufacture (software-relevant)

| GSPR | Requirement (paraphrase) | Applicable? | Evidence / where in repo | Met? |
|---|---|---|---|---|
| 14.2(d) | Minimise risks from the interaction of software with the IT environment it runs in | [RA] | arc42 §3/§7; [SOUP.md](../SOUP.md) (environment) | [RA] |
| **17.1** | Electronic programmable systems / software: **repeatability, reliability, performance** in line with intended use; mitigate single-fault consequences | [RA] | IEC 62304 evidence ([IEC-62304-COVERAGE](IEC-62304-COVERAGE.md); SOUP; TRACEABILITY) | [RA] |
| **17.2** | Software developed per **state of the art** — development life cycle, **risk management incl. information security**, **verification & validation** | [RA] | IEC 62304 + IEC 81001-5-1; HARM_RISK.md; [TRACEABILITY.md](../TRACEABILITY.md) | [RA] |
| **17.3** | Software for mobile computing platforms designed for the platform's features + external use factors | [RA] | project design notes (iff mobile) | [RA] |
| **17.4** | Minimum requirements set out: **IT hardware, IT-network characteristics, IT-security measures** incl. protection against unauthorised access | [RA] | IEC 81001-5-1; MDCG 2019-16; security-review docs | [RA] |

> **GSPR 17.3 (mobile):** if the product runs on a mobile computing platform, add the
> platform-specific design evidence — screen size / contrast ratio, and external factors
> such as varying light or noise in the use environment. Otherwise mark 17.3 not applicable.

## Chapter III — Information supplied with the device

| GSPR | Requirement (paraphrase) | Applicable? | Evidence / where in repo | Met? |
|---|---|---|---|---|
| 23.1 | Label + instructions for use — device identity, safe use, residual risks | [RA] | labelling/IFU (ISO 20417 / EN ISO 15223-1 — [CONFORMANCE.md](CONFORMANCE.md) §4) | [RA] |
| 23.4 | IFU content — intended purpose, intended users, warnings/precautions, residual risks, version | [RA] | product IFU; `disclose-in-ifu` harm-risks | [RA] |

**How to use.** At the MDSW flip, complete the *whole* Annex I (not only these rows) as part
of the technical documentation; keep this checklist's software rows pointing at living repo
evidence. Transfers to the manufacturer ([CONFORMANCE_TRANSFER.md](../CONFORMANCE_TRANSFER.md)).
