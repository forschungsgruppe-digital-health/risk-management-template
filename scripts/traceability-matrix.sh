#!/usr/bin/env bash
# Emit an ADVISORY traceability matrix (Markdown): requirement issue → cross-referenced
# PRs → do those PRs touch test files? Flags requirements with no linked test.
# Covers: requirement → PR → test (via gh) AND SOUP → requirement (from soup.yaml `req:`).
# The risk-control → test edge lives inside each harm-risk issue (docs/TRACEABILITY.md).
# Always exits 0 — a gap is review input, not a failure (docs/TRACEABILITY.md).
#
# Usage: scripts/traceability-matrix.sh <owner>/<repo>
# Needs: gh CLI (repo scope); jq.

set -euo pipefail

REPO="${1:?usage: traceability-matrix.sh <owner>/<repo>}"
TEST_PATTERN='(^|/)(test|tests|spec|__tests__)/|\.(test|spec)\.[jt]sx?$|Test\.java$|_test\.(go|py)$|\.cy\.[jt]s$'

echo "# Traceability matrix — $REPO"
echo
echo "| Requirement | State | Linked PRs | Tests touched | Status |"
echo "|---|---|---|---|---|"

gh issue list --repo "$REPO" --label requirement --state all --limit 200 \
  --json number,title,state --jq '.[] | [.number, .state, .title] | @tsv' \
| while IFS=$'\t' read -r num state title; do
  prs="$(gh api "repos/$REPO/issues/$num/timeline" --paginate \
    --jq '[.[] | select(.event == "cross-referenced") | .source.issue | select(.pull_request != null) | .number] | unique | .[]' 2>/dev/null || true)"
  if [ -z "$prs" ]; then
    echo "| REQ-$num — $title | $state | — | — | ⚠ no linked PR |"
    continue
  fi
  tests="no"
  pr_list=""
  for pr in $prs; do
    pr_list="${pr_list:+$pr_list, }#$pr"
    if gh pr view "$pr" --repo "$REPO" --json files \
      --jq '.files[].path' 2>/dev/null | grep -qE "$TEST_PATTERN"; then
      tests="yes"
    fi
  done
  if [ "$tests" = "yes" ]; then
    echo "| REQ-$num — $title | $state | $pr_list | yes | ✓ |"
  else
    echo "| REQ-$num — $title | $state | $pr_list | no | ⚠ no linked test |"
  fi
done

# --- SOUP → requirement coverage (advisory; reads local soup.yaml if present) ---
if [ -f soup.yaml ]; then
  echo
  echo "## SOUP → requirement (from soup.yaml \`req:\`)"
  echo
  echo "| SOUP component | Requirement | Status |"
  echo "|---|---|---|"
  awk '
    function emit() {
      if (name == "") return
      if (req == "") printf "| %s | — | ⚠ no linked requirement |\n", name
      else printf "| %s | %s | ✓ |\n", name, req
    }
    /^[[:space:]]*-[[:space:]]*name:/ {
      emit()
      name=$0; sub(/^[[:space:]]*-[[:space:]]*name:[[:space:]]*/,"",name); sub(/[[:space:]]+#.*/,"",name); gsub(/"/,"",name); req=""; next
    }
    /^[[:space:]]*req:/ {
      req=$0; sub(/^[[:space:]]*req:[[:space:]]*/,"",req); sub(/[[:space:]]+#.*/,"",req); gsub(/"/,"",req)
    }
    END { emit() }
  ' soup.yaml
fi

echo
echo "_Advisory only (docs/TRACEABILITY.md) — generated $(date -u +%Y-%m-%d)_"
exit 0
