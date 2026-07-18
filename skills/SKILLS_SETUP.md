# Skills setup

`skills/` is the **single source of truth** for agent capabilities in this repo, using the vendor-neutral
[Agent Skills](https://agentskills.io) format (`skills/<name>/SKILL.md` with `name`/`description`
frontmatter, plus Claude-specific extension fields that other agents safely ignore).

## Skills

- **`apply-risk-management`** — this repo's own skill: retrofit risk management onto an existing repo
  (inventory → proposed diff → additive apply).
- **Shared FGDH toolkit** (kept identical across the FGDH repos; single source = the
  [`arc42-project-template`](https://github.com/forschungsgruppe-digital-health/arc42-project-template)):
  `arc42-generator`, `docs-auditor`, `release-manager`, `branching-strategist`, `dependency-scanner`,
  `security-scanner`, `security-reviewer`, `template-updater`, `grilling`, `grill-me`.

## Tool wiring

- **Claude Code** discovers them via `.claude/skills/<name>` — symlinks into `skills/`.
- **OpenAI Codex / Cursor / Gemini** discover them via `.codex/skills/<name>` — the same symlinks — or the
  tool's own skills path.
- **Any other agent** (e.g. GitHub Copilot): read the catalog in [AGENTS.md](../AGENTS.md) and perform the
  skill's instructions inline.

Adding a skill: create `skills/<name>/SKILL.md`, then add both symlinks
(`ln -s ../../skills/<name> .claude/skills/<name>` and the `.codex` twin) and a catalog line in
`AGENTS.md`. **Never edit the symlinked copies — edit `skills/` only.**

## Staying in sync with the shared toolkit

This repo tracks the `arc42-project-template` via **`.arc42-template.json`** (version stamp). The monthly
**`.github/workflows/template-sync-check.yml`** notifier opens an issue when a newer template release
exists; the **`template-updater`** skill then reconciles the shared skills + tooling into this repo
**while preserving its risk-management / conformance / GitLab specialization** and its own
`apply-risk-management` skill.
