# Security risk management — method (MDCG 2019-16 / IEC 81001-5-1)

How this project analyses, evaluates, controls, and tracks **information-security risks**
of the product — the security counterpart to the safety method in
[`HARM_RISK.md`](HARM_RISK.md), documented in parallel as **MDCG 2019-16** (rev. 1, July
2020) expects and as MDR **GSPR 17.2/17.4** require ("risk management **including
information security**"; minimum IT-security requirements incl. protection against
unauthorised access — see [GSPR-CHECKLIST](standards/GSPR-CHECKLIST.md)). The secure
life-cycle activities themselves follow **IEC 81001-5-1:2021** (applies to health software
regardless of MDSW status — [CONFORMANCE.md](standards/CONFORMANCE.md) §2).

> **No third register.** Security risks are worked in the **delivery-risk register**
> (label `risk` + `risk-cat:vulnerability|secret|supply-chain|compliance`,
> [`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md)) using this method for analysis. What earns
> its own file here is the **method + the coupling rules** — a notified body looks for a
> documented security risk process distinct from (and linked to) the safety process, not
> necessarily a third issue tracker.

## 1. Analysis chain (per security risk)

`asset → threat → vulnerability → security impact` — e.g. *patient-record store (asset) ←
credential stuffing (threat) via missing rate limit (vulnerability) → confidentiality
breach (impact)*. Score in the register's 5×5: **L** = likelihood of successful
exploitation (consider exposure, attacker capability, existing controls); **I** = security
impact on confidentiality / integrity / availability of the product and its data. STRIDE
(the [`security-reviewer`](../skills/security-reviewer/SKILL.md) skill's threat-model
pass) and the CI scanners feed this analysis; detectors feed, never decide.

## 2. Coupling rules — security ↔ safety (MDCG 2019-16 §3.2)

- **Security → safety:** if a security risk's impact can reach a patient (wrong/blocked
  data, manipulated device behaviour), raise a **linked [harm-risk](HARM_RISK.md)** and
  evaluate it there on the S×P harm scale. The security issue and harm-risk reference
  each other; neither substitutes for the other.
- **Safety → security:** every harm-risk **control** is checked for security side-effects
  (a new interface, a stored credential, a logging change) — record the check in the
  harm-risk's §7.5 field ("new/changed risks introduced by the controls").
- **Weakening conflicts** (a security control that degrades safe use, e.g. aggressive
  session timeout during clinical use) are decided in the harm-risk's benefit–risk note
  with the security issue linked.

## 3. Controls, residual risk, lifecycle

Controls follow defence-in-depth (prevent → detect → respond); state per control what it
does and where it lives (code/config/process; ADR if architectural — arc42 §8 security
concept). After controls: re-score L×I, judge per the register's severity bands
([`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md) §4), and track lifecycle with the normal
`risk:*` labels. Residual acceptance of a Critical/High security risk is the project
lead's call, recorded in the issue.

## 4. Evidence wiring (what exists in this repo)

| Activity (IEC 81001-5-1) | Where |
|---|---|
| Known-vulnerability monitoring | Dependabot / Trivy → register ([`risk-automation.yml`](../.github/workflows/risk-automation.yml), [`.gitlab-ci.yml`](../.gitlab-ci.yml)) — inert until configured |
| Third-party components | [`SOUP.md`](SOUP.md) + [`soup.yaml`](../soup.yaml) + per-release SBOM ([`sbom.yml`](../.github/workflows/sbom.yml)) |
| Coordinated vulnerability disclosure | [`SECURITY.md`](../SECURITY.md) (CVD policy stub) |
| Deep review | `security-reviewer` skill (STRIDE + checklist → dated `docs/reports/`), if installed |
| Secure-development context | per-project: SAST/secret scanning (see the `security-scanner` wizard), arc42 §8 security concept |

## 5. Plan slot (fill per project — mirrors HARM_RISK.md §1)

| Plan element | This project |
|---|---|
| Scope (assets, interfaces, data categories) | <…> |
| Responsibilities & authorities (who accepts residual security risk) | <…> |
| Criteria for security-risk acceptability | the register's severity bands (§4 of RISK_MANAGEMENT.md) — ratify or adapt consciously |
| Verification of security controls | <per control: test/scan/review evidence> |
| Post-release monitoring | the CVE→register feed + [`SECURITY.md`](../SECURITY.md) intake |

> **Transfer:** this method file, the security risks in the register, and the CVD policy
> transfer to the future manufacturer ([`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md));
> the manufacturer's own ISMS/IT-security organisation stays manufacturer-side.
