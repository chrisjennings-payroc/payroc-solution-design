#!/usr/bin/env python3
"""Tests for review-sd.py SDK (8.2f) checks and key-material detection. Stdlib only."""
import os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "scripts", "review-sd.py")
fails = 0


def check(cond, msg):
    global fails
    print(("PASS  " if cond else "FAIL  ") + msg)
    if not cond:
        fails += 1


def review(html, md="---\npartner: \"Acme\"\n---\n<!-- sd:section=worldnet-sdks -->\n"):
    d = tempfile.mkdtemp()
    h = os.path.join(d, "Acme-Solution-Design.html")
    open(h, "w", encoding="utf8").write(html)
    open(os.path.join(d, "Acme-Solution-Design.md"), "w", encoding="utf8").write(md)
    r = subprocess.run([sys.executable, "-I", SCRIPT, h], capture_output=True, text=True)
    return r.returncode, r.stdout


def page(sdk_body, extra_sections=""):
    return ('<html><body><main>'
            '<section id="worldnet-sdks" data-platform="worldnet"><div class="subsection-scope">'
            '<input type="checkbox" checked></div>%s</section>%s</main></body></html>' % (sdk_body, extra_sections))


rc, out = review(page('<p class="fill" contenteditable="true">{{SDK version}}</p>'))
check("8.2f (Worldnet SDK) is in scope but has 1 unresolved" in out, "unresolved SDK fields are reported")
check("8.6b Card-present operational requirements was removed" in out, "missing 8.6b is reported when SDK in scope")
check("Section 9" in out, "missing go-live section is reported when SDK in scope")

rc, out = review(page('<p class="fill filled">1.6.89</p>',
                      '<section id="card-present-ops"></section><section id="golive"></section>'))
check("8.2f (Worldnet SDK)" not in out, "resolved SDK section has no 8.2f warnings")

# key material must be flagged (values below are made-up, non-sensitive test patterns)
rc, out = review(page('<p class="fill filled">KSI: ABCDEF123456 and 0123456789abcdef0123456789abcdef</p>'))
check(rc == 1 and "key identifier / KCV" in out, "KSI/KCV value is flagged as an error")
rc, out = review(page('<p class="fill filled">0123456789abcdef0123456789abcdef</p>'))
check(rc == 1 and "hex key component" in out, "32-hex key component is flagged")

print("%d failure(s)" % fails)
sys.exit(1 if fails else 0)
