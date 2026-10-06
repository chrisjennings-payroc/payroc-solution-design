---
description: Check the age of the Worldnet docs snapshot (maintainers re-sync it from the plugin source repo)
allowed-tools: Read
---

Check how fresh the Worldnet documentation snapshot is.

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/worldnet-reference/references/snapshot.json` and report `syncedAt`,
   the number of pages, and how many days old it is. If it is older than 90 days, say it is stale.
2. The installed plugin directory is read-only, so the snapshot cannot be refreshed from here. A **maintainer**
   re-syncs it in the plugin source repository:
   `python3 payroc-solution-design/skills/worldnet-reference/scripts/refresh-worldnet.py` (about 2 minutes, no credentials),
   then bumps the plugin version, updates `CHANGELOG.md` and publishes (there is no separate build step).
   Tell the SE to ask the maintainer and to update the plugin (`/plugin update`).
