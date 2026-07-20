# The compiled Risk Management File — one document for the auditor

This repo keeps its risk-management records **distributed** (each a single source of truth).
For a handover — to an **MDR/CE** (Medical Device Regulation / Conformité Européenne) auditor,
or to the future manufacturer's regulatory function — those records are **compiled into one
document** ordered by the **ISO** (International Organization for Standardization) **14971**
process. You do not maintain this document; you **generate** it. Rationale:
[ADR-0004](adr/0004-risk-management-file-deliverable.md).

## What it is (and is not)

- **Is:** a single-file **Risk Management File & Report** per **ISO 14971:2019 §4.5 / §9** — a
  *compiled view* of the living records (narrative sections transcluded verbatim; the `harm-risk`
  register rendered inline from the release export). It is the deliverable an auditor reads
  instead of navigating the repo.
- **Is not:** a claim of conformity. Unfilled `<…>` / `[RA]` (regulatory-affairs decision)
  placeholders **show through** — the generator fabricates nothing. It does **not** replace a
  **NB** (Notified Body) assessment or an **ISO 13485** (quality-management-system, QMS)
  internal audit. It pairs with the [`mdr-audit-readiness`](../skills/mdr-audit-readiness/SKILL.md)
  scorecard, which measures how far the file is from auditable.

## Structure (mapped to the standards)

| Section | Clause | Source (transcluded / rendered) |
|---|---|---|
| 0. Provenance & standards frame | — | generated (release, commit, editions, MDSW state) |
| 1. Risk management plan | §4.4 | `docs/HARM_RISK.md` §1 |
| 2. Intended use, foreseeable misuse & MDSW qualification | §5.2 + MDR qualification | `docs/adr/0001-mdsw-qualification.md` |
| 3. Risk acceptability criteria | §4.4(d)/§4.2 + MDR AFAP | `docs/HARM_RISK.md` §4 |
| 4. Risk analysis, evaluation & control — **per hazard** | §5, §6, §7 (traceable per §4.5) | the `harm-risk` register export (rendered as the 14971 chain) |
| 5. Overall residual risk & benefit–risk | §8 / §7.4 (MDR GSPR 8) | `docs/HARM_RISK_REPORT.md` |
| 6. Risk management review & report | §9 | `docs/HARM_RISK_REPORT.md` |
| 7. Production & post-production plan | §10 | `docs/HARM_RISK.md` §8 |
| Annex A | IEC 62304 §4.3 | `docs/adr/0002-…` (software safety class) |
| Annex B | IEC 62304 coverage | `docs/standards/IEC-62304-COVERAGE.md` |
| Annex C | IEC 62304 §8.1.2 | `soup.yaml` (**SOUP** — software of unknown provenance) + release SBOM |
| Annex D | MDR Annex I | `docs/standards/GSPR-CHECKLIST.md` (**GSPR** — general safety & performance requirements) |
| Annex E | IEC 81001-5-1 | `docs/SECURITY_RISK.md` (+ **CVD** — coordinated vulnerability disclosure) |
| Annex F | IEC 62366-1 | `docs/USABILITY.md` (use-related risk; summative deferred) |
| Annex G | §4.5 / IEC 62304 §5.1.1(c) | `docs/TRACEABILITY.md` |
| Annex H | editions | `docs/standards/CONFORMANCE.md` |
| Annex I | design history | `docs/adr/` index |
| Annex J | context | delivery-risk register (kept separate from safety) |
| Annex K | self-check | latest `mdr-audit-readiness` scorecard |

The per-hazard chain (§4) renders each `harm-risk` issue raised via the form as a table:
hazard → sequence → hazardous situation → harm → S/P → tiered control (§7.1) → new-risks (§7.5)
→ residual (§7.3) → the two verifications (§7.2) — the traceability §4.5 requires. A free-text
issue (not raised via the form) is included verbatim with a note.

## Generate it

```sh
# needs Python 3.8+; pandoc optional (PDF also needs a LaTeX engine, e.g. xelatex)
scripts/build-risk-management-file.py --repo . --tag v1.2.0 \
    --register harm-risk-register-v1.2.0.json \
    --delivery-register risk-register-v1.2.0.json \
    --out docs/risk-management-file --formats md,docx,pdf,html
```

- Without `--register`, pass `--owner-repo <owner>/<repo>` to fetch the registers live via
  `gh`, or omit both — the §4 section then points at the forge (the authoritative record).
- No pandoc → Markdown master only. No PDF engine → Markdown/DOCX/HTML (never fails over PDF).
- The Markdown master is always written; DOCX is the editable QMS copy; PDF is the frozen copy.

## Automate it (per release)

- **GitHub:** [`.github/workflows/risk-management-file.yml`](../.github/workflows/risk-management-file.yml)
  runs on every published release — exports the registers, compiles the file, **attaches the
  PDF + DOCX to the release**, and opens a **PR archiving the Markdown master** under
  `docs/risk-management-file/`. Manual runs via *workflow_dispatch*. Set the repo variable
  `RMF_COMMIT_PDF=true` to also commit the PDF into the repo (default: PDF stays a release
  asset to avoid git bloat).
- **GitLab:** the `risk-management-file` job in [`.gitlab-ci.yml`](../.gitlab-ci.yml) runs on
  tags, produces the same formats as CI artifacts (attach to a GitLab release via `release-cli`
  if you use them). Mapping: [`docs/GITLAB.md`](GITLAB.md).

Both are **inert until you cut a release**; delete the workflow/job to opt out.

## For the transfer

The compiled file per release is a first-class **conformance-transfer** artifact
([`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md)): each release's PDF is a frozen snapshot
of the risk-management state at that version, and the Markdown masters give the manufacturer a
diffable history of how the file evolved. Run [`mdr-audit-readiness`](../skills/mdr-audit-readiness/SKILL.md)
before a release so Annex J carries an honest self-assessment of the distance to auditable.
