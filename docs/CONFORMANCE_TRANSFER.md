# Conformance transfer — handing the evidence to the future manufacturer

The strategy behind the conformance layer ([`standards/CONFORMANCE.md`](standards/CONFORMANCE.md),
[ADR-0001](adr/0001-mdsw-qualification.md)): the research project maintains the evidence
that is **cheap to keep live but near-impossible to reconstruct**, and the organization
that eventually places the product on the market — the **manufacturer** in the MDR/CRA
sense, TBD via the dissemination/exploitation plan — adopts it.

## What transfers (adoptable from this repo, with history)

- **Delivery-risk register** + method ([`RISK_MANAGEMENT.md`](RISK_MANAGEMENT.md)) —
  issues, board, decisions.
- **Harm-risk file** ([`HARM_RISK.md`](HARM_RISK.md)) — the 14971 chain per risk,
  controls with both verifications, residual-risk and benefit–risk records.
- **Design history**: ADRs ([`adr/`](adr/README.md)) and the arc42 architecture
  documentation ([`arc42/`](arc42/README.md)), risk-linked via
  [§11](arc42/11_technical_risks.md).
- **SOUP inventory** ([`SOUP.md`](SOUP.md), [`soup.yaml`](../soup.yaml)) and the
  **per-release SBOMs** (release assets from
  [`sbom.yml`](../.github/workflows/sbom.yml)).
- **Traceability** ([`TRACEABILITY.md`](TRACEABILITY.md)) — reconstructable from the
  project forge (issues + PRs, exported with the boards at transfer); matrix via the
  advisory script.
- **Qualification history** — every re-evaluation recorded in ADR-0001.
- **GSPR checklist** ([`standards/GSPR-CHECKLIST.md`](standards/GSPR-CHECKLIST.md)) — the
  software-side MDR Annex I evidence, pre-staged for the manufacturer's technical file.

## Provenance & IP hygiene (do this while contributions happen)

- **License:** the repo must carry a `LICENSE` before anything is published; the
  template deliberately ships none (per-project decision). Verify compatibility of all
  SOUP licenses (`soup.yaml` license column, SBOM) with the chosen outbound license.
- **Contribution provenance:** enable **DCO sign-off** (`git commit -s` + the DCO check)
  so every contribution carries a certified origin — lightweight and sufficient for
  most research consortia. A **CLA** gives the future manufacturer broader relicensing
  rights but adds contributor friction and needs a legal entity to receive it — decide
  consciously; retrofitting either onto old commits is painful to impossible.
- Keep author/affiliation metadata honest (no shared accounts), so the chain of title
  stays reconstructable.

## What does NOT transfer — manufacturer-side obligations

Deliberately **not** maintained here (organizational, not repo artifacts):

- **ISO 13485:2016** quality management system (incl. EN A11:2021 mapping)
- The **person responsible for regulatory compliance** (MDR Art. 15 / "PRRC") — an
  organizational role a research project cannot pre-provision
- Notified-body engagement, **CE marking**, declaration of conformity, and the **UDI
  registration act** (Basic UDI-DI in EUDAMED). *Design-side* UDI/labelling (the UDI
  carrier, electronic-IFU content per ISO 20417 / EN ISO 15223-1) is prepared *with* the
  product — see the labelling rows in [`standards/CONFORMANCE.md`](standards/CONFORMANCE.md)
  §4 — only the *registration* is manufacturer-side.
- **Clinical evaluation** execution per MDR Art. 61 / MDCG 2020-1 (the repo carries the
  inputs: intended purpose, risk file, verification evidence)
- **Summative usability validation** per IEC 62366-1 (formative notes may live here)
- Post-market surveillance & vigilance (MDR Art. 83–92) — though §10-feed mechanics
  (detectors → registers) prototype the inputs

## Handover checklist (run at transfer)

1. Freeze + export both boards (Projects v2) alongside the issue export; the issues
   themselves move with the repo.
2. Verify `soup.yaml` matches the last release's SBOM; close the gap or document it.
3. Re-run the traceability matrix; attach it to the handover record.
4. Walk ADR-0001 with the manufacturer's regulatory function — the qualification
   decision and its trigger history are the entry point to everything else.
5. Agree which `watch`-tier obligations ([CONFORMANCE.md §5](standards/CONFORMANCE.md#5-watch--eu-horizontal-product-law-applicability-window-approaching))
   fall due before their launch date: CRA (2027-12-11) if not MDR-covered, EHDS EHR
   obligations (2029-03-26) if applicable.
