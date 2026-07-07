#!/usr/bin/env bash
# GitLab twin of setup-project-board.sh / setup-harm-risk-board.sh — configures the
# project's issue board with LABEL LISTS for both registers. IDEMPOTENT: existing
# lists are skipped.
#
# Free tier: ONE board per project -> the delivery-risk and harm-risk lifecycle lists
# sit side by side on the default board (Open/Closed columns are built in). With
# Premium (multiple boards) you can split them into a "Risk Register" and a
# "Harm Risk File" board manually — the lists below are the recipe either way.
#
# Usage: scripts/setup-boards-gitlab.sh <group/project>
# Needs: glab authenticated; jq. Run setup-labels-gitlab.sh (both label files) FIRST.

set -euo pipefail

PROJECT="${1:?usage: setup-boards-gitlab.sh <group/project>}"
ENC="$(printf '%s' "$PROJECT" | sed 's|/|%2F|g')"

command -v jq >/dev/null || { echo "jq is required" >&2; exit 1; }

BOARD_ID="$(glab api "projects/$ENC/boards" | jq -r '.[0].id')"
[ -n "$BOARD_ID" ] && [ "$BOARD_ID" != "null" ] || { echo "no issue board found (enable Issues for the project)" >&2; exit 1; }
echo "Default board: $BOARD_ID"

existing_label_ids="$(glab api "projects/$ENC/boards/$BOARD_ID/lists" | jq -r '.[].label.id')"

add_list() { # scoped label name, in board-column order
  local label="$1"
  local label_id
  label_id="$(glab api "projects/$ENC/labels?search=$(printf '%s' "$label" | sed 's/:/%3A/g')&per_page=100" \
    | jq -r --arg n "$label" '.[] | select(.name == $n) | .id' | head -1)"
  if [ -z "$label_id" ]; then
    echo "skip (label missing — run setup-labels-gitlab.sh first): $label"
    return
  fi
  if grep -Fxq "$label_id" <<<"$existing_label_ids"; then
    echo "skip list (exists): $label"
  else
    glab api -X POST "projects/$ENC/boards/$BOARD_ID/lists" -f "label_id=$label_id" >/dev/null
    echo "created list:       $label"
  fi
}

# Delivery-risk lifecycle (docs/RISK_MANAGEMENT.md §5) — Closed column covers risk::closed
add_list "risk::open"
add_list "risk::mitigated"
add_list "risk::accepted"
# Harm-risk lifecycle (docs/HARM_RISK.md §7)
add_list "harm-risk::open"
add_list "harm-risk::controlled"
add_list "harm-risk::residual-accepted"

cat <<'EOF'

Lists done. Working views (filter the board or the issue list):
  - Severity table:      filter label risk::sev-critical / risk::sev-high / …
  - Matrix walk (§7):    board as-is, sorted by weight (= Score, set via /weight at triage)
  - Residual audit:      filter label harm-risk::residual-accepted
Premium option: create a second board ("Harm Risk File") and move the harm-risk:: lists there.
EOF
