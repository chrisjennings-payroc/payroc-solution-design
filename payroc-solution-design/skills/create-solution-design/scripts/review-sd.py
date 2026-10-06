#!/usr/bin/env python3
"""Review a finished Solution Design (HTML + Markdown twin) before it is shared.

Usage: review-sd.py PARTNER-Solution-Design.html [--md PARTNER-Solution-Design.md]

Checks (stdlib only, no network):
  - unresolved placeholders (HTML `.fill` fields without `filled`, leftover {{tokens}}, [TODO: ...] in the .md)
  - HTML <-> Markdown twin in sync (same section ids; unresolved count within the .md front matter)
  - provenance recorded (Payroc skills freshness; Worldnet snapshot when any workflow uses Worldnet)
  - Worldnet consistency (Worldnet/Both sections need the Worldnet snapshot recorded; boarding flag vs blocker row)
  - credential-shaped values in EITHER file (API keys, tokens, JWTs, secrets, private keys) — must never appear

Exit code: 0 = no errors (warnings allowed), 1 = errors found.
"""
import argparse, json, os, re, sys
from html.parser import HTMLParser

SECRET_PATTERNS = [
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}")),
    ("Authorization header value", re.compile(r"(?i)authorization\s*:\s*(?:basic|bearer)\s+(?!<|\{|your|xxx)[A-Za-z0-9+/=._-]{16,}")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("hex secret (40+ chars)", re.compile(r"(?<![\w/.-])[0-9a-fA-F]{40,}(?![\w/-])")),
    ("key/secret/token assignment", re.compile(r"(?i)\b(api[_ -]?key|secret|password|passwd|token|client[_ -]?secret)\b[\"']?\s*[:=]\s*[\"']?(?!<|\{|your|xxx|placeholder|example|required|string|\[)[A-Za-z0-9+/_=-]{16,}")),
    ("long mixed-case token", re.compile(r"(?<![/\w.=+-])(?=[A-Za-z0-9+]*\d)(?=[A-Za-z0-9+]*[a-z])(?=[A-Za-z0-9+]*[A-Z])[A-Za-z0-9+]{40,}(?![\w/=+-])")),
]


PROVENANCE_LABEL = re.compile(r"(?i)(commit|release|docs|docsRelease|sha-?256|specSha|source|hash|checksum)\W{0,6}$")


class Scan(HTMLParser):
    """Collect section ids (outside the trash), unresolved .fill fields and provenance JSON from the HTML."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []           # (tag, flags)
        self.section_ids = []
        self.platforms = {}
        self.unresolved = 0
        self.token_left = 0
        self.prov = None
        self._in_prov = False
        self._prov_buf = []
        self.wn_flag_checked = False
        self.auto_blocker_row = False
        self.in_scope = {}
        self._cur_section = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        trash = a.get("id") == "section-trash" or any(f.get("trash") for _, f in self.stack)
        inmain = tag == "main" or any(f.get("main") for _, f in self.stack)
        in_bar = "subsection-scope" in cls or any(f.get("bar") for _, f in self.stack)
        self.stack.append((tag, {"trash": trash, "main": inmain, "bar": in_bar}))
        if tag == "script" and a.get("id") == "sd-provenance":
            self._in_prov = True
        if tag == "section" and a.get("id") and not trash and inmain:
            self.section_ids.append(a["id"])
            self._cur_section = a["id"]
            if a.get("data-platform"):
                self.platforms[a["id"]] = a["data-platform"]
        if tag == "option" and "selected" in a and self._cur_section:
            self.platforms[self._cur_section] = a.get("value", "payroc")
        if tag == "input" and a.get("type") == "checkbox" and self._cur_section and not trash:
            if "checked" in a and in_bar:
                self.in_scope[self._cur_section] = True
            if a.get("id") == "wn-boarding-flag" and "checked" in a:
                self.wn_flag_checked = True
        if tag == "tr" and "data-auto" in a and not trash:
            self.auto_blocker_row = True
        if "fill" in cls and "filled" not in cls and inmain and not trash:
            self.unresolved += 1

    def handle_endtag(self, tag):
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag:
                break
        if tag == "script" and self._in_prov:
            self._in_prov = False
            try:
                self.prov = json.loads("".join(self._prov_buf))
            except Exception:
                self.prov = None

    def handle_data(self, data):
        if self._in_prov:
            self._prov_buf.append(data)
        elif any(f.get("main") for _, f in self.stack) and not any(f.get("trash") for _, f in self.stack):
            if "{{" in data:
                self.token_left += data.count("{{")


def front_matter(md):
    m = re.match(r"^---\n(.*?)\n---\n", md, re.S)
    fm = {}
    if m:
        for ln in m.group(1).split("\n"):
            k, _, v = ln.partition(":")
            if k.strip():
                try:
                    fm[k.strip()] = json.loads(v.strip())
                except Exception:
                    fm[k.strip()] = v.strip()
    return fm


def scan_secrets(name, text, findings):
    for i, ln in enumerate(text.split("\n"), 1):
        l2 = re.sub(r"https?://\S+", "", ln)
        for label, pat in SECRET_PATTERNS:
            m = pat.search(l2)
            if m and label.startswith("hex") and PROVENANCE_LABEL.search(l2[max(0, m.start() - 48):m.start()]):
                continue  # a commit SHA / docs release hash / spec hash recorded as provenance
            if m:
                findings.append(("error", "%s:%d possible %s: %s…" % (name, i, label, m.group(0)[:6])))
                break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--md")
    a = ap.parse_args()
    md_path = a.md or re.sub(r"\.html?$", ".md", a.html)
    html = open(a.html, encoding="utf8").read()
    md = open(md_path, encoding="utf8").read() if os.path.exists(md_path) else None
    f = []  # (level, message)

    sc = Scan()
    sc.feed(html)

    # 1. unresolved
    if sc.unresolved:
        f.append(("warn", "%d unresolved field(s) in the HTML (highlighted fields without an answer)." % sc.unresolved))
    if sc.token_left:
        f.append(("warn", "%d leftover {{token}} placeholder(s) in the HTML body." % sc.token_left))

    # 2. twin sync
    if md is None:
        f.append(("error", "No Markdown twin found at %s — enable Markdown autosave or download the .md." % md_path))
    else:
        fm = front_matter(md)
        md_ids = re.findall(r"<!-- sd:section=([a-z0-9-]+) -->", md)
        only_html = [i for i in sc.section_ids if i not in md_ids]
        only_md = [i for i in md_ids if i not in sc.section_ids]
        if only_html:
            f.append(("error", "Sections in the HTML but not in the .md: %s (twin out of sync — re-save the .md)." % ", ".join(only_html)))
        if only_md:
            f.append(("error", "Sections in the .md but not in the HTML: %s." % ", ".join(only_md)))
        todo = md.count("[TODO:")
        if todo:
            f.append(("warn", "%d [TODO: …] marker(s) in the Markdown twin." % todo))
        if isinstance(fm.get("unresolved_fields"), int) and abs(fm["unresolved_fields"] - sc.unresolved) > 2:
            f.append(("warn", "Unresolved count differs: HTML %d vs .md front matter %s (the .md may be older than the HTML)." % (sc.unresolved, fm.get("unresolved_fields"))))
        if not fm.get("partner"):
            f.append(("warn", "Partner name is not filled in (front matter `partner` is null)."))

    # 3. provenance + Worldnet consistency
    p = sc.prov or {}
    sk = p.get("skills") or {}
    if sk.get("result") in (None, "not-run"):
        f.append(("warn", "Payroc skills freshness was not checked (run check-skills.py --record and fill provenance)."))
    elif sk.get("result") not in ("current",):
        f.append(("warn", "Payroc skills result is %r (stale / not verified) — mention this to the reader." % sk.get("result")))
    uses_wn = any(v in ("worldnet", "both") for k, v in sc.platforms.items() if k != "worldnet-sdks") or \
        ("worldnet-sdks" in sc.section_ids and sc.in_scope.get("worldnet-sdks"))
    wn = p.get("worldnet") or {}
    if uses_wn and not wn.get("snapshot"):
        f.append(("warn", "A workflow runs on Worldnet but the Worldnet docs snapshot date is not recorded in provenance."))
    if sc.wn_flag_checked and not sc.auto_blocker_row:
        f.append(("warn", "Worldnet Boarding API flag is ticked but the open item is missing from Section 4."))

    # 4. secrets in both files
    scan_secrets(os.path.basename(a.html), html, f)
    if md:
        scan_secrets(os.path.basename(md_path), md, f)

    errors = [m for l, m in f if l == "error"]
    warns = [m for l, m in f if l == "warn"]
    for m in errors:
        print("ERROR  " + m)
    for m in warns:
        print("WARN   " + m)
    print("%s: %d error(s), %d warning(s). Sections: %d%s." % (
        os.path.basename(a.html), len(errors), len(warns), len(sc.section_ids),
        "; Worldnet in use" if uses_wn else ""))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
