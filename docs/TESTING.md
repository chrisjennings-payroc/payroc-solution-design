# Pilot testing guide

## Prerequisites
- Claude Code, Python 3 (3.9+), and Chrome or Edge (Safari/Firefox use the download button instead of file autosave).
- Payroc skills installed: `npx skills add payroc/skills --agent claude-code`.
- Network access to `api.github.com` (the skills freshness check makes one unauthenticated call; about 60 per hour per IP — if it
  says "not verified", that is expected when offline or rate-limited).

## Install
See the README. Confirm `/payroc-solution-design:` commands appear.

## Scenarios (try at least three; use a past or fictional partner — no real partner data in feedback)
1. **New SD from scratch** — `/payroc-solution-design:sd-new <partner>`; answer the interview; open the HTML in Chrome/Edge, enable
   autosave and Markdown autosave; confirm the `.md` updates within ~2 s of an edit.
2. **Import a plan** — `/payroc-solution-design:sd-import <integration-plan.md>`; check the proposed sections, ordered API calls,
   manual steps and warnings match the plan.
3. **Worldnet partner** — tick Worldnet/Both on a workflow; check the Worldnet block, Appendix A and provenance; confirm the Worldnet
   Boarding API appears only as "not supported" with the flag in 8.1.
4. **Card-present partner** — Cloud and/or 8.2f; check 8.6b appears, pre-filled rows look right, rows can be edited or removed.
5. **Review** — `/payroc-solution-design:sd-review <file.html>`; it should flag unresolved fields, twin sync and any credential-shaped value
   (try pasting a fake key to see it caught — then remove it).
6. **No-Claude path** — open `template.html` directly; edit, autosave/download, then run `scripts/review-sd.py`.
7. **Safari/Firefox** — use "Download updated copy (HTML + .md)"; confirm both files download and reopen correctly.

## What to report
Anything confusing, wrong or missing — especially endpoint/field mistakes versus the Payroc skills, Worldnet content that disagrees with
what you know, and open questions in 8.6b that need an owner. Use the **Pilot test feedback** issue template. Never attach files that
contain partner details or keys.

## Known gaps
- The self-serve wizard for people without Claude is not built.
- Plan import has been exercised on one real plan plus plans synthesised from workflow pages; real plans from other workflows are welcome.
- `close-a-terminal-batch` and `check-dcc-eligibility` workflow mappings are judgement calls.
- Worldnet "not documented in snapshot" items and open 8.6b questions need Payroc owners.
