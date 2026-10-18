#!/usr/bin/env python3
"""ECP-OS helper: validate records and compute key-result progress.

Usage (from the vault root, Python 3.8+, no extra packages):
  python3 00-system/tools/ecp.py check            # validate all records against schemas.md
  python3 00-system/tools/ecp.py kr               # compute `current` for active key results
  python3 00-system/tools/ecp.py kr --write       # ...and save it into the key-result files
  python3 00-system/tools/ecp.py kr --cycle 2026-11 --all   # a given cycle, including closed ones

Optional: agents that can't run Python follow the same rules by hand
(schemas.md and the metric_key table in protocols/okr-planning.md).
"""
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIRS = ["01-profile", "02-okr", "03-tasks", "04-daily", "05-reviews",
             "06-library", "07-inbox", "08-output"]

ALLOWED = {
    "onboarding": {"not-started", "in-progress", "complete"},
    "tier": {"light", "steady", "committed", "intensive"},
    "writing_mode": {"typing", "handwriting", "both"},
    "prior_chinese": {"none", "a-little", "some"},
    "area": {"listening-speaking", "vocabulary-reading", "writing", "pronunciation", "confidence-fun"},
    "kind": {"lead", "lag"},
    "task_type": {"learn", "practice", "test", "input", "output", "review", "setup"},
    "origin": {"agent", "learner"},
    "period": {"weekly", "monthly", "quarterly"},
    "pos": {"noun", "verb", "adj", "adv", "measure", "pron", "num", "particle", "conj", "prep", "phrase", "other"},
    "category": {"food", "shopping", "transport", "directions", "lodging", "health", "social", "work",
                 "services", "emergency", "other"},
    "media_type": {"doc", "video", "audio", "web"},
    "level": {"easy", "ok", "hard"},
    "output_type": {"speaking", "writing", "role-play", "test", "pronunciation-check", "reflection", "real-world"},
    "feedback_by": {"agent", "teacher", "self"},
    "check": {"reading-check", "writing-check", "pron-accuracy"},
}
STATUS = {
    "objective": {"active", "closed"}, "key-result": {"active", "closed"},
    "scene": {"planned", "learning", "passed"}, "source": {"new", "in-progress", "done"},
}
ERROR_TYPES = {"tone", "aspiration", "retroflex", "initial", "final", "word-order", "measure-word", "le",
               "complement", "word-choice", "character", "grammar-other", "pragmatics", "fluency"}
METRIC_KEYS = {"scenes-toolkit", "roleplays", "scenes-passed", "words-added", "words-recognized",
               "words-pronounced", "characters-recognized", "input-minutes", "reading-check", "writing-pieces",
               "writing-check", "handwriting", "pron-checks", "pron-accuracy", "study-days", "real-world",
               "fun-avg", "confidence-avg"}
FOLDER_OF = {
    "profile": "01-profile", "vision": "01-profile", "objective": "02-okr", "key-result": "02-okr",
    "task": "03-tasks", "daily": "04-daily", "review": "05-reviews", "word": "06-library/words",
    "pattern": "06-library/patterns", "scene": "06-library/scenes", "source": "07-inbox", "output": "08-output",
}
INTERVALS = {1: 1, 2: 3, 3: 7, 4: 14, 5: 30}
LINK = re.compile(r"\[\[([^\]|#]+)")


# ---------- reading records ----------

def scalar(raw):
    raw = raw.strip()
    if raw in ("", "~", "null"):
        return None
    if (raw[0] == raw[-1]) and raw[0] in "\"'" and len(raw) >= 2:
        return raw[1:-1]
    if raw in ("true", "false"):
        return raw == "true"
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    if re.fullmatch(r"-?\d+\.\d+", raw):
        return float(raw)
    return raw


def split_flow(inner):
    items, buf, quote = [], "", None
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            buf += ch
        elif ch == ",":
            items.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        items.append(buf)
    return [scalar(i) for i in items if i.strip()]


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data, last = {}, None
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") or line.startswith("- "):
            if last is not None:
                if not isinstance(data.get(last), list):
                    data[last] = []
                data[last].append(scalar(line.split("- ", 1)[1]))
            continue
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        raw = re.sub(r"\s+#.*$", "", raw) if not raw.strip().startswith(("\"", "'")) else raw
        raw = raw.strip()
        last = key.strip()
        if raw.startswith("[") and raw.endswith("]"):
            data[last] = split_flow(raw[1:-1])
        else:
            data[last] = scalar(raw)
    return data


def load():
    records = []
    for d in DATA_DIRS:
        for p in (ROOT / d).rglob("*.md"):
            fm = frontmatter(p)
            if fm is not None:
                fm["_path"] = p
                fm["_name"] = p.stem
                records.append(fm)
    return records


def links(value):
    vals = value if isinstance(value, list) else [value]
    return [m for v in vals if isinstance(v, str) for m in LINK.findall(v)]


def as_date(value):
    try:
        return date.fromisoformat(str(value)) if value else None
    except ValueError:
        return None


# ---------- check ----------

def check(records):
    names = {p.stem for p in ROOT.rglob("*.md")} | {p.name for p in ROOT.rglob("*")}
    by_name = {r["_name"]: r for r in records}
    problems, samples = [], 0

    def bad(rec, msg):
        problems.append(f"{rec['_path'].relative_to(ROOT)}: {msg}")

    for r in records:
        t = r.get("type")
        if r.get("sample"):
            samples += 1
        if t not in FOLDER_OF:
            bad(r, f"unknown or missing type {t!r}")
            continue
        rel = str(r["_path"].relative_to(ROOT))
        if not rel.startswith(FOLDER_OF[t]):
            bad(r, f"type {t} belongs in {FOLDER_OF[t]}/")
        if not r.get("created"):
            bad(r, "missing created")
        for key, allowed in ALLOWED.items():
            v = r.get(key)
            if v is not None and v not in allowed:
                bad(r, f"{key}: {v!r} not in {sorted(allowed)}")
        if t in STATUS and r.get("status") not in STATUS[t]:
            bad(r, f"status: {r.get('status')!r} not in {sorted(STATUS[t])}")
        for e in r.get("error_types") or []:
            if e not in ERROR_TYPES:
                bad(r, f"error_types: unknown {e!r}")
        for key, v in r.items():
            if key.startswith("_"):
                continue
            for target in links(v):
                if target not in names and target + ".md" not in names:
                    bad(r, f"{key}: link [[{target}]] has no file")
        if t == "task":
            objs = links(r.get("objective"))
            if len(objs) != 1:
                bad(r, "task must link exactly one objective")
            elif by_name.get(objs[0], {}).get("type") != "objective":
                bad(r, f"objective [[{objs[0]}]] is not an objective")
        if t == "key-result":
            if r.get("metric_key") not in METRIC_KEYS:
                bad(r, f"metric_key {r.get('metric_key')!r} unknown")
            obj = by_name.get((links(r.get("objective")) or [None])[0])
            if not obj:
                bad(r, "key result without a valid objective")
            elif str(r.get("due")) != str(obj.get("end")):
                bad(r, "due should equal the objective's end")
        if t == "objective":
            if not (as_date(r.get("start")) and as_date(r.get("end"))):
                bad(r, "objective needs start and end dates")
        if t in ("word", "pattern", "scene"):
            box = r.get("box")
            if box not in INTERVALS:
                bad(r, f"box {box!r} must be 1–5")
            if t != "scene" and isinstance(box, int) and r.get("recognize") != (box >= 3):
                bad(r, f"recognize should be {box >= 3} for box {box}")
            last, nxt = as_date(r.get("last_review")), as_date(r.get("next_review"))
            if t != "scene" and not nxt:
                bad(r, "missing next_review")
            if last and nxt and box in INTERVALS and (nxt - last).days not in (1, INTERVALS[box]):
                bad(r, f"next_review is {(nxt - last).days} days after last_review; box {box} expects {INTERVALS[box]}")
        if t == "daily" and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["_name"]):
            bad(r, "daily log file name must be YYYY-MM-DD")
    for p in problems:
        print("  -", p)
    print(f"{len(records)} records checked, {len(problems)} problems, {samples} sample records.")
    return 1 if problems else 0


# ---------- key results ----------

def compute(kr, records, by_name):
    obj = by_name.get((links(kr.get("objective")) or [None])[0], {})
    start, end = as_date(obj.get("start")), as_date(obj.get("end"))
    oname = obj.get("_name")

    sample_mode = bool(kr.get("sample"))  # sample key results count sample records only

    def of(t):
        return [r for r in records if r.get("type") == t and bool(r.get("sample")) == sample_mode]

    def in_window(r, key):
        d = as_date(r.get(key))
        return d and start and end and start <= d <= end

    def linked(r):  # scenes list every objective they served
        return oname in links(r.get("objectives"))

    def chars(words):
        return len({c for w in words for c in (w.get("characters") or list(w["_name"].split(" ")[0]))})

    def latest_accuracy(key):
        tests = [o for o in of("output") if o.get("check") == key and in_window(o, "date")]
        tests.sort(key=lambda o: str(o.get("date")))
        acc = tests[-1].get("accuracy") if tests else None
        return round(acc * 100) if isinstance(acc, (int, float)) else 0

    def mean(key):
        vals = [d.get(key) for d in of("daily") if in_window(d, "date") and isinstance(d.get(key), (int, float))]
        return round(sum(vals) / len(vals), 1) if vals else 0

    words, outputs = of("word"), of("output")
    m = kr.get("metric_key")
    return {
        "scenes-toolkit": lambda: sum(1 for s in of("scene") if linked(s) and s.get("status") in ("learning", "passed")),
        "roleplays": lambda: sum(1 for o in outputs if o.get("output_type") == "role-play" and in_window(o, "date")),
        "scenes-passed": lambda: sum(1 for s in of("scene") if linked(s) and s.get("status") == "passed"),
        "words-added": lambda: sum(1 for w in words if in_window(w, "created")),
        "words-recognized": lambda: sum(1 for w in words if w.get("recognize")),
        "words-pronounced": lambda: sum(1 for w in words if w.get("recognize") and w.get("pronounce_ok")),
        "characters-recognized": lambda: chars([w for w in words if w.get("recognize")]),
        "input-minutes": lambda: sum(d.get("input_min") or 0 for d in of("daily") if in_window(d, "date")),
        "reading-check": lambda: latest_accuracy("reading-check"),
        "writing-pieces": lambda: sum(1 for o in outputs if o.get("output_type") == "writing" and in_window(o, "date")),
        "writing-check": lambda: latest_accuracy("writing-check"),
        "handwriting": lambda: chars([w for w in words if w.get("handwrite")]),
        "pron-checks": lambda: sum(1 for o in outputs if o.get("output_type") == "pronunciation-check" and in_window(o, "date")),
        "pron-accuracy": lambda: latest_accuracy("pron-accuracy"),
        "study-days": lambda: sum(1 for d in of("daily") if in_window(d, "date") and (d.get("minutes") or 0) > 0),
        "real-world": lambda: sum(1 for o in outputs if o.get("output_type") == "real-world" and in_window(o, "date")),
        "fun-avg": lambda: mean("fun"),
        "confidence-avg": lambda: mean("confidence"),
    }.get(m, lambda: None)()


def kr_command(records, write=False, cycle=None, include_closed=False):
    by_name = {r["_name"]: r for r in records}
    krs = [r for r in records if r.get("type") == "key-result"
           and (include_closed or r.get("status") == "active")
           and (cycle is None or str(r.get("cycle")) == cycle)]
    krs.sort(key=lambda r: (str(r.get("cycle")), str(r.get("code"))))
    print(f"{'KR':<8}{'metric_key':<24}{'current':>9}{'target':>8}  title")
    for kr in krs:
        cur = compute(kr, records, by_name)
        print(f"{str(kr.get('code')):<8}{str(kr.get('metric_key')):<24}{str(cur):>9}{str(kr.get('target')):>8}  {kr.get('title')}")
        if write and cur is not None:
            p = kr["_path"]
            text = p.read_text(encoding="utf-8")
            text = re.sub(r"(?m)^current:.*$", f"current: {cur}", text, count=1)
            p.write_text(text, encoding="utf-8")
    if write:
        print("current values saved.")


if __name__ == "__main__":
    args = sys.argv[1:]
    recs = load()
    if not args or args[0] == "check":
        sys.exit(check(recs))
    if args[0] == "kr":
        cyc = args[args.index("--cycle") + 1] if "--cycle" in args else None
        kr_command(recs, write="--write" in args, cycle=cyc, include_closed="--all" in args)
    else:
        print(__doc__)
