#!/usr/bin/env bash
# soup-sbom-diff.sh — advisory drift check between the hand-curated SOUP inventory
# (soup.yaml, IEC 62304 §8.1.2) and a generated SBOM (CycloneDX JSON, from sbom.yml).
#
# The mdr-audit-readiness run flagged soup.yaml-vs-SBOM drift as a real risk: the SBOM is the
# authoritative full-tree enumeration, so a soup.yaml entry that is NOT in the SBOM is stale or
# wrong, and a component in the SBOM not covered by soup.yaml may be an un-triaged SOUP.
#
# ADVISORY ONLY — always exits 0. Prints warnings for a human to triage (see docs/SOUP.md).
#
# Usage: scripts/soup-sbom-diff.sh [soup.yaml] [sbom.cdx.json]
#   Without the SBOM arg it looks for *.cdx.json / sbom-*.json in the working dir.
# Requires: jq. (soup.yaml names are read with grep/sed — no YAML parser needed.)

set -uo pipefail

SOUP="${1:-soup.yaml}"
SBOM="${2:-}"

warn() { printf '  ⚠ %s\n' "$1"; }
info() { printf '  · %s\n' "$1"; }

if [ ! -f "$SOUP" ]; then
  echo "soup-sbom-diff: no $SOUP — nothing to check (advisory)."; exit 0
fi
if ! command -v jq >/dev/null 2>&1; then
  echo "soup-sbom-diff: jq not found — install jq to run this check (advisory, skipped)."; exit 0
fi

# locate an SBOM if not given
if [ -z "$SBOM" ]; then
  for c in sbom-*.cdx.json *.cdx.json sbom-*.json; do
    [ -f "$c" ] && { SBOM="$c"; break; }
  done
fi
if [ -z "$SBOM" ] || [ ! -f "$SBOM" ]; then
  echo "soup-sbom-diff: no SBOM found (pass one, or run sbom.yml first) — advisory, skipped."
  echo "  soup.yaml components are listed below for reference:"
  sed -n 's/^[[:space:]]*-\{0,1\}[[:space:]]*name:[[:space:]]*\([^[:space:]#]\{1,\}\).*/  · \1/p' "$SOUP"
  exit 0
fi

echo "soup-sbom-diff: comparing $SOUP against $SBOM (advisory)"

# component names from soup.yaml (the only `name:` keys in the schema are component names)
soup_names=$(sed -n 's/^[[:space:]]*-\{0,1\}[[:space:]]*name:[[:space:]]*\([^[:space:]#]\{1,\}\).*/\1/p' "$SOUP" | sort -u)
# component names from the SBOM (CycloneDX: .components[].name)
sbom_names=$(jq -r '[.components[]?.name] | .[]' "$SBOM" 2>/dev/null | sort -u)

if [ -z "$sbom_names" ]; then
  echo "  (SBOM has no .components[].name — is it CycloneDX JSON? advisory, skipped)"; exit 0
fi

# 1) soup.yaml entry NOT in the SBOM -> stale / wrong / not actually shipped
missing_in_sbom=$(comm -23 <(echo "$soup_names") <(echo "$sbom_names"))
n_missing=$(printf '%s' "$missing_in_sbom" | grep -c . || true)
echo ""
echo "[1] SOUP entries not found in the SBOM ($n_missing) — stale/renamed/not shipped? (triage)"
if [ "$n_missing" -gt 0 ]; then
  while IFS= read -r n; do [ -n "$n" ] && warn "$n — in soup.yaml but not in the SBOM"; done <<< "$missing_in_sbom"
else
  info "none — every soup.yaml component appears in the SBOM"
fi

# 2) SBOM component NOT covered by soup.yaml -> candidate un-triaged SOUP (informational:
#    the SBOM includes transitive deps that need no hand entry; this is a candidate list only)
missing_in_soup=$(comm -13 <(echo "$soup_names") <(echo "$sbom_names"))
n_cand=$(printf '%s' "$missing_in_soup" | grep -c . || true)
echo ""
echo "[2] SBOM components not in soup.yaml ($n_cand) — candidates to triage (many are low-risk transitive; soup.yaml covers DIRECT runtime SOUP — docs/SOUP.md)"
if [ "$n_cand" -gt 0 ]; then
  printf '%s\n' "$missing_in_soup" | head -20 | while IFS= read -r n; do [ -n "$n" ] && info "$n"; done
  [ "$n_cand" -gt 20 ] && info "… and $((n_cand - 20)) more (showing first 20)"
fi

echo ""
echo "soup-sbom-diff: done (advisory — resolve real drift in soup.yaml; transitive-only gaps are covered by the SBOM + the anomaly feed)."
exit 0
