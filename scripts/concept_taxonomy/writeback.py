#!/usr/bin/env python3
"""Dry-run or apply a small, reviewed concept relation writeback batch."""
from __future__ import annotations

import paths
import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import yaml

from boundary_policy import FORBIDDEN_UP_PAIRS

ROOT = paths.ROOT
CONCEPT_DIR = paths.CONCEPT_DIR
OUT_DIR = paths.OUT_DIR
LEDGER_JSON = OUT_DIR / "relation-decision-ledger.json"
DRY_JSON = OUT_DIR / "writeback-dry-run.json"
DRY_MD = OUT_DIR / "writeback-dry-run.md"
APPLY_JSON = OUT_DIR / "writeback-apply-report.json"
APPLY_MD = OUT_DIR / "writeback-apply-report.md"
TODAY = "2026-05-16"
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
TOP_LEVEL_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*:\s*")


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def clean_link(value: Any) -> str | None:
    if value is None or isinstance(value, dict):
        return None
    s = str(value).strip().strip('"').strip("'")
    m = WIKILINK_RE.search(s)
    if m:
        s = m.group(1)
    s = s.split("|")[0].split("#")[0].strip()
    if "/" in s:
        s = Path(s).stem
    return s or None


def load_fm(path: Path) -> tuple[dict[str, Any], str, str, str]:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        return {}, "", "", text
    raw = m.group(1)
    return yaml.safe_load(raw) or {}, raw, text[:m.start()], text[m.end():]


def existing_up(path: Path) -> list[str]:
    fm, _raw, _prefix, _body = load_fm(path)
    return [x for x in (clean_link(v) for v in as_list(fm.get("up"))) if x]


def block_end(lines: list[str], start: int) -> int:
    i = start + 1
    while i < len(lines) and (not lines[i].strip() or not TOP_LEVEL_RE.match(lines[i])):
        i += 1
    return i


def find_insert_index(lines: list[str]) -> int:
    preferred = ["related", "evidence", "source", "freshness", "last_checked", "updated"]
    last = None
    for field in preferred:
        for idx, line in enumerate(lines):
            if line.startswith(f"{field}:"):
                last = block_end(lines, idx)
    if last is not None:
        return last
    for idx, line in enumerate(lines):
        if line.startswith("aliases:") or line.startswith("conflicts:"):
            return idx
    return len(lines)


def set_updated(lines: list[str]) -> list[str]:
    for idx, line in enumerate(lines):
        if line.startswith("updated:"):
            lines[idx] = f"updated: {TODAY}"
            return lines
    for idx, line in enumerate(lines):
        if line.startswith("created:"):
            lines.insert(idx + 1, f"updated: {TODAY}")
            return lines
    lines.insert(0, f"updated: {TODAY}")
    return lines


def add_up_field(path: Path, target: str) -> str:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        raise ValueError(f"{path} has no YAML frontmatter")
    raw = m.group(1)
    fm = yaml.safe_load(raw) or {}
    current = [x for x in (clean_link(v) for v in as_list(fm.get("up"))) if x]
    if target in current:
        return "already_present"
    if current:
        raise ValueError(f"{path} already has up={current}; refusing to create multi-parent edge")
    lines = raw.splitlines()
    lines = set_updated(lines)
    insert_at = find_insert_index(lines)
    block = ["up:", f"  - \"[[{target}]]\""]
    if insert_at > 0 and lines[insert_at - 1].strip():
        block = [""] + block
    if insert_at < len(lines) and lines[insert_at].strip():
        block = block + [""]
    lines[insert_at:insert_at] = block
    new_text = "---\n" + "\n".join(lines).rstrip() + "\n---\n" + text[m.end():]
    path.write_text(new_text, encoding="utf-8")
    return "applied"


def selected_writebacks(limit: int | None = None) -> list[dict[str, Any]]:
    if not LEDGER_JSON.exists():
        raise SystemExit(f"missing {LEDGER_JSON}; run decide.py first")
    data = json.loads(LEDGER_JSON.read_text(encoding="utf-8"))
    rows = [d for d in data.get("decisions", []) if d.get("writeback_action") == "add_up"]
    forbidden = sorted((d["source"], d["target"]) for d in rows if (d["source"], d["target"]) in FORBIDDEN_UP_PAIRS)
    if forbidden:
        raise SystemExit(f"Refusing forbidden non-taxonomy up writebacks: {forbidden}")
    order = {"high": 0, "medium": 1, "low": 2}
    rows = sorted(rows, key=lambda d: (order.get(d.get("judge_confidence"), 9), d["source"], d["target"]))
    if limit is not None:
        rows = rows[:limit]
    return rows


def planned_row(row: dict[str, Any]) -> dict[str, Any]:
    source_path = CONCEPT_DIR / f"{row['source']}.md"
    target_path = CONCEPT_DIR / f"{row['target']}.md"
    current_up = existing_up(source_path) if source_path.exists() else []
    status = "ready"
    if not source_path.exists():
        status = "missing_source"
    elif not target_path.exists():
        status = "missing_target"
    elif current_up and row["target"] not in current_up:
        status = "skip_existing_up"
    elif row["target"] in current_up:
        status = "already_present"
    return {
        "source": row["source"],
        "target": row["target"],
        "source_file": str(source_path.relative_to(ROOT)) if source_path.exists() else str(source_path),
        "target_file": str(target_path.relative_to(ROOT)) if target_path.exists() else str(target_path),
        "status": status,
        "current_up": current_up,
        "decision_rationale": row.get("decision_rationale", ""),
        "judge_confidence": row.get("judge_confidence", ""),
    }


def write_report(path_json: Path, path_md: Path, artifact_type: str, rows: list[dict[str, Any]], applied: list[dict[str, Any]] | None = None) -> None:
    payload = {
        "schema_version": 1,
        "artifact_type": artifact_type,
        "generated_at": subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip(),
        "ledger": str(LEDGER_JSON.relative_to(ROOT)),
        "summary": {
            "planned": len(rows),
            "ready": sum(1 for r in rows if r["status"] == "ready"),
            "applied": len(applied or []),
            "skipped": sum(1 for r in rows if r["status"] != "ready"),
            "write_policy": "small batch only; no topic_family_review and no down/children mirror fields",
        },
        "planned": rows,
        "applied": applied or [],
    }
    path_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md: list[str] = []
    title = "Concept Relation Writeback Dry Run" if "dry" in artifact_type else "Concept Relation Writeback Apply Report"
    md.append(f"# {title}")
    md.append("")
    md.append(f"Generated: `{payload['generated_at']}`")
    md.append("")
    md.append("> 写回边界：只写子卡 `up`；不手写 `down` / `children`；不把 `topic_family_review` 写入概念卡；不新增 Juggl 镜像字段。")
    md.append("")
    md.append("## Summary")
    md.append("")
    for k, v in payload["summary"].items():
        md.append(f"- {k}: {v}")
    md.append("")
    md.append("## Planned rows")
    md.append("")
    md.append("| Source | Target | Status | Confidence | Rationale |")
    md.append("|---|---|---|---|---|")
    for r in rows:
        rationale = str(r["decision_rationale"]).replace("|", "/")
        md.append(f"| [[{r['source']}]] | [[{r['target']}]] | {r['status']} | {r['judge_confidence']} | {rationale} |")
    if applied is not None:
        md.append("")
        md.append("## Applied rows")
        md.append("")
        md.append("| Source | Target | Result |")
        md.append("|---|---|---|")
        for r in applied:
            md.append(f"| [[{r['source']}]] | [[{r['target']}]] | {r['result']} |")
    md.append("")
    path_md.write_text("\n".join(md), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dry-run", action="store_true")
    group.add_argument("--apply", action="store_true")
    parser.add_argument("--limit", type=int, default=None, help="Limit selected accepted writebacks; required for every apply.")
    args = parser.parse_args()

    if args.apply and args.limit is None:
        raise SystemExit("Refusing unbounded apply. Pass --limit N for a reviewed small batch.")

    rows = [planned_row(r) for r in selected_writebacks(args.limit)]
    if args.dry_run:
        write_report(DRY_JSON, DRY_MD, "concept_relation_writeback_dry_run", rows)
        print(json.dumps({"ok": True, "mode": "dry-run", "planned": len(rows), "ready": sum(1 for r in rows if r["status"] == "ready"), "json": str(DRY_JSON.relative_to(ROOT)), "markdown": str(DRY_MD.relative_to(ROOT))}, ensure_ascii=False, indent=2))
        return

    applied: list[dict[str, Any]] = []
    for r in rows:
        if r["status"] != "ready":
            applied.append({**r, "result": f"skipped:{r['status']}"})
            continue
        result = add_up_field(ROOT / r["source_file"], r["target"])
        applied.append({**r, "result": result})
    write_report(APPLY_JSON, APPLY_MD, "concept_relation_writeback_apply_report", rows, applied)
    print(json.dumps({"ok": True, "mode": "apply", "planned": len(rows), "applied": sum(1 for r in applied if r["result"] == "applied"), "json": str(APPLY_JSON.relative_to(ROOT)), "markdown": str(APPLY_MD.relative_to(ROOT))}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
