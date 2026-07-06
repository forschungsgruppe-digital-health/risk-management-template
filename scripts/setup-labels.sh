#!/usr/bin/env bash
# Create the risk-management label set on a repository — IDEMPOTENT and ADDITIVE:
# existing labels are skipped (never recolored, never deleted).
#
# Usage: scripts/setup-labels.sh <owner>/<repo>
# Needs: gh CLI authenticated with `repo` scope; jq.

set -euo pipefail

REPO="${1:?usage: setup-labels.sh <owner>/<repo>}"
LABELS_FILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/.github/risk-labels.json"

command -v jq >/dev/null || { echo "jq is required" >&2; exit 1; }
[ -f "$LABELS_FILE" ] || { echo "labels file not found: $LABELS_FILE" >&2; exit 1; }

existing="$(gh label list --repo "$REPO" --limit 200 --json name --jq '.[].name')"

created=0; skipped=0
while IFS=$'\t' read -r name color description; do
  if grep -Fxq "$name" <<<"$existing"; then
    echo "skip (exists): $name"
    skipped=$((skipped + 1))
  else
    gh label create "$name" --repo "$REPO" --color "$color" --description "$description"
    echo "created:       $name"
    created=$((created + 1))
  fi
done < <(jq -r '.[] | [.name, .color, .description] | @tsv' "$LABELS_FILE")

echo "Done: $created created, $skipped skipped (already existed)."
