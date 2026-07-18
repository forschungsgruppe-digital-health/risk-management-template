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
- **GitLab side:** Dependabot does not read `.gitlab-ci.yml` image tags, so a
  [`renovate.json`](../../renovate.json) (gitlabci manager; the github-actions manager is
  disabled to avoid overlap with Dependabot) keeps `anchore/syft` and `aquasec/trivy`
  current — inert until the Renovate app is enabled. Keep the two platforms in parity
  (`docs/GITLAB.md`).
- The GitHub Actions are **SHA-pinned** (not just version tags) — `actions/checkout` and
  `anchore/sbom-action`; Dependabot updates the pinned SHA together with the `# vX` comment.
