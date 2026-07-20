#!/usr/bin/env bash
# check-harm-risk.sh — advisory completeness & consistency linter for the harm-risk register
# (ISO 14971). Operationalises, as a warn-only CI check, the per-issue rules the
# mdr-audit-readiness skill applies: both verifications (§7.2), new-risks-from-controls (§7.5),
# residual risk (§7.3), disclose-in-ifu for tier-3 controls (§8), and lifecycle-label consistency.
#
# ADVISORY ONLY — always exits 0. It annotates; it never blocks (enable, not enforce).
# Method: docs/HARM_RISK.md. Requires: gh (authenticated) + python3.
#
# Usage: scripts/check-harm-risk.sh [owner/repo]   (defaults to the current gh repo)

set -uo pipefail

REPO="${1:-}"
if ! command -v gh >/dev/null 2>&1; then
  echo "check-harm-risk: gh not found — advisory, skipped."; exit 0
fi
[ -n "$REPO" ] || REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)"
if [ -z "$REPO" ]; then
  echo "check-harm-risk: no repo (pass <owner/repo>) — advisory, skipped."; exit 0
fi

JSON="$(gh issue list --repo "$REPO" --label harm-risk --state all --limit 500 \
        --json number,title,body,labels,state 2>/dev/null)" || {
  echo "check-harm-risk: gh query failed (auth/scope?) — advisory, skipped."; exit 0; }

# stash to a temp file: the python script itself arrives on stdin (heredoc), so the JSON
# is passed by path, not piped.
TMP="$(mktemp)"; trap 'rm -f "$TMP"' EXIT
printf '%s' "$JSON" > "$TMP"

echo "check-harm-risk: linting the harm-risk register of $REPO (advisory)"
python3 - "$TMP" <<'PY'
import json, re, sys

issues = json.load(open(sys.argv[1], encoding="utf-8"))

def norm(s): return re.sub(r"\s+", " ", (s or "")).strip().lower()

FIELD_RE = re.compile(r"^###\s+(.*)$", re.MULTILINE)
def fields(body):
    out, parts = {}, FIELD_RE.split(body or "")
    for i in range(1, len(parts) - 1, 2):
        out[norm(parts[i])] = parts[i + 1].strip()
    return out

def get(f, prefix):
    p = norm(prefix)
    for k, v in f.items():
        if k.startswith(p):
            return v
    return None

def blank(v):
    return v is None or norm(v) in ("", "_no response_", "none", "n/a")

total = warns = 0
struct = 0
for it in issues:
    num, title = it.get("number"), (it.get("title") or "").strip()
    labels = {l.get("name", "") for l in it.get("labels", []) if isinstance(l, dict)}
    f = fields(it.get("body", ""))
    total += 1
    msgs = []
    if not f:
        # free-text issue — not machine-checkable; note once, skip detailed rules
        print(f"  · HR-{num}: not raised via the harm-risk form — detailed checks skipped")
        continue
    struct += 1
    verification = get(f, "verification plan")
    new_risks = get(f, "new/changed risks")
    residual_eval = get(f, "residual risk evaluation")
    residual_s = get(f, "residual severity")
    residual_p = get(f, "residual probability")
    controls = get(f, "risk control measure") or ""
    benefit = get(f, "benefit")

    if blank(new_risks):
        msgs.append("§7.5 new-risks-from-controls not recorded (required field blank)")
    if blank(verification):
        msgs.append("§7.2 verification (implemented + effective) not recorded")
    if blank(residual_eval) and blank(residual_s) and blank(residual_p):
        msgs.append("§7.3 residual risk not recorded (no residual S/P or evaluation)")
    # tier-3 information-for-safety control must reach the IFU
    if re.search(r"tier[\s-]*3|information for safety", controls, re.I) and "disclose-in-ifu" not in labels:
        msgs.append("tier-3 'information for safety' control but no `disclose-in-ifu` label (§8)")
    # lifecycle-label consistency
    if "harm-risk:controlled" in labels and blank(verification):
        msgs.append("labelled `harm-risk:controlled` but no verification recorded")
    if "harm-risk:residual-accepted" in labels and blank(benefit):
        msgs.append("labelled `harm-risk:residual-accepted` but no benefit–risk record (§7.4)")

    if msgs:
        warns += 1
        print(f"  ⚠ HR-{num} — {title[:60]}")
        for m in msgs:
            print(f"      - {m}")

print("")
print(f"check-harm-risk: {total} harm-risk issue(s), {struct} form-structured; "
      f"{warns} with advisory findings. Triage per docs/HARM_RISK.md (nothing is blocked).")
PY
exit 0
