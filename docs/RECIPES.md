# Risk-management recipes — what to do when, step by step

This is the **hands-on cookbook** for the risk management this template sets up. It is
written so that you can act correctly **without prior risk-management experience**: every
recipe tells you *when it applies*, *what the concepts mean*, *exactly what to do* (with a
worked example), *how you know you are done*, and *the mistakes people typically make*.

The recipes add **no rules of their own** — they only walk you through the methods in
[`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md) and [`HARM_RISK.md`](HARM_RISK.md); if anything
here seems to contradict those documents, the method documents win. Everything is
**guidance you may adapt**, not a mandate. Labels are written GitHub-style (`risk:open`);
on GitLab the same label is scoped (`risk::open` — see [`GITLAB.md`](GITLAB.md)).
Recipes marked **(conformance layer)** need the optional MDR/62304/14971 layer.

---

## Before anything else: the system in four sentences

1. A **risk** is something that *might* happen and would matter — it is not a bug (a bug
   already happened; use a normal issue for bugs).
2. Every risk lives as a **GitHub issue** created through a form; forms apply the right
   **labels** automatically, and labelled issues appear on a **project board** where the
   team works them.
3. There are **two strictly separate registers**: *delivery* risks (deadlines, money,
   dependencies, security of the project) and *harm* risks (a patient/user could be
   injured). They use different forms, different scales, different boards — **never** put
   patient-safety concerns in the delivery register.
4. You personally never need to decide anything alone: forms let you write **"none known
   yet"**, and a regular **triage/review meeting** makes the actual decisions.

**Which recipe do I need?**

| Something… | Go to |
|---|---|
| …might go wrong with the project (deadline, dependency, budget, security) | Recipe 1 |
| …is a new risk issue waiting for scoring/decisions | Recipe 2 |
| …was flagged by Dependabot/Trivy as a vulnerability | Recipe 3 |
| …was reported by a pilot user / clinician / monitoring | Recipe 4 |
| …could hurt a patient or user | Recipe 5 (immediately) |
| …needs controls implemented/checked for a harm risk | Recipe 6 |
| …can't be fixed further and someone must accept what remains | Recipe 7 |
| …that we logged as a risk has actually happened | Recipe 8 |
| We are about to release | Recipe 9 |
| It's time for the regular review meeting | Recipe 10 |
| A new feature might make us a medical device | Recipe 11 |
| A third-party library version changed | Recipe 12 |
| The project ends / a company takes over | Recipe 13 |

**Mini-glossary** (all defined properly in the method docs):

| Term | Meaning |
|---|---|
| L, I, Score | Likelihood (1–5), Impact (1–5), Score = L × I → severity band: Critical ≥ 15 · High 10–14 · Medium 5–9 · Low < 5 |
| S, P | (harm register) Severity of the *harm* (1 = negligible … 5 = death) × Probability of the harm |
| Mitigation / Control | An action that makes a risk less likely or less bad. "Control" is the harm-register word, and there the *order* of control types is prescribed |
| Residual risk | What is still left *after* the controls — someone must consciously accept it |
| Triage | The short part of a regular meeting where new risks are scored and decisions are made |
| SOUP | "Software of unknown provenance" — third-party libraries the product depends on (IEC 62304 term) |

---

## Recipe 1 — You think something might go wrong (raise a delivery risk)

**When:** any moment you catch yourself thinking *"if X happens, we have a problem"* —
a dependency looks unmaintained, a deadline seems unrealistic, a single person holds
critical knowledge, a server contract expires. **Not** for: things that already happened
(that's a bug/incident) and **not** for possible patient harm (→ Recipe 5).

**What you should know first:** raising a risk is *cheap and welcome* — anyone may do it,
nobody needs permission, and a raised risk that never materializes is a success, not an
embarrassment. You only *propose*; the review meeting decides (Recipe 2).

**Steps:**

1. Go to **Issues → New issue** and pick the **"Risk"** form. (It applies the labels
   `risk` + `risk:open` for you — don't remove them.)
2. Describe the risk as a **cause → uncertain event → consequence** chain. Worked
   example: *"Because the upstream terminology server has no SLA* (cause)*, it may be
   unavailable during the pilot* (uncertain event)*, which would block coded data entry in
   demos* (consequence)*."* If you can't fill all three parts, you probably have a task or
   a bug, not a risk.
3. Pick a **category** (dropdown). If nothing fits, choose *other* and say what it is.
4. Propose **Likelihood** and **Impact**, each 1–5. Don't agonize — use the anchors shown
   in the form (e.g. L3 = "a credible path exists", I3 = "a milestone slips") and let
   triage correct you. Example: terminology-server outage → L3, I3.
5. **Mitigation actions:** write at least one idea *or* — honestly —
   *"None known yet — to be proposed at triage"* plus one line why. Never invent a fake
   mitigation just to fill the field.
6. Optionally: name an owner, early-warning triggers ("latency already increasing"), a
   contingency ("demo against local snapshot"), affected milestones.
7. Submit. That's all that is expected of you as the raiser.

**Done when:** the issue exists with its two labels. It will show up on the **Risk
Register** board automatically (or be pulled in at the next triage) — you don't need to
chase anyone.

**Common mistakes:** filing a bug as a risk ("login is broken" — that's a bug) · filing a
patient-safety concern here (→ Recipe 5, different register!) · waiting until you're
"sure" (uncertainty is the point) · inflating I so the risk "gets attention" (triage will
distrust your next one).

---

## Recipe 2 — Triage: scoring and deciding (at the review meeting)

**When:** for every new risk, in the regular review meeting (Recipe 10) — not ad hoc in
the issue thread, so decisions have quorum.

**What you should know first:** triage turns a *proposal* into a *decision*. The response
is mechanical once the Score is agreed — that's the point of the bands: no arguing about
"how much attention does this deserve" each time.

**Steps:**

1. Open the new risk on the **Risk Register** board.
2. Challenge the proposed L and I together — the *anchors* in
   [`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md) §3 are the shared yardstick. Update the
   board fields.
3. Set **Score = L × I** (board field; it is not auto-computed) and the **Severity**
   field + `risk-sev:*` label per band: **Critical ≥ 15 · High 10–14 · Medium 5–9 ·
   Low < 5**.
4. Apply the band's **response rule** (§4):
   - **Critical** — act *now*: named owner, mitigation started, reviewed every sprint,
     escalated to the lead.
   - **High** — mitigation planned & scheduled, named owner, reviewed every sprint.
   - **Medium** — watch: define triggers, revisit at the regular review.
   - **Low** — accept & log; only re-check if a trigger fires.
5. Record the decision in one issue comment: *"Triage 2026-07-19: L3×I3=9 Medium — watch;
   trigger = terminology-server latency alerts; owner @maria; review 2026-08-02."*
6. Set the board's **Review date**.

**Done when:** the risk has Score, severity, an owner (mandatory for Critical/High), a
review date, and one of three explicit decisions: **mitigate / accept / watch**.

**Common mistakes:** skipping the Score field ("the label is enough" — the board views
sort by Score) · Critical/High without a *named* owner · decisions made silently in the
board without an issue comment (the issue is the record, the board is the working view).

---

## Recipe 3 — A dependency vulnerability (CVE) arrives

**When:** Dependabot (GitHub), Trivy (GitLab), or any scanner reports a critical/high
vulnerability in something you depend on.

**What you should know first:** scanners **feed** the register, they never decide.
An automated alert becomes a *risk like any other* and goes through triage. The template's
automation (if enabled — it's off until configured) opens the register issue for you.

**Steps:**

1. If the automation opened a `risk` + `risk-cat:vulnerability` issue: continue with it.
   If not, raise one yourself (Recipe 1; category *vulnerability*), linking the alert.
2. Triage it (Recipe 2). For L, think *exploitability in our context*; for I, think
   *what an attacker actually reaches*.
3. **(conformance layer)** Check [`soup.yaml`](../soup.yaml): is the affected component
   **inventoried** as SOUP (i.e., the product itself relies on it at runtime)?
   - If yes: additionally record the evaluation via the **"SOUP anomaly"** issue form —
     that is the formal IEC 62304 §7.1.3 record: does the vulnerability affect the
     *functions we rely on*? Update the component's `anomalies:` block in `soup.yaml`.
   - If it's only a build/dev dependency, the register issue alone is enough.
4. **Always ask the safety question** out loud at triage: *"Can this contribute to a
   situation where a patient/user is harmed?"* (e.g., data manipulation → wrong clinical
   display). **If yes or unclear → Recipe 5 now**, linked both ways.
5. Fix, upgrade, or mitigate like any other work; close per Recipe 2's decision.

**Done when:** the vulnerability is a scored, decided register entry; SOUP bookkeeping is
updated if applicable; the safety question has an explicit answer in the issue.

**Common mistakes:** patching silently without a register entry (auditors ask "how do you
*handle* vulnerabilities", not "did you patch this one") · treating the scanner severity
as your Score (CVSS ≠ your context) · skipping the safety question because "it's just a
library".

---

## Recipe 4 — A pilot user or clinician reports something **(conformance layer)**

**When:** any observation from real use reaches you: user feedback, a complaint, an odd
behaviour in the pilot, a monitoring alert. This is the ISO 14971 **§10** "production and
post-production information" channel — the standard expects you to *actively collect and
process* such information.

**What you should know first:** the intake form is a **funnel, not a register**. It
captures the observation quickly and completely; *triage* then decides which register (if
any) it belongs in. One observation can spawn several entries.

**Steps:**

1. Capture it via **Issues → New issue → "Field feedback / incident"** (label
   `field-feedback`). Write **what was observed, when, in which context** — and use
   **synthetic identifiers only, never real patient data** (e.g. "a clinician", "patient
   record A" — no names, no MRNs).
2. Answer the form's question **"possible safety relevance?"** honestly — *unclear* is a
   valid and common answer.
3. At triage, route it (create the target issue, link both ways):
   - could a patient/user be harmed → **Recipe 5** (harm-risk),
   - a project-level risk became visible → **Recipe 1**,
   - a third-party component misbehaved → **Recipe 3/12**,
   - it's simply a defect → normal **bug** issue.
4. Close the intake issue once routing is done — it has served its purpose; the analysis
   lives in the created entries.

Note: **security vulnerability reports from outsiders** don't use this form — they follow
the disclosure channel in [`SECURITY.md`](../SECURITY.md).

**Done when:** the intake issue links its routing outcome ("→ raised #42 harm-risk") and
is closed. Nothing was analysed *in* the intake issue.

**Common mistakes:** pasting real patient data into the issue (never — this is a hard
boundary) · analysing and "resolving" inside the intake issue (then the registers stay
blind) · discarding "minor" feedback (patterns emerge from collected minors).

---

## Recipe 5 — A possible patient-harm hazard **(conformance layer)**

**When:** *anything* that could end in injury or damage to health — including harm caused
by wrong or delayed clinical decisions based on what the software shows. Examples: wrong
patient's data displayed; a score computed wrongly; stale data after a refresh bug; an
alert that silently fails. **Do this immediately when the possibility is recognized — do
not wait for the next meeting.**

**What you should know first — the vocabulary of the form** (this chain is the heart of
ISO 14971, and the form walks you through it):

- **Hazard** — the potential source of harm (*"score shown for the wrong patient"*).
- **Sequence of events** — how normal use or failure gets there (*"two records open in
  adjacent tabs; stale component state renders A's score in B's view"*).
- **Hazardous situation** — who is exposed, in what circumstances (*"clinician reads the
  wrong score during triage"*).
- **Harm** — the actual damage to health (*"delayed escalation of care"*).

Scoring differs from the delivery register: **S** = severity *of the harm* (1 negligible …
5 death), **P** = probability of the harm. For software, the failure probability usually
can't be estimated meaningfully — the convention (from ISO/TR 24971) is to set it to the
**worst case (P1 = 1)** and let S and P2 (probability that the situation leads to harm)
carry the evaluation. The form has fields for this; when unsure, score conservatively and
say so.

**Steps:**

1. **Issues → New issue → "Harm risk (ISO 14971)"** (labels `harm-risk` +
   `harm-risk:open`). Never use the delivery "Risk" form for this.
2. Fill the four chain fields (above — the worked example is a valid pattern to copy).
3. Pick the **hazard category** and score **S** and **P** with the anchors shown.
4. Read the **acceptability matrix** result (HARM_RISK.md §4): `reduce` means controls
   are required; `investigate` means control if practicable and justify if not;
   `acceptable` still means document and monitor. An S5 hazard is always `reduce`.
5. Propose **controls in the prescribed order** (§5 — this order is *mandatory* in the
   method, and the notified-body world takes it seriously):
   1. **Inherently safe design** — make the hazard impossible by construction
      (*bind patient context immutably per view*);
   2. **Protective measures** — checks, confirmations, alarms
      (*patient banner with name/DOB on every clinical view*);
   3. **Information for safety** — warnings, training. Weakest tier, never the first
      resort.
   Writing *"To be determined at evaluation"* is legitimate for a freshly identified
   hazard.
6. Answer the **§7.5 field**: could these controls *introduce or shift* a hazard?
   (*a re-fetch adds a race window; an alarm adds alarm fatigue*). "None identified" +
   one line of reasoning is a valid answer.
7. Submit; the issue lands on the **Harm Risk File** board. Continue with Recipe 6.

**Done when:** the chain is complete and comprehensible to someone who wasn't there, S×P
is scored, a control plan (or an honest TBD) exists.

**Common mistakes:** putting it in the delivery register because "it's also a project
problem" (it may be *both* — then two linked issues, one per register) · scoring P low
because "our code is good" (use the P1=1 convention) · jumping straight to a warning
banner (tier 3) when a design change (tier 1) is feasible · describing the fix instead of
the *hazard* (the register documents the danger, not the ticket to close it).

---

## Recipe 6 — Implementing and verifying controls **(conformance layer)**

**When:** working the controls of a harm-risk from Recipe 5.

**What you should know first:** for each control the method requires **two separate
verifications** — that it is **implemented** (it exists in the shipped product) and that
it is **effective** (it actually reduces the risk). A merged PR proves the first, never
the second.

**Steps:**

1. Implement the controls, preferring the highest feasible tier. If a control changes the
   architecture, record it as an **ADR** and link it (it will show up in arc42 §11).
2. For each control, add to the harm-risk issue:
   - **implemented** — link the PR and the test that pins it;
   - **effective** — link the evidence: a test that provokes the hazardous situation and
     shows the control catching it, an analysis, or (for controls that depend on the user
     noticing/doing something) a usability evaluation per IEC 62366-1.
3. Track progress in the board field **Control verification**: `None → Implemented →
   Verified effective`.
4. If a tier-3 control (information for safety) relies on the user *being told*
   something, add the **`disclose-in-ifu`** label — that sentence must reach the
   user-facing accompanying information, and the label is how it is found later
   (Recipe 9).
5. Re-visit the §7.5 answer now that the controls are real: did implementation introduce
   anything new? If yes → new harm-risk (Recipe 5), linked.
6. Confirm **completeness** (the form's §7.6 checkbox): all hazardous situations for this
   hazard considered, all control activities done. Then set `harm-risk:controlled`.
   Continue to Recipe 7 for the residual.

**Done when:** every control shows *two* pieces of verification evidence, the §7.5/§7.6
answers are recorded, the label/state moved to `harm-risk:controlled`.

**Common mistakes:** "the PR is merged, so we're done" (that's only verification #1) ·
verifying effectiveness with the same happy-path test that existed before · forgetting
`disclose-in-ifu` (the warning then never reaches the manual) · closing the issue here —
closing needs Recipe 7.

---

## Recipe 7 — Accepting a residual risk

**When:** (delivery) the team consciously decides *not* to mitigate further; (harm) after
Recipe 6, something remains — it almost always does.

**What you should know first:** acceptance is a **named person's conscious decision with
a written reason** — never a silent timeout. In this template the project lead accepts
(delivery: any Critical; harm: any residual, and anything with S ≥ 4 explicitly).

**Steps — delivery risk:**

1. In the issue, write *what* is accepted and *why* ("cost of mitigation exceeds
   exposure; trigger defined"), and *who* accepts.
2. Label `risk:accepted`, keep a review date — accepted ≠ forgotten.

**Steps — harm risk (conformance layer):**

1. Re-score after controls: set **Residual severity** and **Residual probability** (form
   dropdowns and board fields exist for exactly this).
2. Judge the residual against the acceptability matrix (§4) again.
3. **If the product is (or may become) a medical device, mind the AFAP note** (§4): under
   MDR, "acceptable" does **not** exempt you from the control hierarchy — risks must be
   reduced *as far as possible* without hurting the benefit-risk ratio, and "not
   practicable" needs a justification that isn't purely cost.
4. If the residual is still above acceptability and no further control is practicable:
   write a **benefit–risk analysis** in the issue — *why the medical benefit outweighs
   this residual risk* — and have the project lead accept it. Label
   `harm-risk:residual-accepted`.
5. Every residual acceptance feeds the **overall** evaluation at release time (Recipe 9)
   — one acceptable residual can still make an unacceptable sum.

**Done when:** residual scored, acceptance + rationale + acceptor recorded in the issue,
label set.

**Common mistakes:** acceptance by silence ("nobody objected in the meeting") ·
accepting per-risk and never looking at the *sum* (that's exactly what Recipe 9 is for) ·
using cost as the sole AFAP justification for a medical device.

---

## Recipe 8 — A risk has materialized (it actually happened)

**When:** the thing you logged as uncertain is now reality — the server *is* down during
the pilot, the key person *did* leave.

**Steps:**

1. Execute the **contingency** from the issue — that's why you wrote it. No contingency?
   Improvise, and write down what you did.
2. The event itself is now an **incident/bug** — open a normal issue for the operational
   work; link risk ↔ incident both ways. **(conformance layer)** If patients were or
   could have been affected: **Recipe 4/5 immediately**, before anything else.
3. When the dust settles, close the risk (`risk:closed`) with a three-line post-mortem in
   the issue: Did our triggers fire in time? Was L honest in hindsight? What would we log
   earlier next time?
4. Ask the question that turns pain into value: *what new risks did the event reveal?* →
   Recipe 1 for each.

**Done when:** incident handled in its own issue, risk closed *with* lessons, follow-up
risks raised.

**Common mistakes:** handling the incident inside the risk issue (mixes the record of
*anticipation* with the record of *response*) · closing without the post-mortem lines
(the register's learning loop is its main long-term value).

---

## Recipe 9 — Preparing a release **(conformance layer)**

**When:** before every release/tag. Plan ~30–60 minutes with the lead present.

**What you should know first:** ISO 14971 requires a pre-release **review of the overall
residual risk** — all harm-risks *together*, not each alone — and a **written report**
with a named sign-off (§9). The template automates the evidence; the judgment is human.

**Steps:**

1. Open the **Harm Risk File** board: no `harm-risk:open` items without a decision; every
   `controlled` item has its two verifications (Recipe 6).
2. Ask the **overall** question: *is the sum of all residual risks acceptable for this
   release?* — e.g., many small residuals in the same clinical workflow may compound.
3. Fill a copy of [`HARM_RISK_REPORT.md`](HARM_RISK_REPORT.md) for the release: the three
   §9 conclusions (plan executed · overall residual acceptable · §10 feed in place), the
   overall benefit-risk statement, and the **sign-off** by the acceptance authority named
   in your plan (HARM_RISK.md §1).
4. Reconcile **`soup.yaml`** against reality: does it match the versions actually
   shipping? The release's **SBOM** (attached automatically by the sbom workflow) is the
   cross-check.
5. Walk all **`disclose-in-ifu`**-labelled items: is each warning/instruction actually in
   the user-facing documentation of this release?
6. Publish the release — the workflows attach the SBOM and the **register exports**
   (JSON snapshots of both registers) as release assets: that's your frozen evidence for
   this version.

**Done when:** the report is filled and signed, IFU items are placed, SOUP is reconciled,
and the release carries its SBOM + register exports.

**Common mistakes:** treating this as a checkbox ritual in the last hour before the tag ·
"overall acceptable because each one was accepted" (the sum is its own question) ·
signing without the named authority from the plan.

---

## Recipe 10 — The regular review meeting

**When:** on the cadence your team set in the plan (sprint or bi-weekly). 15–30 minutes
is normal; protect the slot.

**Steps** (an agenda you can copy):

1. **New risks** → triage them (Recipe 2).
2. **Critical/High** → owner reports progress in one sentence each; stale ones are
   escalated, not re-admired.
3. **Review queue** view (review date reached) → for each: still real? score still
   honest? next review date set.
4. **Triggers** → did any early-warning sign fire since last time?
5. **Closed risks** → celebrate briefly; it keeps the register liked.
6. **(conformance layer)** also walk: the **Harm Risk File** board (anything
   uncontrolled?), open **SOUP anomalies** and **field-feedback** intakes (Recipes 3/4/12
   routing done?), and once a quarter the `watch` tier of
   [`standards/CONFORMANCE.md`](standards/CONFORMANCE.md) — has a law/standard moved? If
   yes, that's a `risk-cat:compliance` entry (Recipe 1).

**Done when:** the Review-queue view is empty of overdue items and every Critical/High
had a heartbeat.

**Common mistakes:** letting the meeting become a status meeting (it's a *decision*
meeting) · skipping it "because nothing happened" (the empty walk takes five minutes and
is the proof of an *operated* register — which is exactly what an auditor asks for).

---

## Recipe 11 — A feature might change our regulatory status **(conformance layer)**

**When:** the PR template's checkbox question fires: the feature touches **clinical
decision support, alarms on clinical values, risk scores, care-plan logic, AI/ML used for
clinical decisions, EHR embedding, or changes the stated intended purpose**.

**What you should know first:** whether software is a **medical device** is not decided
once — it can *flip* with a single feature. The living decision lives in
[ADR-0001](adr/0001-mdsw-qualification.md); this recipe keeps it honest. "We checked and
nothing changed" is a *good and recordable* outcome.

**Steps:**

1. **Before merging** the feature PR, raise a `risk` issue referencing ADR-0001 (this
   makes the check visible and assignable).
2. Walk the decision aid: MDCG 2019-11 rev. 1 (for AI/ML features also MDCG 2025-6) — the
   ADR's *Context* section tells you what to look at.
3. Record the result in ADR-0001's **Current decision** (+ date + deciders) — even if the
   answer is "unchanged: not MDSW".
4. **If it flips to "is MDSW":** the dormant conformance tier becomes binding — classify
   per MDR Annex VIII Rule 11 (the ladder is in the ADR), bind the software safety class
   in [ADR-0002](adr/0002-software-safety-classification.md), and treat the gaps the
   [62304 coverage map](standards/IEC-62304-COVERAGE.md) marks `not-yet` as work to plan.
   Get regulatory-affairs advice — this step is exactly where it pays.

**Done when:** ADR-0001 shows a dated, decided entry that covers this feature.

**Common mistakes:** ticking the PR checkbox "no" reflexively (read the trigger list —
"risk scores" catches many innocent-looking features) · doing the walk *after* merging ·
treating the flip as a catastrophe (the whole template exists so that this moment is
orderly).

---

## Recipe 12 — A third-party (SOUP) component version bump **(conformance layer)**

**When:** a Dependabot/Renovate PR (or manual upgrade) touches a component that is
inventoried in [`soup.yaml`](../soup.yaml).

**What you should know first:** for SOUP, an upgrade is a *change to evaluate*, not just
a lockfile diff: does the new version still provide the functions we rely on, and does it
bring known problems?

**Steps:**

1. In the bump PR, check the component's **release notes / bug tracker / errata** for the
   new version — *not only CVEs*; functional anomalies count (that's IEC 62304 §7.1.3).
2. Anything relevant → a **"SOUP anomaly"** issue (Recipe 3 step 3 pattern) with the
   impact assessment against the functions listed in the component's
   `requirements:` block.
3. Confirm in one PR comment that the **relied-upon functional/performance requirements
   still hold** (or what changed).
4. Update the component's `version:` in `soup.yaml` in the same PR.
5. Merge per your normal review flow.

**Done when:** the PR links the check ("release notes reviewed, no relevant anomalies;
soup.yaml bumped") and `soup.yaml` matches what ships.

**Common mistakes:** auto-merging bumps of *inventoried* components without the check
(fine for dev-tooling, not for SOUP) · updating the code but not `soup.yaml` (Recipe 9
will catch it, expensively late).

---

## Recipe 13 — Handover to the future manufacturer **(conformance layer)**

**When:** the research project ends, or an organization prepares to place the product on
the market as a medical device.

**What you should know first:** everything this template had you maintain exists for
this moment: the evidence that is *impossible to reconstruct later* (risk history, SOUP
trail, qualification decisions) transfers; the *organizational* obligations (QMS,
CE marking, clinical evaluation) were always the manufacturer's and start fresh on their
side.

**Steps:** run the **handover checklist** in
[`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md) top to bottom — it covers exporting
the boards and issues, reconciling SOUP against the last SBOM, regenerating the
traceability matrix, walking ADR-0001/0002 with the manufacturer's regulatory people,
confirming §9 reports exist, and agreeing who picks up the `watch`-tier deadlines
(CRA, EHDS) and the CVD policy.

**Done when:** that checklist says so — it is the single source for this recipe on
purpose (no duplicated steps to drift apart).

---

*Maintainer note: keep recipes and methods in sync — a change to
`RISK_MANAGEMENT.md`/`HARM_RISK.md` that affects a step here should update both in the
same PR. Recipes deliberately contain no rules of their own.*
