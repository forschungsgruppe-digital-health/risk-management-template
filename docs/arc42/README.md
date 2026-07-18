# Architecture documentation (arc42 v9.0)

Risk mitigation lives in **code and documentation**: design decisions, cross-cutting
concepts, and quality scenarios are how architectural risks actually get reduced — and
they need a place to be written down. This directory is that place: the
[arc42](https://arc42.org) template (v9.0-EN, July 2025), split into one file per section,
pre-wired to the [risk register](../RISK_MANAGEMENT.md).

## Files

| Section | File | Risk-register touchpoint |
|---|---|---|
| 1. Introduction and Goals | [01_introduction_and_goals.md](01_introduction_and_goals.md) | quality goals a risk may threaten |
| 2. Architecture Constraints | [02_architecture_constraints.md](02_architecture_constraints.md) | constraints are frequent risk *causes* |
| 3. Context and Scope | [03_context_and_scope.md](03_context_and_scope.md) | external interfaces → `risk-cat:dependency` |
| 4. Solution Strategy | [04_solution_strategy.md](04_solution_strategy.md) | strategy choices as mitigations |
| 5. Building Block View | [05_building_block_view.md](05_building_block_view.md) | — |
| 6. Runtime View | [06_runtime_view.md](06_runtime_view.md) | error/exception scenarios |
| 7. Deployment View | [07_deployment_view.md](07_deployment_view.md) | infra/operations risks |
| 8. Cross-cutting Concepts | [08_concepts.md](08_concepts.md) | security/safety concepts as mitigations |
| 9. Architecture Decisions | [09_architecture_decisions.md](09_architecture_decisions.md) | ADRs back-link the risk they mitigate |
| 10. Quality Requirements | [10_quality_requirements.md](10_quality_requirements.md) | scenarios that pin mitigations down |
| **11. Risks and Technical Debts** | [**11_technical_risks.md**](11_technical_risks.md) | **the hook: architecture-level view of the register** |
| 12. Glossary | [12_glossary.md](12_glossary.md) | — |

**How the linkage works** (two directions, no duplication):

- **Register → architecture:** a `risk` issue whose mitigation is architectural links the
  ADR/section that implements it; [§11](11_technical_risks.md) lists these risks with
  their issue numbers.
- **Architecture → register:** §11 is the only section that *enumerates* risks, and it
  defers scoring/ownership/status entirely to the register. §9 decisions taken because of
  a risk cite the issue in their rationale.

Sections you don't need yet can stay skeletal — arc42 is meant to be filled
incrementally. Delete the `>` guidance quotes as you fill each section.

## Reference

[`arc42-reference/arc42-template-EN-withhelp.md`](arc42-reference/arc42-template-EN-withhelp.md)
is the **unmodified** official "with help" edition of the template — per-section
explanations of contents, motivation, and form. The guidance quote at the top of each
section file links straight into it.

## Attribution & license (arc42)

The arc42 template — original and this adaptation — is licensed under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

- **Source:** [arc42/arc42-template](https://github.com/arc42/arc42-template),
  Template Version **9.0-EN** (based upon the AsciiDoc version), July 2025.
- **Authors:** created, maintained and © by Dr. Peter Hruschka, Dr. Gernot Starke and
  contributors — see <https://arc42.org>.
- **Changes made** (this adaptation, files `01_…` – `12_…`): split the single-file EN
  "plain" Markdown distribution into one file per section using arc42's canonical section
  file names; added a short guidance quote with a link into the with-help edition at the
  top of each section; extended §11 with the risk-register integration described above.
  `arc42-reference/` is vendored unmodified.
- Per arc42's license note: the **content you write into** the template is yours — you
  are free to license your own architecture documentation however you choose; the
  template structure itself remains CC BY-SA 4.0.
