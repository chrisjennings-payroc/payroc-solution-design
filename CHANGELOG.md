# Changelog

## 0.2.0 — unreleased (pilot)
- Template v0.2.0: Payroc / Worldnet / Both platform selector, Worldnet blocks and 8.2f (SDKs, POS, plugins);
  unresolved-fields counter; Markdown twin with autosave; TOC sync; removed sections persist across save/reopen.
- New 8.6b card-present operational requirements & open questions (pre-filled with Payroc-confirmed answers).
- `worldnet-reference` skill: snapshot of developers.worldnetpayments.com (Boarding API excluded) with a refresh script.
- Skills freshness check against payroc/skills; integration-plan + Worldnet addendum importer; pre-share review script.
- Plugin commands: sd-new, sd-import, sd-review, sd-refresh-worldnet.
- Commands no longer pre-approve `Bash(python3:*)`; script runs prompt for approval.
