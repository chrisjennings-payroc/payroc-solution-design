#!/usr/bin/env bash
# Symlink the skills in this repo into ~/.claude/skills (or $1 if given).
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dest="${1:-$HOME/.claude/skills}"
mkdir -p "$dest"
for d in "$here"/skills/*/; do
  n="$(basename "$d")"
  ln -sfn "${d%/}" "$dest/$n"
  echo "linked $dest/$n"
done
echo "Restart Claude Code to load the skills."
