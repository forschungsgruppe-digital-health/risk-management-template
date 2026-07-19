#!/usr/bin/env bash
# Create the "Risk Register" Projects v2 board + its custom fields — IDEMPOTENT:
# skips creation if a project of that name already exists under the owner.
#
# Usage: scripts/setup-project-board.sh <owner> [project-title]
# Needs: gh CLI with the `project` scope (gh auth refresh -s project).
#
# NOTE: Projects v2 VIEWS cannot be created via the API — the script prints the
# 4-view recipe (Matrix / By severity / By owner / Review queue) to add manually.

set -euo pipefail

OWNER="${1:?usage: setup-project-board.sh <owner> [title]}"
TITLE="${2:-Risk Register}"

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

field "Likelihood"  SINGLE_SELECT "1,2,3,4,5"
field "Impact"      SINGLE_SELECT "1,2,3,4,5"
field "Score"       NUMBER
field "Severity"    SINGLE_SELECT "Critical,High,Medium,Low"
field "Risk Status" SINGLE_SELECT "Open,Mitigating,Mitigated,Accepted,Closed"
field "Category"    SINGLE_SELECT "schedule,scope,dependency,tech-debt,resource,supply-chain,vulnerability,secret,compliance,other"
field "Owner"       TEXT
field "Review date" DATE

cat <<'EOF'

Fields done. Add the four VIEWS manually (Projects v2 views are not API-creatable):
  1. "Matrix"      — Board layout, group by: Impact, sort: Likelihood desc, filter: -Risk Status:Closed
  2. "By severity" — Table layout, sort: Score desc
  3. "By owner"    — Table layout, group by: Owner
  4. "Review queue"— Table layout, filter: Risk Status:Open OR Review date <= today, sort: Review date asc

Then (optional) enable the board's built-in auto-add workflow for issues labelled `risk`,
and set the repo variable RISK_PROJECT_URL to the board URL for the automation workflow.
EOF
