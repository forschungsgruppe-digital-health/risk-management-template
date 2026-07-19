---
name: apply-risk-management
description: >
  Apply the risk-management template (delivery-risk register, optional MDR/62304
  conformance layer, arc42 architecture docs) to an EXISTING repository — additively and
  idempotently. Runs as a zero-mutation dry-run (`MODE = plan`, the default) that previews
  the full changeset via a throwaway scratch clone, or applies it (`MODE = apply`) behind a
  proposed-diff approval gate. Use when a repo that was not created from the template should
  adopt its risk management.
---

# apply-risk-management

You retrofit the **risk-management-template** onto an existing repository. You never
overwrite existing files, labels, boards, or workflows; collisions are skipped or merged
per the rules in `docs/APPLY_TO_EXISTING_REPO.md` of the template. Human-in-the-loop:
propose before you mutate.

## Inputs (ask if missing)

- `TARGET`: <owner/repo> of the existing repository (must have a local clone or `gh` access)
- `TEMPLATE`: <owner>/risk-management-template (source; clone shallow to a temp dir)
- `LAYERS`: any of `base` (delivery-risk register — always recommended),
  `conformance` (MDR/62304 readiness), `architecture` (arc42 v9.0, §11 risk-wired)
- `PROJECT_OWNER`: org/user that owns the Projects v2 boards
- `MODE`: `plan` (default) or `apply` — see **Modes** below. `plan` is a dry-run: it
  produces the full proposed changeset and a real scratch-clone preview but makes **zero**
  mutations to `TARGET` (no files, labels, boards, or workflows).

## Modes (dry-run by default)

Mirrors the `MODE` contract of [`docs/SETUP_PROMPT.md`](../../docs/SETUP_PROMPT.md) — one
concept, two entry points.

- **`plan` (default) — dry-run.** Run Procedure steps 1–3b only, then **STOP and end the
  turn**. Make **zero** mutations to `TARGET`: no `cp`, no `Write`, no `setup-*.sh`, no
  `gh`/`glab` writes. The deliverable is a review artifact: the inventory, the additive
  diff, the collision matrix, the exact scripts that *would* run, and the scratch-clone
  preview (step 3b). Re-running `plan` is always safe and side-effect-free.
- **`apply` — mutate, still gated.** Only after a `plan` has been reviewed (or the user
  explicitly sets `MODE = apply`) do you run steps 4–6, and even then step 3's approval
  gate and step 5's workflow rule still hold. `apply` is not blanket consent.

## Procedure

1. **Inventory the target** (read-only): existing `risk*`/`harm-risk*` labels, issue
   templates, PR template, CODEOWNERS, `docs/adr/` numbering, architecture docs, CI
   workflows named `risk-automation.yml`/`sbom.yml`/`register-export.yml`, boards titled
   "Risk Register" / "Harm Risk File" (`gh project list --owner`). Report what exists.
2. **Clone the template** shallow to a temp dir; read `docs/APPLY_TO_EXISTING_REPO.md`
   (file manifest per layer + collision rules — that file is canonical, do not restate
   it from memory).
3. **Propose the diff**: files to copy verbatim, files to merge (PR template →
   append the *Traceability* + *Conformance gate* sections; CODEOWNERS → append
   entries; existing ADR dir → the template's three ADRs under the next free numbers,
   links fixed), files skipped (exist already), scripts to run, manual follow-ups.
   **Wait for approval.**
3b. **High-fidelity preview (both modes, still read-only on `TARGET`).** Prove the plan
   instead of describing it: `git clone` (or `git worktree`) the target to a **throwaway**
   dir, apply the file layer there with `cp -n`, hand-merge PR-template/CODEOWNERS, and
   `git diff` so the user sees the *real* resulting tree — there is no server-side
   `--dry-run` for labels or boards. For the API layer, use read-only `gh label list` /
   `gh project list` (or the `glab` twins) to render a **would-create-vs-skip** table for
   every label and board the scripts touch. Discard the scratch dir afterwards. In `plan`
   mode this preview is the final deliverable — **STOP here and end the turn.**
4. **Apply** (`MODE = apply` only) with `cp -n` semantics (or Write only where the file is absent), run the
   idempotent scripts (`setup-labels.sh` for both label sets, the two board scripts),
   and print the manual view recipes the scripts emit.
5. **Never** create or modify CI workflows if same-named ones exist — instead present
   the Phase-E3 wiring instructions from `docs/CONFORMANCE_EXTENSION_PROMPT.md` as a
   proposed diff for human review.
6. **Verify** with the checklist at the end of `docs/APPLY_TO_EXISTING_REPO.md`; report
   created vs skipped vs merged, and the open manual steps (fill ADR-0001 with the
   product's real qualification answer + date; fill ADR-0002 with the software safety
   classification — or its "N/A while not MDSW" default; HARM_RISK §1 plan table; replace
   the `soup.yaml` example; set CODEOWNERS owners; set `RISK_PROJECT_URL`).

## Hard rules

- Additive + idempotent; re-running must be safe and produce "skip" lines, not changes.
- **`plan` (dry-run) is the default** when `MODE` is unstated — zero mutations to `TARGET`;
  the step-3b scratch clone is a throwaway, discarded and never pushed.
- No mutation before the approval in step 3; workflows follow the stricter rule in
  step 5 even after approval.
- Keep the delivery-risk and harm-risk registers distinct (separate labels, forms,
  boards).
- If `gh` lacks a scope (e.g. `project`), stop and name the exact grant needed
  (`gh auth refresh -s project`).
