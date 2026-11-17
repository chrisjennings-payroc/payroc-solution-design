#!/usr/bin/env python3
"""Fixture tests for scripts/parse-integration-plan.py. Run: python3 tests/test_parse.py"""
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("pip", os.path.join(ROOT, "scripts", "parse-integration-plan.py"))
pip = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pip)
WMAP = json.load(open(os.path.join(ROOT, "workflow-map.json")))


def load(name):
    return pip.parse(open(os.path.join(HERE, "fixtures", name), encoding="utf8").read(), WMAP)


def check(cond, msg):
    if not cond:
        print("FAIL:", msg)
        sys.exit(1)
    print("ok  :", msg)


p = load("integration-plan-01.md")
h = p["header"]
check(h["contract"] == "docs-planner/1" and h["builder"] == "0.15.1", "header: contract + builder parsed")
check(h["docsRelease"].startswith("3efc3240"), "header: docs release parsed")
check(not p["warnings"], "no warnings for a supported contract")
check([t["n"] for t in p["tasks"]] == [1, 2, 3], "three tasks in order")
check([t["stepId"] for t in p["tasks"]][0] == "01M46F17B9K43543KP2H3YJ79E", "step ids kept")
secs = p["mapping"]["sections"]
check(set(secs) == {"boarding", "hosted-fields", "reporting", "equipment", "card-present-ops"}, "sections in scope: %s" % sorted(secs))
check(not p["mapping"]["unmapped"], "no unmapped workflows")
manual = sum(1 for t in p["tasks"] for a in t["apis"] if a.get("manual"))
check(manual == 6, "6 manual (non-API) steps flagged (got %d)" % manual)
check(sum(1 for a in secs["boarding"]["apis"] if not a.get("manual")) == 8, "8 REST calls under boarding")
check(any(a.get("path") == "/payments" for a in secs["hosted-fields"]["apis"]), "hosted-fields includes POST /payments")
check(any("Idempotency-Key" in d["text"] for d in secs["boarding"]["doneWhen"]), "Done-when criteria carried over (Idempotency-Key)")
check("create-merchant-platform" in secs["boarding"]["skills"], "skills carried over")
check(len(p["summary"]["assumptions"]) == 4, "4 plan assumptions")
check(p["summary"]["readings"], "'How we read your brief' parsed")
check(p["summary"]["whyOrder"].startswith("Boarding must happen"), "'Why this order' parsed")
# changed contract -> warning
bad = pip.parse(open(os.path.join(HERE, "fixtures", "integration-plan-01.md")).read().replace("docs-planner/1", "docs-planner/2"), WMAP)
check(bad["warnings"], "changed contract version produces a warning")
# unknown slug is reported, not guessed
unk = pip.parse(open(os.path.join(HERE, "fixtures", "integration-plan-01.md")).read().replace("collect-with-hosted-fields", "brand-new-workflow"), WMAP)
check(any(u["slug"] == "brand-new-workflow" for u in unk["mapping"]["unmapped"]), "unknown workflow slug listed as unmapped")
print("ALL PASSED")

# ---- Worldnet addendum ----
import copy
add_text = open(os.path.join(HERE, "fixtures", "worldnet-addendum-01.md"), encoding="utf8").read()
add = pip.parse_addendum(add_text, WMAP)
check(not add["warnings"], "addendum: no warnings for supported contract")
check({p["product"] for p in add["products"]} == {"hosted-pages", "rest-api", "sdk-pos"}, "addendum: ticked products parsed")
check(add["unsupported"] and add["unsupported"][0]["product"] == "boarding-api", "addendum: Worldnet Boarding API reported as unsupported")
check(add["details"].get("Processor / acquirer on the Worldnet terminals (Elavon, FDRC, TSYS, unknown)") == "Elavon", "addendum: details captured")
merged = pip.merge_addendum(copy.deepcopy(p), add)
ms = merged["mapping"]["sections"]
check("hpp" in ms and ms["hpp"]["platform"] == "worldnet", "hpp is worldnet-only (not in the Payroc plan)")
check(ms["worldnet-sdks"]["platform"] == "worldnet", "SDK section is worldnet-only")
check(ms["boarding"]["platform"] == "payroc", "boarding stays payroc")
check(any("NOT supported" in w for w in merged["warnings"]), "warning raised for unsupported Worldnet boarding")
# a product that overlaps the Payroc plan becomes 'both'
add2 = pip.parse_addendum(add_text.replace("- [ ] `worldnet:reporting`", "- [x] `worldnet:reporting`"), WMAP)
m2 = pip.merge_addendum(copy.deepcopy(p), add2)
check(m2["mapping"]["sections"]["reporting"]["platform"] == "both", "overlap with the Payroc plan -> platform 'both'")
print("ALL PASSED (incl. addendum)")

# ---- Synthetic plans (built from live docs.payroc.com workflow pages; see make_synthetic_plan.py) ----
EXPECT = {
    "synthetic-hpp.md": {"hpp", "reporting"},
    "synthetic-links-recurring.md": {"payment-links", "recurring"},
    "synthetic-wallets.md": {"wallets", "direct-api"},
    "synthetic-cloud.md": {"cloud", "card-present-ops"},
    "synthetic-funding.md": {"boarding", "funding", "reporting"},
}
for name, want in EXPECT.items():
    sp = load(name)
    got = set(sp["mapping"]["sections"])
    check(got == want, "%s -> sections %s" % (name, sorted(got)))
    check(not sp["mapping"]["unmapped"] and not sp["warnings"], "%s: nothing unmapped, no warnings" % name)
    check(all(t["apis"] for t in sp["tasks"]), "%s: every task has ordered steps" % name)
# every workflow slug in the map must parse as a single-task plan without being 'unmapped'
check(len(WMAP["workflows"]) == 74, "workflow map covers all 74 docs.payroc.com workflow slugs")
print("ALL PASSED (incl. synthetic plans)")

# ---- card-present operational section is derived ----
check(secs["card-present-ops"]["derivedFrom"] == ["equipment"], "card-present-ops derived from equipment (terminal orders)")
check("card-present-ops" not in load("synthetic-hpp.md")["mapping"]["sections"], "no card-present-ops for a pure card-not-present plan")
check("card-present-ops" in ms and "worldnet-sdks" in ms["card-present-ops"]["derivedFrom"], "Worldnet SDK/POS addendum also drives card-present-ops")
solo = pip.merge_addendum(load("synthetic-hpp.md"), pip.parse_addendum(add_text, WMAP))["mapping"]["sections"]
check(solo["card-present-ops"]["derivedFrom"] == ["worldnet-sdks"], "addendum alone (SDK/POS) derives card-present-ops from worldnet-sdks")
print("ALL PASSED (incl. card-present ops)")
