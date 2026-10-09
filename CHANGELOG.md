# Changelog

## 0.2.0 — unreleased (pilot)
- Template v0.2.0: Payroc / Worldnet / Both platform selector, Worldnet blocks and 8.2f (SDKs, POS, plugins);
  unresolved-fields counter; Markdown twin with autosave; TOC sync; removed sections persist across save/reopen.
- New 8.6b card-present operational requirements & open questions (pre-filled with Payroc-confirmed answers).
- `worldnet-reference` skill: snapshot of developers.worldnetpayments.com (Boarding API excluded) with a refresh script.
- Skills freshness check against payroc/skills; integration-plan + Worldnet addendum importer; pre-share review script.
- Plugin commands: sd-new, sd-import, sd-review, sd-refresh-worldnet.
- Section 12 sign-off now mirrors the Certification Scripts approach: certified date (auto-filled when both parties have signed) plus a name, title and typed or drawn signature for the Payroc and partner representatives. Electronic signature (typed name + drawn image + timestamp); not a cryptographic signature. Images live in the HTML; the `.md` twin records names, titles and signed-at timestamps only.
- **Download .pdf** for the final signed version: built in the browser (dependency-free PDF writer) from the Markdown twin, with signature images embedded.
- Native SDK scoping (8.2f rebuilt from the Payroc GoChip SDK guides, SDK 1.6.89): platform table (Android, iOS, Windows, Java, Ubuntu/Linux; iOS = BBPOS only; Windows/Java/Ubuntu = IDTech and Ingenico only), device matrix with per-device prerequisites, partner build deliverables, mandatory logging requirements, SDK assumptions/milestones and an SDK / device certification checklist; Section 9 links to it. Payroc owns certification sign-off.
- 8.6b: production key injection confirmed (PAX = RKI; Ingenico/IDTech/BBPOS = approved KIF; Ingenico `loadRKI` is dev/test only); new rows for PAX app/terminal prerequisites (PAXstore) and device registration to a Terminal ID.
- `worldnet-reference`: new `references/sdk-integration-guides.md` (derived, non-sensitive summary; the source guides are confidential and stay out of the repo); `sdks.md` and `device-operations.md` updated.
- Worldnet addendum: SDK platform, device, feature, logging and credential questions. `review-sd.py`: SDK-scope checks and detection of key material (KSI/KCV, 32-hex key components); new `tests/test_review_sd.py`.
- Template: table row numbers renumber automatically when a row is added or removed (including undo); numbered first columns such as 8.6b, Section 4/5 and the SDK milestones. Removed the Section 9 rollback plan. 8.2f scoped to Websockets vs native SDK (plugin and legacy XML rows removed); 8.6b no longer has the separate encryption-model row.
