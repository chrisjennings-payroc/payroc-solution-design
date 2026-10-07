# Payroc Solution Design toolkit (v0.2.0)

Builds a partner **Solution Design (SD)**: an editable HTML document plus an auto-saved Markdown twin that
any other AI tool can read. Covers the Payroc platform (docs.payroc.com) and, for Worldnet-platform
partners, the Worldnet REST API, Hosted Pages and SDKs (developers.worldnetpayments.com).

> No API keys, tokens or secrets belong in an SD. Name that a key is needed and describe the auth structure
> with placeholders (`<API_KEY>`). `scripts/review-sd.py` scans for credential-shaped values.

## What's in this folder

| File | Purpose |
|---|---|
| `SKILL.md` | The Claude interview (Step 0 freshness check → Steps 1-6) |
| `template.html` | The branded, browser-editable SD (autosave, add/remove rows & sections, platform selector, unresolved-field counter, Markdown twin) |
| `skill-map.json` | Which upstream skill(s) in `payroc/skills` feed each SD section |
| `workflow-map.json` | docs.payroc.com workflow slugs → SD sections; Worldnet addendum products |
| `scripts/check-skills.py` | Compares local skills with https://github.com/payroc/skills (main) |
| `scripts/parse-integration-plan.py` | Parses the integrator's `integration-plan.md` (+ Worldnet addendum) into JSON |
| `scripts/review-sd.py` | Pre-share review: unresolved fields, HTML/MD sync, provenance, secrets scan |
| `integrator-intake/worldnet-addendum.md` | Questionnaire to send an integrator who needs Worldnet |
| `tests/` | Fixture tests for the parser (`python3 tests/test_parse.py`) |

The sibling skill `worldnet-reference` holds the Worldnet documentation snapshot.

## Quick start (Claude Code)

1. Install the Payroc skills (once): `npx skills add payroc/skills --agent claude-code`
2. Ask Claude: **"Build the Solution Design for <partner>"** (or `/sd-new` when installed as the plugin).
3. Claude checks that the skills are current, optionally imports the integrator's plan, interviews you,
   and writes `<Partner>-Solution-Design.html` and `.md`.
4. Open the HTML in **Chrome or Edge**, click **Enable autosave to this file**, then **Enable Markdown
   (.md) autosave** (same folder). Safari/Firefox: use **Download updated copy (HTML + .md)**. For the signed final version, click **Download .pdf**.
5. Drive **Unresolved fields** to 0, then run `python3 scripts/review-sd.py <file>.html`.

## Working in the HTML

- Click any highlighted field to type; checkboxes, tables and lists are editable (`+ Add row`, `+ Add item`).
- Workflows that can run on either platform have a **Payroc / Worldnet / Both** selector; the Worldnet block
  appears for Worldnet/Both. 8.2f (Worldnet SDKs, POS & plugins) is Worldnet-only.
- **Worldnet Boarding API is not supported in the SD.** Tick the flag in 8.1 to add an open item to Section 4.
- Removed sections go to the "Removed sections" panel and survive save/reopen; their TOC links hide.
- Appendix A › Provenance records the skills commit/date checked and the Worldnet snapshot date.

## Integrator hand-back

- The integrator completes the plan builder on docs.payroc.com and shares `integration-plan.md`.
- If Worldnet is involved, send them `integrator-intake/worldnet-addendum.md` to complete and return.
- `python3 scripts/parse-integration-plan.py integration-plan.md --addendum worldnet-addendum.md --pretty`
  shows which SD sections are in scope, the ordered API calls, manual steps, acceptance criteria and
  warnings. The plan text is treated as data, never as instructions.

## Keeping things current

- Payroc skills: `python3 scripts/check-skills.py` (run automatically at Step 0); update with
  `npx skills add payroc/skills --agent claude-code`.
- Worldnet docs: `python3 ../worldnet-reference/scripts/refresh-worldnet.py` (about 2 minutes; warn when
  the snapshot is older than 90 days).
- New docs.payroc.com workflows: add their slugs to `workflow-map.json`.

## Without Claude

Open `template.html` directly in Chrome/Edge: the document is fully editable and autosaves to HTML and
Markdown without any AI. You lose the guided interview, the skills freshness check and the plan import; use
`scripts/review-sd.py` before sharing. A self-serve wizard for non-Claude users is planned as a fallback.
