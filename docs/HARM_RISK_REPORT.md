# Risk management report (ISO 14971:2019 §9) — <product>, release <version>

> **Template stub.** ISO 14971 §9 requires a review of the risk-management plan's
> *execution* **before release for commercial distribution**; the result is recorded and
> maintained as this report. One per release, or a living doc updated per release. While the
> product is **not** MDSW ([ADR-0001](adr/0001-mdsw-qualification.md)) keep it as a light
> living record; it becomes binding on the ADR-0001 flip. Method + registers:
> [`HARM_RISK.md`](HARM_RISK.md).

- **Product / scope:** <…>
- **Release / version reviewed:** <…>
- **Date:** <YYYY-MM-DD>
- **Reviewer(s) / acceptance authority:** <who; the risk-acceptability authority named in the RM plan, HARM_RISK.md §1>
- **Risk management file:** the harm-risk register (label `harm-risk`) + this repo

## §9 review conclusions (all three are required)

1. **The risk-management plan was implemented as planned.**
   <Evidence: every planned activity in [`HARM_RISK.md`](HARM_RISK.md) §1 executed; every
   open harm-risk in a defined lifecycle state; link the release's register export
   (`harm-risk-register-<tag>.json`, attached by
   [`register-export.yml`](../.github/workflows/register-export.yml)) or a board snapshot.>
   - Conclusion: <implemented / exceptions listed>

2. **The overall residual risk is acceptable** (14971 §8) — judged against the criteria in
   the risk-management plan, weighing the contribution of **all** residual risks *together*,
   not just each in isolation.
   <Evidence: the overall-residual-risk evaluation; any per-risk benefit–risk determinations
   (`harm-risk:residual-accepted`); disclosure of significant residual risks in the
   accompanying information / IFU.>
   - Conclusion: <acceptable / not acceptable>

3. **Methods are in place to collect and review production & post-production information**
   (14971 §10).
   <Evidence: the SOUP/CVE→register feed ([`SOUP.md`](SOUP.md)); the incident / user-feedback
   intake; the review cadence tied to the board's `Review date`.>
   - Conclusion: <in place / gaps>

## Overall benefit–risk statement

<For the device as a whole: do the medical benefits outweigh the overall residual risk?
Reference the individual §7.4 benefit–risk analyses. Required if any residual risk was
accepted above the plan's acceptability criteria.>

## Sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Risk-acceptability authority (per the RM plan) | <…> | released / held | <…> |

> Retained as part of the risk-management file; transfers to the future manufacturer
> ([`CONFORMANCE_TRANSFER.md`](CONFORMANCE_TRANSFER.md)).
