---
name: apply-risk-management
description: >
  Apply the risk-management template (delivery-risk register, optional MDR/62304
  conformance layer, arc42 architecture docs) to an EXISTING repository — additively and
  idempotently, with a proposed diff before any mutation. Use when a repo that was not
  created from the template should adopt its risk management.
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
  `conformance` (MDR/62304 readiness), `architecture` (arc42 v9, §11 risk-wired)
- `PROJECT_OWNER`: org/user that owns the Projects v2 boards

## Procedure

1. **Inventory the target** (read-only): existing `risk*`/`harm-risk*` labels, issue
   templates, PR template, CODEOWNERS, `docs/adr/` numbering, architecture docs, CI
   workflows named `risk-automation.yml`/`sbom.yml`, boards titled "Risk Register" /
   "Harm Risk File" (`gh project list --owner`). Report what exists.
2. **Clone the template** shallow to a temp dir; read `docs/APPLY_TO_EXISTING_REPO.md`
   (file manifest per layer + collision rules — that file is canonical, do not restate
   it from memory).
3. **Propose the diff**: files to copy verbatim, files to merge (PR template →
   append the *Traceability* + *Conformance gate* sections; CODEOWNERS → append
   entries; existing ADR dir → qualification ADR under the next free number, links
   fixed), files skipped (exist already), scripts to run, manual follow-ups. **Wait for
   approval.**
4. **Apply** with `cp -n` semantics (or Write only where the file is absent), run the
   idempotent scripts (`setup-labels.sh` for both label sets, the two board scripts),
   and print the manual view recipes the scripts emit.
5. **Never** create or modify CI workflows if same-named ones exist — instead present
   the Phase-E3 wiring instructions from `docs/CONFORMANCE_EXTENSION_PROMPT.md` as a
   proposed diff for human review.
6. **Verify** with the checklist at the end of `docs/APPLY_TO_EXISTING_REPO.md`; report
   created vs skipped vs merged, and the open manual steps (fill ADR-0001 with the
   product's real qualification answer + date; HARM_RISK §1 plan table; replace the
   `soup.yaml` example; set CODEOWNERS owners; set `RISK_PROJECT_URL`).

## Hard rules

- Additive + idempotent; re-running must be safe and produce "skip" lines, not changes.
- No mutation before the approval in step 3; workflows follow the stricter rule in
  step 5 even after approval.
- Keep the delivery-risk and harm-risk registers distinct (separate labels, forms,
  boards).
- If `gh` lacks a scope (e.g. `project`), stop and name the exact grant needed
  (`gh auth refresh -s project`).
