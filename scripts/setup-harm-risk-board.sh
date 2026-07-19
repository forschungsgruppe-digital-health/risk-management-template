#!/usr/bin/env bash
# Create the "Harm Risk File" Projects v2 board + its custom fields — IDEMPOTENT:
# skips creation if a project of that name already exists under the owner.
# SEPARATE from the delivery "Risk Register" board by design (docs/HARM_RISK.md).
#
# Usage: scripts/setup-harm-risk-board.sh <owner> [owner/repo] [project-title]
#   If an owner/repo is given, the project is LINKED to that repository (it then
#   appears in the repo's Projects tab). Re-linking is a harmless no-op.
# Needs: gh CLI with the `project` scope (gh auth refresh -s project).
#
# NOTE: Projects v2 VIEWS cannot be created via the API — the script prints the
# 3-view recipe (Risk table S×P / Uncontrolled / Residual accepted) to add manually.

set -euo pipefail

OWNER="${1:?usage: setup-harm-risk-board.sh <owner> [owner/repo] [title]}"
REPO=""
if [[ "${2:-}" == */* ]]; then REPO="$2"; TITLE="${3:-Harm Risk File}"; else TITLE="${2:-Harm Risk File}"; fi

if gh project list --owner "$OWNER" --limit 100 --format json \
  | grep -Fq "\"title\":\"$TITLE\""; then
  echo "Project '$TITLE' already exists under $OWNER — skipping creation."
  PROJECT_NUMBER="$(gh project list --owner "$OWNER" --limit 100 --format json \
    | jq -r --arg t "$TITLE" '.projects[] | select(.title == $t) | .number' | head -1)"
else
  echo "Creating project '$TITLE' under $OWNER …"
  PROJECT_NUMBER="$(gh project create --owner "$OWNER" --title "$TITLE" --format json | jq -r '.number')"
fi
echo "Project number: $PROJECT_NUMBER"

field() { # name type [options-csv]
  local name="$1" type="$2" options="${3:-}"
  if gh project field-list "$PROJECT_NUMBER" --owner "$OWNER" --format json \
    | jq -e --arg n "$name" '.fields[] | select(.name == $n)' >/dev/null; then
    echo "skip field (exists): $name"
  elif [ -n "$options" ]; then
    gh project field-create "$PROJECT_NUMBER" --owner "$OWNER" \
      --name "$name" --data-type "$type" --single-select-options "$options"
    echo "created field:       $name ($type: $options)"
  else
    gh project field-create "$PROJECT_NUMBER" --owner "$OWNER" \
      --name "$name" --data-type "$type"
    echo "created field:       $name ($type)"
  fi
}

field "Severity"             SINGLE_SELECT "1,2,3,4,5"
field "Probability"          SINGLE_SELECT "1,2,3,4,5"
field "Residual severity"    SINGLE_SELECT "1,2,3,4,5"
field "Residual probability" SINGLE_SELECT "1,2,3,4,5"
field "Risk Status"          SINGLE_SELECT "Open,Controlling,Controlled,Residual accepted,Closed"
field "Hazard category"      SINGLE_SELECT "data-integrity,availability,confidentiality,clinical-misinterpretation,interoperability,usability,other"
field "Control verification" SINGLE_SELECT "None,Implemented,Verified effective"
field "Owner"                TEXT
field "Review date"          DATE

if [ -n "$REPO" ]; then
  if gh project link "$PROJECT_NUMBER" --owner "$OWNER" --repo "$REPO" >/dev/null 2>&1; then
    echo "linked project to $REPO (visible in the repo's Projects tab)"
  else
    echo "note: link to $REPO not confirmed (already linked, or missing scope/permission)"
  fi
fi

cat <<'EOF'

Fields done. Add the three VIEWS manually (Projects v2 views are not API-creatable):
  1. "Risk table (S×P)"      — Table layout, sort: Severity desc then Probability desc, filter: -Risk Status:Closed
  2. "Uncontrolled"          — Table layout, filter: -"Control verification":"Verified effective" -Risk Status:Closed
  3. "Residual accepted (audit)" — Table layout, filter: Risk Status:"Residual accepted"

Then (optional) enable the board's built-in auto-add workflow for issues labelled `harm-risk`,
and review the board before every release (overall residual risk, ISO 14971 §8).
EOF
