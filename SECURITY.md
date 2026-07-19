# Security policy — coordinated vulnerability disclosure

> **Template stub — fill per project before publishing.** A published CVD policy is the
> vulnerability-handling entry point the CRA (Annex I Part II) expects for products with
> digital elements (reporting obligations from **2026-09-11**, see
> [CONFORMANCE.md §5](docs/standards/CONFORMANCE.md)) and an
> [OpenSSF Scorecard](https://securityscorecards.dev) check. Method:
> [`docs/SECURITY_RISK.md`](docs/SECURITY_RISK.md).

## Reporting a vulnerability

- **Contact:** <security@your-org.example — a monitored mailbox or GitHub private
  vulnerability reporting (Settings → Code security → Private vulnerability reporting)>
- Please include: affected version/commit, reproduction steps, impact assessment; do
  **not** open a public issue for an unpatched vulnerability.
- **Acknowledgement target:** <e.g. 3 business days>. **Assessment + fix-or-mitigation
  target:** <e.g. 90 days, faster for patient-safety-relevant findings — those are
  triaged into the [harm-risk register](docs/HARM_RISK.md) immediately>.

## Scope & supported versions

| Version / branch | Supported |
|---|---|
| <main / latest release> | ✅ |
| <older releases> | ❌ |

## Disclosure

We follow coordinated disclosure: we ask reporters to give us the window above before
publication; we credit reporters (opt-in) in the release notes. Vulnerabilities in
third-party components are additionally recorded against the [SOUP
inventory](docs/SOUP.md) and, where patient safety could be affected, evaluated in the
harm-risk register.
