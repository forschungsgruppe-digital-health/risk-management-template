#!/usr/bin/env bash
# Emit an ADVISORY traceability matrix (Markdown): requirement issue → cross-referenced
# PRs → do those PRs touch test files? Flags requirements with no linked test.
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

echo
echo "_Advisory only (docs/TRACEABILITY.md) — generated $(date -u +%Y-%m-%d)_"
exit 0
