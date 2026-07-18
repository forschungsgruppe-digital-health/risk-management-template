# Extension prompt: Add MDR/62304 conformance-readiness to an existing risk-managed repo

> Paste below the line into Claude Code (or an agent with `gh` CLI + repo write access),
> **after** the base risk-management setup has been applied (see
> [`SETUP_PROMPT.md`](SETUP_PROMPT.md)). This is an **additive amendment**: it presupposes
> the base scaffolding (risk labels, `risk.yml` form, "Risk Register" board,
> `docs/RISK_MANAGEMENT.md`, optional risk-automation workflow) and does not recreate it.
> Runs **dry-run by default**; mutates nothing until you approve at each gate.
>
> **Template note.** Repos created *from this template* already contain every artifact
> this prompt produces — use it only to retrofit an **existing** repo (or run the
> [apply-to-existing-repo skill](APPLY_TO_EXISTING_REPO.md), which folds base + extension
> into one pass). Standards editions below were verified 2026-07 — re-verify at run time
> against [`standards/CONFORMANCE.md`](standards/CONFORMANCE.md).

---

## Context & strategy (why this extension exists)

The product is intended for **market placement after project end**; the manufacturer is
**TBD** (resolved by the dissemination plan). Strategy = **design for conformance, defer
certification**: capture the artifacts that are cheap to maintain live but
near-impossible to reconstruct for a notified body later, while deferring the
organizational QMS apparatus to whoever ultimately certifies. Qualification as
medical-device software (MDSW) is **living** — it can flip as features move from
displaying data toward influencing clinical decisions.

## Role & execution contract (overrides everything below)

You are extending an existing GitHub repo. Operate under strict **human-in-the-loop**
control, **idempotently** and **additively**. Never delete or overwrite existing
base-setup artifacts; detect and reuse them.

1. **Two modes.** `MODE = dry-run` (default) makes ZERO mutations — read and propose
   only. `MODE = apply` authorizes mutation *only past individually approved gates*; it
   is not blanket consent.
2. **Gates are hard stops.** At each gate present the concrete diff (full file contents,
   label names, form YAML, workflow YAML, field/view schema), then **end your turn and
   wait**. Proceed only on the exact approval token. "Looks good", questions, or edits
   are **not** approval — respond and re-present.
3. **Ambiguity / missing scope = stop and ask.** Never work around a missing permission.
4. **CI/security-scoped steps are quarantined** behind their own gate (Gate E3) and are
   never auto-approved by `apply`.
5. At every gate also offer `SKIP`, `EDIT <changes>`, `ABORT`.

### Gate map (this extension)

- **Gate 0 — Plan approval.** After detecting existing base scaffolding. Token: `APPROVE PLAN`.
- **Gate E1 — Qualification & standards docs.** Living qualification ADR, ADR template
  (if absent), standards conformance index. Token: `APPROVE E1`.
- **Gate E2 — Harm-risk register (ISO 14971).** Distinct labels, harm-risk issue form,
  board/views — kept separate from the delivery-risk register. Token: `APPROVE E2`.
- **Gate E3 — SOUP + SBOM + traceability (CI, quarantined).** SOUP inventory, SBOM
  generation, traceability conventions + optional CI checks, wiring into existing
  risk-automation. Token: `APPROVE E3`.
- **Gate E4 — Transferability, feature-gate re-eval, verification.** IP/licensing
  hygiene, qualification re-evaluation mechanism, example artifacts, final report.
  Token: `APPROVE E4`.

## Inputs

- `REPO`: <owner/repo>
- `PROJECT_OWNER`: <org/user owning the boards>
- `MODE`: `dry-run` (default) | `apply`
- `HARM_REGISTER_TARGET`: `separate-board` (recommended) | `separate-view-on-existing-board`
- `SBOM_FORMAT`: `cyclonedx` (default) | `spdx`
- `PRIMARY_STACK`: <e.g. Angular + Node, .NET, Java — drives SBOM tooling choice; a
  Syft-based generator auto-detects and stays stack-agnostic>

If `REPO`/`PROJECT_OWNER` missing, stop and ask.

## Phase 0 — Pre-flight (→ Gate 0)

1. Confirm `gh auth status` and scopes (issues, labels, `project`, actions/workflows,
   security-events).
2. Detect base artifacts: `risk*` labels, `.github/ISSUE_TEMPLATE/risk.yml`, the "Risk
   Register" board and its fields, `docs/RISK_MANAGEMENT.md`,
   `.github/workflows/risk-automation.yml`, existing `LICENSE`, existing `docs/adr/` or
   ADR template, existing SBOM/dependency tooling. Report what exists; the extension
   **reuses** it.
3. Detect stack for SBOM tooling (lockfiles present).
4. Present the written plan (all artifacts per gate, collisions → skip, manual actions).
   **GATE 0 — wait for `APPROVE PLAN`.**

## Phase E1 — Qualification & standards documentation (→ Gate E1)

- **ADR mechanism.** If no ADR setup exists, add `docs/adr/` with a MADR-style
  `TEMPLATE.md` and an index. Reuse if present.
- **Living qualification ADR** `docs/adr/NNNN-mdsw-qualification.md`: records that
  market placement is intended post-project; manufacturer TBD; the current MDSW
  qualification decision against **Regulation (EU) 2017/745 (MDR)** Annex VIII Rule 11 +
  **MDCG 2019-11 rev. 1 (June 2025)** with rationale; strategy = conformance-ready
  upstream, deferred certification; and a **re-evaluation trigger list** (features
  touching clinical decision support, alerting on values, risk scores, care-plan logic
  influencing treatment, AI/ML decision input). Mark status `accepted` but explicitly
  `living / re-evaluated at feature gates`.
- **Standards conformance index** `docs/standards/CONFORMANCE.md`: a table with columns
  *Standard | Edition | Role | Status (active / conditional / iff MDSW /
  deferred-to-manufacturer / watch) | Where evidenced in repo*. Seed it tiered:
  - *Active now:* ISO/IEC/IEEE 16085:2021 (risk process), ISO/IEC/IEEE 42010:2022 +
    arc42 (architecture), ISO/IEC/IEEE 29148:2018 (requirements), ISO/IEC 25010:2023
    (quality vocabulary); GDPR + ISO/IEC 27001:2022 / ISO 27799:2025 baseline;
    ISO/IEC/IEEE 12207:2017 / 15288:2023 as life-cycle frame; IEC 81001-5-1:2021
    (secure health-software lifecycle — applies to health software regardless of MDSW
    status).
  - *German-TI-driven (independent of MDSW, iff the product integrates):* gematik
    specifications (ISiK, ePA), BSI TR-03161 (parts 1–3), BSI C5:2020.
  - *Activated iff MDSW = yes:* IEC 62304:2006+A1:2015 (Ed. 2 at Committee Draft —
    forecast ~2028, monitor), ISO 14971:2019 (+ ISO/TR 24971:2020), IEC 62366-1:2015+A1:2020,
    IEC 82304-1:2016, IEC 80001-1:2021, MDCG 2020-1 (clinical evaluation of MDSW),
    MDCG 2019-16 rev.1 (cybersecurity), ISO 20417:2026 + EN ISO 15223-1:2021 (labelling/IFU),
    ISO 13485:2016 (marked *deferred-to-manufacturer — organizational QMS, not a repo
    artifact*).
  - *Watch (EU horizontal product law):* Cyber Resilience Act (EU) 2024/2847 (main
    obligations 2027-12-11; applies iff **not** MDR-covered), AI Act (EU) 2024/1689
    (iff AI components), EHDS (EU) 2025/327 (EHR-system obligations 2029-03-26, iff the
    product is/embeds an EHR system).

Present all file contents. **GATE E1 — wait for `APPROVE E1`.**

## Phase E2 — Harm-risk register, ISO 14971 (→ Gate E2)

Keep this **separate** from the delivery-risk register so patient-harm risk is never
conflated with schedule/scope risk.

- **Labels:** `harm-risk`, lifecycle `harm-risk:open|controlled|residual-accepted|closed`,
  and `hazard-cat:*` (e.g. `data-integrity`, `availability`, `confidentiality`,
  `clinical-misinterpretation`, `interoperability`, `usability`).
- **Issue form** `.github/ISSUE_TEMPLATE/harm-risk.yml` (auto-applies `harm-risk` +
  `harm-risk:open`) capturing the 14971 chain: hazard; foreseeable sequence of events;
  hazardous situation; harm; **Severity (S)** 1–5 with anchors; **Probability** (support
  P1 = probability of the hazardous situation, P2 = probability it leads to harm, or a
  single P if the team prefers) with anchors; risk-control measure(s) following the
  14971 §7.1 hierarchy (inherently safe design ⇒ protective measures ⇒ information for
  safety); **residual risk** evaluation; **two verifications** (control implemented;
  control effective — §7.2); benefit–risk note; links to the design element/ADR/
  requirement the control lives in.
- **Register target** per `HARM_REGISTER_TARGET`: a distinct **"Harm Risk File"** board
  (fields: Severity, Probability, Residual severity/probability, Risk Status, Hazard
  category, Control verification, Owner, Review date) with views *Risk table (S×P)*,
  *Uncontrolled*, *Residual accepted (audit)*; or a clearly separated view-set on the
  existing board. Auto-add `harm-risk`-labeled issues.

Present labels, form, schema. **GATE E2 — wait for `APPROVE E2`.**

## Phase E3 — SOUP, SBOM, traceability — QUARANTINED (→ Gate E3)

The 62304 evidence most costly to backfill. Touches CI, so quarantined.

- **SOUP inventory** `docs/SOUP.md` + machine-readable `soup.yaml`: per
  third-party/open-source component — name, version/unique designator (IEC 62304
  §8.1.2), publisher/source, license, purpose, functional & performance requirements
  relied upon (§5.3.3), required environment (§5.3.4), and **known anomalies (CVEs/known
  bugs) with an impact assessment** (§7.1.3). State that entries are required for
  components before a class-B/C release; low-risk transitive deps may be covered by the
  SBOM + anomaly feed rather than hand-written entries.
- **SBOM generation** in CI (`.github/workflows/sbom.yml`) using `SBOM_FORMAT` and
  stack-appropriate tooling (a Syft-based action auto-detects ecosystems); publish the
  SBOM as a release asset so each tagged release carries its bill of materials. Minimal
  permissions.
- **Wire into existing risk-automation:** a critical/high Dependabot or code-scanning
  alert on a SOUP component should open/comment a `risk` + `risk-cat:vulnerability`
  issue (delivery side) **and** flag the corresponding SOUP anomaly entry for review; if
  it can affect patient safety, prompt creation of a linked `harm-risk` issue. Extend
  the existing workflow additively — do not rewrite it.
- **Traceability conventions** `docs/TRACEABILITY.md`: define the linking model
  requirement issue (`requirement` label) ⇒ design/ADR ⇒ implementing PR/commit ⇒ test,
  using issue references and PR keywords so the chain is reconstructable from the project
  forge (issues + PRs + cross-references, exported at transfer alongside the git history).
  Optionally add a CI check that flags a merged requirement with no linked test, and/or
  a script that emits a traceability matrix artifact. Keep checks advisory (warn), not
  blocking, at template stage.

Present every file and workflow diff; list anything needing org/admin rights.
**GATE E3 — wait for `APPROVE E3`.** Never auto-approved by `apply`.

## Phase E4 — Transferability, feature-gate re-eval, verification (→ Gate E4)

- **Transferability / IP hygiene** `docs/CONFORMANCE_TRANSFER.md`: state that the risk
  file, harm-risk file, design history, SOUP, and SBOM are intended to be **adoptable by
  the future market-placing manufacturer**; confirm `LICENSE` is present and compatible;
  recommend **DCO sign-off** (or note CLA trade-offs) so provenance of contributions is
  clean; note that ISO 13485 QMS, notified-body engagement, CE marking, clinical
  evaluation (MDR Art. 61 / MDCG 2020-1), and summative IEC 62366-1 usability validation
  are **deferred to the manufacturer**, not repo artifacts.
- **Feature-gate re-evaluation mechanism:** add a checklist item to the PR template
  (create/extend additively) — "Does this change move the product toward clinical
  decision support / influencing diagnosis or treatment? If yes, link/trigger a re-eval
  of the MDSW qualification ADR" — and a CODEOWNERS entry so changes to
  `docs/adr/NNNN-mdsw-qualification.md` and `CONFORMANCE.md` require review.
- **Verify & report:** open one example `harm-risk` issue and triage it on its board;
  add one example SOUP entry with a known-anomaly assessment; confirm the SBOM workflow
  runs. Final report: created vs skipped, manual actions (org security features,
  manufacturer-side items), and URLs of the qualification ADR, conformance index,
  harm-risk board, and SBOM workflow.

**GATE E4 — wait for `APPROVE E4`,** then execute.

## Constraints

- Additive and idempotent; never clobber base-setup artifacts or existing files; extend
  workflows, don't rewrite them.
- Dry-run by default; mutate only past an individually approved gate; CI/security steps
  never auto-approved.
- Keep delivery-risk and harm-risk registers distinct.
- Stay inside `REPO` and the named boards.
- If a call needs a scope you lack, stop and name the exact setting to grant.
