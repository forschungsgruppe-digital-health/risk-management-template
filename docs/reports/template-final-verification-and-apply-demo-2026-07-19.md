# Final verification + apply-demo — full-run report

> **Provenance**
> - **Audited commit:** `99d3211` (`main`); fixes verified on the stack tip `fix/polish`
> - **Date:** 2026-07-19 (overnight run, interrupted once by a session limit)
> - **Question:** Would this template — applied to a child repo — satisfy the **formal
>   risk-management requirements for CE/MDR certification**? Does it **enable rather than
>   enforce**? Verified end-to-end by **actually applying it** to a copy of a real child
>   (cross-hub-patientportal) and driving the register live on GitHub.
> - **Method:** (1) adversarial 5-lens verification workflow (apply-manifest completeness ·
>   CE/MDR formal readiness · enable-not-enforce · post-merge consistency · external web
>   research on notified-body expectations), each lens adversarially re-verified —
>   **31 confirmed findings**; (2) fixes as a stacked PR chain; (3) live apply-demo;
>   (4) this report. Previous report: `whole-repo-audit-2026-07-18.md`.

---

## 1. Certification-readiness verdict

**Before the fixes: "NOT YET — near-ready, two-gate conditional."**
A child created via *Use this template* and diligently filled would satisfy the core
**ISO 14971:2019 documentation set** (plan slot, §5–§8 per-risk chain incl. §7.1 hierarchy,
§7.2 dual verification, §7.4 benefit–risk, §7.5 new-risks, §7.6 completeness, §8
disclosure, §9 report, §10 feed, SOUP/SBOM/traceability, GSPR + 62304-coverage maps,
living qualification + classification ADRs) — but with **two gates open**:

1. **Delivery gate (blocker):** all three retrofit paths omitted the six recently-added
   artifacts; GitLab children got the pre-audit harm-risk form. → **closed by PR #6.**
2. **Slot gate:** five formal slots missing that a notified body predictably flags —
   no security-risk-management file (MDCG 2019-16 / GSPR 17.2), no MDR **AFAP**
   reconciliation (EN ISO 14971:2019+**A11:2021** absent), plan lacking §4.4(e)
   overall-residual criteria + §4.2 policy basis, no per-release register snapshot, no
   CVD policy. → **closed by PR #7.**

**After the stack (#6→#7→#8): the formal slot set is complete.** Content correctness
remains the child's job by design — the template provides every slot, tool, and method,
and is explicit that it is *not* a compliance claim (the honesty that makes it safe).
What can never be templated: the **RA/QA/legal determinations** (real qualification
answer, safety class, ratified acceptability criteria, benefit-risk acceptances, DPO/legal
sign-offs) — all marked `[NEEDS RA INPUT]`-style throughout.

## 2. Enable, don't enforce — verdict: **HOLDS**

Verified line-by-line: no shipped workflow triggers on `pull_request` or blocks a merge;
risk-automation + GitLab vuln-to-register are variable/token-guarded inert; SBOM +
register-export run only on the child's own release/tag events; scripts are additive,
idempotent, advisory (matrix always exits 0 — now literally, via an ERR trap); the skill
defaults to a zero-mutation `plan` mode; obligations are attributed to the standards, not
commanded by the template. Four deviations found and fixed in #8: `template-sync-check`
now has a documented opt-out (`TEMPLATE_SYNC_OPTOUT=1`) and the README states the three
activation models honestly; every required free-text field now sanctions an honest
"none yet — decided at triage" answer (the §7.5 pattern); closed dropdowns gained
`other`/`tbd` options (boards kept congruent); the one "enforces" self-description is now
"scaffolds".

## 3. The stacked fix PRs

| PR | Base | Content |
|---|---|---|
| **#6** `fix/apply-manifests` | `main` | Blocker: 6 artifacts into every apply path; portable `cp -rn src/. dest/` (GNU nested `docs/adr/adr/`); ADR guidance pluralized (0001–0003); verify checklist extended; extension-prompt phases E1–E4 to post-audit parity; **GitLab parity restored** (harm-risk §7.5/§7.6/residual-S-P/disclosure + `Requirement.md` twin + GITLAB.md rows); README/AGENTS manifests |
| **#7** `fix/formal-slots` | #6 | `docs/SECURITY_RISK.md` (MDCG 2019-16 parallel process, safety↔security coupling, **no third register**); `SECURITY.md` CVD stub (CRA 2026-09-11); AFAP note (EN ISO 14971+A11 Annex ZA) + EN edition in the index; §4.4(e)+(f) + §4.2 plan rows; `register-export.yml` + GitLab twin (per-release §9 register snapshots); watch rows **COM(2025) 1023** (MDR/IVDR Simplification Package), **MDCG 2025-6/AIB 2025-1** (AI-Act interplay, cited from ADR-0001's AI trigger), **MDCG 2025-4**; all new artifacts registered in the #6 manifests |
| **#8** `fix/polish` | #7 | Escape hatches; `other`/`tbd` options; risk-form Impact-5 "safety" bleed removed; `TEMPLATE_SYNC_OPTOUT`; truthful README inertness paragraph; literal exit-0 trap; SBOM extension follows `SBOM_FORMAT`; §-reference precision; transfer-list completeness; **+ the live-found label fix** (below) |
| *(#9)* `docs/final-verification-report` | #8 | this report |

**Merge order:** #6 → retarget #7 to `main` → merge → retarget #8 → merge → #9. (No
`--delete-branch` on a PR that is another PR's base.)

## 4. Apply-demo on a real child (cross-hub-patientportal copy)

**Setup:** local clone (`dev` @ `c69980c`) in the session scratchpad; template source =
stack tip. Skill executed inline: `plan` (inventory) → `apply` (user-pre-approved).

**Collision surface found by plan mode** — exactly the interesting case: 28 existing ADRs,
existing `SECURITY.md` + `dependabot.yml`, existing CODEOWNERS + 8 issue forms, no PR
template, no label/workflow/doc collisions, own architecture docs.

**Apply result (25 files):**
- Collision rules all fired correctly: `SECURITY.md` + `dependabot.yml` **skipped with
  merge-by-hand notes**; CODEOWNERS **appended**; PR template copied clean; **arc42 layer
  skipped** (own docs); ADRs **renumbered 0001–0003 → 0028–0030** with every cross-link in
  the copied set rewritten (verified zero stale references).
- The pr1-fixed manifest delivered **all** new artifacts (validating the blocker fix).

**Live register demo** (temp private repo `msusky/tmp-patientportal-risk-demo`, containing
**only the applied template artifact set — zero portal source code**; the auto-mode
policy correctly refused a full-tree snapshot push, and the artifact-only repo is the
better demo anyway):

| Check | Result |
|---|---|
| `setup-labels.sh` both sets | ✅ 18 + 14 labels; **idempotency proven** (re-run: 0 created, 18 skipped) |
| **Live bug found** | ❌→✅ `disclose-in-ifu` description exceeded GitHub's **100-char limit** (HTTP 422) — fixed in the template (on #8) and re-run clean. *This is why you demo.* |
| Board scripts w/o `project` scope | ✅ graceful stop **naming the exact grant**: `gh auth refresh -s project,read:project` (exit 0, no partial state) |
| Demo issues (synthetic) | ✅ #1 `[RISK]` (honest-none mitigation demonstrated), #2 `[HARM]` (full §5–§8 chain incl. §7.5 + TR 24971 P1=1 convention), #3 `[REQ]` — all auto-labelled correctly |
| `traceability-matrix.sh` | ✅ REQ-3 listed with `⚠ no linked PR` (advisory flagging works); SOUP→requirement edge rendered; exits 0. (First run missed REQ-3 — GitHub list-API indexing lag of seconds, not a defect) |
| Workflow inertness | ✅ 3 workflows active but dormant: risk-automation guarded (no `RISK_PROJECT_URL`), sbom + register-export release/dispatch-gated |
| **Live workflow run** | ✅ `sbom` dispatched → **success in 11 s** (SHA-pinned action resolved, `SBOM_FORMAT`→extension derivation worked, artifact uploaded) |

## 5. Remaining manual steps (enable-side: yours to decide, nothing blocks)

1. **Merge the stack** #6→#7→#8→#9 (conformance-critical paths — human review per repo rules).
2. **`gh auth refresh -s project,read:project`** to let the board scripts create the two
   Projects v2 boards (the only capability the demo could not exercise).
3. Enable the **Renovate app** if the GitLab-image bumps should actually flow.
4. **Cleanup of the demo:** `gh repo delete msusky/tmp-patientportal-risk-demo --yes`
   (needs `delete_repo` scope: `gh auth refresh -s delete_repo`) — the repo is private,
   clearly marked TEMPORARY, and contains no portal code. Scratchpad copies are ephemeral.
5. The **AI-Act Digital-Omnibus** dates: enacted dates remain operative; re-check the OJ
   (the deferral was signed 2026-07-08 but not yet published as of this run).
6. The RA/QA determinations that only humans can make (ADR-0028/0029 content in a real
   child, acceptability ratification, §9 sign-offs).

## 6. Bottom line

With the stack merged, a child repo gets — **through every apply path, on both
platforms** — a formally complete, tool-supported, honestly-scoped risk-management
apparatus: every ISO 14971 deliverable slot, the security-risk parallel process, the MDR
AFAP semantics, per-release evidence exports, and living qualification/classification
decisions — while enforcing nothing: every automation is disclosed, guarded, or opt-out,
every required field accepts an honest "not yet", and every legal determination is left,
explicitly, to the humans who must make it.
