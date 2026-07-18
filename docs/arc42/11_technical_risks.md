# Risks and Technical Debts

> **arc42 §11.** Known technical risks and accumulated technical debt, ordered by
> priority, so that management and stakeholders can factor them in ("risk management is
> project management for grown-ups" — Tim Lister).
> Guidance: [reference](arc42-reference/arc42-template-EN-withhelp.md#risks-and-technical-debts).

## Risk register integration

This project tracks **all** risks operationally in the GitHub risk register — Issues
labelled `risk`, worked on the **Risk Register** board, scored and reviewed per
[`docs/RISK_MANAGEMENT.md`](../RISK_MANAGEMENT.md). This section does **not** duplicate
the register. It holds the **architecture-level view**:

- List here only the **architecturally significant** risks and technical debts — the ones
  whose mitigation is (or should be) a design decision, and the debt that constrains
  future architecture work.
- Every entry **links its register issue** (single source of truth for score, owner,
  status, review date).
- Every entry names its **architectural mitigation** and links the section that documents
  it: a decision in [§9](09_architecture_decisions.md), a strategy choice in
  [§4](04_solution_strategy.md), a concept in [§8](08_concepts.md), or a quality scenario
  guarding against regression in [§10](10_quality_requirements.md).
- Risks of **harm** (safety) live in the separate ISO 14971 register
  ([`docs/HARM_RISK.md`](../HARM_RISK.md), label `harm-risk`, board *Harm Risk File*);
  list them here only when their control is architectural, linking both the harm-risk
  issue and the controlling decision/concept.

| Risk / Technical debt | Register issue | Architectural mitigation | Documented in |
|---|---|---|---|
| *\<one-line description\>* | *#\<issue\>* | *\<decision / strategy / concept\>* | *\<§4 / §8 / §9 / §10 link\>* |

## Technical debt

*\<Debt without register relevance (local, low exposure) can be listed here directly —
promote it to a `risk` + `risk-cat:tech-debt` issue as soon as it might affect delivery,
quality, or security.\>*
