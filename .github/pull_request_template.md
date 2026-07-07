## What & why

<!-- one logical change; link context -->

## Traceability (docs/TRACEABILITY.md)

- Requirement / risk issues: Closes #
- Verifying tests: <!-- in this PR, or link -->

## Conformance gate (docs/adr/0001-mdsw-qualification.md)

- [ ] **Clinical-function triggers** — this change does **not** add clinical decision
      support, alerting on clinical values, risk scores / dosing, treatment-influencing
      pathway/care-plan logic, or AI/ML decision input.
- [ ] **Regulatory-scope triggers** — this change does **not** make the product become or
      embed an EHR system for priority-category data (EHDS), nor change its intended-purpose
      statement, target users, or claims.
      <!-- If ANY box can't be checked: raise a `risk` issue referencing ADR-0001 and link
           it here — the MDSW qualification (all seven triggers, ADR-0001) must be
           re-evaluated before merge. -->
- [ ] `soup.yaml` updated if runtime dependencies changed (docs/SOUP.md)
