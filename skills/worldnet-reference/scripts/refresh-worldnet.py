#!/usr/bin/env python3
"""Re-sync the worldnet-reference snapshot from https://developers.worldnetpayments.com.

Maintainer tool (stdlib only, no credentials). It:
  1. crawls the public DokuWiki page index,
  2. exports each in-scope page as raw DokuWiki text and converts it to Markdown
     (headings, code, links, lists, tables; everything else kept verbatim),
  3. downloads the public Merchant REST API OpenAPI spec and builds an endpoint index,
  4. rewrites references/_sources.md (URL, local file, sync date, sha256) and prints a summary.

SCOPE EXCLUSION: the Worldnet Boarding API (/apis/boarding/) is deliberately NOT fetched
or documented here — it is out of scope for the Solution Design. Pages that are not
integration documentation (playground, sidebar, signup, ...) are skipped.

Usage:  refresh-worldnet.py [--only PREFIX] [--dry-run]
"""
import argparse, datetime, hashlib, json, os, re, sys, time, urllib.parse, urllib.request

BASE = "https://developers.worldnetpayments.com/"
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
REF = os.path.join(SKILL, "references")
UA = {"User-Agent": "payroc-sd-worldnet-snapshot"}
SEED_NS = ["gochip", "hosted_pages", "plugins", "selfcare"]
SKIP_PREFIX = ("selfcare:playground", "selfcare:sidebar", "selfcare:start", "selfcare:home",
               "selfcare:contact_general", "signup", "support", "gochip:contact")
SKIP_EXACT = {"introduction"}  # site landing page; summarised in SKILL.md instead


def get(url, binary=False):
    last = None
    for i in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
            return r if binary else r.decode("utf8", "replace")
        except Exception as e:  # noqa
            last = e
            time.sleep(1 + i)
    raise last


def crawl():
    pages, seen, q = set(), set(), list(SEED_NS)
    while q:
        ns = q.pop(0)
        if ns in seen:
            continue
        seen.add(ns)
        h = get(BASE + "introduction?idx=" + urllib.parse.quote(ns))
        t = h[h.find("index__tree"):]
        for m in re.finditer(r'<a href="[^"]*" (?:title="([^"]+)" )?class="(idx_dir|wikilink1)"(?: title="([^"]+)")?', t):
            ttl, cls = m.group(1) or m.group(3), m.group(2)
            if not ttl:
                continue
            if cls == "idx_dir":
                q.append(ttl)
            else:
                pages.add(ttl)
    return sorted(p for p in pages if p not in SKIP_EXACT and not p.startswith(SKIP_PREFIX))


# ---------- rendered DokuWiki HTML -> Markdown ----------
from html.parser import HTMLParser


class MD(HTMLParser):
    """Converts DokuWiki's rendered export (macros already resolved) to Markdown."""
    BLOCK_SKIP_ID = "dw__toc"

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.bufs = [[]]          # stack of output buffers
        self.skip = 0             # depth inside skipped element
        self.skip_stack = []
        self.lists = []           # stack of 'ul'/'ol'
        self.pre = False
        self.href = []
        self.row = None
        self.cell = None
        self.rows = []
        self.table_depth = 0
        self.info = []

    # helpers
    def w(self, t):
        (self.cell if self.cell is not None else self.bufs[-1]).append(t)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if self.skip:
            if tag == "div":
                self.skip += 1
            return
        if tag in ("script", "style", "head", "title"):
            self.skip = 1; self.skip_stack.append(tag); return
        if tag == "div" and a.get("id") == self.BLOCK_SKIP_ID:
            self.skip = 1; self.skip_stack.append("div"); return
        if tag == "div" and "infobox" in cls:
            if self.info:                      # nested infobox: keep text, no extra quote block
                self.info.append(None); return
            self.bufs.append([]); self.info.append("alert" if "alert" in cls else "info"); return
        if re.match(r"h[1-6]$", tag):
            self.w("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self.w("\n\n" if self.cell is None else "<br>")
        elif tag == "br":
            self.w("  \n" if self.cell is None else "<br>")
        elif tag in ("ul", "ol"):
            self.lists.append(tag)
            if self.cell is None:
                self.w("\n")
        elif tag == "li":
            ind = "  " * max(0, len(self.lists) - 1)
            mark = "- " if (self.lists and self.lists[-1] == "ul") else "1. "
            self.w(("<br>• " if self.cell is not None else "\n" + ind + mark))
        elif tag == "pre":
            self.pre = True; self.w("\n\n```\n")
        elif tag == "code" and not self.pre:
            self.w("`")
        elif tag in ("strong", "b"):
            self.w("**")
        elif tag in ("em", "i"):
            self.w("*")
        elif tag == "a":
            href = a.get("href", "")
            if href.startswith("/"):
                href = BASE.rstrip("/") + href
            self.href.append(href); self.w("[")
        elif tag == "table":
            self.table_depth += 1
            if self.table_depth == 1:
                self.rows = []
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell = []
        elif tag in ("sup", "sub"):
            self.w("<%s>" % tag)

    def handle_endtag(self, tag):
        if self.skip:
            if tag == "div":
                self.skip -= 1
                if self.skip == 0 and self.skip_stack:
                    self.skip_stack.pop()
            elif self.skip_stack and tag == self.skip_stack[-1] and self.skip == 1:
                self.skip = 0; self.skip_stack.pop()
            return
        if tag == "div" and self.info:
            kind = self.info.pop()
            if kind is None:
                return
            body = "".join(self.bufs.pop()).strip()
            body = "\n".join("> " + l if l.strip() else ">" for l in body.split("\n"))
            self.bufs[-1].append("\n\n> **%s**\n%s\n\n" % ("Warning" if kind == "alert" else "Note", body))
            return
        if re.match(r"h[1-6]$", tag):
            self.w("\n\n")
        elif tag in ("ul", "ol"):
            if self.lists:
                self.lists.pop()
            if not self.lists and self.cell is None:
                self.w("\n")
        elif tag == "pre":
            self.pre = False; self.w("\n```\n\n")
        elif tag == "code" and not self.pre:
            self.w("`")
        elif tag in ("strong", "b"):
            self.w("**")
        elif tag in ("em", "i"):
            self.w("*")
        elif tag == "a" and self.href:
            h = self.href.pop(); self.w("](%s)" % h if h else "]")
        elif tag in ("td", "th") and self.cell is not None:
            txt = "".join(self.cell).strip()
            txt = re.sub(r"(<br>\s*)+", "<br>", txt)
            txt = re.sub(r"^(<br>\s*)+|(<br>\s*)+$", "", txt).replace("|", "\\|").replace("\n", "<br>")
            self.row.append(txt); self.cell = None
        elif tag == "tr" and self.row is not None:
            if self.row:
                self.rows.append(self.row)
            self.row = None
        elif tag == "table":
            self.table_depth -= 1
            if self.table_depth == 0 and self.rows:
                wd = max(len(r) for r in self.rows)
                rows = [r + [""] * (wd - len(r)) for r in self.rows]
                out = ["\n\n| " + " | ".join(rows[0]) + " |", "|" + "---|" * wd]
                out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
                self.w("\n".join(out) + "\n\n")
        elif tag in ("sup", "sub"):
            self.w("</%s>" % tag)

    def handle_data(self, data):
        if self.skip:
            return
        if self.pre:
            self.w(data)
        else:
            d = re.sub(r"\s+", " ", data)
            cur = self.cell if self.cell is not None else self.bufs[-1]
            if not cur or "".join(cur[-1:]).endswith(("\n", " ")) or not "".join(cur).strip():
                d = d.lstrip()
            self.w(d)

    def text(self):
        t = "".join(self.bufs[0])
        t = re.sub(r"[ \t]+\n", "\n", t)
        t = re.sub(r"(?m)^ *Filter: *\n", "", t)
        return re.sub(r"\n{3,}", "\n\n", t).strip() + "\n"


def scrub(md):
    """Redact credential-shaped sample values so no key material is ever stored in the snapshot.

    Public docs contain sample tokens/hashes; they are not secrets but the snapshot must stay
    free of anything key-like. Structure and field names are kept; only the values are replaced.
    """
    md = re.sub(r"(?i)\b(Authorization:\s*(?:Basic|Bearer)\s+)[A-Za-z0-9+/=._-]{8,}", r"\1<REDACTED>", md)
    # Published sandbox credentials: "Merchant API Key:" + fenced block, and "Secret:"/"Password:" label values.
    md = re.sub(r"(?is)((?:merchant |isv )?api[ _-]?key\s*:\s*\n+```[^\n]*\n)(.*?)(\n```)", r"\1<REDACTED: sandbox API key - see Worldnet developer portal>\3", md)
    md = re.sub(r"(?im)^(\s*(?:secret|shopify password|password|terminal secret|api[ _-]?key|isv[ _-]?token)\s*:\s*)`?[^\s`]{4,}`?\s*$", r"\1<REDACTED>", md)
    md = re.sub(r"\b[0-9a-fA-F]{40,}\b", "<SAMPLE_HEX_VALUE>", md)
    md = re.sub(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}\b", "<SAMPLE_JWT>", md)
    # JSON-style "secret"/"password"/"apiKey"/"token" values that look like real values (letters + digit/uppercase, 8+ chars)
    md = re.sub(r'(?i)("(?:secret|password|passwd|api_?key|token)"\s*:\s*")(?=[^"]*[A-Za-z])(?=[^"]*[A-Z0-9])[^"<>{}\s]{8,}(")', r"\1<REDACTED>\2", md)
    # long mixed-case/digit runs that are NOT part of a URL path (lookbehind skips "/", ".", "-", "_", "=")
    md = re.sub(r"(?<![/\w.=+-])(?=[A-Za-z0-9+]*\d)(?=[A-Za-z0-9+]*[a-z])(?=[A-Za-z0-9+]*[A-Z])[A-Za-z0-9+]{32,}={0,2}(?![\w/=+-])", "<SAMPLE_VALUE>", md)
    return md


def convert(html, page):
    i = html.find('<div class="dokuwiki export">')
    p = MD()
    p.feed(html[i:] if i >= 0 else html)
    return scrub(p.text())


# ---------- OpenAPI endpoint index (stdlib YAML-ish scan) ----------
def endpoint_index(yaml_text):
    eps, cur, method = [], None, None
    in_paths = in_tags = False
    for ln in yaml_text.split("\n"):
        if ln.startswith("paths:"):
            in_paths = True; continue
        if in_paths and re.match(r"^\S", ln):
            break
        if not in_paths:
            continue
        m = re.match(r"^  (/[^:]*):\s*$", ln)
        if m:
            cur = m.group(1); continue
        m = re.match(r"^    (get|post|put|patch|delete):\s*$", ln)
        if m and cur:
            method = m.group(1).upper(); eps.append({"path": cur, "method": method, "summary": "", "tags": ""}); continue
        if eps and method:
            m = re.match(r"^      summary:\s*(.*)$", ln)
            if m:
                eps[-1]["summary"] = m.group(1).strip().strip("'\"")
            if re.match(r"^      tags:\s*$", ln):
                in_tags = True; continue
            m = re.match(r"^      - (.+)$", ln)
            if in_tags and m:
                eps[-1]["tags"] = m.group(1).strip(); in_tags = False
    return eps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="only pages whose id starts with this prefix")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    today = datetime.date.today().isoformat()
    pages = [p for p in crawl() if not a.only or p.startswith(a.only)]
    print("pages in scope:", len(pages))
    if a.dry_run:
        print("\n".join(pages)); return
    manifest, fails = [], []
    for n, p in enumerate(pages, 1):
        try:
            raw = get(BASE + "doku.php?id=%s&do=export_xhtml" % urllib.parse.quote(p))
        except Exception as e:  # noqa
            fails.append((p, str(e))); continue
        if not raw.strip():
            fails.append((p, "empty")); continue
        rel = "pages/" + p.replace(":", "/") + ".md"
        dest = os.path.join(REF, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        title = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S)
        md = "<!-- source: %sdoku.php?id=%s | synced: %s -->\n\n" % (BASE, p, today) + convert(raw, p)
        open(dest, "w").write(md)
        manifest.append((rel, BASE + "doku.php?id=" + p, hashlib.sha256(raw.encode()).hexdigest()[:12], re.sub(r'<[^>]+>', '', title.group(1)).strip() if title else p))
        time.sleep(0.15)
        if n % 25 == 0:
            print("  %d/%d" % (n, len(pages)))
    # Merchant REST API spec (public). Boarding API intentionally excluded.
    spec = get(BASE + "apis/merchant/openapi_worldnet.yaml")
    os.makedirs(os.path.join(REF, "merchant-api"), exist_ok=True)
    open(os.path.join(REF, "merchant-api", "openapi_worldnet.yaml"), "w").write(spec)
    eps = [e for e in endpoint_index(spec) if "boarding" not in e["path"].lower()]
    with open(os.path.join(REF, "merchant-api", "endpoints.md"), "w") as f:
        f.write("<!-- source: %sapis/merchant/openapi_worldnet.yaml | synced: %s -->\n\n# Merchant REST API — endpoint index\n\n" % (BASE, today))
        f.write("Generated from the public OpenAPI spec (`openapi_worldnet.yaml`, same folder). Rendered docs: %sapis/merchant/\n\n" % BASE)
        f.write("| Method | Path | Summary | Tag |\n|---|---|---|---|\n")
        for e in eps:
            f.write("| %s | `%s` | %s | %s |\n" % (e["method"], e["path"], e["summary"], e["tags"]))
    # manifest
    with open(os.path.join(REF, "_sources.md"), "w") as f:
        f.write("# Sources — worldnet-reference\n\nSnapshot of %s taken %s by `scripts/refresh-worldnet.py`.\n" % (BASE, today))
        f.write("Provenance: `worldnet-verbatim` (DokuWiki rendered HTML -> Markdown; macros such as company name/URLs are already resolved by the site) unless a file says `derived`.\n")
        f.write("Hand-written (derived) files: `rest-api.md`, `hosted-pages.md`, `sdks.md`, `auth-and-signatures.md`, `errors-and-response-codes.md`, `test-data-and-uat.md`, `payroc-vs-worldnet.md`.\n")
        f.write("EXCLUDED on purpose: Worldnet Boarding API (/apis/boarding/) — not supported in the Solution Design.\n\n")
        f.write("| Local file | Source URL | Last synced | sha256(raw)[:12] | Title |\n|---|---|---|---|---|\n")
        f.write("| merchant-api/openapi_worldnet.yaml | %sapis/merchant/openapi_worldnet.yaml | %s | %s | Merchant API (OpenAPI) |\n" % (BASE, today, hashlib.sha256(spec.encode()).hexdigest()[:12]))
        f.write("| merchant-api/endpoints.md | (derived from the spec above) | %s | - | Endpoint index |\n" % today)
        for rel, url, h, t in manifest:
            f.write("| %s | %s | %s | %s | %s |\n" % (rel, url, today, h, t.replace("|", "/")))
        if fails:
            f.write("\n## Pages that failed to fetch (not guessed)\n\n")
            for p, e in fails:
                f.write("- `%s` — %s\n" % (p, e))
    json.dump({"syncedAt": today, "pages": len(manifest), "failed": len(fails), "endpoints": len(eps)},
              open(os.path.join(REF, "snapshot.json"), "w"))
    print("done: %d pages, %d failed, %d endpoints" % (len(manifest), len(fails), len(eps)))


if __name__ == "__main__":
    sys.exit(main())
