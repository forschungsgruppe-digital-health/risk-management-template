#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-risk-management-file.py — assemble ONE hand-to-auditor Risk Management File.

Compiles the risk-management records that this template keeps *scattered across the repo*
(so each stays a single source of truth) into a single document ordered by the ISO 14971
process — the deliverable an MDR/CE auditor reads instead of navigating the repo. It is a
compiled VIEW, not a fork: narrative sections are transcluded verbatim from their source
files; the harm-risk register is rendered from the release's register export
(`harm-risk-register-<tag>.json`, produced by `.github/workflows/register-export.yml`) or a
live `gh` query.

Standards frame (editions per docs/standards/CONFORMANCE.md):
  ISO 14971:2019 §4.4 (plan) · §4.5 (file/traceability) · §5 (analysis) · §6 (evaluation) ·
  §7 (control) · §8 (overall residual) · §9 (review/report) · §10 (post-production);
  ISO/TR 24971:2020; IEC 62304:2006+A1:2015 (§4.3 class, §7 SW risk, §8.1.2 SOUP);
  IEC 62366-1 (use-related risk); IEC 81001-5-1 (security); MDR (EU) 2017/745 Annex I GSPRs.

Honesty contract (mirrors the template's philosophy):
  * It never fabricates content — an unfilled `<…>` / `[RA]` placeholder shows THROUGH so the
    reader sees exactly what is filled vs. not.
  * It makes NO conformity claim; applicability/acceptance determinations stay [NEEDS RA INPUT].
  * The authoritative records remain the project forge (issues/PRs) + git history; this file
    is a per-release snapshot/view of them.

Dependencies: Python 3.8+ stdlib only. pandoc is OPTIONAL — always writes the Markdown
master; DOCX/PDF/HTML are produced only if pandoc (and, for PDF, a LaTeX engine) is present.

Usage:
  scripts/build-risk-management-file.py \
      --repo . --tag v1.2.0 \
      --register harm-risk-register-v1.2.0.json \
      --delivery-register risk-register-v1.2.0.json \
      --out docs/risk-management-file --formats md,docx,pdf,html
Exit codes: 0 always for a successful Markdown master (missing optional formats warn, not fail).
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys

# --------------------------------------------------------------------------------------
# small IO + markdown helpers
# --------------------------------------------------------------------------------------

def read(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except (FileNotFoundError, IsADirectoryError):
        return None


def run(cmd):
    """Run a command, return (rc, stdout, stderr); never raise."""
    try:
        p = subprocess.run(cmd, capture_output=True, text=True)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except FileNotFoundError:
        return 127, "", "not found: %s" % cmd[0]


def strip_frontmatter(md):
    if md and md.startswith("---\n"):
        end = md.find("\n---\n", 4)
        if end != -1:
            return md[end + 5:]
    return md or ""


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)


def _norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def extract_section(md, heading_text):
    """Return the slice from the heading whose text matches `heading_text` (normalized,
    startswith-tolerant) up to the next heading of the SAME-or-higher level. Heading line
    excluded. Returns None if not found."""
    if not md:
        return None
    target = _norm(heading_text)
    matches = list(HEADING_RE.finditer(md))
    for i, m in enumerate(matches):
        level = len(m.group(1))
        htext = _norm(m.group(2))
        if htext == target or htext.startswith(target):
            start = m.end()
            end = len(md)
            for n in matches[i + 1:]:
                if len(n.group(1)) <= level:
                    end = n.start()
                    break
            return md[start:end].strip("\n")
    return None


def demote_headings(md, target_top):
    """Shift all headings so the shallowest becomes level `target_top`."""
    if not md:
        return ""
    levels = [len(m.group(1)) for m in HEADING_RE.finditer(md)]
    if not levels:
        return md
    shift = target_top - min(levels)
    if shift <= 0:
        return md

    def repl(m):
        new = min(6, len(m.group(1)) + shift)
        return "#" * new + " " + m.group(2)

    return HEADING_RE.sub(repl, md)


# optional leading '!' so a relative IMAGE ![alt](rel) collapses to its alt text (no stray '!')
REL_LINK_RE = re.compile(r"!?\[([^\]]+)\]\((?!https?://|#)[^)]+\)")


def neutralize_relative_links(md):
    """A compiled PDF/DOCX has no repo tree around it, so drop relative link (and relative
    image) targets, keeping the text; absolute http(s) links pass through. Prevents dangling
    links in the deliverable."""
    return REL_LINK_RE.sub(r"\1", md or "")


def transclude(md, top_level=3, source_note=None):
    """Prepare a source slice for inclusion: strip frontmatter, neutralize relative links,
    demote headings, optionally prefix a provenance italic line."""
    body = neutralize_relative_links(demote_headings(strip_frontmatter(md), top_level))
    if source_note:
        return "*Source: %s*\n\n%s" % (source_note, body)
    return body


# --------------------------------------------------------------------------------------
# harm-risk register rendering (ISO 14971 §5–§7 per-hazard chain)
# --------------------------------------------------------------------------------------

FIELD_RE = re.compile(r"^###\s+(.*)$", re.MULTILINE)

# form-field label -> (14971 element label with clause). Order defines table order.
CHAIN = [
    ("Hazard", "Hazard (§5.4)"),
    ("Foreseeable sequence of events", "Foreseeable sequence of events (§5.4)"),
    ("Hazardous situation", "Hazardous situation (§5.4)"),
    ("Harm", "Harm (§5.4; def. §3.3)"),
    ("Hazard category", "Hazard category"),
    ("Severity of harm", "Severity of harm S (§5.5)"),
    ("Probability of harm", "Probability of harm P (§5.5)"),
    ("P1", "P1 × P2 decomposition (§5.5 / TR 24971 §5.5.2)"),
    ("Risk control measure", "Risk control — tiered (§7.1)"),
    ("New/changed risks", "New/changed risks from controls (§7.5)"),
    ("Residual severity", "Residual severity S (§7.3)"),
    ("Residual probability", "Residual probability P (§7.3)"),
    ("Residual risk evaluation", "Residual risk evaluation (§6/§7.3)"),
    ("Verification plan", "Verification — implemented + effective (§7.2)"),
    ("Benefit", "Benefit–risk note (§7.4)"),
    ("Completeness of risk control", "Completeness (§7.6)"),
    ("Disclosure", "Disclosure to IFU (§8)"),
    ("Design element", "Design element / ADR / requirement"),
    ("Proposed owner", "Owner"),
]


def parse_issue_body(body):
    """Split a GitHub issue-form body into {field-label: value} on '### ' headings."""
    out = {}
    if not body:
        return out
    parts = FIELD_RE.split(body)
    # parts = [pre, label1, val1, label2, val2, ...]
    for i in range(1, len(parts) - 1, 2):
        out[_norm(parts[i])] = parts[i + 1].strip()
    return out


def _field(fields, key_prefix):
    kp = _norm(key_prefix)
    # exact match first (so the short key "hazard" is not stolen by "hazard category" /
    # "hazardous situation"), then fall back to prefix match for keys carrying a suffix
    # (e.g. "severity of harm (s)" for the "Severity of harm" chain entry).
    if kp in fields:
        return fields[kp]
    for k, v in fields.items():
        if k.startswith(kp):
            return v
    return None


def _label_names(labels):
    """gh returns labels as [{name:..}, ..]; some callers pass [str, ..]. Handle both."""
    if not isinstance(labels, list):
        return ""
    names = [(l.get("name", "") if isinstance(l, dict) else str(l)) for l in labels]
    return ", ".join(n for n in names if n)


def render_harm_risk(issue):
    num = issue.get("number", "?")
    title = (issue.get("title") or "").replace("[HARM]", "").strip()
    state = issue.get("state", "")
    labels = _label_names(issue.get("labels"))
    fields = parse_issue_body(issue.get("body", ""))
    header = ["### HR-%s — %s" % (num, title or "(untitled hazard)"),
              "",
              "*State: %s%s*" % (state, (" · labels: " + labels) if labels else ""),
              ""]
    if not fields:
        # Issue not created via the harm-risk form (free-text body): the 14971 chain is not
        # machine-separable. Include the raw body verbatim rather than an empty table, and
        # flag it so a reviewer knows this entry is not field-structured.
        body = (issue.get("body") or "").strip() or "*(empty issue body — [NEEDS INPUT])*"
        header.append("> *Unstructured issue body — not raised via the harm-risk form, so the "
                      "ISO 14971 chain below is not field-separated. Consider re-raising via the "
                      "form for per-element traceability (§4.5).*")
        header.append("")
        header.append("\n".join("> " + ln for ln in body.splitlines()))
        header.append("")
        return "\n".join(header)
    lines = header + ["| 14971 element | Content |", "|---|---|"]
    for prefix, elem in CHAIN:
        val = _field(fields, prefix)
        if val is None:
            continue
        val = re.sub(r"\s*\n\s*", " ", val).strip()
        val = val.replace("|", "\\|")
        if not val or _norm(val) in ("_no response_", "none"):
            if prefix in ("Benefit", "P1"):
                continue  # genuinely-optional fields: omit when blank
            # residual S/P are §7.3-mandatory once controls exist — flag, never hide
            val = "*(blank — [NEEDS INPUT])*"
        lines.append("| %s | %s |" % (elem, val))
    lines.append("")
    return "\n".join(lines)


def render_register(issues, kind, tag):
    if issues is None:
        return ("> **Register not bundled into this build.** The authoritative %s file is the "
                "`%s` issues on the project forge. Attach `%s-register-%s.json` "
                "(`register-export.yml`) or pass `--register` to make this section "
                "self-contained.\n" % (kind, kind, kind, tag))
    if len(issues) == 0:
        return ("> **No `%s` issues in the register at this release.** For a market-bound "
                "device an empty risk analysis is a finding (ISO 14971 §5); at research stage "
                "it is expected. [NEEDS INPUT]\n" % kind)
    if kind == "harm-risk":
        return "\n".join(render_harm_risk(i) for i in issues)
    # delivery-risk: compact table
    rows = ["| # | Title | State | Labels |", "|---|---|---|---|"]
    for i in issues:
        labs = ", ".join(l.get("name", "") for l in i.get("labels", []) if isinstance(l, dict))
        rows.append("| %s | %s | %s | %s |" % (
            i.get("number", "?"),
            (i.get("title") or "").replace("|", "\\|"),
            i.get("state", ""), labs.replace("|", "\\|")))
    return "\n".join(rows) + "\n"


def load_register(path, owner_repo, label):
    """Return list-of-issues from a file, else a live gh query, else None."""
    if path:
        raw = read(path)
        if raw:
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                sys.stderr.write("WARN: could not parse register %s\n" % path)
    if owner_repo:
        rc, out, err = run(["gh", "issue", "list", "--repo", owner_repo, "--label", label,
                            "--state", "all", "--limit", "1000",
                            "--json", "number,title,state,labels,body,createdAt,closedAt"])
        if rc == 0 and out:
            try:
                return json.loads(out)
            except json.JSONDecodeError:
                pass
        elif rc != 0:
            sys.stderr.write("WARN: gh register query failed (%s)\n" % (err or rc))
    return None


# --------------------------------------------------------------------------------------
# document assembly
# --------------------------------------------------------------------------------------

def section(title, clause, body):
    """One clause-mapped H2 section."""
    head = "## %s" % title
    if clause:
        head += "  \n*ISO 14971 %s*" % clause if clause.startswith("§") else "  \n*%s*" % clause
    return "%s\n\n%s\n" % (head, (body or "*(not present in the repository — [NEEDS INPUT])*"))


def build_master(repo, tag, hr_issues, dr_issues, date_iso, commit, generator):
    R = lambda p: read(os.path.join(repo, p))  # noqa: E731
    st = lambda p: os.path.exists(os.path.join(repo, p))  # noqa: E731

    harm = R("docs/HARM_RISK.md")
    report = R("docs/HARM_RISK_REPORT.md")

    # --- intended purpose + safety class from the ADRs (Current decision sections) ---
    adr1 = R("docs/adr/0001-mdsw-qualification.md")
    adr2 = R("docs/adr/0002-software-safety-classification.md")
    intended = extract_section(adr1, "Current decision") or (adr1 and strip_frontmatter(adr1)) or None
    safety_class = extract_section(adr2, "Current decision") or None

    # --- latest audit-readiness self-assessment, if any ---
    reports_dir = os.path.join(repo, "docs", "reports")
    latest_audit = None
    if os.path.isdir(reports_dir):
        cands = sorted([f for f in os.listdir(reports_dir) if f.startswith("mdr-audit-readiness")])
        if cands:
            latest_audit = "docs/reports/%s" % cands[-1]

    # ---- front matter (pandoc metadata) ----
    meta = [
        "---",
        "title: Risk Management File",
        "subtitle: '%s — release %s'" % (os.path.basename(os.path.abspath(repo)), tag),
        "date: '%s'" % date_iso,
        "lang: en",
        "toc: true",
        "toc-depth: 2",
        "numbersections: true",
        "---",
        "",
    ]

    banner = (
        "> **What this document is.** A single-file **Risk Management File & Report** compiled "
        "per **ISO 14971:2019 §4.5 / §9** from this repository's living records at release "
        "`%s` (commit `%s`). It is a *compiled view* — the authoritative records remain the "
        "project forge (issues + pull requests) and git history; narrative sections are "
        "transcluded verbatim from their source files, and the harm-risk register is rendered "
        "from the release's register export.\n>\n"
        "> **Honesty & scope.** Unfilled `<…>` / `[RA]` placeholders are shown *as-is* — this "
        "document fabricates nothing. It makes **no claim of conformity**; determinations of "
        "applicability and acceptance remain **[NEEDS RA INPUT]** (the manufacturer's "
        "regulatory function decides, not this generator). Whether the product qualifies as "
        "medical-device software (MDSW) is stated in the transcluded ADR-0001. This is a "
        "manufacturer self-compilation and does **not** replace a Notified-Body assessment or "
        "an ISO 13485 quality-management-system internal audit.\n>\n"
        "> **Generated by** `%s` — do not hand-edit; re-run the generator to refresh.\n"
        % (tag, commit, generator)
    )

    parts = []
    parts.append("".join([m + "\n" for m in meta]))
    parts.append("# Risk Management File — %s (release %s)\n" % (os.path.basename(os.path.abspath(repo)), tag))
    parts.append(banner)

    parts.append(section(
        "0. Provenance & standards frame", "",
        "| Item | Value |\n|---|---|\n"
        "| Release / version | %s |\n| Source commit | %s |\n| Compiled (UTC) | %s |\n"
        "| Generator | %s |\n"
        "| Standards frame | EN ISO 14971:2019(+A11:2021), ISO/TR 24971:2020, "
        "IEC 62304:2006+A1:2015, IEC 62366-1, IEC 81001-5-1, ISO 81001-1, MDR (EU) 2017/745 "
        "Annex I (editions per Annex A9) |\n"
        "| MDSW qualification | see §1 (ADR-0001) |\n"
        "| Audit-readiness self-check | %s |\n"
        % (tag, commit, date_iso, generator, latest_audit or "*(none in docs/reports/)*")))

    # --- Part 1: Risk management plan (§4.4) ---
    plan = extract_section(harm, "1. Risk management plan")
    parts.append(section("1. Risk management plan", "§4.4",
                         (transclude(plan, 3, "docs/HARM_RISK.md §1") if plan else None)))

    # intended use / qualification (§5.2 anchor + MDSW state). §5.2 requires intended use AND
    # reasonably foreseeable misuse; ADR-0001 carries the intended purpose, so an explicit
    # misuse slot is always appended (it must not silently vanish — honesty contract).
    misuse_home = extract_section(harm, "2. The 14971 chain")  # HARM_RISK.md §2 frames the misuse input
    sec2 = (transclude(intended, 3, "docs/adr/0001-mdsw-qualification.md") if intended else None)
    misuse_note = (
        "\n\n**Reasonably foreseeable misuse (§5.2).** " +
        ("The systematic-identification method (intended use + foreseeable misuse → hazards) is "
         "in docs/HARM_RISK.md §2; per-hazard misuse paths are captured in each register entry's "
         "*foreseeable sequence of events*. Confirm a documented misuse INPUT list exists for this "
         "release — otherwise **[NEEDS INPUT]**." if misuse_home else
         "No documented foreseeable-misuse input was found — **[NEEDS INPUT]** (§5.2 requires it "
         "alongside the intended use)."))
    parts.append(section("2. Intended use, foreseeable misuse & MDSW qualification", "§5.2 (+ MDR qualification)",
                         (sec2 or "*(ADR-0001 not present — [NEEDS INPUT])*") + misuse_note))

    # --- Part 3: acceptability criteria (§4.4 d / §4.2) ---
    crit = extract_section(harm, "4. Acceptability matrix") or extract_section(harm, "Acceptability matrix")
    parts.append(section("3. Risk acceptability criteria", "§4.4(d) / §4.2 (+ MDR AFAP)",
                         (transclude(crit, 3, "docs/HARM_RISK.md §4") if crit else None)))

    # --- Part 4: risk analysis / evaluation / control per hazard (§5–§7) ---
    parts.append(section(
        "4. Risk analysis, evaluation & control — per hazard", "§5, §6, §7 (traceable per §4.5)",
        "The harm-risk register below carries, for **each hazard**, the full ISO 14971 chain — "
        "analysis (§5.2–5.5) → evaluation (§6) → control in priority order (§7.1) → the two "
        "verifications (§7.2) → new-risks-from-controls (§7.5) → residual risk (§7.3) — giving "
        "the per-hazard **traceability** ISO 14971 §4.5 requires.\n\n"
        + render_register(hr_issues, "harm-risk", tag)))

    # --- Part 5: overall residual risk (§8) ---
    # The METHOD for overall-residual + benefit-risk (HARM_RISK.md §7); the per-release
    # JUDGEMENT (§9 conclusion 2) lives in Part 6, so this does not duplicate the report.
    overall = extract_section(harm, "7. Residual risk, benefit") \
        or extract_section(harm, "7. Residual risk") or extract_section(harm, "Residual risk, benefit")
    parts.append(section("5. Overall residual risk & benefit–risk — method", "§8 / §7.4 (MDR GSPR 8)",
                         (transclude(overall, 3, "docs/HARM_RISK.md §7") if overall else None)
                         + "\n\n*The per-release overall-residual **judgement** (§8 acceptability) is "
                         "recorded as conclusion 2 of the §9 review in Part 6.*"))

    # --- Part 6: risk management review / report (§9) ---
    parts.append(section("6. Risk management review & report", "§9",
                         (transclude(strip_frontmatter(report), 3, "docs/HARM_RISK_REPORT.md")
                          if report else None)))

    # --- Part 7: production & post-production (§10) ---
    postprod = extract_section(harm, "8. Production & post-production feed") \
        or extract_section(harm, "Production & post-production")
    parts.append(section("7. Production & post-production plan", "§10 (MDR Art. 83–92 inputs)",
                         (transclude(postprod, 3, "docs/HARM_RISK.md §8") if postprod else None)))

    # ---------------- Annexes ----------------
    parts.append("# Annexes\n")

    def annex(letter, title, note, src_file, src_heading=None, verbatim=False):
        body = None
        raw = R(src_file)
        if raw:
            if verbatim:
                body = "```\n%s\n```" % raw.strip()
            else:
                sec = extract_section(raw, src_heading) if src_heading else strip_frontmatter(raw)
                body = transclude(sec, 3, src_file) if sec else None
        head = "## Annex %s — %s\n\n*%s*\n" % (letter, title, note)
        return head + "\n" + (body or "*(%s not present — [NEEDS INPUT])*" % src_file) + "\n"

    parts.append(annex("A", "Software safety classification", "IEC 62304 §4.3 (risk-based A/B/C)",
                       "docs/adr/0002-software-safety-classification.md",
                       "Current decision") if safety_class else
                 annex("A", "Software safety classification", "IEC 62304 §4.3 (risk-based A/B/C)",
                       "docs/adr/0002-software-safety-classification.md"))
    parts.append(annex("B", "IEC 62304 process-area coverage", "design-for-conformance map (covered / partial / not-yet / deferred)",
                       "docs/standards/IEC-62304-COVERAGE.md"))
    parts.append("## Annex C — SOUP inventory\n\n*IEC 62304 §5.3.3–5.3.4, §7.1.3, §8.1.2 — "
                 "software of unknown provenance. The per-release SBOM (software bill of "
                 "materials) is the authoritative full-tree enumeration, attached separately "
                 "to the release.*\n\n" +
                 ("```yaml\n%s\n```\n" % (R("soup.yaml").strip()) if R("soup.yaml")
                  else "*(soup.yaml not present — [NEEDS INPUT])*\n"))
    parts.append(annex("D", "MDR Annex I GSPR checklist", "General Safety and Performance Requirements — software rows; applicability/met = [NEEDS RA INPUT]",
                       "docs/standards/GSPR-CHECKLIST.md"))
    parts.append(annex("E", "Security risk management", "IEC 81001-5-1 — security activities, SOUP/vulnerability handling, Coordinated Vulnerability Disclosure",
                       "docs/SECURITY_RISK.md"))
    parts.append(annex("F", "Traceability model", "ISO 14971 §4.5 / IEC 62304 §5.1.1(c),§7.3 — requirement → design → implementation → test → risk",
                       "docs/TRACEABILITY.md"))
    parts.append(annex("G", "Standards & regulatory index", "editions applied and their status",
                       "docs/standards/CONFORMANCE.md"))
    # Annex H: ADR index
    adr_dir = os.path.join(repo, "docs", "adr")
    adr_list = ""
    if os.path.isdir(adr_dir):
        for f in sorted(os.listdir(adr_dir)):
            if re.match(r"\d{4}-.*\.md$", f):
                first = (read(os.path.join(adr_dir, f)) or "").splitlines()
                title = next((l.lstrip("# ").strip() for l in first if l.startswith("#")), f)
                adr_list += "- **%s** — %s\n" % (f, title)
    parts.append("## Annex H — Architecture decision records (design history)\n\n"
                 "*Risk-relevant design decisions; each ADR that reduces a risk cites the "
                 "register issue and vice versa.*\n\n" + (adr_list or "*(no ADRs found)*") + "\n")
    # Annex I: delivery-risk register (context, not safety)
    parts.append("## Annex I — Delivery-risk register (context)\n\n"
                 "*Project/delivery risk (schedule, scope, supply chain) — kept **separate** "
                 "from the safety file above; included for completeness, never merged with "
                 "harm risk.*\n\n" + render_register(dr_issues, "risk", tag) + "\n")
    # Annex J: audit-readiness self-assessment
    parts.append("## Annex J — Audit-readiness self-assessment\n\n" +
                 ("*Latest `mdr-audit-readiness` mock-audit scorecard: `%s`. A self-check of the "
                  "distance to auditable — not a conformity statement.*\n" % latest_audit
                  if latest_audit else
                  "*No `mdr-audit-readiness` report found in `docs/reports/`. Run the "
                  "`mdr-audit-readiness` skill to attach a scorecard of the distance to "
                  "auditable.*\n"))

    parts.append("\n---\n\n*End of compiled Risk Management File. Generated by `%s` from commit "
                 "`%s`. This document is decision-input for the manufacturer's regulatory "
                 "function and a Notified Body; it asserts no conformity.*\n" % (generator, commit))

    return "\n".join(parts)


# --------------------------------------------------------------------------------------
# conversion (pandoc, optional)
# --------------------------------------------------------------------------------------

def have(cmd):
    return run([cmd, "--version"])[0] == 0


# Glyphs the default LaTeX font (Latin Modern) lacks — mapped to meaning-preserving text so
# the PDF has no blank characters. Applied to the PDF INPUT ONLY; the Markdown/DOCX/HTML
# masters keep the original Unicode (they render it correctly).
_PDF_GLYPHS = {
    "≥": ">=", "≤": "<=", "≠": "!=", "≈": "~",
    "→": "->", "↔": "<->", "⇒": "=>", "⇔": "<=>",
    "⟶": "-->", "⚠": "[!]", "✓": "[x]", "✗": "[ ]",
}


def _pdf_sanitize(text):
    for k, v in _PDF_GLYPHS.items():
        text = text.replace(k, v)
    return text


def convert(master_path, out_base, formats):
    produced = [master_path]
    if not have("pandoc"):
        sys.stderr.write("NOTE: pandoc not found — wrote Markdown master only.\n")
        return produced
    common = ["pandoc", master_path, "--from", "gfm", "--toc", "--number-sections",
              "--metadata", "title=Risk Management File"]
    if "html" in formats:
        out = out_base + ".html"
        rc, _, err = run(common + ["--standalone", "--embed-resources", "-o", out])
        produced.append(out) if rc == 0 else sys.stderr.write("WARN html: %s\n" % err)
    if "docx" in formats:
        out = out_base + ".docx"
        rc, _, err = run(common + ["-o", out])
        produced.append(out) if rc == 0 else sys.stderr.write("WARN docx: %s\n" % err)
    if "pdf" in formats:
        out = out_base + ".pdf"
        engine = next((e for e in ("xelatex", "lualatex", "pdflatex", "tectonic",
                                   "weasyprint", "wkhtmltopdf", "typst") if have(e)), None)
        if engine:
            # sanitize a small glyph set for the PDF input only (font-coverage safety)
            src = read(master_path)
            pdf_src = master_path + ".pdfsrc.md"
            with open(pdf_src, "w", encoding="utf-8") as fh:
                fh.write(_pdf_sanitize(src))
            rc, _, err = run(["pandoc", pdf_src, "--from", "gfm", "--toc", "--number-sections",
                              "--metadata", "title=Risk Management File",
                              "--pdf-engine", engine, "-o", out])
            try:
                os.remove(pdf_src)
            except OSError:
                pass
            produced.append(out) if rc == 0 else sys.stderr.write(
                "WARN pdf (%s): %s\n" % (engine, err.splitlines()[-1] if err else "?"))
        else:
            sys.stderr.write("NOTE: no PDF engine (xelatex/tectonic/weasyprint/…) — skipped "
                             "PDF; DOCX/HTML/MD produced. CI uses a pandoc+LaTeX container.\n")
    return produced


# --------------------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Assemble a single ISO 14971 Risk Management File.")
    ap.add_argument("--repo", default=".", help="repository root (default: .)")
    ap.add_argument("--tag", default=None, help="release/version label (default: git describe)")
    ap.add_argument("--register", default=None, help="harm-risk register export JSON")
    ap.add_argument("--delivery-register", default=None, help="delivery risk register export JSON")
    ap.add_argument("--owner-repo", default=None, help="owner/repo for a live gh register query")
    ap.add_argument("--out", default="docs/risk-management-file", help="output directory")
    ap.add_argument("--formats", default="md,docx,pdf,html", help="comma list: md,docx,pdf,html")
    args = ap.parse_args()

    repo = os.path.abspath(args.repo)
    tag = args.tag
    if not tag:
        rc, out, _ = run(["git", "-C", repo, "describe", "--tags", "--always", "--dirty"])
        tag = out if rc == 0 and out else "unreleased"
    rc, commit, _ = run(["git", "-C", repo, "rev-parse", "--short", "HEAD"])
    commit = commit if rc == 0 else "unknown"
    date_iso = os.environ.get("SOURCE_DATE_EPOCH_ISO") or \
        datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    generator = "scripts/build-risk-management-file.py"

    hr = load_register(args.register, args.owner_repo, "harm-risk")
    dr = load_register(args.delivery_register, args.owner_repo, "risk")

    master = build_master(repo, tag, hr, dr, date_iso, commit, generator)

    out_dir = os.path.join(repo, args.out) if not os.path.isabs(args.out) else args.out
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, "risk-management-file-%s" % re.sub(r"[^\w.-]", "_", tag))
    master_path = base + ".md"
    with open(master_path, "w", encoding="utf-8") as fh:
        fh.write(master)

    formats = [f.strip() for f in args.formats.split(",") if f.strip()]
    produced = convert(master_path, base, formats) if formats != ["md"] else [master_path]

    print("Risk Management File compiled for release %s (commit %s):" % (tag, commit))
    for p in produced:
        print("  - %s" % os.path.relpath(p, repo))
    hrn = "n/a" if hr is None else len(hr)
    drn = "n/a" if dr is None else len(dr)
    print("Register: harm-risk=%s · delivery-risk=%s" % (hrn, drn))
    return 0


if __name__ == "__main__":
    sys.exit(main())
