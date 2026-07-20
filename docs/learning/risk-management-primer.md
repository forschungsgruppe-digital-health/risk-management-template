# Risk management for medical-device software — a primer for beginners

A self-contained lecture on what risk management *is*, why it exists, and how it works —
written for someone who has never done it. It then shows how the **risk-management-template**
and its **[example repo](https://github.com/forschungsgruppe-digital-health/risk-management-template-example)**
turn each idea into something you can click on.

> **Copyright & sourcing — please read.**
> Every factual claim is grounded in the actual text of the standards and cites the
> **clause** it comes from (e.g. *14971 §7.1*) so you can verify it. The standards are
> **copyrighted works** (© ISO/IEC and their national adopters). This primer explains them
> in its **own words** and uses only **short, attributed quotations** — a handful of words
> each, for education and commentary (the *right of quotation*; e.g. §51 of the German
> Copyright Act / fair use). It reproduces **no tables, figures, diagrams, or substantial
> portions** of any standard, and it is **not a substitute** for them: you must **obtain
> the standards** (see §9) to do real work. The MDR (EU law) wording was confirmed against
> public full-text renderings of Regulation (EU) 2017/745; **verify against the
> [Official Journal / EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/745/oj)** before
> relying on it. This primer is educational — **not legal, regulatory, or clinical advice**.
>
> **Editions used:** ISO 14971:2019 · ISO/TR 24971:2020 · IEC 62304:2006+A1:2015 ·
> IEC 62366-1:2015+A1:2020 · IEC 82304-1:2016 · IEC 81001-5-1:2021 · ISO 81001-1:2021 ·
> Regulation (EU) 2017/745 (MDR), Annex I. *(Full bibliographic entries in §9.)*
>
> *(Eine deutsche Fassung: [`risk-management-primer.de.md`](risk-management-primer.de.md).)*

---

## 1. The one big idea

You cannot make risk zero. A useful medical device that carries **no** risk essentially
does not exist. So the goal of risk management is **not** to eliminate risk — it is to
**bring risk down to a level you can justify, and prove that you did**.

The standard that defines this for medical devices, **ISO 14971:2019**, captures the idea
in its definition of *safety*: **"freedom from unacceptable risk"** (14971 §3.26). Read
that carefully — safety is not the *absence* of risk, it is the absence of risk judged
*unacceptable*. Some risk always remains after you have done your best; the standard calls
what is left the **residual risk** (14971 §3.17), and it too must be looked at and
accepted on purpose.

Two consequences follow, and they shape everything else:

- **Risk has two ingredients, always considered together:** how *likely* a harm is
  (probability) and how *bad* it would be (severity). ISO 14971 defines *risk* as exactly
  the *"combination of the probability of occurrence of harm and the severity of that
  harm"* (14971 §3.18). You can never describe a risk with only one of the two.
- **Judgement, not just calculation, is required.** The standard's Introduction notes that
  different people accept the same risk differently depending on the expected *benefit*
  (14971, Introduction). That is why "is this acceptable?" is a decision a competent,
  responsible person makes against pre-agreed criteria — not a number a tool spits out.

This template implements that mindset directly: its harm-risk method
([`../HARM_RISK.md`](../HARM_RISK.md)) ships an acceptability matrix explicitly labelled
*"example — adopt consciously"*, because — as the next sections show — **the standard makes
you set your own criteria**, it does not hand them to you.

---

## 2. The vocabulary you must own

Almost every beginner mistake is really a vocabulary mistake. Four words form a **chain**,
and keeping them distinct is the whole game (all from ISO 14971 Clause 3):

| Term | Plain meaning | Clause |
|---|---|---|
| **Hazard** | A *potential* source of harm. On its own it has hurt no one yet — it is just the thing that *could* (electricity, a sharp edge, unsafe software behaviour). | §3.4 |
| **Hazardous situation** | A circumstance in which people are actually **exposed** to the hazard. This is the bridge from "a hazard exists" to "harm can now happen". | §3.5 |
| **Harm** | The actual injury or damage to health (including harm from wrong or delayed clinical decisions caused by software). | §3.3 |
| **Risk** | Probability of that harm **×** its severity — the two ingredients from §1. | §3.18 |

The chain is: **hazard → (sequence of events) → hazardous situation → harm.** A hazard
becomes dangerous only through a *foreseeable sequence of events* that exposes someone, and
**one hazard can lead to several different hazardous situations and harms** (14971 §5.4).

**Worked example (from the example repo).** Issue
[#2 in the example repo](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/2)
is a complete, synthetic harm-risk written in exactly this chain:
*Hazard* — a questionnaire score is shown for the **wrong patient**; *Sequence* — two
records open in adjacent tabs, stale state renders patient A's score in patient B's view;
*Hazardous situation* — a clinician reads the wrong score during triage; *Harm* — delayed
escalation of care. Notice how the *fix* is **not** the hazard — the register documents the
danger, not the ticket that closes it.

A few more definitions you will meet (ISO 14971 Clause 3):

- **Intended use / intended purpose** (§3.6) — what the manufacturer says the device is
  *for*; you cannot find hazards until you are honest about this.
- **Reasonably foreseeable misuse** (§3.15) — predictable *wrong* use you must consider,
  because many real harms come from human behaviour, not device faults.
- **Benefit** (§3.2) — a positive effect on health, patient management, or public health;
  what residual risk is weighed against.
- **State of the art** (§3.28) — current *generally accepted good practice* — importantly,
  **not** necessarily the newest or most advanced technology.

---

## 3. The process, step by step

ISO 14971 organises everything into **one ongoing process** that the manufacturer must
*"establish, implement, document and maintain"* and that *"shall apply throughout the life
cycle of the medical device"* (14971 §4.1). "Ongoing" and "life cycle" are the point: risk
work is never finished at launch.

The process has four required parts — **risk analysis, risk evaluation, risk control, and
production/post-production activities** — all governed by a written **risk management plan**
(14971, Figure 1). Below is the whole loop, each step with *what it is*, *why it exists*,
its clause, and **how this template does it**.

### 3.0 Before the work: plan, file, policy, people

- **A risk-management PLAN, written up front** (14971 §4.4). For the specific device you
  plan the work *before* doing it. The plan must contain at least: scope and life-cycle
  phases; responsibilities; when reviews happen; **the criteria for risk acceptability**;
  a **method and criteria for the overall residual risk**; verification activities; and how
  production/post-production information is collected. Acceptance criteria are set *up
  front* so later decisions cannot be bent to fit a result.
  → *Template:* [`../HARM_RISK.md`](../HARM_RISK.md) **§1** is that plan table, with rows for
  the policy basis (§4.2), the overall-residual method (§4.4 e) and review requirements
  (§4.4 c) — filled in per project.
- **The risk-management FILE** (14971 §4.5) — the evidence trail that, *for each hazard*,
  lets a reviewer trace analysis → evaluation → control + its verification → residual
  result. → *Template:* the register itself (GitHub issues), plus the §9 report and the
  per-release register exports.
- **Top management sets a POLICY for acceptable risk** (14971 §4.2): *"Top management shall
  define and document a policy for establishing criteria for risk acceptability"*, framed
  by regulations, standards, the state of the art, and stakeholder concerns. Acceptability
  is a company-level decision, not each engineer improvising.
- **Competent people** (14971 §4.3) — those doing the work must be competent by education,
  training, skills and experience, with records kept. A risk analysis is only as
  trustworthy as the people making the judgements.

### 3.1 Risk analysis — find the hazards, size the risks (14971 §5)

1. **Intended use & reasonably foreseeable misuse** (§5.2) — document what the device is
   for *and* how it will predictably be mis-used. → *Template:* the intended purpose lives
   in [ADR-0001](../adr/0001-mdsw-qualification.md); the harm-risk form's *sequence of
   events* field captures foreseeable misuse.
2. **Characteristics related to safety** (§5.3) — list every device property that could
   affect safety, to make sure no hazard-source is overlooked.
3. **Identify hazards and hazardous situations** (§5.4) — list known and foreseeable
   hazards in *both normal and fault conditions*, then work out the event chains that turn
   each into a hazardous situation. → *Template:* the four required fields of the
   [harm-risk form](../../.github/ISSUE_TEMPLATE/harm-risk.yml) are exactly this chain;
   `hazard-cat:*` labels categorise it. **Guidance (ISO/TR 24971):** *Annex A* is a
   question checklist to surface characteristics related to safety, and *Annex B* lists
   analysis techniques (PHA, FTA, FMEA, HAZOP, HACCP) — you often need more than one
   (TR 24971 Annex A, Annex B).
4. **Risk estimation** (§5.5) — for each hazardous situation, estimate **probability** and
   **severity** (qualitatively or quantitatively). If you genuinely cannot estimate a
   probability, list the possible consequences instead. The categorisation *system* you use
   must be recorded. → *Template:* the form's S and P dropdowns; [`../HARM_RISK.md`](../HARM_RISK.md) §3.

   **Guidance you will need (ISO/TR 24971 §5.5.2):** probability of harm *P* can be split
   into **P1 × P2** — *P1* = probability that the **hazardous situation** occurs (someone
   gets exposed), *P2* = probability that it then **leads to harm**. This split *"is not
   mandatory"* — it is a helpful option. And when a probability truly cannot be estimated,
   a **conservative approach** is *"setting the unknown probability equal to 1"*. For
   **software**, failure probability is the classic un-estimable case (TR 24971 §5.5.3), so
   the usual move is P1 = 1 (worst case) and let severity and P2 carry the evaluation — the
   convention the template's method documents.

### 3.2 Risk evaluation — the go/no-go gate (14971 §6)

For each hazardous situation you **compare the estimated risk against the acceptability
criteria from your plan** and decide: acceptable or not (14971 §6). If acceptable, you may
skip the reduction steps and treat the estimate as residual risk; if not, you must do risk
control. Because the criteria were fixed earlier, this is an honest yes/no test, not a
negotiation.

**Does the standard give you the scale or the matrix?** No — and this surprises beginners.
ISO 14971 requires you to establish *objective* criteria for risk acceptability but
deliberately does **not** specify what risk level counts as acceptable (14971 §1); the
criteria come from *your* documented policy (§4.2) and plan (§4.4). ISO/TR 24971 *shows* example 3×3 and 5×5 risk
matrices but stresses *"this does not imply that this method has general applicability to
all medical devices"* (TR 24971 §5.5.1) — you choose the levels, define each one, and
justify the matrix for your device. → *That* is why the template's matrix says
*"example — adopt consciously"* and its plan asks who ratified it.

### 3.3 Risk control — reduce, in a mandatory order (14971 §7)

This is one of the most important teaching points. To reduce an unacceptable risk you must
try control options in a **fixed priority order** — not whichever is cheapest (14971 §7.1):

1. **(a) Inherently safe design and manufacture** — engineer the hazard *out* (e.g. make a
   wrong-patient display impossible by construction).
2. **(b) Protective measures** in the device or manufacturing process — guards, checks,
   confirmations, alarms — for risks you could not design out.
3. **(c) Information for safety** — warnings, instructions, and, where appropriate, user
   training. The **weakest** control, because it depends on people reading and obeying it;
   never the first resort.

The order exists because safe design protects everyone automatically, whereas a warning
label does not. → *Template:* the harm-risk form makes you *"state the hierarchy tier per
measure"*; [`../HARM_RISK.md`](../HARM_RISK.md) §5 restates the order as mandatory.

Then, for each control (14971 §7.2), you must **verify two separate things**:
*"Implementation of each risk control measure shall be verified"* **and** its
*effectiveness* — a control can exist yet not work, so both are required. → *Template:* the
board's `Control verification` field (`None → Implemented → Verified effective`) and the
form's verification-plan field.

The rest of §7 closes the loop:

- **Residual risk after control** (§7.3) — re-check what's left against the same criteria;
  if still unacceptable, loop back for more control.
- **Benefit-risk analysis** (§7.4) — if a residual risk stays unacceptable and no further
  control is practicable, you *may* gather data to judge whether the *"benefits of the
  intended use outweigh this residual risk"*. This is the **only** route by which an
  otherwise-unacceptable risk can be justified — by evidenced benefit, not assertion. →
  *Template:* the form's benefit-risk field.
- **Risks arising from the controls** (§7.5) — every fix can create *new* hazards (an alarm
  causes alarm-fatigue; a re-fetch adds a race window). You must review for *"whether new
  hazards or hazardous situations are introduced"* and manage them through the process
  again. → *Template:* a **required** §7.5 field on the harm-risk form ("none identified,
  with a rationale, is a valid answer").
- **Completeness of risk control** (§7.6) — confirm risks from *all* identified hazardous
  situations were considered and *all* control activities finished. → *Template:* the
  §7.6 completeness checkbox.

### 3.4 Overall residual risk, and telling users (14971 §8)

Individual risks can each be acceptable yet **add up** to too much. So after all controls
are implemented and verified, you evaluate the **overall residual risk** of the whole
device against its benefits, using the method and criteria from the plan (14971 §8). If it
is acceptable, you must **disclose** the significant residual risks to users — *"include
the necessary information in the accompanying documentation"* (the instructions for use) —
so they can decide informed. → *Template:* the overall review lives in
[`../HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md); the `disclose-in-ifu` label marks
controls whose warning must reach the user documentation.

### 3.5 Review and report — the gate before market (14971 §9)

Before commercial release, a responsible person **reviews that the plan was executed**:
the plan was implemented, the overall residual risk is acceptable, and methods are in place
to collect production/post-production information. The result is kept as the **risk
management report** in the file (14971 §9). → *Template:*
[`../HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md) encodes exactly those three conclusions
plus a sign-off; the release workflows attach the report evidence and register snapshots.

### 3.6 After launch — keep watching (14971 §10)

Risk management does not end at release. The manufacturer must *"actively collect and
review information"* from production, users, installers, the supply chain, public sources
and the evolving state of the art (§10.1–§10.2), review it for safety relevance — new
hazards? a risk no longer acceptable? state of the art moved on? (§10.3) — and take defined
**actions** when it is (§10.4), feeding back into leadership's process review. "Actively"
is the key word: you go looking, you do not just wait for complaints. → *Template:* the
[field-feedback form](../../.github/ISSUE_TEMPLATE/field-feedback.yml) (§10 intake), the
SOUP-anomaly form, and the CVE→register automation are this loop; example repo issues
[#4](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/4)
and
[#5](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/5)
demonstrate the two intake forms.

---

## 4. The wider picture: software, usability, security

ISO 14971 is the *method*, but a health-software product touches four neighbouring
standards a beginner should recognise.

**IEC 62304 — the software life cycle.** Software rarely injures anyone *directly*, so this
standard makes you trace *how* a software fault could lead to harm and prove you controlled
it. Its risk process is explicitly *"embedded in the device risk management process
according to ISO 14971"* (62304 §4.2/§7) — it plugs in, it does not replace. Two things a
novice must know:

- **Software safety classes A / B / C** (62304 §4.3, as revised by AMD1:2015) are
  **risk-based**. You assume a software failure *does* happen (probability = 1) and look
  only at risk controls *outside* the software. **Class A is not simply "no injury
  possible"** — a system that *could* contribute to harm is still Class A if external
  measures keep the risk acceptable; **B** = possible non-serious injury; **C** = possible
  death or serious injury. The class then decides how much of the standard you must do. →
  *Template:* [ADR-0002](../adr/0002-software-safety-classification.md) records this class;
  [`../standards/IEC-62304-COVERAGE.md`](../standards/IEC-62304-COVERAGE.md) maps which
  clauses apply.
- **SOUP** ("software of unknown provenance", 62304 §3.29) — reused third-party code you
  did not develop under the standard. You must **identify** it with a unique version
  designator (§8.1.2), state the **functional/performance requirements you rely on** it for
  (§5.3.3), and **evaluate the supplier's published anomaly (bug) lists** for your exact
  version (§7.1.3). → *Template:* [`../soup.yaml`](../../soup.yaml) + [`../SOUP.md`](../SOUP.md)
  + the SOUP-anomaly form.

**IEC 62366-1 — usability engineering.** Many devices fail not because hardware breaks but
because a user mis-operates them — a **use error**: *"unacceptable risk can arise from use
error"* (62366-1). The standard runs a process to find and reduce use errors, distinguishing
**formative** evaluation (*"during design … to explore … strengths, weaknesses, and
unanticipated use errors"*, 62366-1 §3.7 — rehearsal, iterative) from **summative**
evaluation (at the end, *"to obtain objective evidence"* the interface can be used
**safely**, §3.13 — the validation). → *Template:* the `hazard-cat:usability` category and
the effectiveness verification that may rely on a usability evaluation.

**IEC 82304-1 — product-level safety of standalone health software.** It sets whole-product
safety+security requirements for software that runs on general computing platforms *without
dedicated hardware*, and it does not re-invent anything: for the life cycle it points to
**IEC 62304**, and through it to **ISO 14971** for risk management (82304-1 Clause 2 & §5).

**IEC 81001-5-1 — security across the life cycle.** The security counterpart to the
development process: it *"defines the life cycle requirements for development and
maintenance of health software"* for **security**, is *"arranged in the ordering of IEC
62304"* so it plugs into your existing steps, and mandates handling third-party/SOUP
components and **vulnerability management** that continues after release (81001-5-1 §1,
§0.1, §9). → *Template:* [`../SECURITY_RISK.md`](../SECURITY_RISK.md) (security-risk method)
and [`../../SECURITY.md`](../../SECURITY.md) (vulnerability disclosure).

**ISO 81001-1 — the foundation.** It names the **three "key properties"** that must be
managed *together* for health software: **safety, effectiveness and security** (81001-1
§3.2.8), and stresses they are **interdependent** — locking down one can help or hurt
another, so they are balanced, not optimised alone. This is the shared language beneath the
others.

---

## 5. MDR specifically — the law behind the method

Everything above is *how* to manage risk. In the EU, *why you must* comes from the
**Medical Device Regulation, Regulation (EU) 2017/745 (MDR)** — the **law**. Its **Annex I,
"General Safety and Performance Requirements" (GSPRs)** is where risk management is
mandated. ISO 14971 is the recognised method that satisfies it. The key GSPRs (Annex I,
Chapter I):

- **GSPR 1** — the top-level promise: devices must be *"safe and effective"* and not
  compromise patients' clinical condition or safety, *provided any risks are acceptable
  when weighed against the benefits* and compatible with a high level of protection, taking
  the state of the art into account. Every other requirement serves this benefit-risk
  promise.
- **GSPR 2 — "reduce risks as far as possible" (AFAP).** The MDR requires reducing risks
  *as far as possible* — and clarifies this means *without adversely affecting the
  benefit-risk ratio*. In plain terms: **not zero risk, and not "as low as economically
  convenient" either**, but the lowest risk reachable while keeping the clinical benefit.
  This is exactly why ISO 14971's benefit-risk step exists.
- **GSPR 3** — a **risk-management system and plan** are mandatory: manufacturers must
  *"establish, implement, document and maintain a risk management system"* as a continuous,
  iterative process across the whole life cycle. This is the legal mandate behind ISO 14971
  §4.
- **GSPR 4 — the same priority order, in law.** Control measures must follow, *"in the
  following order of priority"*: (a) eliminate/reduce risks through safe design and
  manufacture; (b) protective measures, including alarms if needed; (c) information for
  safety and, where appropriate, training. It is the legal twin of ISO 14971 §7.1.
- **GSPR 8** — residual risks and side-effects must be *"minimised and be acceptable when
  weighed against the evaluated benefits"*, and the remaining residual risks **disclosed**
  to users. This is the legal basis for ISO 14971 §8.
- **GSPR 17** — software is explicitly covered: devices that incorporate *"electronic
  programmable systems, including software"*, and software that is itself a device, must be
  developed per the state of the art including *development life cycle, risk management …
  and verification and validation* — tying software risk management to IEC 62304.

**How law meets standard: the "harmonised standard" bridge.** The MDR states the goals
(GSPRs) but not the method. A **harmonised standard** is one the European Commission has
cited in the Official Journal; applying it gives a legal **"presumption of conformity"** —
regulators presume the covered requirements are met. **EN ISO 14971:2019+A11:2021** was
cited for the MDR/IVDR by Commission Implementing Decision (EU) 2022/757 (2022); the **A11
amendment adds the "Annex Z" tables** mapping the standard's clauses to the MDR's GSPRs. So
*applying EN ISO 14971 is the recognised route to satisfy the MDR's risk-management
requirements.* (Note: the plain **ISO** edition contains **no Annex ZA** — that EU mapping
lives only in the **EN** version.)

→ *Template:* [`../standards/CONFORMANCE.md`](../standards/CONFORMANCE.md) is the tiered
standards/regulation index; [`../standards/GSPR-CHECKLIST.md`](../standards/GSPR-CHECKLIST.md)
maps the software-relevant GSPRs to repo evidence;
[ADR-0001](../adr/0001-mdsw-qualification.md) is the living "are we even a medical device?"
decision that decides whether all of this becomes binding.

---

## 6. How the template maps to the process

A single table you can keep next to you. Each ISO 14971 (or neighbour-standard) step → the
concrete template artifact that operationalises it → where to see it live.

| Process step (clause) | Template artifact | Live in the example repo |
|---|---|---|
| Risk-management plan (14971 §4.4) | [`HARM_RISK.md`](../HARM_RISK.md) §1 plan table | `docs/HARM_RISK.md` |
| Acceptability policy & criteria (§4.2, §6) | the §4 matrix ("adopt consciously") + plan policy row | — |
| Intended use / misuse (§5.2) | [ADR-0001](../adr/0001-mdsw-qualification.md); harm-risk *sequence* field | issue #2 |
| Hazard → situation → harm chain (§5.4) | harm-risk form's four chain fields; `hazard-cat:*` labels | [issue #2](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/2) |
| Risk estimation, P1×P2 (§5.5; TR 24971 §5.5.2) | S / P / P1×P2 form fields; `HARM_RISK.md` §3 | issue #2 |
| Risk control hierarchy (§7.1) | "state the tier per measure" field; `HARM_RISK.md` §5 | issue #2 |
| Two verifications (§7.2) | `Control verification` board field; verification-plan field | Harm Risk File board |
| Benefit-risk (§7.4) | benefit-risk form field | — |
| New risks from controls (§7.5) | required §7.5 form field | issue #2 |
| Completeness (§7.6) | §7.6 completeness checkbox | — |
| Overall residual + disclosure (§8) | [`HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md); `disclose-in-ifu` label | — |
| Review & report (§9) | [`HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md) | — |
| Production/post-production (§10) | field-feedback + SOUP-anomaly forms; CVE→register | [#4](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/4), [#5](https://github.com/forschungsgruppe-digital-health/risk-management-template-example/issues/5) |
| Software safety class (62304 §4.3) | [ADR-0002](../adr/0002-software-safety-classification.md) | `docs/adr/0002…` |
| SOUP (62304 §8.1.2/§5.3.3/§7.1.3) | [`soup.yaml`](../../soup.yaml) + [`SOUP.md`](../SOUP.md) + SOUP-anomaly form | issue #4 |
| Security life cycle (81001-5-1) | [`SECURITY_RISK.md`](../SECURITY_RISK.md) + [`SECURITY.md`](../../SECURITY.md) | — |
| MDR GSPRs / harmonised standard | [`CONFORMANCE.md`](../standards/CONFORMANCE.md) + [`GSPR-CHECKLIST.md`](../standards/GSPR-CHECKLIST.md) | `docs/standards/` |

For the *situations* ("a CVE arrived", "a release is coming", "a pilot user reported
something"), the step-by-step companion is [`../RECIPES.md`](../RECIPES.md).

---

## 7. Common beginner misunderstandings

- **"Safe means zero risk."** No — safety is *"freedom from unacceptable risk"* (14971
  §3.26). Some residual risk always remains and must be accepted deliberately.
- **"A high-severity finding is automatically high risk."** No — risk is severity **and**
  probability together (14971 §3.18). A catastrophic but truly remote harm and a mild but
  frequent one are different risks (though a good method still treats catastrophic harm
  conservatively).
- **"A hazard is a harm."** No — a hazard is only *potential*; it becomes harm only through
  a hazardous situation (14971 §3.4–§3.5).
- **"Pick the cheapest control."** No — the priority order is **mandatory**: safe design →
  protective measures → information for safety (14971 §7.1; MDR GSPR 4).
- **"The PR is merged, so the control is verified."** That is only *implementation* — you
  also owe *effectiveness* (14971 §7.2).
- **"Each risk is acceptable, so we're fine."** Not necessarily — the **overall** residual
  risk is its own separate judgement (14971 §8).
- **"AFAP means as low as we can afford."** No — *as far as possible without adversely
  affecting the benefit-risk ratio* (MDR, Annex I, GSPR 2); cost alone is not a valid justification.
- **"The standard will give me the risk matrix."** It will not — you set the criteria
  (14971 §1, §4.2, §4.4); TR 24971's matrices are *examples* to justify per device
  (TR 24971 §5.5.1).
- **"Class A software means no injury is possible."** No — Class A can include software that
  *could* contribute to harm if external measures keep the risk acceptable (62304 §4.3).

---

## 8. Glossary

**Glossary** (all ISO 14971:2019 Clause 3 unless noted): *harm* §3.3 · *hazard* §3.4 ·
*hazardous situation* §3.5 · *risk* §3.18 · *severity* §3.27 · *residual risk* §3.17 ·
*safety* §3.26 · *risk analysis* §3.19 · *risk evaluation* §3.23 · *risk assessment*
(analysis + evaluation) §3.20 · *risk control* §3.21 · *risk management* §3.24 · *risk
management file* §3.25 · *benefit* §3.2 · *intended use* §3.6 · *reasonably foreseeable
misuse* §3.15 · *state of the art* §3.28 · *SOUP* (62304 §3.29) · *use error* (62366-1
§3.21) · *software safety class* (62304 §4.3) · *key properties: safety/effectiveness/
security* (81001-1 §3.2.8) · *GSPR* — General Safety and Performance Requirements (MDR
Annex I) · *AFAP* — as far as possible (MDR, Annex I, GSPR 2) · *harmonised standard / presumption of
conformity* (MDR + OJEU).

---

## 9. Citation style & references

**How sources are cited.** In-text citations use a **short tag + clause**, e.g. *(14971
§7.1)* = ISO 14971:2019, Clause 7.1; *(24971 §5.5.2)* = ISO/TR 24971:2020, Clause 5.5.2;
*(MDR, Annex I, GSPR 4)* = Regulation (EU) 2017/745, Annex I, requirement 4. A parenthetical
without a clause (e.g. *(62366-1)*) is a general reference to that standard. Tags → sources:

| Tag | Source |
|---|---|
| 14971 | [1] ISO 14971:2019 |
| 24971 | [2] ISO/TR 24971:2020 |
| 62304 | [3] IEC 62304:2006 + AMD1:2015 |
| 62366-1 | [4] IEC 62366-1:2015 (+A1:2020) |
| 82304-1 | [5] IEC 82304-1:2016 |
| 81001-5-1 | [6] IEC 81001-5-1:2021 |
| 81001-1 | [7] ISO 81001-1:2021 |
| MDR | [9] Regulation (EU) 2017/745 |

**Verification.** Every clause citation and every bibliographic entry below was checked
against the **primary source** — the standard PDFs' own cover pages and clause text. The
MDR (EU law) was verified against public full-text renderings of Regulation (EU) 2017/745
because EUR-Lex blocked automated retrieval; **confirm MDR wording against the
[Official Journal / EUR-Lex](https://eur-lex.europa.eu/eli/reg/2017/745/oj)**.

### References

1. **ISO 14971:2019(E)**, *Medical devices — Application of risk management to medical
   devices*. Third edition, 2019-12. International Organization for Standardization (ISO),
   Geneva. Prepared by ISO/TC 210 with IEC/SC 62A; cancels and replaces ISO 14971:2007. EU
   harmonised form: **EN ISO 14971:2019+A11:2021** (adds the Annex ZA/ZB mapping to the
   MDR / IVDR).
2. **ISO/TR 24971:2020(E)**, *Medical devices — Guidance on the application of ISO 14971*.
   Second edition, 2020-06 (Technical Report). ISO, Geneva.
3. **IEC 62304:2006**, *Medical device software — Software life cycle processes*. First
   edition, 2006-05. International Electrotechnical Commission (IEC), Geneva; consolidated
   with **IEC 62304:2006/AMD1:2015** (Amendment 1, 2015-06) as Edition 1.1.
4. **IEC 62366-1:2015**, *Medical devices — Part 1: Application of usability engineering to
   medical devices*. Edition 1.0, 2015-02. IEC, Geneva (with Amendment 1:2020).
5. **IEC 82304-1:2016**, *Health software — Part 1: General requirements for product
   safety*. Edition 1.0, 2016-10. IEC, Geneva.
6. **IEC 81001-5-1:2021**, *Health software and health IT systems safety, effectiveness and
   security — Part 5-1: Security — Activities in the product life cycle*. Edition 1.0,
   2021-12. IEC, Geneva.
7. **ISO 81001-1:2021(E)**, *Health software and health IT systems safety, effectiveness
   and security — Part 1: Principles and concepts*. First edition, 2021-03. ISO, Geneva.
8. **ISO/IEC Guide 63:2019** — cited within [1] as the source of several ISO 14971
   definitions (e.g. *risk* §3.18, *safety* §3.26).
9. **Regulation (EU) 2017/745** of the European Parliament and of the Council on medical
   devices (**MDR**) — Annex I, *General Safety and Performance Requirements*. Authoritative
   text at [EUR-Lex (ELI reg/2017/745/oj)](https://eur-lex.europa.eu/eli/reg/2017/745/oj).
10. **Commission Implementing Decision (EU) 2022/757** (2022) — listed **EN ISO
    14971:2019+A11:2021** among the harmonised standards for the MDR, conferring a
    presumption of conformity. Verify at EUR-Lex.

**Obtain the standards** (they are copyrighted; this primer is not a substitute): ISO/IEC
standards via the official catalogues (iso.org, webstore.iec.ch) or a national body (DIN,
BSI, ANSI, …); the MDR is free on EUR-Lex. For the EU risk-management route, obtain **EN ISO
14971:2019+A11:2021** and read **ISO/TR 24971:2020** alongside it for the how-to.

---

*Part of the [risk-management-template](https://github.com/forschungsgruppe-digital-health/risk-management-template).
Educational material — not legal, regulatory, or clinical advice. Grounded in the standard
editions in §9; each clause citation was verified against the primary source, so you can
check every statement yourself.*
