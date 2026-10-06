---
description: Pre-share review of a Solution Design (unresolved fields, HTML/MD sync, skills freshness, endpoint accuracy, secrets)
argument-hint: <path to Partner-Solution-Design.html>
allowed-tools: Bash(python3:*), Read, Glob, Grep, Skill
---

Review the Solution Design at: $ARGUMENTS

1. Run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/create-solution-design/scripts/review-sd.py" <file.html>`
   (it reads the `.md` twin next to it) and report every ERROR and WARN.
2. Run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/create-solution-design/scripts/check-skills.py" --json`.
   If skills are stale or missing, say so and tell the SE to run `npx skills add payroc/skills --agent claude-code`.
3. Endpoint accuracy: for each in-scope **Payroc** workflow, compare the SD's endpoint tables and
   "common pitfalls" with the matching skill listed in `skill-map.json` (read that skill's SKILL.md and its
   `references/api-schema.md`). List any endpoint, required field or pitfall that differs; the skill is the
   more current source. For each **Worldnet** block, spot-check 3 endpoints/fields against
   `worldnet-reference` (`references/rest-api.md`, `hosted-pages.md`, `sdks.md`) and warn if the Worldnet
   snapshot is older than 90 days (`references/snapshot.json`).
4. Platform consistency: Worldnet/Both sections must have a recorded snapshot date; Worldnet Boarding API
   must appear only as the "not supported" flag.
5. Confirm there are NO API keys, tokens or secrets in either file. Summarise findings as a short checklist
   and offer to fix them. Do not edit the files without confirmation.
