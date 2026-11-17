---
name: sd-refresh-worldnet
description: Check the age of the Worldnet docs snapshot (maintainers re-sync it from the source repo)
disable-model-invocation: true
allowed-tools: Bash(python3:*), Read
---

Check how fresh the Worldnet documentation snapshot is.

1. Read `${CLAUDE_SKILL_DIR}/../worldnet-reference/references/snapshot.json` and report `syncedAt`,
   the number of pages, and how many days old it is. If it is older than 90 days, say it is stale.
2. The snapshot is refreshed by a **maintainer** in the source repository (not from an installed copy):
   `python3 skills/worldnet-reference/scripts/refresh-worldnet.py` (about 2 minutes, no credentials),
   then bumps the skill version, updates `CHANGELOG.md` and commits (there is no separate build step).
   Tell the SE to ask the maintainer and then re-copy the updated `skills/` folders.
