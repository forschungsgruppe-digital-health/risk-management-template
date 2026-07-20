# MDR/CE audit-readiness review — template + applied example

> Inaugural run of the [`mdr-audit-readiness`](../../skills/mdr-audit-readiness/SKILL.md) skill,
> performed inline. A **read-only mock audit** — it does not certify anything and issues no
> conformity verdict.

## Provenance

- **Audited:** `risk-management-template` @ `27125db` (the tooling) + applied example
  `forschungsgruppe-digital-health/risk-management-template-example` @ `9bb1c8d` (the file candidate)
- **Date:** 2026-07-20
- **Scope:** the delivery-risk + harm-risk + conformance layers as applied; arc42 layer not applied in the example
- **ADR-0001 qualification state:** **undecided / placeholder** in both (intended purpose still `<…>`)
- **Standards checked against (primary-source-verified):** EN ISO 14971:2019(+A11:2021), ISO/TR 24971:2020,
  IEC 62304:2006+A1:2015, IEC 62366-1:2015+A1:2020, IEC 82304-1:2016, IEC 81001-5-1:2021, ISO 81001-1:2021,
  MDR (EU) 2017/745 Annex I GSPR 1/2/3/4/8/17, Commission Implementing Decision (EU) 2022/757
- **Method:** ADR-0001 scope gating → artifact inventory → placeholder scan → clause checklist (groups A–H)
  → drift & error catalog → live-register probe (`gh issue/project list`)
- **Previous report:** none (first run)

## Readiness verdict

**Would the delivered documentation hold an MDR/CE audit today? No — and it is not meant to, nor is it
structurally able to as an unfilled template.** An auditor audits a **device-specific risk-management
file** inside an **ISO 13485 quality system**, not a template. The applied example is a faithful *template
snapshot*: the machinery is live and correct (labels, two Projects boards, issue forms, five synthetic
register issues, a genuinely-decided supply-chain ADR), but **every device-specific determination is still
a placeholder** — no intended purpose, no MDSW qualification, no software safety class, no adopted
acceptability criteria, no signed §9 release review, no real SOUP, no applicable/met GSPR calls. On a real
device this set of blanks is a **major nonconformity** (ISO 14971 §4.4 "shall": there is no usable risk
management plan). For a research-stage repo it is the *expected* state — the blanks are exactly the work
the future manufacturer must do.

**The important, positive half of the answer:** the *structure* is unusually audit-shaped. Filled in and
wrapped in a QMS, this scaffolding lands the right artifacts in the right ISO 14971 places, and it makes
the AFAP reconciliation, the mandatory control hierarchy, the two verifications, the §7.5 new-risk gate,
and the SOUP/security overlays first-class instead of afterthoughts. **The distance to auditable is
completion + organizational context, not redesign.** This report measures that distance per clause.

## Scorecard — the applied example as a risk-management FILE

| # | Group (clauses) | Status | Notes |
|---|---|---|---|
| A | RM system & governance (§4.1–4.3; GSPR 3) | **method present; policy/competence = dependency** | process documented; §4.2 acceptability *policy* + §4.3 competence are organizational |
| B | RM **plan** (§4.4 a–g) | **major — no usable plan** | all seven elements still `<…>`/`[NEEDS RA/lead INPUT]`; matrix "example — adopt consciously" (criteria not ratified) |
| C | RM **file** & traceability (§4.5) | **major (market-bound) / expected (research)** | 1 synthetic `harm-risk` issue only; a real file needs the populated per-hazard chain |
| D | Analysis & evaluation (§5.2–5.5, §6) | **blocked on intended use** | intended purpose `<…>` → nothing downstream is anchored; method otherwise sound |
| E | Risk **control** (§7; GSPR 2/4 AFAP) | **method exemplary; no device data yet** | hierarchy + two verifications + §7.5 + severity-floor + AFAP all encoded in the issue form; nothing to grade until risks exist |
| F | Overall residual, review, post-prod (§8, §9, §10) | **major before any release** | `HARM_RISK_REPORT.md` is an empty stub — no product/date/reviewer/3 conclusions/sign-off |
| G | Software/usability/security overlays | **pre-staged; class undecided** | ADR-0002 class still `<A\|B\|C>`; `soup.yaml` example-only; security-RM + CVD present |
| H | MDR GSPR pre-staging (iff MDSW) | **correct pre-staging (not a finding)** | rows + evidence links real; every applicable?/met? = `[RA]` — determinations correctly left to RA |

**Counts:** majors **3** (all "unfilled load-bearing artifact", not design defects) · minors ~6
(placeholders in ADRs/soup/report) · observations ~3 (dangling `arc42/…` links from the un-applied layer;
edition re-verify cadence) · **documented deferrals** many (the whole `not-yet` / `deferred-to-manufacturer`
/ `iff MDSW` split — **not findings**) · **organizational audit-dependencies** 5 (QMS, acceptability
policy, competence records, PRRC, the Notified Body).

## Findings — majors first (the applied example)

1. **MAJOR · §4.4 (a–g) · `docs/HARM_RISK.md` §1 (L26–L32)** — No usable risk management plan: scope,
   responsibilities, review cadence, overall-residual method, and the policy basis are all placeholders,
   and the acceptability matrix is still "example — adopt consciously" (§4.4 d not ratified). *Remediation:*
   fill the §1 table with real values and adopt the §4 matrix via an ADR before any risk is scored.
2. **MAJOR · §9 · `docs/HARM_RISK_REPORT.md` (L10–L13, L23/31/37, L49)** — No risk-management review record:
   the §9 report is an empty stub, so a release could not be signed off (all three required conclusions and
   the sign-off row are `<…>`). *Remediation:* this must exist and be signed **before the first release**;
   until then it is an **audit dependency**, not yet a live nonconformity.
3. **MAJOR · §4.5 / §5 · register** — Risk analysis not yet performed: the `harm-risk` register holds one
   synthetic demo issue, so the file's per-hazard traceable content does not exist. *Remediation:* populate
   from the real intended use + a systematic hazard identification (TR 24971 Annex A). (Expected at
   research stage — grade rises to hard-major once market intent firms up.)

**Minors** (illustrative): ADR-0001 intended purpose `<…>` (§5.2) · ADR-0002 class `<A|B|C>` (62304 §4.3) ·
ADR-0003 metadata `<YYYY-MM-DD>`/`<project lead>` (a *decided* ADR that is not provenance-clean) ·
`soup.yaml` example-only entry (62304 §8.1.2) · GSPR determinations `[RA]` (correct pre-staging while not
MDSW — becomes a minor only at the MDSW flip).

**Observations:** dangling `arc42/…` links in `HARM_RISK.md`/ADRs because the arc42 layer was not applied
here (the README documents the skip — borderline documented-deferral) · re-verify cited standard editions at
the review cadence.

## The template as tooling — does the machinery produce audit-shaped evidence?

Evaluating the template *itself* (not a device file), from the auditor's seat:

**Genuinely audit-shaped (credit where due):**
- The **ISO 14971 process is the spine** — plan (§4.4), file+traceability (§4.5), analysis (§5),
  evaluation (§6), control hierarchy **in order** (§7.1), **two** verifications (§7.2), **§7.5**
  new-risks-from-controls as a *required* issue field (commonly-missed clause), overall residual (§8),
  §9 report, §10 feed — all present and correctly placed.
- **Harm-risk kept strictly separate** from delivery-risk (different scales, boards, lifecycle) — matches
  how an auditor expects the safety file to be isolated from project risk.
- **MDR AFAP done correctly** — `HARM_RISK.md` §4 reconciles via EN ISO 14971:2019+A11:2021 Annex ZA and
  explicitly rejects cost-only justification and the ALARP economic trade-off — the single most common
  MDR risk-management finding, pre-empted.
- **Honest covered / partial / not-yet / deferred-to-manufacturer split** (`IEC-62304-COVERAGE.md`,
  `CONFORMANCE.md`, `CONFORMANCE_TRANSFER.md`) — the line between "deferred on purpose" and "silently
  missing" is explicit, which is exactly what lets a reviewer trust the file.
- **Supply-chain + SOUP + security** overlays (SBOM, `soup.yaml`, §7.1.3 anomaly monitoring, 81001-5-1
  security RM, a CVD policy, SHA-pinned CI) — the software-specific evidence a 62304/81001-5-1 assessor asks for.
- **Evidence hygiene** — immutable dated `docs/reports/`, PR-only changes, CODEOWNERS gate on the
  conformance-critical files, register export at release, verified citations to primary sources.

**Structural gaps / audit risks in the tooling (as tooling), and how they are handled:**
- **The RM plan lives as a table inside `HARM_RISK.md` §1.** An auditor accepts a plan-as-section, but it
  must be *identifiable, approved, versioned*. Recommend the project ratify it (e.g. an ADR) so it reads as
  a controlled plan, not prose. *(Observation — not a defect.)*
- **Document/record control is implicit** (git history + PR + CODEOWNERS). Defensible, but the file should
  *state* that git history is the record-control mechanism, with approval = merge and effective date =
  merge date — otherwise an auditor asks "where is your version/approval control?". *(Observation.)*
- **"Enable, not enforce" vs the auditor's indifference to philosophy.** The template intentionally never
  forces completion — but an empty plan is a nonconformity regardless of intent. The mitigation is a
  *readiness gate that measures the distance to auditable* — **which is precisely this skill**
  (`mdr-audit-readiness`). The design tension is resolved by pairing enablement with self-audit.
- **QMS + organizational context is out of repo by design** (ISO 13485, §4.2 policy, §4.3 competence,
  PRRC). Correct — but they are the **first questions** a real audit asks, so the report surfaces them as
  inherited dependencies rather than letting them read as "done".

## Documented deferrals (NOT findings) & organizational dependencies

*Deferred and correctly declared* — inherited by the future manufacturer, per `CONFORMANCE_TRANSFER.md`:
summative usability validation (IEC 62366-1 §5.9), clinical evaluation (MDR Art. 61 / MDCG 2020-1), PMS/PMCF
(MDR Art. 83–92), ISO 20417 / EN ISO 15223-1 labelling/IFU, full 62304 class-B/C records (SRS, detailed
design, integration/system-test records), UDI/EUDAMED registration.

*Organizational audit-dependencies* — cannot be repo artifacts: an **ISO 13485 QMS**; the **top-management
risk-acceptability policy** (§4.2); **competence records** (§4.3); the **PRRC** (MDR Art. 15); the
**Notified Body** engagement, CE marking, and Declaration of Conformity.

## Bottom line

- **As delivered, today:** not auditable — a template snapshot whose device-specific determinations are
  blank. On a real device that is a major nonconformity; at research stage it is the expected, honest
  starting point.
- **As a foundation to build an auditable file on:** unusually well-aligned with ISO 14971 + the MDR — the
  gap is *completion and QMS context*, not structure. Fill the plan, adopt the criteria, decide ADR-0001/2,
  populate the registers, run the §9 review, and place it under an ISO 13485 QMS, and the same scaffolding
  becomes a defensible file.
- **This skill is the bridge:** run `mdr-audit-readiness` after `apply-risk-management` and after each
  milestone to keep the distance-to-auditable visible and drift-free — before a Notified Body measures it
  for you.

*A mock audit is not a real one: this does not replace a Notified Body or an ISO 13485 internal audit; it
lowers the odds of surprises at the real one. Applicability and acceptance determinations remain
`[NEEDS RA INPUT]`.*
