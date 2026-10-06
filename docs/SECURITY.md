# Security & data-handling notes (for plugin review)

Audience: whoever approves Claude Code plugin sources. Audited 2026-10-06 against `main` at v0.2.0 by reading every script and
command; re-check on each release.

## What the plugin is
Markdown instructions (skills and slash commands), four small Python 3 scripts that use only the standard library, one HTML template,
and a static copy of public Worldnet developer documentation. It has **no hooks, no MCP servers, no background processes, no installers,
no third-party dependencies, no telemetry**.

## Network access
| Script | Runs when | Requests | Notes |
|---|---|---|---|
| `check-skills.py` | Every SD run (Step 0) and `/sd-review` | `GET https://api.github.com/repos/payroc/skills/{commits,git/trees}` | Unauthenticated, read-only, no data sent. Compares file hashes of locally installed Payroc skills with upstream. Fails safe when offline/rate-limited ("not verified"). |
| `refresh-worldnet.py` | Maintainers only (manually) | `GET https://developers.worldnetpayments.com/...` | Re-syncs the public Worldnet docs snapshot. Not invoked by any command. Redacts credential-shaped sample values. |
| `tests/make_synthetic_plan.py` | Developer tests only | `GET https://docs.payroc.com/...` | Builds synthetic test plans. Not shipped in any command. |
| `parse-integration-plan.py`, `review-sd.py` | On demand | none | Read local files and print results. |

No script uses `subprocess`, `eval`, `exec`, sockets or shell-outs. No script sends partner, merchant or SD content anywhere.
Separately, `/sd-new` and the skill's Step 3 can use Claude's `WebFetch`/`WebSearch` to read public docs.payroc.com pages (Section 8.7).

## Filesystem access
- Scripts only read the files you point them at. The generated SD (`.html`, `.md`) is written by Claude into the folder the SE chooses, or
  saved by the browser from the template's autosave buttons (File System Access API, user-picked file).
- `refresh-worldnet.py` (maintainers) writes only inside the skill's `references/` folder.
- `check-skills.py --record` makes a best-effort write of `skills-upstream.json` next to itself; it is optional and ignored if the install is read-only.

## Credentials
- None are stored, required or requested. The repo and snapshot contain no API keys, tokens or secrets; credential-shaped sample values in the
  Worldnet snapshot are redacted at sync time (`scrub()` in `refresh-worldnet.py`).
- The SD template and skill instructions forbid keys in an SD (placeholders like `<API_KEY>` only), and `review-sd.py` scans the HTML and
  Markdown twin for credential-shaped values and fails the review if it finds any.

## Tool permissions requested by the commands
| Command | `allowed-tools` | Reviewer note |
|---|---|---|
| `/sd-new` | `Bash(python3:*)`, Read, Write, Edit, Glob, Grep, Skill, WebFetch | `Bash(python3:*)` permits any `python3` command, not just the bundled scripts; it could be narrowed to the plugin's script paths if policy requires. |
| `/sd-import` | `Bash(python3:*)`, Read, Write, Edit, Glob, Grep, Skill | as above |
| `/sd-review` | `Bash(python3:*)`, Read, Glob, Grep, Skill | as above; read-only intent (edits only with SE confirmation) |
| `/sd-refresh-worldnet` | `Bash(python3:*)`, Read | reports snapshot age only |

## Known item: broad Bash permission (left as is)
The commands request `Bash(python3:*)`, which lets any `python3` command run without an approval prompt while that slash command is
running; it is not limited to the bundled scripts. This was chosen for a smooth pilot (no prompt on each script run) and is intentionally
left as is for now. It will be narrowed to the bundled script paths, or removed so each run asks for approval, if the reviewing admin
recommends it. Note that `/sd-import` reads an integrator-supplied plan; the skills treat plan text as data, never as instructions.

## Content to be aware of
- `worldnet-reference` is a copy of **public** developer documentation (developers.worldnetpayments.com).
- `tests/fixtures/` holds one real plan-builder output (no secrets; contains request/release identifiers) and synthetic plans.
- Generated SDs describe partners and are confidential; they are produced locally and are not part of this repo.
