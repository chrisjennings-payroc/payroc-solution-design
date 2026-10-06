# Payroc Solution Design toolkit

Builds partner **Solution Designs (SDs)** for Payroc Sales Engineers: an editable HTML document plus an
auto-saved Markdown twin that other AI tools can read. Covers the Payroc platform (docs.payroc.com) and the
Worldnet platform (REST API, Hosted Pages, SDKs), imports the integrator's docs.payroc.com
`integration-plan.md`, and checks on every run that the Payroc skills are current against
https://github.com/payroc/skills.

This repo is a **Claude Code plugin marketplace** containing one plugin, `payroc-solution-design`
(skills `create-solution-design` and `worldnet-reference`, plus four slash commands).

> No API keys, tokens or secrets belong in this repo or in any SD. Docs name that a key is required and
> describe the auth structure with placeholders such as `<API_KEY>`.

## Install (testers and SEs)

1. Install the Payroc skills the SD cross-checks against (once):
   ```bash
   npx skills add payroc/skills --agent claude-code
   ```
2. In Claude Code, add this marketplace and install the plugin:
   ```text
   /plugin marketplace add chrisjennings-payroc/payroc-solution-design
   /plugin install payroc-solution-design@payroc-sales-engineering
   ```
   From a local checkout: `/plugin marketplace add ./payroc-solution-design` (path to this folder).

## Use

| Command | What it does |
|---|---|
| `/payroc-solution-design:sd-new [partner]` | Guided interview -> `<Partner>-Solution-Design.html` + `.md` |
| `/payroc-solution-design:sd-import <plan.md> [addendum.md]` | Pre-fill scope from the integrator's plan (and Worldnet addendum) |
| `/payroc-solution-design:sd-review <file.html>` | Unresolved fields, HTML/MD sync, skills freshness, endpoint accuracy, secrets scan |
| `/payroc-solution-design:sd-refresh-worldnet` | Reports the age of the Worldnet docs snapshot (maintainers re-sync it) |

Open the generated HTML in Chrome/Edge, click **Enable autosave to this file**, then **Enable Markdown (.md)
autosave**. Full guide: `payroc-solution-design/skills/create-solution-design/README.md`.

Without Claude: open `payroc-solution-design/skills/create-solution-design/template.html` directly in
Chrome/Edge. It is fully editable and autosaves HTML + Markdown, without the interview, skills check or plan import.

## Testing

See [docs/TESTING.md](docs/TESTING.md). Report findings with the issue template in `.github/ISSUE_TEMPLATE/`.

## Maintainers

The skills live directly in `payroc-solution-design/skills/` (single source of truth — there is no build step).

```bash
cd payroc-solution-design/skills
python3 worldnet-reference/scripts/refresh-worldnet.py      # re-sync Worldnet docs (~2 min, no credentials)
python3 create-solution-design/tests/test_parse.py          # parser tests
python3 create-solution-design/scripts/check-skills.py      # skills freshness vs payroc/skills
```

Release: update `CHANGELOG.md`, bump the version in `payroc-solution-design/.claude-plugin/plugin.json` and
`.claude-plugin/marketplace.json`, commit on a feature branch and open a PR; tag after merge. Installed plugins
are read-only, so scripts never write next to themselves.
