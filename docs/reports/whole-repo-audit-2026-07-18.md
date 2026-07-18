# Whole-repo audit — internal consistency + real-world MDR fitness

> **Provenance**
> - **Audited commit:** `3c8cf62` (`main`), 2026-07-18
> - **Scope:** the entire repository — structure/layout, framing/narrative, style/terminology,
>   and the MDR / IEC 62304 / ISO 14971 conformance-readiness layer; plus a web-verification
>   pass on every standard edition/date/title the audit flagged. The vendored
>   `docs/arc42/arc42-reference/` upstream copy was out of scope (referenced, not critiqued).
> - **Question answered:** "Is the repo internally consistent in structure, layout, framing and
>   style, AND could it be used for *actual* risk management of production-ready software that
>   might fall under the MDR?"
> - **Method / tools:** two adversarially-verified agent workflows — (1) a 7-lens review
>   (structure, framing, style, MDR-standards-accuracy, ISO 14971 fitness, IEC 62304 fitness,
>   automation) → per-finding adversarial verification → cross-cutting fitness verdict
>   (16 agents, 47 verified findings); (2) a 3-lens standards web-verification
>   (EU regs + MDCG · ISO/IEC med-device editions · cross-cutting + labelling; 31 claims,
>   each requiring a fetched primary source). The completeness-critic agent of workflow (1)
>   dropped on a transient connection error and is not reflected here.
> - **Previous report:** none (first audit of this repo).
> - **Status:** analysis + verification. Findings are leads a human confirms; the fixes applied
>   from this report are tracked in the same-day PR, not in this immutable snapshot.

---

## 0. Verdict

| Axis | Result |
|---|---|
| **MDR fitness** | **USABLE_WITH_FILLIN** — for its stated purpose ("design for conformance, defer certification") the scaffolding is sound and audit-defensible, and a team can start real risk management on it today. It is **not** a complete MDR risk-management file and does not claim to be: several ISO 14971 / IEC 62304 method clauses are genuinely absent, so no MDR audit passes on this content alone. It needs its marked placeholders filled **plus** a handful of method additions before the conformance layer is audit-complete. |
| **Internal quality** | **B (high-B)** — structure, cross-linking and intellectual honesty are excellent; the What's-inside inventory maps to real files, the base/conformance layering is deliberate, and every artifact needing project input is marked. Kept off an A by one genuine internal contradiction (delivery "safety" bleed), unpinned supply-chain generators in a supply-chain-rigor template, terminology/edition drift, and method-level clause gaps. |

The single most important property: the repo is **repeatedly explicit that it is not a compliance claim** and that completeness is the future manufacturer's obligation (`HARM_RISK.md:18-20`). That honesty is what makes "USABLE_WITH_FILLIN" safe rather than dangerous.

---

## Part A — Internal consistency (structure, framing, style)

47 findings survived adversarial verification; the mechanical link sweep found **zero** genuinely broken links and the `docs/architecture → docs/arc42` rename is 100 % clean. Notable (high/medium) items:

| # | Sev | Finding | Evidence | Fix |
|---|---|---|---|---|
| A1 | **medium** | Delivery-risk Impact **L5 anchor invokes "safety"** inside the very doc that swears delivery risk is *not* safety — blurs the `harm ≠ delivery` invariant the whole design rests on. | `RISK_MANAGEMENT.md:46` ("…legal, or safety in question") vs `:15-16` ("risks of harm (safety) … the separate harm-risk register") | Drop "safety" from the L5 anchor. **[FIXED]** |
| A2 | medium | Conformance **status vocabulary diverges** from CONFORMANCE.md's own legend (`iff-MDSW`/`deferred` vs canonical `iff MDSW`/`deferred-to-manufacturer`); the generator prompt even contradicts itself (`:98` vs `:108`). | `README.md:41`, `CONFORMANCE.md:9-13`, `CONFORMANCE_EXTENSION_PROMPT.md:98/108` | Adopt CONFORMANCE.md spelling everywhere. **[FIXED in prompt + README]** |
| A3 | low | `medical-device software` appears in **three hyphenations**; `arc42 v9` vs `v9.0`; "with-help" vs "with help"; `GitHub↔GitLab` spacing. | multiple | Standardize (deferred — cosmetic sweep). |
| A4 | low | `README.md:7` "**full GitLab equivalents**" over-promises parity that `GITLAB.md:61-68` downgrades to a Free-tier manual convention (scoped-label exclusivity, weight Score, code-owner approval are Premium). | `README.md:7`, `AGENTS.md:14`, `GITLAB.md:10-11,61-68` | Soften headline to "functional parity on Free; a few enforcement conveniences are Premium". (deferred) |
| A5 | low | Extension prompt seeds a **stale ISO 27799:2016** edition that disagrees with the shipped index (2025). | `CONFORMANCE_EXTENSION_PROMPT.md:102` vs `CONFORMANCE.md:35` | Update prompt seed to 27799:2025. **[FIXED]** |

Everything else in Part A is **low/nit** (config.yml absent from the manifest; the `Harm Risk.md` `%20` link; operator-spacing `L × I` vs `L×I`; the `grill-me`/`grilling` alias pair — which is intentional). No structural defect.

---

## Part B — MDR / IEC 62304 / ISO 14971 fitness

### What genuinely works now
- **Two truly separate registers** — delivery-risk 5×5 L×I (`RISK_MANAGEMENT.md`) and ISO 14971 harm-risk S×P (`HARM_RISK.md`), each with its own labels, board, and issue form; the `harm ≠ delivery` invariant is stated and structurally enforced.
- **ADR-0001** is a genuinely usable *living* MDSW-qualification instrument: current "not MDSW" answer, MDCG 2019-11 rev.1 basis, and an operational **per-PR re-evaluation trigger list** (decision support, alarms, risk scores, AI/ML, EHR/EHDS, intended-purpose changes) wired to the PR template. Strongest single artifact.
- **CONFORMANCE.md** — a well-organised, dated, tiered map (active / conditional / iff-MDSW / deferred-to-manufacturer / watch) with a maintenance re-check clause; edition accuracy is high (see Part C).
- The **ISO 14971 core** as far as it goes — hazard→sequence→situation→harm chain, mandatory control hierarchy (§7.1), two verifications per control, residual/benefit gating, worked synthetic example.
- **CONFORMANCE_TRANSFER.md** cleanly separates what transfers vs manufacturer-side obligations; the automation is provably additive and inert-until-configured, with GitHub + GitLab twins.

### Missing for a real MDR product (method-level gaps)
| # | Sev | Gap | Evidence |
|---|---|---|---|
| B1 | **high** | **ISO 14971 §7.5 "risks arising from risk controls / new hazards"** — no step, no form field; the flow goes §5 hierarchy → §6 verification → §7 residual with no loop. The worked example even adds a "re-fetch on focus" control (a classic new-hazard source) with no §7.5 check. | `HARM_RISK.md:77-109`, `harm-risk.yml` — grep empty |
| B2 | **high** | **IEC 62304 §4.3 software safety class (A/B/C) has no home** — cited as *evidenced in* SOUP/traceability but never assigned anywhere, and never distinguished from the MDR Annex VIII Rule 11 *device* class. | `CONFORMANCE.md:53`, `TRACEABILITY.md:5`, `SOUP.md:20` |
| B3 | **high** | **MDCG 2019-16 (cybersecurity) absent** from the MDSW tier — the only cyber anchor is IEC 81001-5-1 in the security tier; the MDR-specific guidance that operationalises the Annex I §17 cybersecurity GSPR is missing. | `CONFORMANCE.md:50,§4` |
| B4 | medium | **No ISO 14971 §9 risk-management report/review** artifact with reviewer + sign-off (the pre-release overall-residual *review* is named, but nothing captures its conclusion). | `HARM_RISK.md:104-105` |
| B5 | medium | **GSPR (Annex I) conformity-checklist** mechanism absent — Annex I is named but attached to no artifact/evidence cell, and is not in the transfer list. | `CONFORMANCE.md:50`, `CONFORMANCE_TRANSFER.md:9-23` |
| B6 | medium | **Rule 11 classification ladder not operationalised** in ADR-0001 (IIa/IIb/III + monitoring sub-rule), so the "if it flips to MDSW" branch is not executable. | `ADR-0001:24,83-84` |
| B7 | medium | **No clause-level IEC 62304 process-coverage map** (§5.1/§5.4-§5.8/§6/§8/§9 = covered/deferred/not-yet); deferral honesty currently covers only organisational items. | `CONFORMANCE_TRANSFER.md:39-50` |
| B8 | medium | **§5.2/§5.3 intended-use / foreseeable-misuse / safety-characteristics** hazard-ID anchor missing; **overall benefit-risk (§8) + residual-risk disclosure** only gestured at; the harm-risk **form under-structures** residual/verification/completeness (all optional free-text; board has structured residual S/P the form never fills). | `HARM_RISK.md:104-105`, `harm-risk.yml:85-103` |
| B9 | medium | **SOUP anomaly review is security-CVE-only** (Dependabot); §7.1.2/§7.1.3 published *functional* anomaly lists and §6 change-on-version-bump re-evaluation are not prompted. | `SOUP.md:8,23,27` |
| B10 | low | **Labelling / IFU / UDI design-side standards** (ISO 20417, EN ISO 15223-1) absent; UDI only as deferred registration; MDR Art. 15 **PRRC** missing from the transfer split; `requirement.yml` issue template absent though `requirement` is the traceability anchor; SOUP→requirement and control→test traceability edges not surfaced. | `CONFORMANCE_TRANSFER.md:38-49`, `TRACEABILITY.md:11-17` |

### Dangerous over-claims (could mislead a team into thinking they're more compliant than they are)
1. **"reconstructable from Git alone"** (`TRACEABILITY.md:3`) — the chain actually depends on **forge metadata** (Issue numbers as REQ IDs, `Closes #n` read via the GitHub timeline API); a bare `git clone` does **not** preserve it. Risk of losing traceability at exactly the MDR transfer moment. **[FIXED]**
2. **Permissive default acceptability matrix** — a catastrophic-harm hazard (S5, P1) rests at `investigate` = "control if practicable, justify if not" rather than mandatory reduction. **[FIXED: S5 is now a hard "reduce" floor]**
3. **Blanket "Standards editions verified 2026-07"** over soft/speculative data — see Part C. **[PARTIALLY FIXED via Part C corrections]**
4. **IEC 62304 §4.3 classes "evidenced in SOUP/traceability"** although no class is ever assigned — implies the classification is handled when it is not. **[FIXED via ADR-0002]**

---

## Part C — Standards verification (web, 2026-07-18)

31 claims fact-checked against fetched primary/authoritative sources: **25 CONFIRMED, 1 WRONG, 5 IMPRECISE, 0 UNVERIFIABLE.** The corrections:

| Claim | Repo said | Verified | Verdict | Source |
|---|---|---|---|---|
| **IEC 62304 Ed. 2** | "final approval, publication expected **from 2026-08**" | At **Committee Draft (CD2)**; IEC forecast publication **~Oct 2028** (FDIS ~2028, poss. 2029). Ed. 1.1 remains state of the art. | **WRONG** | IEC/Johner (blog; direction corroborates audit) |
| **AI Act Annex III high-risk** | 2026-08-02 | Enacted date superseded; **Digital Omnibus (June 2026)** defers standalone Annex III to **2027-12-02** | IMPRECISE *(med conf.)* | EC AI Act page |
| **AI Act Art. 6(1) product** | 2027-08-02 | Digital Omnibus defers Annex I product-embedded high-risk to **2028-08-02** | IMPRECISE *(med conf.)* | EC AI Act page |
| **IEC 80001-1:2021** | title "Application of risk management for IT-networks incorporating medical devices" | Edition/year correct; **title truncated** — append "— Part 1: Safety, effectiveness and security in the implementation and use of connected medical devices or connected health software" (the audit's "2010 title" claim was itself slightly off — the 2010 subtitle was "Roles, responsibilities and activities") | IMPRECISE | webstore.iec.ch/publication/34263 |
| **ISO 20417** | (recommended add) "Information supplied by the manufacturer of medical devices", 2021 | Now **2026** (2nd ed., 2026-03, supersedes 2021); official title **"Medical devices — Information to be supplied by the manufacturer"** | IMPRECISE | iso.org |
| **EN ISO 15223-1:2021** | (recommended add) "Symbols … labels, labelling…" | Year correct (4th ed., 2021-07); title **"Medical devices — Symbols to be used with information to be supplied by the manufacturer — Part 1"** (the "…labels, labelling…" wording is the superseded 2016 title) | IMPRECISE | iso.org |
| **ISO 27799:2025** | "2025, third ed., replaces 27799:2016" | **CONFIRMED** (published 2025-12; also cancels **ISO/TS 14441:2013**). Audit's doubt resolved in the repo's favour. | CONFIRMED (+note) | iso.org |
| **MDCG 2019-11 rev.1** | "rev. 1 (June 2025)", generic link | **17 June 2025**; direct document URL available | CONFIRMED (+precision) | EC health portal |
| **MDCG 2019-16** | (omitted) | Exists, **Rev.1 July 2020** — cybersecurity GSPR guidance; add it | CONFIRMED (add) | EC health portal |

**Confirmed correct as-is:** MDR Rule 11 ladder, MDCG 2020-1 (Mar 2020), CRA all 3 dates, AI Act GPAI (2025-08-02), EHDS all 3 dates, DiGA class I/IIa, IEC 62304 Ed.1.1, ISO 14971:2019, ISO/TR 24971:2020, IEC 62366-1:2015+A1:2020, IEC 82304-1:2016, IEC 81001-5-1:2021, ISO 13485:2016+A11:2021, ISO/IEC 25010:2023 + 25019:2023, ISO/IEC/IEEE 15288:2023, ISO/IEC 27001:2022, 27002:2022, 16085:2021, 42010:2022, 29148:2018, 12207:2017.

### Primary-sources-needed checklist (Q1 answer)
The `/Users/marcel/Nextcloud/Wiss. Arbeiten/Standards` library (60 PDFs) is rich but covers **interoperability / EHR / usability / process-assessment / enterprise-architecture** (ISO 13606, 13940, 13972, 23903, **25237 pseudonymisation**, ISO 9241, ISO/IEC 33xxx SPICE, TOGAF/ArchiMate/HL7 HSRA, eHealth-Network EIF papers) — **not** the med-device-software standards the conformance layer cites. Remaining gaps by who can close them:

- **(A) needs the actual IEC/ISO med-device standard text** (not in the local library; paywalled) — the **clause-level anchors** only: IEC 62304 §5.3.3-5.3.4 / §7.1.2-7.1.3 / §8.1.2; ISO 14971 §7.5/§8/§9/§10; ISO/TR 24971 P1×P2 tables. Editions/titles are now web-confirmed (Part C); only the clause *contents* remain unverified against the source.
- **(B) open — verified in Part C** (EU law, MDCG, ISO/IEC catalogue metadata). Done.
- **(C) not documents — RA/QA/legal decisions**: the real MDSW qualification answer + intended purpose (ADR-0001), the IEC 62304 §4.3 class (ADR-0002), the acceptability-criteria ratification, benefit-risk / residual-risk acceptance. Stay `[NEEDS RA/QA INPUT]`.

### Enrichment candidates from your local library (optional, not defects)
- **ISO 25237:2017 (pseudonymisation)** — directly relevant to the TTP/pseudonym story; candidate for the privacy/security tier.
- **ISO 13606-1..5, ISO 13940 (ContSys), ISO 13972, ISO 23903, eHealth-Network EIF** — candidates to strengthen the **EHDS / EHR-system watch** row.

---

## Part C-bis — Clause-level verification (against the licensed standard PDFs)

After the web pass, the actual IEC/ISO PDFs (IEC 62304:2006+A1:2015, ISO 14971:2019,
ISO/TR 24971:2020, IEC 62366-1, IEC 82304-1, IEC 81001-5-1) were read to verify every
clause anchor the repo cites **and** the content this report added. **23 checks — 20
CONFIRMED, 3 IMPRECISE (all fixed).**

**Confirmed faithful:** ISO 14971 §7.1 (mandatory 3-tier order, verbatim), §7.2 (two
verifications — implementation + effectiveness), §7.4/§7.5/§7.6, §8, §9, §10, §5.2–5.5 —
all exact; the **§7.5 step added above is faithful** to the standard. TR 24971 P1×P2
(§5.5.2), the software-failure-P=1 convention (§5.5.2/5.5.3), and the
matrix-as-manufacturer-example framing (§5.5.1 / Annex C). IEC 62304 §8.1.2, §5.3.3–5.3.4,
§5.1.1(c), §7.3, and the §5.1/5.4–5.8/6/8/9 process map. That ISO 14971 leaves
acceptability criteria to the manufacturer's plan (no prescribed scale/matrix) — confirmed,
so the shipped "example matrix" framing is correct.

**Corrected (3):**
1. **ADR-0002 Class A/B/C** — the initial draft used the IEC 62304:2006 wording; **AMD1:2015
   reworded them into risk-based definitions** (Class A no longer means "no injury possible"
   — the class depends on residual risk after risk-control measures *external* to the
   software). ADR-0002 now uses the amended definitions (§4.3 + Figure 3).
2. **§7.1.2–7.1.3 → §7.1.3** in CONFORMANCE.md — only §7.1.3 ("evaluate published SOUP
   anomaly lists") is the anomaly clause; §7.1.2 is the broader "identify potential causes".
   (SOUP.md already cited §7.1.3 correctly.)
3. **HARM_RISK.md P1 wording** — "P1 is often the only estimable part" was backwards: P1 is
   the software-failure probability *set to 1* (worst case), so severity and P2 carry the
   evaluation. Reworded + cited to TR 24971 §5.5.2.

Precision notes folded in: "unique SOUP designator" (not "version designator", §8.1.2); and
for the future §5.2/5.3 hazard-ID anchor, cite **TR 24971 Annex A** (A.2.1–A.2.37 question
checklist) + **Annex B** (analysis techniques) — **not** Annex C, which governs risk
acceptability, not hazard identification.

## Part D — Prioritized action backlog

**Applied now (this report's same-day PR):**
1. ISO 14971 §7.5 "new risks from controls" — method step in `HARM_RISK.md` + `harm-risk.yml` field. *(B1)*
2. Delivery-risk L5 anchor — drop "safety". *(A1)*
3. Acceptability matrix — S5 is now a hard "reduce" floor + note. *(over-claim 2)*
4. **ADR-0002** software safety classification (IEC 62304 §4.3); Rule 11 ladder embedded in ADR-0001. *(B2, B6)*
5. Pin supply-chain generators (`sbom.yml`, `.gitlab-ci.yml`). *(automation medium)*
6. "reconstructable from Git alone" → "from the project forge…". *(over-claim 1)*
7. CONFORMANCE.md standards corrections from Part C (62304 Ed.2, AI Act deferrals *hedged*, 80001-1 title, MDCG 2019-11 date+URL, **add MDCG 2019-16**, **add ISO 20417:2026 + EN ISO 15223-1:2021**, 27799 also-replaces-14441). *(Part C, B3, B10)*
8. `CONFORMANCE_EXTENSION_PROMPT.md` — 27799:2016→2025 + `iff MDSW`/`deferred-to-manufacturer` terminology. *(A2, A5)*
9. **Deferred-backlog batch (standards on hand, clause-verified):** ISO 14971 §9 risk-management-report stub (`docs/HARM_RISK_REPORT.md`); §5.2/§5.3 intended-use & safety-characteristics hazard-ID anchor in `HARM_RISK.md` §2 (TR 24971 Annex A/B); IEC 62304 process-coverage map (`docs/standards/IEC-62304-COVERAGE.md`); `requirement.yml` issue template. *(B4, B7, B8-partial, B10-partial)*

**Deferred backlog (larger additive work — recommend as follow-up issues):**
- GSPR (MDR Annex I) conformity-checklist artifact. *(B5)*
- Overall benefit-risk + residual-risk-disclosure operationalization; structured residual S/P + §7.6 completeness fields in the harm-risk form. *(B8)*
- SOUP→requirement and control→test traceability edges surfaced in the matrix. *(B10)*
- SOUP functional-anomaly review + change-on-version-bump re-evaluation cadence. *(B9)*
- MDR Art. 15 PRRC in the transfer split; UDI design-vs-registration split. *(B10)*
- Cosmetic terminology sweep (MDSW hyphenation, arc42 v9/v9.0, GitHub ↔ GitLab). *(A3)*
- GitLab "full equivalents" headline softening. *(A4)*

**One item for your confirmation:** the AI Act Digital-Omnibus deferral dates (2027-12-02 / 2028-08-02) rest on a June-2026 development past the assistant's knowledge cutoff; applied as a **hedged** note, not a hard replacement — please confirm against the OJ before treating as final.
