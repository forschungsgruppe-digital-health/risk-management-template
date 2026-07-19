# SOUP inventory — software of unknown provenance

**SOUP** (IEC 62304 §3.29): software not developed for this product under a known
life-cycle process — in practice, every third-party/open-source component the product
*relies on at runtime*. IEC 62304 requires, per SOUP item: identification (title,
manufacturer/publisher, and the **unique SOUP designator** (version is the usual choice) — §8.1.2), the **functional and
performance requirements** the product relies on (§5.3.3), required hardware/software
(§5.3.4), and evaluation of **published anomaly lists** (§7.1.3).

This is the 62304 evidence that is **most costly to backfill** — hence kept live even
while the product is not qualified as MDSW ([ADR-0001](adr/0001-mdsw-qualification.md)).

## How this project keeps it

- **[`soup.yaml`](../soup.yaml)** (repo root) is the machine-readable inventory — one
  entry per SOUP component with the fields above plus known anomalies and their impact
  assessment.
- The **SBOM** ([`.github/workflows/sbom.yml`](../.github/workflows/sbom.yml)) covers
  the *full* dependency tree per release. Hand-written `soup.yaml` entries are required
  for **direct runtime components** (and anything a future class-B/C release depends
  on); low-risk transitive dependencies are covered by the SBOM + the automated
  vulnerability feed rather than hand-written entries.
- **Anomaly feed (security subset):** the risk-automation workflow cross-checks
  critical/high Dependabot alerts against `soup.yaml` — a hit gets the `soup-anomaly`
  label on the register issue and a prompt to update the entry's impact assessment; if
  patient safety could be affected, raise a linked [harm-risk issue](HARM_RISK.md). This
  covers only *security* advisories.
- **Published functional anomalies (§7.1.3, the rest):** the Dependabot sweep is not the
  whole §7.1.3 duty. At the regular risk review, and **on every SOUP version bump**, review
  each component's published anomaly / errata list at the upstream source (bug tracker,
  release notes — not just CVEs) and record the evaluation in the entry's `anomalies` —
  the structured record is the [SOUP-anomaly issue form](../.github/ISSUE_TEMPLATE/soup-anomaly.yml)
  (GitLab: `SOUP Anomaly.md`).
- **Change evaluation on version bump (§6 / §7.4):** when a SOUP version moves, re-run the
  anomaly check for the new version **and** re-confirm the relied-upon functional &
  performance requirements (§5.3.3) still hold *before* merge.
- Review the inventory at the regular risk review; before any release, confirm entries
  match the shipped versions (the SBOM is the cross-check).

## Entry template + example

See the schema comment and the marked example entry in [`soup.yaml`](../soup.yaml).
An anomaly's **impact assessment** answers: does the known bug/CVE affect the functions
this product relies on, and can it contribute to a hazardous situation? (If yes →
harm-risk issue, not just a note.)
