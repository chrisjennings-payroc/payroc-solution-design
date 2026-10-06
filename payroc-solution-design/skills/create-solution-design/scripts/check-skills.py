#!/usr/bin/env python3
"""Check local Payroc skills against https://github.com/payroc/skills (main).

Step 0 of the create-solution-design skill. Uses ONE public GitHub API call
(git tree, recursive) and compares git blob SHAs of every file in each mapped
skill folder against the local copy. No secrets are used or needed.

Usage:
  check-skills.py [--skills-dir DIR] [--sections id,id,...] [--json] [--record]

Exit codes: 0 = all checked skills current, 1 = stale/missing skills found,
            2 = could not verify (offline / rate-limited / API error).
"""
import argparse, hashlib, json, os, sys, urllib.request, urllib.error
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
MAP = json.load(open(os.path.join(SKILL_DIR, "skill-map.json")))
UP = MAP["upstream"]
API = "https://api.github.com/repos/%s" % UP["repo"]
# Files that exist only locally by design (provenance manifests we write).
IGNORE_LOCAL = {"_sources.md"}


def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                               "User-Agent": "payroc-sd-skill-check"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def detect_skills_dir():
    """Pick the candidate folder that contains the most skills named in skill-map.json.

    Candidates: the folder next to this skill (project install), ./.claude/skills (current project),
    ~/.claude/skills and ~/.agents/skills (user-level installs from `npx skills add`).
    """
    names = {n for sec in MAP["sections"].values() for n in sec["skills"]}
    cands = [os.path.dirname(SKILL_DIR), os.path.join(os.getcwd(), ".claude", "skills"),
             os.path.join(os.getcwd(), ".agents", "skills"),
             os.path.expanduser("~/.claude/skills"), os.path.expanduser("~/.agents/skills")]
    best, best_n = cands[0], -1
    for c in cands:
        n = sum(1 for x in names if os.path.isdir(os.path.join(c, x)))
        if n > best_n:
            best, best_n = c, n
    return best, best_n, cands


def blob_sha(path):
    data = open(path, "rb").read()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-dir", help="folder holding the installed Payroc skills (default: auto-detect)")
    ap.add_argument("--sections", help="comma-separated section ids to check (default: all)")
    ap.add_argument("--record", action="store_true", help="write skills-upstream.json")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    searched = []
    if a.skills_dir:
        skills_dir = a.skills_dir
    else:
        skills_dir, found, searched = detect_skills_dir()
        if found == 0:
            msg = ("No Payroc skills were found. Searched: %s. If you installed them with `npx skills add payroc/skills --agent claude-code`, "
                   "run this from that project folder or pass --skills-dir DIR; otherwise install them first." % ", ".join(searched))
            if a.json:
                print(json.dumps({"result": "stale", "reason": "no-skills-found", "searched": searched, "message": msg}))
            else:
                print("NO SKILLS FOUND: " + msg)
                print("RESULT: stale -> run: npx skills add payroc/skills --agent claude-code   (then re-run this check)")
            return 1
    wanted = set()
    for sid, s in MAP["sections"].items():
        if not a.sections or sid in a.sections.split(","):
            wanted.update(s["skills"])

    try:
        head = get("%s/commits/%s" % (API, UP["ref"]))
        tree = get("%s/git/trees/%s?recursive=1" % (API, head["sha"]))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, KeyError, ValueError) as e:
        out = {"result": "not-verified", "reason": str(e)}
        print(json.dumps(out) if a.json else "NOT VERIFIED: could not reach GitHub (%s). Proceed, but mark skills as not verified in the SD." % e)
        return 2

    # upstream: skill name -> {relpath: blobsha}
    root = UP["skillsRoot"] + "/"
    up = {}
    for t in tree["tree"]:
        if t["type"] != "blob" or not t["path"].startswith(root) or "/skills/" not in t["path"]:
            continue
        after = t["path"].split("/skills/", 1)[1]
        name, _, rel = after.partition("/")
        if rel:
            up.setdefault(name, {})[rel] = t["sha"]

    mapped = {s for sec in MAP["sections"].values() for s in sec["skills"]}
    known = mapped | set(MAP.get("unmappedOk", [])) | set(MAP.get("localOnly", []))
    report = {"commit": head["sha"], "commitDate": head["commit"]["committer"]["date"],
              "checkedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "current": [], "stale": {}, "missing": [], "notUpstream": [],
              "newUnmappedUpstream": sorted(set(up) - known)}

    for name in sorted(wanted):
        local = os.path.join(skills_dir, name)
        if name not in up:
            report["notUpstream"].append(name)
            continue
        if not os.path.isdir(local):
            report["missing"].append(name)
            continue
        diffs = []
        for rel, sha in up[name].items():
            lp = os.path.join(local, rel)
            if not os.path.isfile(lp):
                diffs.append("missing locally: " + rel)
            elif blob_sha(lp) != sha:
                diffs.append("differs: " + rel)
        for dp, _, fs in os.walk(local):
            for f in fs:
                rel = os.path.relpath(os.path.join(dp, f), local)
                if rel not in up[name] and f not in IGNORE_LOCAL and not f.startswith("."):
                    diffs.append("local-only: " + rel)
        if diffs:
            report["stale"][name] = diffs
        else:
            report["current"].append(name)

    ok = not report["stale"] and not report["missing"]
    report["result"] = "current" if ok else "stale"

    if a.record:
        # Best effort: an installed plugin directory is read-only, so a failure here is not an error —
        # the same data is in the --json output, which is what gets stamped into the SD's provenance.
        try:
            json.dump({k: report[k] for k in ("commit", "commitDate", "checkedAt", "result")} |
                      {"repo": UP["repo"], "ref": UP["ref"]},
                      open(os.path.join(SKILL_DIR, "skills-upstream.json"), "w"), indent=2)
        except OSError:
            print("note: could not write skills-upstream.json (read-only install); use --json output instead", file=sys.stderr)

    if a.json:
        print(json.dumps(report, indent=2))
    else:
        print("Upstream %s@%s  commit %s (%s)" % (UP["repo"], UP["ref"], head["sha"][:7], report["commitDate"]))
        print("Local skills folder: %s" % skills_dir)
        print("Checked %d skills: %d current" % (len(wanted), len(report["current"])))
        for n, d in report["stale"].items():
            print("  STALE   %s" % n)
            for x in d[:5]:
                print("            - " + x)
            if len(d) > 5:
                print("            - ... +%d more" % (len(d) - 5))
        for n in report["missing"]:
            print("  MISSING %s" % n)
        for n in report["notUpstream"]:
            print("  NOTE    %s is in skill-map.json but not upstream (renamed/removed?)" % n)
        if report["newUnmappedUpstream"]:
            print("  NEW upstream skills not in skill-map.json: " + ", ".join(report["newUnmappedUpstream"]))
        if ok:
            print("RESULT: current")
        else:
            print("RESULT: stale -> run: npx skills add payroc/skills --agent claude-code   (then re-run this check)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
