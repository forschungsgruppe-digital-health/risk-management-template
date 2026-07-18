# 0003 — Pin CI supply-chain actions; keep current with Dependabot

- **Status:** accepted
- **Date:** <YYYY-MM-DD>
- **Deciders:** <project lead>
- **Linked risks:** <supply-chain risk issue, if raised>

## Context and problem statement

The SBOM and CVE generators — `anchore/sbom-action` in
[`.github/workflows/sbom.yml`](../../.github/workflows/sbom.yml), and the `anchore/syft` +
`aquasec/trivy` images in [`.gitlab-ci.yml`](../../.gitlab-ci.yml) — produce conformance
*evidence* (the SBOM; the CVE-to-register bridge). A floating tag (`@v0`, `:latest`) makes
that evidence non-reproducible and pulls unreviewed third-party code on every run — at odds
with the repo's own SBOM/SOUP supply-chain thesis.

## Decision

1. **Pin** every third-party CI action/image to an explicit version (`actions/checkout` is
   SHA-pinned, matching [`template-sync-check.yml`](../../.github/workflows/template-sync-check.yml)).
2. **Keep them current with Dependabot** ([`.github/dependabot.yml`](../../.github/dependabot.yml),
   `github-actions` ecosystem, weekly) so the pins do not rot silently.

## Considered options

1. Floating tags — rejected: non-reproducible; unreviewed auto-upgrades.
2. Pin + manual bumps — rejected: pins rot; no one remembers.
3. **Pin + Dependabot** (chosen) — reproducible now, current over time, each bump a
   reviewable PR.

## Consequences

- Good: reproducible SBOM/scan generators; supply-chain upgrades arrive as reviewable PRs.
- **GitLab gap (accepted):** Dependabot does not read `.gitlab-ci.yml` image tags, so
  `anchore/syft` and `aquasec/trivy` there must be bumped by **Renovate** (or manually) on
  the GitLab side — keep the two platforms in parity (`docs/GITLAB.md`).
- Further hardening available later: SHA-pin the GitHub Actions (not just version tags), as
  already done for `actions/checkout`.
