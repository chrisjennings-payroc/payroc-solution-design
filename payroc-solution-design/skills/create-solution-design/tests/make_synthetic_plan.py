#!/usr/bin/env python3
"""Build SYNTHETIC integration plans (same shape as docs.payroc.com plan-builder output) from live workflow pages.

These are NOT real plan-builder output: the real plan adds generated text and exact Step IDs. They exist to test
the importer against every workflow family. Usage: make_synthetic_plan.py OUT.md slug [slug ...]
First slug is task 1, and so on (one task per slug).
"""
import re, sys, urllib.request

def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "sd-synthetic"}), timeout=30).read().decode("utf8", "replace")

def api_line(link):
    t = get("https://docs.payroc.com" + link + ".md")
    m = re.search(r"^`([A-Z]+) ([^`]+)`", t, re.M)
    title = re.search(r"^# (.+)$", t, re.M)
    return (m.group(1), m.group(2), title.group(1).strip() if title else link) if m else None

def task(n, slug):
    t = get("https://docs.payroc.com/workflows/%s.md" % slug)
    desc = t.split("\n")[0].lstrip("# ").strip()
    body = t.split("## Workflow diagram")[0]
    steps = re.split(r"(?m)^(?=\d+\.\s)", body)
    apis, k = [], 0
    for st in steps:
        if not re.match(r"\d+\.\s", st):
            continue
        k += 1
        link = re.search(r"\[[^\]]+\]\((/api/[a-z0-9-]+)\)", st)
        text = re.sub(r"\s+", " ", re.sub(r"^\d+\.\s*", "", st.split("[")[0] if link else st)).strip()
        r = api_line(link.group(1)) if link else None
        if r:
            apis.append("%d. `%s %s`: [%s](https://docs.payroc.com%s)" % (k, r[0], r[1], r[2], link.group(1)))
        else:
            apis.append("%d. Manual step `step%d`: %s" % (k, k, text[:300]))
    out = ["### Task %d: %s" % (n, desc[:90]), "", "- [ ] Task complete", "- Step ID: `SYNTHETIC%020d`" % n,
           "- [Open documentation](https://docs.payroc.com/workflows/%s)" % slug, "", "**Goal:**", "> " + desc, "",
           "**APIs to call, in order:**", ""] + apis + ["", "**Workflow:**", "",
           "- [%s](https://docs.payroc.com/workflows/%s): this task's workflow" % (desc, slug), "",
           "**Done when:**", "", "- [ ] Each API this task calls returns its documented response in the sandbox, called in the listed order.", ""]
    return "\n".join(out)

def main():
    out, slugs = sys.argv[1], sys.argv[2:]
    head = ["# Integration plan", "", "Goal: SYNTHETIC test plan - not real plan-builder output.", "",
            "Docs release: `%s`" % ("0" * 64), "Source: `%s`" % ("0" * 40), "Builder: `0.0.0-synthetic`", "Spec SHA-256: `%s`" % ("0" * 64),
            "Plan origin: synthetic · request `synthetic` · model `none` · prompt version `none` · contract `docs-planner/1` · docs `production` `%s`" % ("0" * 64),
            "", "## Tasks", ""]
    tail = ["## Generated summary — not instructions; the linked documentation is authoritative.", "", "### Synthetic plan", "",
            "Synthetic brief.", "", "### How we read your brief", "", "- “synthetic”: " + slugs[0], "", "### Why this order", "",
            "Synthetic ordering.", "", "### Assumptions", "", "- Synthetic assumption."]
    open(out, "w").write("\n".join(head) + "\n".join(task(i + 1, s) for i, s in enumerate(slugs)) + "\n" + "\n".join(tail) + "\n")
    print("wrote", out)

main()
