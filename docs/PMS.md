# Post-market surveillance — plan (ISO 14971 §10 / MDR Art. 83–92)

How this project **actively** collects and reviews information after release, and feeds it back
into risk management. ISO 14971 §10 (production & post-production) is the method; for medical-device
software (MDSW) the MDR **Post-Market Surveillance (PMS)** system (Art. 83–92) is the legal frame.
The *execution* of PMS needs a device placed on the market (and EUDAMED access) and is
**deferred-to-manufacturer** ([`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md)); the **plan and
the intake mechanics** are pre-staged here so they are not reconstructed later.

> **Scope note.** Kept live even while not MDSW ([ADR-0001](adr/0001-mdsw-qualification.md)): the
> §10 feedback loop is good practice for any health software, and a PMS plan is cheap to keep now.
> This is not a claim of conformity.

## 1. The loop (ISO 14971 §10.1–§10.4)

`actively collect → review for safety relevance → act → feed back into the file & top-management review`

- **§10.1 Collect (actively).** Establish and maintain a system to *go looking* for information —
  not just wait for complaints.
- **§10.2 Sources.** Production/monitoring; user-generated information; installers/maintainers;
  the supply chain; publicly available information; and the evolving **state of the art**.
- **§10.3 Review.** Is a *previously unrecognised* hazard present? Is a risk *no longer acceptable*?
  Is the *overall* residual risk still acceptable vs. benefit? Has the *state of the art* changed?
- **§10.4 Act.** If safety-relevant: reassess/assess risks, update the risk-management file, consider
  action on devices already in use; and feed the result into top management's process review (§4.2).

## 2. What already feeds the loop in this repo

The intake mechanics are live now — the PMS plan wires these together:

| Input (ISO 14971 §10.2) | Mechanism in this repo |
|---|---|
| Publicly available info — vulnerabilities in dependencies | SBOM ([`sbom.yml`](../.github/workflows/sbom.yml)) + CVE→register automation ([`risk-automation.yml`](../.github/workflows/risk-automation.yml) / GitLab `vuln-to-register`) → `risk` / `harm-risk` issues |
| SOUP anomalies | [`SOUP.md`](SOUP.md) + `soup-anomaly` issues (IEC 62304 §7.1.3) |
| User-generated info / incidents from use | [`field-feedback` form](../.github/ISSUE_TEMPLATE/field-feedback.yml) → triaged into the registers |
| State of the art (standards/regulatory drift) | [`CONFORMANCE.md`](standards/CONFORMANCE.md) `watch` rows, re-checked at the review cadence |
| The periodic review itself | the [`pms-review.yml`](../.github/workflows/pms-review.yml) scheduled action (§4) |

## 3. PMS plan (MDR Art. 84 / Annex III) — fill per project

| Plan element | This project |
|---|---|
| Data to collect & indicators | <complaints, incidents, CVEs, usage/error signals, literature; the sources in §2> |
| Thresholds / trigger criteria | <what signal triggers a reassessment — e.g. any serious incident; a CVSS-high on a runtime SOUP; a trend> |
| Methods & tools | the register feeds (§2) + the periodic review (§4) |
| Roles & responsibilities | <who runs PMS; who accepts a resulting residual-risk change — the RM-plan authority, [`HARM_RISK.md`](HARM_RISK.md) §1> |
| Review cadence | <e.g. quarterly review + per-release; the `pms-review` action default is quarterly> |
| Link to risk management | §10.4 actions update the [harm-risk register](HARM_RISK.md) + the [§9 report](HARM_RISK_REPORT.md) |

## 4. The periodic review (the `pms-review` action)

[`.github/workflows/pms-review.yml`](../.github/workflows/pms-review.yml) (GitLab twin: the
`pms-review` job in [`.gitlab-ci.yml`](../.gitlab-ci.yml)) opens a **PMS / §10 review** tracking issue
on a cadence (default quarterly) with a checklist that walks §10.2–§10.4:

- review new `field-feedback`, `soup-anomaly`, and vulnerability→register issues since last time;
- check for **trends** (Art. 88) across incidents/complaints;
- re-check `CONFORMANCE.md` `watch` rows for state-of-the-art / regulatory change;
- decide §10.4 actions → update the harm-risk register / open new harm-risks;
- record the outcome (and, at a release, roll it into the [§9 report](HARM_RISK_REPORT.md)).

**Inert until you opt in:** the schedule fires only when the repo variable
`PMS_REVIEW_ENABLED=true` is set; a manual `workflow_dispatch` run always works. (Enable, not
enforce — a template adopter chooses when the cadence starts.)

## 5. Manufacturer-side (deferred, MDR — Art. 85–92)

Pre-staged as *inputs*, executed by the future manufacturer once the device is on the market:

- **PMS report** (Art. 85, class I) / **Periodic Safety Update Report — PSUR** (Art. 86, class IIa+):
  the periodic summary of PMS findings; the §4 review produces its inputs.
- **Serious-incident & field-safety-corrective-action reporting** (Art. 87) and **trend reporting**
  (Art. 88) — via EUDAMED; needs a registered device.
- **Post-Market Clinical Follow-up (PMCF)** (Annex XIV Part B) — clinical evidence over time.

## 6. Where things live

- **Plan & method:** this document · **feedback intake:** [`field-feedback` form](../.github/ISSUE_TEMPLATE/field-feedback.yml)
  + the automated feeds (§2) · **review:** [`pms-review.yml`](../.github/workflows/pms-review.yml).
- **Feeds back into:** [`HARM_RISK.md`](HARM_RISK.md) §8/§10, the [§9 report](HARM_RISK_REPORT.md),
  the delivery register ([`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md) §8).
- **Standards context:** [`standards/CONFORMANCE.md`](standards/CONFORMANCE.md) · transfer:
  [`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md).
