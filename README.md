# Payroc Solution Design toolkit

Builds partner **Solution Designs (SDs)** for Payroc Sales Engineers: an editable HTML document plus an
auto-saved Markdown twin that other AI tools can read. Covers the Payroc platform (docs.payroc.com) and the
Worldnet platform (REST API, Hosted Pages, SDKs), imports the integrator's docs.payroc.com
`integration-plan.md`, and checks on every run that the Payroc skills are current against
https://github.com/payroc/skills.

This repo is a set of **Claude Code skills** (no plugin or marketplace needed): `create-solution-design` and
`worldnet-reference`, plus four command skills (`sd-new`, `sd-import`, `sd-review`, `sd-refresh-worldnet`).

> No API keys, tokens or secrets belong in this repo or in any SD. Docs name that a key is required and
> describe the auth structure with placeholders such as `<API_KEY>`.

## Install (testers and SEs)

1. Install the Payroc skills the SD cross-checks against (once):
   ```bash
   npx skills add payroc/skills --agent claude-code
   ```
2. Clone this repo and install the skills. Keep all six folders together as siblings (they reference each other):
   ```bash
   git clone https://github.com/chrisjennings-payroc/payroc-solution-design.git
   cd payroc-solution-design
   ./install.sh            # symlinks skills/* into ~/.claude/skills
   ```
   Or copy the folders by hand: `cp -R skills/* ~/.claude/skills/` (user-level) or into `<project>/.claude/skills/` (one project).
   Restart Claude Code so the skills load. To update, `git pull` (symlinks) or re-copy.

> For reviewers: see [docs/security_payroc.md](docs/security_payroc.md) (what the skills run, what they fetch, and that they store no credentials).

## Use

| Command | What it does |
|---|---|
| `/sd-new [partner]` | Guided interview -> `<Partner>-Solution-Design.html` + `.md` |
| `/sd-import <plan.md> [addendum.md]` | Pre-fill scope from the integrator's plan (and Worldnet addendum) |
| `/sd-review <file.html>` | Unresolved fields, HTML/MD sync, skills freshness, endpoint accuracy, secrets scan |
| `/sd-refresh-worldnet` | Reports the age of the Worldnet docs snapshot (maintainers re-sync it) |

Open the generated HTML in Chrome/Edge, click **Enable autosave to this file**, then **Enable Markdown (.md)
autosave**. Full guide: `skills/create-solution-design/README.md`.

Without Claude: open `skills/create-solution-design/template.html` directly in
Chrome/Edge. It is fully editable and autosaves HTML + Markdown, without the interview, skills check or plan import.

## Testing

See [docs/TESTING.md](docs/TESTING.md). Report findings with the issue template in `.github/ISSUE_TEMPLATE/`.

## Maintainers

The skills live directly in `skills/` (single source of truth — there is no build step).

```bash
cd skills
python3 worldnet-reference/scripts/refresh-worldnet.py      # re-sync Worldnet docs (~2 min, no credentials)
python3 create-solution-design/tests/test_parse.py          # parser tests
python3 create-solution-design/scripts/check-skills.py      # skills freshness vs payroc/skills
```

Release: update `CHANGELOG.md`, bump `metadata.version` in the changed `SKILL.md` files, commit on a feature branch and open a PR; tag after merge.

## License

The original content in this repo is released under the [MIT License](LICENSE). The Worldnet documentation snapshot under
`skills/worldnet-reference/references/` is third-party material and is not covered by that license.
