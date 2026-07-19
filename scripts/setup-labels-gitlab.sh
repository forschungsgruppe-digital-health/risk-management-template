#!/usr/bin/env bash
# GitLab twin of setup-labels.sh — creates the label set on a GitLab project,
# IDEMPOTENT and ADDITIVE (existing labels are skipped, never recolored/deleted).
#
# Reads the SAME JSON files as the GitHub script and maps the canonical flat names
# to GitLab SCOPED labels: the FIRST ':' becomes '::' (risk:open -> risk::open). This
# yields DISTINCT scopes per axis — lifecycle (risk::), severity (risk-sev::), category
# (risk-cat::), harm lifecycle (harm-risk::), hazard category (hazard-cat::) — so each
# axis is single-value without collapsing the others (severity uses its own risk-sev
# key precisely so a severity label does not evict the lifecycle label under one scope).
# On Premium/Ultimate GitLab ENFORCES one value per scope; on Free the labels are plain
# and the single-value rule stays a convention (docs/GITLAB.md § Labels).
# Names without ':' (risk, harm-risk, requirement, soup-anomaly, disclose-in-ifu) stay unchanged.
#
# Usage: scripts/setup-labels-gitlab.sh <group/project> [labels-file]
#   default labels-file: .github/risk-labels.json (delivery risks)
#   conformance layer:   scripts/setup-labels-gitlab.sh <group/project> .github/conformance-labels.json
# Needs: glab CLI authenticated against your instance (glab auth login --hostname <host>); jq.

set -euo pipefail

PROJECT="${1:?usage: setup-labels-gitlab.sh <group/project> [labels-file]}"
LABELS_FILE="${2:-"$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/.github/risk-labels.json"}"

command -v jq >/dev/null || { echo "jq is required" >&2; exit 1; }
command -v glab >/dev/null || { echo "glab is required (https://gitlab.com/gitlab-org/cli)" >&2; exit 1; }
[ -f "$LABELS_FILE" ] || { echo "labels file not found: $LABELS_FILE" >&2; exit 1; }

existing="$(glab label list --repo "$PROJECT" --per-page 200 -F json 2>/dev/null | jq -r '.[].name' || true)"

created=0; skipped=0
while IFS=$'\t' read -r name color description; do
  # canonical flat name -> GitLab scoped label (first ':' -> '::')
  scoped="$(printf '%s' "$name" | sed 's/:/::/')"
  if grep -Fxq "$scoped" <<<"$existing"; then
    echo "skip (exists): $scoped"
    skipped=$((skipped + 1))
  else
    glab label create --repo "$PROJECT" --name "$scoped" --color "#$color" --description "$description" >/dev/null
    echo "created:       $scoped"
    created=$((created + 1))
  fi
done < <(jq -r '.[] | [.name, .color, .description] | @tsv' "$LABELS_FILE")

echo "Done: $created created, $skipped skipped (already existed)."
echo "Note: docs use the canonical flat spelling (risk:open) — on GitLab that is the scoped risk::open."
