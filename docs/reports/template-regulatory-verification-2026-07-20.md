# Template regulatory & standards verification — with application + novice audit

> Verification of the whole template against its standards/regulatory foundation (checked against
> the **primary-source PDFs + EU law, not memory**), plus a template→example application check and a
> novice-understandability audit. Read-only analysis; the fixes it drove were applied in follow-up PRs.

## Provenance

- **Audited:** `risk-management-template` @ `f923d1d` (pre-fix) + applied example `risk-management-template-example` @ `7a62afe`
- **Date:** 2026-07-20
- **Method:** 13-agent workflow — one agent per standard reading the licensed PDF (ISO 14971, ISO/TR 24971, IEC 62304+A1, 62366-1, 81001-5-1, 82304-1, ISO 81001-1) or EUR-Lex-grade sources (MDR Annex I, GDPR, editions/dates); + 2 application-completeness agents; + 2 novice personas; + synthesis. One verify agent dropped on a transient error (its finder result was used).
- **Result:** **4 defects · 10 gaps · 42 observations.**
- **Disposition:** all defects + high-value gaps FIXED — template PR #22 (standards corrections), PR #23 (novice onboarding); example PR #10 (mirror + label creation). Remaining items are the lower-tier observations enumerated below (decision-input; "enable, not enforce").

---

## Verdict

**(A) Standards fidelity — substantially faithful, three verifiable clause errors.** Every load-bearing citation was checked against the primary text, not memory: ISO/TR 24971:2020 (§5.5.2/§5.5.3, Annex A/B) against the official ISO preview plus a full-text mirror; IEC 62304:2006+A1:2015, IEC 81001-5-1:2021, ISO 81001-1:2021 and IEC 82304-1:2016 against the licensed PDFs on disk; MDR and GDPR against EUR-Lex/authoritative full-text (no licensed PDF exists for EU law); the CONFORMANCE.md editions table against ISO/IEC catalogue and OJ records. The result is strong — ISO/TR 24971, IEC 81001-5-1, ISO 81001-1/IEC 82304-1, MDR and GDPR each verified **clean** (no case where the source contradicts the template), and the CONFORMANCE.md edition/date stamps all hold. Three genuine defects survive: a §4.4 element-letter slip in the ISO 14971 primer, a §7.2-vs-§7.3 mis-attribution in the IEC 62304 traceability edge, and the IEC 62366-1 abbreviation written as "UIUP" where the standard defines "UOUP". One caveat: the ISO 14971 and IEC 62366-1 primary PDFs the harness intended to supply were absent from disk (an unresolved `undefined/` path), so those two standards were corroborated against web-authoritative renderings rather than the paginated PDF — the ISO 14971 defect additionally rests on the template contradicting *itself* across three files.

**(B) Template→example application — complete and faithful, one stale count propagated.** The applied child (`risk-management-template-example`) is a correctly-scoped base+conformance apply: every doc, issue form, workflow, script, GitLab twin, label config and all four ADRs are present and byte-identical to the template, both Projects boards exist, and the generated risk-management-file showcase is current and includes the new Usability and PMS content. Every file the example *lacks* is an intentional, mostly-documented omission (the optional arc42 layer, the `skills/` authoring tooling, the apply meta-docs). The real gaps are small and mostly upstream: the manifest itself undercounts its own ADRs ("three / 0001-0003" while shipping four), the example's live GitHub label set was never re-run so `use-scenario`/`pms-review` are missing, and six conformance docs hard-link into `../skills/` which dangles in every child.

**(C) Novice understandability — the method teaches well, the orientation does not.** For day-to-day *use* the template is genuinely good (RECIPES.md's "system in four sentences", the "you generate it, you don't maintain it" framing, consistent `<...>`/`[NEEDS RA INPUT]` fill-in markers). The failures are in signposting, and one is serious: `SETUP_PROMPT.md` — a prominently linked apply path that advertises "a complete risk-management system" — scaffolds only the delivery-risk half and never points at the harm-risk/conformance extension, so a newcomer can finish it believing they set up patient-safety risk management when they did not. Beyond that there is no start-here/reading order over ~35 catalog rows, the scope-gating acronym MDSW (and IFU/GSPR) is never expanded in any beginner doc, and "enable, not enforce" is stated literally once.

## A. Standards & regulatory conformance

### Confirmed defects

| Severity | Standard / clause | Location | Issue | Fix | Verified against |
|---|---|---|---|---|---|
| Defect | IEC 62366-1:2015, Annex C (normative) | `docs/USABILITY.md:49, :103, :105` + §7 heading | Abbreviates "User interface of unknown provenance" as **UIUP** throughout; the standard's defined term is **UOUP** ("UIUP" occurs 0× in the standard). Breaks an auditor's term search. | Replace UIUP → UOUP in the §5.10 row, the §7 heading and the Annex C reference. | IEC 62366-1:2015 Annex C title "Evaluation of a USER INTERFACE OF UNKNOWN PROVENANCE (UOUP)" (AAMI preview Contents; full en-fr text, 0 hits for UIUP) |
| Defect | IEC 62304:2006 §7.3 | `docs/TRACEABILITY.md:22` | The "risk control → test" row attributes a control's *effectiveness verification* to §7.2. §7.2 only *defines/implements* risk-control measures; their **verification** is §7.3 (7.3.1; 7.3.3 d) traceability "from the risk control measure to the verification"). | Change `(§7.2)` → `(§7.3)`, most precisely `(§7.3.1 / §7.3.3 d))`. | IEC 62304:2006 §7.2 "Risk control measures" vs §7.3 "Verification of risk control measures", printed p.57 |
| Defect | ISO 14971:2019 §4.4 c) | `docs/learning/risk-management-primer.md:119-120` | Cites "review requirements (**§4.4 f**)". In §4.4 the plan elements are a)…g); **review of RM activities is c)**, and f) is *verification of implementation & effectiveness*. Contradicted by the repo's own `HARM_RISK.md §1` and `skills/mdr-audit-readiness/SKILL.md §B`, which both map review=c, verification=f. The primer is the outlier. | Change `§4.4 f` → `§4.4 c`. | ISO 14971:2019 §4.4 a)–g) ordering (web-corroborated + internal cross-file contradiction; primary PDF unavailable) |

### Notable observations (no change required for correctness)

- **ISO 14971** — `docs/PMS.md:18-20` labels §10.1 "Collect (actively)" / §10.2 "Sources"; substance is placed correctly but the exact sub-clause headings (10.1 General / 10.2 Information collection / 10.3 Information review / 10.4 Actions) were unverifiable without the PDF. `docs/HARM_RISK.md:98` uses a bare "§5" that means *this document's* §5, not ISO 14971 Clause 5 (the control hierarchy is 14971 §7.1) — internally consistent but re-readable as a mis-citation.
- **MDR (EU) 2017/745** — `docs/PMS.md:1,5` labels the whole Art. 83–92 span "the PMS system"; strictly PMS = Art. 83–86 and Art. 87–92 = Vigilance (the doc handles the specifics correctly later). `docs/adr/0001-mdsw-qualification.md:88-89` drops "vital" from the Rule 11 monitoring branch ("monitoring of **vital** physiological parameters").
- **IEC 62366-1** — `docs/USABILITY.md:87` cites a bare "§7.5" (alarm fatigue) that is actually ISO 14971 §7.5 — 62366-1 has no Clause 7. `.github/ISSUE_TEMPLATE/use-scenario.yml:73` pins the three-tier control hierarchy to 62366-1 §5.3 (which is hazard identification); the hierarchy is ISO 14971 §7.1.
- **IEC 62304** — `docs/adr/0002` paraphrases "external to the software item" where the standard says "external to the software **system**" (defensible via the A1:2015 item-d parenthetical); the SOUP gloss in `docs/SOUP.md:4-5` is looser than the §3.29 definition.
- **IEC 81001-5-1** — `docs/standards/CONFORMANCE.md:38` says "designed to plug into IEC 62304"; accurate but the normative clauses are primarily *derived from IEC 62443-4-1* (62304 is the ordering/extension, Annex A.2). "FDA-recognized" is true (externally confirmed Dec 2022/Jan 2023) but not a claim the standard text can support.
- **CONFORMANCE.md editions** — the "verified 2026-07" table holds throughout; two items only unverified: the AI-Act "signed 8 Jul 2026" specific date, and `COM(2025) 1023` (out of the named scope). No edition/date needs correction.

### Verified clean (explicitly)

ISO/TR 24971:2020 (P=P1×P2 in §5.5.2, software-P1=1 in §5.5.2/§5.5.3, Annex A A.2.1–A.2.37, Annex B techniques) — **zero defects**. IEC 81001-5-1:2021 (§4.1.5 third-party, §6.2.1 monitoring, §9 problem-resolution) — **clean**. ISO 81001-1:2021 §3.2.8 triad + IEC 82304-1:2016 pointer chain (Clause 2/§5 → 62304 → 14971) — **clean**. MDR GSPR-2 AFAP wording, GSPR-4 priority order, Annex VIII Rule 11 ladder, Art. 83–88 PMS map (incl. Art. 84 → Annex III, correctly not Annex II) — **clean**. GDPR Art. 35/36 DPIA mapping and the Art. 32 TOM register — **clean**.

## B. Application completeness (template → example)

| Severity | Item | Location | Status |
|---|---|---|---|
| Defect (manifest) | ADR count is stale | `docs/APPLY_TO_EXISTING_REPO.md:34, :81`; `skills/apply-risk-management/SKILL.md:55`; propagated to example `README.md:19, :33` | Says "three ADRs / renumber 0001-0003" but the template ships and references **four** (ADR-0004 risk-management-file deliverable, cited at APPLY :47/:99). The `cp -rn` glob copies 0004, but a prose-following applier renumbers/cross-links only 0001-0003. |
| Gap | Live labels stale in example | example repo GitHub labels vs `.github/conformance-labels.json` | `use-scenario` and `pms-review` are defined in the (byte-identical) JSON but were never created on the live repo — `setup-labels.sh` not re-run since they were added. `use-scenario.yml` declares `labels: ["use-scenario"]`, so filing the form can't apply its label. Fix: re-run `setup-labels.sh` (idempotent). |
| Gap | Dead `../skills/` links in every child | `docs/SECURITY_RISK.md:26`, `docs/RISK_MANAGEMENT_FILE.md:19,85`, `docs/dpia/README.md:7,101`, `docs/dpia/technical-organisational-measures.md:7`, `docs/adr/0004:68`, `docs/standards/CONFORMANCE.md:35` | Hard-link to `../skills/*/SKILL.md`; `skills/` is authoring tooling the manifest never copies, so these break in **every** applied repo — and, unlike arc42, the omission is documented nowhere. Fix: point at absolute template-repo URLs or drop the links. |

**Intentional / documented omissions (not defects):** the optional arc42 architecture layer was not applied (documented at example `README.md:20`; 13 dangling `arc42/...` links resolve only after adopting it); `skills/`, `AGENTS.md`/`CLAUDE.md`, the apply meta-docs and `docs/reports/*` are correctly absent per the manifest.

**Placeholders (expected for a promoted demo):** `soup.yaml`, `docs/adr/0001`, `docs/adr/0002` and `docs/HARM_RISK.md §1` remain byte-identical to the template (still carry EXAMPLE content) — flagged by the manifest's own Verify checklist as manual follow-ups a real applier must complete.

**Example ahead of template (not stale):** `register-export.yml` pins `actions/upload-artifact` at v7.0.1 in the example vs v4.5.0 in the template (a Dependabot bump in the child) — optionally forward-port so children start current.

## C. Novice understandability

| Severity | Gap a newcomer hits | Location | Concrete fix |
|---|---|---|---|
| Defect | `SETUP_PROMPT.md` bills itself as "a complete… risk-management system" but Gates 0–4 scaffold **only** the delivery-risk register — zero mention of the ISO 14971 harm-risk layer, SOUP, usability, the §9 report, or `CONFORMANCE_EXTENSION_PROMPT.md`. A novice finishes believing they set up patient-safety risk management. | `docs/SETUP_PROMPT.md:12, :24-32` | Add a scope banner ("this sets up ONLY the delivery-risk register; continue with `docs/CONFORMANCE_EXTENSION_PROMPT.md` for the harm-risk + MDR/62304 layer") and soften the Role line to "the delivery-risk register (base layer)". |
| Gap | **No start-here / reading order.** README opens with two tables (~35 rows) with no signal of the four must-reads; the best on-ramp is buried in RECIPES.md. | `README.md:24-71`; `docs/RECIPES.md:17-30` | Add a "Start here (first 30 minutes)" ordered list before the tables: primer → RISK_MANAGEMENT.md → RECIPES.md → APPLY. Mark the two tables "reference catalog". |
| Gap | **MDSW is never expanded** in any novice-facing doc, though it gates the whole optional layer; missing from the primer's "vocabulary you must own" table and the RECIPES glossary. Same for IFU and GSPR. | `docs/HARM_RISK.md:15,112,96`; `docs/learning/risk-management-primer.md:64-72`; `docs/RECIPES.md:49-58` | Add MDSW (Medical Device Software), MDR, IFU (Instructions For Use), GSPR (General Safety & Performance Requirements) to the primer §2 table and the RECIPES glossary; expand on first use. |
| Gap | **"Enable, not enforce"** appears literally once (a workflow table row); no consolidated required-vs-optional-vs-inert map, so a beginner can't answer "what must I do vs what's off by default?" | `README.md:65, :126-139, :16-22` | Add a "Required vs optional vs inert" table: REQUIRED = base register; OPTIONAL = conformance layer; INERT = every workflow until configured/released. State "nothing blocks a merge" once, prominently. |
| Gap | The two agent entry points name the same zero-mutation default differently — skill `MODE=plan` vs `SETUP_PROMPT MODE=dry-run` — without saying they're identical. | `skills/apply-risk-management/SKILL.md:26-42`; `docs/SETUP_PROMPT.md:17,38`; `docs/APPLY_TO_EXISTING_REPO.md:11-12` | Add an explicit "plan (skill) = dry-run (setup prompt) — same default". |
| Gap | The manual "what you fill vs what CI generates" obligations are scattered across four places, no single checklist. | `docs/APPLY_TO_EXISTING_REPO.md:68-73`; `SKILL.md:73-82`; `docs/HARM_RISK.md §1` | Promote into one "After you apply: fill these (everything else is generated)" checklist tagging each field (you fill) vs (CI generates). |
| Observation | `harm-risk.yml` intermixes raise-time fields with post-control lifecycle fields (residual S/P, benefit-risk, §7.6 completeness) with no phase marker. | `.github/ISSUE_TEMPLATE/harm-risk.yml:93-128` | Add a divider: "Fill the section below LATER, once controls are implemented (RECIPES 6-7) — leave blank at raise time." |

## Prioritised fix list

1. **`docs/SETUP_PROMPT.md`** · add scope banner (only the delivery-risk register; point to `CONFORMANCE_EXTENSION_PROMPT.md`) and soften the "complete" Role line — stops a novice shipping with no harm register.
2. **`docs/USABILITY.md`** (:49, :103, :105, §7 heading) · replace UIUP → UOUP to match IEC 62366-1 Annex C.
3. **`docs/TRACEABILITY.md:22`** · change `(§7.2)` → `(§7.3)` for risk-control-measure verification.
4. **`docs/learning/risk-management-primer.md:119-120`** · change `§4.4 f` → `§4.4 c` (review requirements), matching HARM_RISK.md §1 and SKILL.md §B.
5. **`docs/APPLY_TO_EXISTING_REPO.md:34, :81`** + **`skills/apply-risk-management/SKILL.md:55`** + example **`README.md:19, :33`** · "three ADRs / 0001-0003" → "four ADRs / 0001-0004" (add ADR-0004 RMF deliverable).
6. **`docs/SECURITY_RISK.md`, `RISK_MANAGEMENT_FILE.md`, `dpia/README.md`, `dpia/technical-organisational-measures.md`, `adr/0004`, `standards/CONFORMANCE.md`** · repoint `../skills/*/SKILL.md` links to absolute template-repo URLs (or drop) so children don't dangle.
7. **example repo** · re-run `setup-labels.sh …/conformance-labels.json` to create the missing `use-scenario` + `pms-review` labels.
8. **`README.md`** · add a "Start here (first 30 minutes)" ordered reading path and label the two big tables "reference catalog".
9. **`docs/learning/risk-management-primer.md §2` + `docs/RECIPES.md` glossary** · expand and define MDSW, MDR, IFU, GSPR; expand on first use in HARM_RISK.md/README.
10. **`README.md` Principles** · add a "Required vs optional vs inert" table and state "enable, not enforce — nothing blocks a merge" prominently.
11. **`docs/APPLY_TO_EXISTING_REPO.md` + `SKILL.md`** · add "plan = dry-run (same zero-mutation default)"; and consolidate a single "after you apply: fill these" checklist.
12. **Minor standards cleanups** · `docs/PMS.md:1,5` reword "Art. 83–92 PMS" → "PMS (83–86) + Vigilance (87–92)"; `docs/adr/0001:88-89` reinsert "vital" (Rule 11); `docs/USABILITY.md:87` attribute the bare §7.5 to ISO 14971; `use-scenario.yml:73` drop the §5.3 attribution for the ISO 14971 §7.1 hierarchy; `HARM_RISK.md:98` disambiguate the bare "§5"; optionally add an ISO 81001-1:2021 row to `CONFORMANCE.md` (cited as foundational in the primer but absent from the standards index) and broaden the 82304-1 role cell to "safety and security".