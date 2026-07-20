# 0004 — Compile a single Risk Management File deliverable per release

- **Status:** accepted
- **Date:** <YYYY-MM-DD>
- **Deciders:** <project lead>
- **Linked risks:** <compliance / audit-readiness risk issue, if raised>

## Context and problem statement

This template keeps the risk-management records **distributed** across the repo on purpose —
the plan in [`HARM_RISK.md`](../HARM_RISK.md), the review in
[`HARM_RISK_REPORT.md`](../HARM_RISK_REPORT.md), the per-hazard chain in the `harm-risk`
issues, the software split in [`IEC-62304-COVERAGE.md`](../standards/IEC-62304-COVERAGE.md),
the GSPR rows in [`GSPR-CHECKLIST.md`](../standards/GSPR-CHECKLIST.md), the SOUP in
[`soup.yaml`](../../soup.yaml), the decisions in `docs/adr/` — so each stays a **single source
of truth**, versioned and diffable.

That is right for *maintaining* the file, but wrong for *handing it over*. An MDR/CE auditor,
or the future manufacturer's regulatory function, wants **one document** ordered by the
ISO 14971 process — not a scavenger hunt across a repository. ISO 14971:2019 §4.5 defines the
**Risk Management File** and §9 the **Risk Management Report**; both are expected as an
assemblable whole. Re-typing that document by hand each release would drift from the living
records immediately.

## Decision

Generate the hand-to-auditor document **mechanically** from the living records, per release.

1. A stdlib-only script — [`scripts/build-risk-management-file.py`](../../scripts/build-risk-management-file.py)
   — assembles ONE document ordered by the ISO 14971 process (§4.4 plan → §5–§7 per-hazard
   analysis/evaluation/control → §8 overall residual → §9 review → §10 post-production →
   annexes for IEC 62304 class + coverage, SOUP, GSPR, security, traceability, ADRs). It is a
   **compiled view**: narrative sections are transcluded verbatim from their source files and
   the register is rendered from the release's export — no content is re-authored, so it
   **cannot drift** from the sources.
2. **pandoc** converts the Markdown master to **PDF** (frozen sign-off copy) and **DOCX**
   (editable copy a quality-management system can ingest); HTML is also available.
3. A release-triggered workflow ([`.github/workflows/risk-management-file.yml`](../../.github/workflows/risk-management-file.yml),
   GitLab twin in [`.gitlab-ci.yml`](../../.gitlab-ci.yml)) runs the script on every published
   release, **attaches the PDF + DOCX to the release**, and opens a **PR archiving the Markdown
   master** under `docs/risk-management-file/`.

**Honesty contract (non-negotiable):** the generator fabricates nothing — unfilled
`<…>`/`[RA]` placeholders show through — and it asserts **no conformity**; applicability and
acceptance determinations remain `[NEEDS RA INPUT]`. The compiled file does not replace the
Notified Body or an ISO 13485 internal audit; it is the deliverable they read.

## Considered options

1. **Hand-written single RMF, updated per release** — rejected: drifts from the living records
   the moment either changes; duplicative; error-prone.
2. **No single document — auditor navigates the repo** — rejected: fails the "one file to hand
   over" need; high friction for an assessor; no frozen per-release snapshot.
3. **External document / quality-management system (DMS) authoring** — rejected as the *source*
   (it would fork the truth away from the repo) but supported as a *destination*: the DOCX is
   built precisely so a DMS can ingest it.
4. **Scripted compilation from the living records (chosen)** — single source of truth
   preserved; zero drift; reproducible; a versioned per-release artifact; pandoc gives the
   formats auditors expect.

## Consequences

- **Good:** a single, standards-ordered deliverable per release with zero maintenance and zero
  drift; PDF/DOCX are release assets (no git bloat), the Markdown master is archived in-repo
  (diffable). Transfers cleanly to the manufacturer ([`CONFORMANCE_TRANSFER.md`](../CONFORMANCE_TRANSFER.md)).
- **Placeholders are visible:** because nothing is fabricated, an unfilled repo produces a
  document full of `[NEEDS INPUT]` — which is *correct* (it shows the real state) and pairs with
  the [`mdr-audit-readiness`](../../skills/mdr-audit-readiness/SKILL.md) scorecard that measures
  the distance to auditable.
- **Toolchain:** pandoc + a LaTeX engine are needed for PDF; the CI installs them
  (GitHub: apt `texlive-xetex`; GitLab: the `pandoc/latex` image). Locally the script degrades
  to Markdown/DOCX/HTML if no PDF engine is present — it never fails the build over a missing
  format.
- **PDF glyphs:** a small set of symbols the default LaTeX font lacks (≥, ↔, ⇒, ⚠) is
  transliterated for the PDF input only; the Markdown/DOCX/HTML keep the original Unicode.
- **In-repo binaries:** the PDF is committed only if `RMF_COMMIT_PDF=true` (repo variable) —
  default keeps binaries as release assets to avoid git bloat.
- **Supersedes** the `HARM_RISK_REPORT.md` "board snapshot" evidence slot's manual assembly:
  that report is now one *section* of the compiled file, with the register rendered inline.
