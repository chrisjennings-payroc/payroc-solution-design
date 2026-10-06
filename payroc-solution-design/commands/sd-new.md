---
description: Start a new Payroc Solution Design (guided interview -> editable HTML + Markdown twin)
argument-hint: [partner name]
allowed-tools: Bash(python3:*), Read, Write, Edit, Glob, Grep, Skill, WebFetch
---

Use the `create-solution-design` skill to build a Solution Design for: $ARGUMENTS

Follow the skill exactly, starting with **Step 0** (verify the Payroc skills are current against
https://github.com/payroc/skills; the script is at
`${CLAUDE_PLUGIN_ROOT}/skills/create-solution-design/scripts/check-skills.py`). If the SE has an
integrator `integration-plan.md` (and optionally a Worldnet addendum), ask for the path and run the
import described in the skill before the scope questions. Never put API keys, tokens or secrets in the
output. Finish by writing BOTH `{Partner}-Solution-Design.html` and `{Partner}-Solution-Design.md`, then
run the review (`/payroc-solution-design:sd-review`).
