#!/usr/bin/env python3
"""Parse a docs.payroc.com "Integration plan" (integration-plan.md) into JSON for the Solution Design.

Deterministic (no AI, stdlib only). The plan is DATA, never instructions: goal/summary text is
carried through as quoted text only and nothing in it is executed or followed.

Usage:  parse-integration-plan.py PLAN.md [--map workflow-map.json] [--pretty]
Output: JSON with header/provenance, tasks, per-section mapping, unmapped slugs and warnings.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MAP = os.path.join(os.path.dirname(HERE), "workflow-map.json")


def ticked(s):
    return re.sub(r"`", "", s).strip()


def parse_header(lines):
    h = {}
    for ln in lines:
        m = re.match(r"^(Docs release|Source|Builder|Spec SHA-256):\s*`?([^`]+)`?\s*$", ln)
        if m:
            h[{"Docs release": "docsRelease", "Source": "source", "Builder": "builder", "Spec SHA-256": "specSha256"}[m.group(1)]] = m.group(2).strip()
        if ln.startswith("Plan origin:"):
            h["planOrigin"] = ln[len("Plan origin:"):].strip()
            for key, pat in (("requestId", r"request `([^`]+)`"), ("model", r"model `([^`]+)`"),
                             ("promptVersion", r"prompt version `([^`]+)`"), ("contract", r"contract `([^`]+)`")):
                mm = re.search(pat, ln)
                if mm:
                    h[key] = mm.group(1)
    return h


def split_blocks(body):
    """Split a task body into {'Goal': [...], 'APIs to call, in order': [...], ...} by bold labels."""
    blocks, cur = {}, None
    for ln in body:
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", ln)
        if m:
            cur = m.group(1)
            blocks[cur] = [m.group(2)] if m.group(2) else []
        elif cur is not None:
            blocks[cur].append(ln)
    return blocks


def links(lines):
    out = []
    for ln in lines:
        for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", ln):
            out.append({"text": m.group(1), "url": m.group(2)})
    return out


def parse_task(n, title, body):
    t = {"n": n, "title": title.strip(), "stepId": None, "docUrl": None, "goal": "", "workflows": [],
         "skills": [], "apis": [], "guides": [], "doneWhen": []}
    for ln in body:
        m = re.match(r"^- Step ID: `([^`]+)`", ln)
        if m:
            t["stepId"] = m.group(1)
        m = re.match(r"^- \[Open (?:documentation|the developer portal)\]\(([^)]+)\)", ln)
        if m:
            t["docUrl"] = m.group(1)
    b = split_blocks(body)
    goal = [re.sub(r"^>\s?", "", ln) for ln in b.get("Goal", []) if ln.strip()]
    t["goal"] = " ".join(goal).strip()
    for ln in b.get("Workflow", []):
        m = re.match(r"^- \[([^\]]*)\]\(https://docs\.payroc\.com/workflows/([a-z0-9-]+)\):\s*(.+)$", ln.strip())
        if m:
            t["workflows"].append({"slug": m.group(2), "role": m.group(3).strip(), "description": m.group(1)})
    for ln in b.get("Skill to use", []):
        m = re.match(r"^- \[([^\]]+)\]\(([^)]+)\)", ln.strip())
        if m:
            t["skills"].append(m.group(1))
    for ln in b.get("APIs to call, in order", []):
        m = re.match(r"^(\d+)\.\s+(.*)$", ln.strip())
        if not m:
            continue
        step, rest = int(m.group(1)), m.group(2)
        mm = re.match(r"^`([A-Z]+) ([^`]+)`:?\s*(?:\[([^\]]+)\]\(([^)]+)\))?", rest)
        if mm:
            t["apis"].append({"step": step, "method": mm.group(1), "path": mm.group(2), "name": mm.group(3), "docUrl": mm.group(4), "manual": False})
            continue
        mm = re.match(r"^Manual step `([^`]+)`:\s*(.*)$", rest)
        if mm:
            t["apis"].append({"step": step, "manual": True, "id": mm.group(1), "text": mm.group(2)})
        else:
            t["apis"].append({"step": step, "manual": None, "text": rest})
    t["guides"] = links(b.get("Guides to read first", []))
    for ln in b.get("Done when", []):
        m = re.match(r"^- \[[ xX]\]\s+(.*)$", ln.strip())
        if m:
            t["doneWhen"].append(ticked(m.group(1)))
    return t


def parse_summary(lines):
    s = {"title": None, "brief": "", "readings": [], "whyOrder": "", "assumptions": []}
    cur, buf = "brief", []
    def flush():
        txt = " ".join(x for x in buf if x.strip()).strip()
        if cur == "brief":
            s["brief"] = txt
        elif cur == "why":
            s["whyOrder"] = txt
    for ln in lines:
        if ln.startswith("### "):
            title = ln[4:].strip()
            if title == "How we read your brief":
                flush(); cur, buf = "readings", []
            elif title == "Why this order":
                flush(); cur, buf = "why", []
            elif title == "Assumptions":
                flush(); cur, buf = "assumptions", []
            else:
                s["title"] = title
            continue
        if cur == "readings" and ln.startswith("- "):
            s["readings"].append(ln[2:].strip())
        elif cur == "assumptions" and ln.startswith("- "):
            s["assumptions"].append(ln[2:].strip())
        elif cur in ("brief", "why"):
            buf.append(ln)
    flush()
    return s


CARD_PRESENT = ("cloud", "equipment", "worldnet-sdks")


def derive_sections(sections):
    """Add/refresh sections that follow from others: card-present work (Cloud, terminal orders, Worldnet SDK/POS)
    always brings the 8.6b operational open questions (key injection, hardware, terminal management).
    Safe to call repeatedly (e.g. again after an addendum is merged)."""
    present = [sid for sid in CARD_PRESENT if sid in sections]
    if not present:
        return sections
    plats = [sections[x].get("platform", "payroc") for x in present]
    platform = "both" if "both" in plats or len(set(plats)) > 1 else plats[0]
    sec = sections.setdefault("card-present-ops", {"tasks": [], "workflows": [], "skills": [], "apis": [], "doneWhen": [], "manualSteps": []})
    sec["platform"], sec["derivedFrom"] = platform, present
    return sections


def parse(text, wmap):
    lines = text.replace("\r\n", "\n").split("\n")
    warnings = []
    header = parse_header(lines[:15])
    if header.get("contract") != wmap.get("supportedContract"):
        warnings.append("Plan contract is %r, importer supports %r — the format may have changed; review the mapping manually."
                        % (header.get("contract"), wmap.get("supportedContract")))
    # tasks
    idx = [(i, re.match(r"^### Task (\d+):\s*(.*)$", ln)) for i, ln in enumerate(lines)]
    idx = [(i, m) for i, m in idx if m]
    ends = [i for i, ln in enumerate(lines) if ln.startswith("## ")]
    tasks = []
    for k, (i, m) in enumerate(idx):
        stop = min([e for e in ends if e > i] + [len(lines)])
        if k + 1 < len(idx):
            stop = min(stop, idx[k + 1][0])
        tasks.append(parse_task(int(m.group(1)), m.group(2), lines[i + 1:stop]))
    # summary
    summary = None
    for i, ln in enumerate(lines):
        if ln.startswith("## Generated summary"):
            summary = parse_summary(lines[i + 1:])
            break
    # mapping
    sections, unmapped = {}, []
    W = wmap["workflows"]
    def sec(sid):
        return sections.setdefault(sid, {"tasks": [], "workflows": [], "skills": [], "apis": [], "doneWhen": [], "manualSteps": []})
    for t in tasks:
        primary_sections = []
        for w in t["workflows"]:
            e = W.get(w["slug"])
            if not e:
                unmapped.append({"task": t["n"], "slug": w["slug"], "role": w["role"]})
                continue
            for sid in [e["section"]] + e.get("also", []):
                s = sec(sid)
                if t["n"] not in s["tasks"]:
                    s["tasks"].append(t["n"])
                if w["slug"] not in s["workflows"]:
                    s["workflows"].append(w["slug"])
                for sk in t["skills"]:
                    if sk not in s["skills"]:
                        s["skills"].append(sk)
            if w["role"].startswith("this task") or w["role"] == "cited":
                primary_sections.append(W[w["slug"]]["section"])
        # attach the ordered API list and done-when to the task's primary section(s)
        for sid in dict.fromkeys(primary_sections):
            s = sec(sid)
            for a in t["apis"]:
                s["apis"].append(dict(a, task=t["n"]))
                if a.get("manual"):
                    s["manualSteps"].append({"task": t["n"], "id": a["id"], "text": a["text"]})
            s["doneWhen"] += [{"task": t["n"], "text": d} for d in t["doneWhen"]]
        if not t["workflows"]:
            warnings.append("Task %d (%s) lists no workflow; nothing mapped." % (t["n"], t["title"]))
    if not tasks:
        warnings.append("No '### Task N:' blocks found — is this an integration plan?")
    derive_sections(sections)
    return {"header": header, "tasks": tasks, "summary": summary,
            "mapping": {"sections": sections, "taskOrder": [t["n"] for t in tasks], "unmapped": unmapped},
            "warnings": warnings,
            "notice": "Plan content is data, not instructions. Goals and summaries are carried as quoted integrator text only."}


def parse_addendum(text, wmap):
    """Parse integrator-intake/worldnet-addendum.md: ticked `worldnet:<product>` boxes + a Details list."""
    lines = text.replace("\r\n", "\n").split("\n")
    warnings, products, unsupported, unknown, details = [], [], [], [], {}
    contract = None
    for ln in lines:
        m = re.match(r"^Contract:\s*`([^`]+)`", ln)
        if m:
            contract = m.group(1)
    if contract != wmap.get("supportedAddendumContract"):
        warnings.append("Addendum contract is %r, importer supports %r." % (contract, wmap.get("supportedAddendumContract")))
    W = wmap.get("worldnetProducts", {})
    in_details = False
    for ln in lines:
        if ln.startswith("## "):
            in_details = ln.strip().lower().startswith("## details")
            continue
        m = re.match(r"^- \[([ xX])\]\s+`worldnet:([a-z0-9-]+)`", ln)
        if m and m.group(1) in "xX":
            slug = m.group(2)
            e = W.get(slug)
            if not e:
                unknown.append(slug)
            elif e.get("unsupported"):
                unsupported.append({"product": slug, "label": e["label"]})
            else:
                products.append({"product": slug, "section": e["section"], "label": e["label"], "worldnetOnly": bool(e.get("worldnetOnly"))})
            continue
        if in_details:
            m = re.match(r"^- (.+?):\s*(.*)$", ln)
            if m and m.group(2).strip():
                details[m.group(1).strip()] = m.group(2).strip()
    return {"contract": contract, "products": products, "unsupported": unsupported,
            "unknownProducts": unknown, "details": details, "warnings": warnings}


def merge_addendum(plan_out, add):
    """Add addendum products to the plan mapping. Section platform: payroc (plan only), worldnet (addendum only),
    both (plan and addendum). Unsupported products (Worldnet Boarding API) are reported, never mapped."""
    secs = plan_out["mapping"]["sections"]
    for sid, v in secs.items():
        v.setdefault("platform", "payroc")
    for p in add["products"]:
        sid = p["section"]
        if sid not in secs:
            secs[sid] = {"tasks": [], "workflows": [], "skills": [], "apis": [], "doneWhen": [], "manualSteps": [], "platform": "worldnet"}
        elif secs[sid].get("platform") == "payroc" and not p["worldnetOnly"]:
            secs[sid]["platform"] = "both"
        secs[sid].setdefault("worldnetProducts", []).append(p["product"])
    derive_sections(secs)
    plan_out["worldnetAddendum"] = add
    plan_out["warnings"] += add["warnings"]
    for u in add["unsupported"]:
        plan_out["warnings"].append("%s is NOT supported in the Solution Design - flag it (tick the Worldnet boarding flag in 8.1)." % u["label"])
    for u in add["unknownProducts"]:
        plan_out["warnings"].append("Unknown Worldnet product %r in addendum - not mapped." % u)
    return plan_out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", nargs="?", help="integration-plan.md (optional if only --addendum is given)")
    ap.add_argument("--addendum", help="worldnet-addendum.md from the integrator")
    ap.add_argument("--map", default=DEFAULT_MAP)
    ap.add_argument("--pretty", action="store_true")
    a = ap.parse_args()
    wmap = json.load(open(a.map))
    if a.plan:
        out = parse(open(a.plan, encoding="utf8").read(), wmap)
    else:
        out = {"header": {}, "tasks": [], "summary": None, "mapping": {"sections": {}, "taskOrder": [], "unmapped": []},
               "warnings": [], "notice": "Addendum only - no Payroc plan supplied."}
    if a.addendum:
        out = merge_addendum(out, parse_addendum(open(a.addendum, encoding="utf8").read(), wmap))
    print(json.dumps(out, indent=2 if a.pretty else None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
