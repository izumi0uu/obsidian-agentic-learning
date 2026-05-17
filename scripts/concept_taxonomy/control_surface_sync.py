#!/usr/bin/env python3
"""Concept taxonomy control-surface synchronization verification.

This project-owned verifier does not mutate concept cards. It checks that the
script README, report README, workflow, health-check, baseline map, and log
surfaces describe the project-owned taxonomy tooling without changing field
semantics.
"""
from __future__ import annotations

import paths
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = paths.ROOT
OUT_DIR = paths.OUT_DIR
PLUGIN_CONTRACT_JSON = OUT_DIR / "plugin-contract-verification.json"
TAX_REVIEW_JSON = OUT_DIR / "concept-hierarchy-placement-review.json"
PLUGIN_JSON = OUT_DIR / "plugin-compat-validation.json"
CONTROL_SYNC_JSON = OUT_DIR / "control-surface-sync.json"
CONTROL_SYNC_MD = OUT_DIR / "control-surface-sync.md"

REQUIRED_SURFACES = {
    "script_readme": ROOT / "scripts" / "concept_taxonomy" / "README.md",
    "report_readme": ROOT / "reports" / "concept-card-relation-map" / "README.md",
    "script_index": ROOT / "scripts" / "README.md",
    "workflow": ROOT / "agentic learning" / "maps" / "LLM Wiki 工作流.md",
    "health_check": ROOT / "agentic learning" / "maps" / "06 Wiki 健康检查.md",
    "baseline_map": ROOT / "agentic learning" / "maps" / "09 概念层级审计基线.md",
    "log": ROOT / "agentic learning" / "log.md",
}

INTENTIONALLY_NOT_CHANGED = {
    "agentic learning/maps/字段规范.md": "Tooling and baseline evidence moved into project-owned paths; no `up` / `relations` field semantics changed.",
    "agentic learning/templates/概念卡.md": "No concept-card page shape or `up` / `relations` writeback contract changed.",
    "AGENTS.md": "Project hard rules already cover systemic script-driven changes; workflow-specific commands live in LLM Wiki 工作流 and scripts README.",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def surface_check(name: str, path: Path, open_review: int, open_writeback: int) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    checks = {
        "mentions_project-owned_tooling": "scripts/concept_taxonomy" in text or "concept_taxonomy" in lowered,
        "mentions_project_reports": "reports/concept-card-relation-map" in text or "project-owned" in lowered or "项目内" in text,
        "mentions_no_direct_writeback": "open_writeback" in text or "不新增概念卡关系" in text or "no writeback" in lowered or "不能直接写" in text,
    }
    if name == "health_check":
        checks.update(
            {
                "mentions_remaining_open_review_count": str(open_review) in text and ("defer_boundary_review" in text or "open_review" in text or "deferred_with_backlog" in text),
                "mentions_open_writeback_zero": f"open_writeback: {open_writeback}" in text or "open_writeback 0" in text,
                "mentions_project_ownership": "项目内" in text or "project-owned" in lowered,
            }
        )
    if name == "workflow":
        checks.update(
            {
                "mentions_intentionally_unchanged_schema_template": "字段规范" in text and "模板" in text and ("故意不改" in text or "不改" in text),
                "mentions_project_ownership": "项目内" in text or "project-owned" in lowered,
            }
        )
    if name in {"script_readme", "report_readme", "script_index", "baseline_map"}:
        checks.update(
            {
                "mentions_alternate_report_dir": "CONCEPT_TAXONOMY_OUT_DIR" in text or "报告目录" in text or "alternate" in lowered,
            }
        )
    return {
        "surface": name,
        "path": rel(path),
        "checks": checks,
        "synced": all(checks.values()),
    }


def main() -> None:
    plugin_contract = load_json(PLUGIN_CONTRACT_JSON)
    tax_review = load_json(TAX_REVIEW_JSON)
    plugin = load_json(PLUGIN_JSON)
    tax_summary = tax_review.get("summary", {})
    plugin_contract_summary = plugin_contract.get("summary", {})
    plugin_summary = plugin.get("summary", {})
    open_review = int(tax_summary.get("open_review", 0) or 0)
    open_writeback = int(tax_summary.get("open_writeback", 0) or 0)

    surfaces = [surface_check(name, path, open_review, open_writeback) for name, path in REQUIRED_SURFACES.items()]
    failed = [s for s in surfaces if not s["synced"]]

    problems: list[str] = []
    if plugin_contract_summary.get("problems") != 0:
        problems.append("plugin-contract verification is not clean")
    if plugin_contract_summary.get("taxonomy_placement_open_writeback") != 0 or open_writeback != 0:
        problems.append("taxonomy open_writeback is not 0")
    if plugin_summary.get("problems") != 0 or plugin_summary.get("forbidden_up_edges") != 0:
        problems.append("plugin compatibility report is not clean")
    if failed:
        problems.append("some required control surfaces are not synced")

    if open_review == 0:
        boundary = [
            "Project tooling verification checks project-owned control surfaces after the audit baseline is closed; it does not adjudicate or write new concept-card relationships.",
            "Remaining defer_boundary_review rows are closed only when review_status=deferred_with_backlog and a backlog home is recorded.",
            "Field spec and concept-card template stay unchanged because the tooling migration moved tooling/evidence locations without changing `up` / `relations` field semantics or concept-card page shape.",
        ]
    else:
        boundary = [
            "Project tooling verification syncs project-owned control surfaces; it does not adjudicate the remaining taxonomy open_review rows.",
            "Remaining defer_boundary_review rows require a future candidate/adjudication/dry-run/limited-apply cycle.",
            "Field spec and concept-card template stay unchanged because the tooling migration introduced no schema or concept-card page-shape semantics.",
        ]

    payload: dict[str, Any] = {
        "schema_version": 1,
        "artifact_type": "taxonomy_tooling_control_surface_sync",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "input_artifacts": {
            "plugin_contract_verification": rel(PLUGIN_CONTRACT_JSON),
            "taxonomy_review": rel(TAX_REVIEW_JSON),
            "plugin_validation": rel(PLUGIN_JSON),
        },
        "summary": {
            "required_surfaces_total": len(surfaces),
            "required_surfaces_synced": len(surfaces) - len(failed),
            "taxonomy_open_review_remaining": open_review,
            "taxonomy_defer_boundary_review_remaining": tax_summary.get("defer_boundary_review"),
            "taxonomy_open_writeback": open_writeback,
            "plugin_contract_problems": plugin_contract_summary.get("problems"),
            "plugin_problems": plugin_summary.get("problems"),
            "forbidden_up_edges": plugin_summary.get("forbidden_up_edges"),
            "concept_card_writebacks_this_check": 0,
            "problems": len(problems),
        },
        "required_surfaces": surfaces,
        "intentionally_not_changed": INTENTIONALLY_NOT_CHANGED,
        "boundary": boundary,
        "problems": problems,
    }

    CONTROL_SYNC_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = ["# Taxonomy Tooling Control-Surface Sync", "", f"Generated: `{payload['generated_at']}`", ""]
    lines.append("## Summary")
    lines.append("")
    for key, value in payload["summary"].items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    lines.append("## Required surfaces")
    lines.append("")
    for surface in surfaces:
        lines.append(f"- {surface['surface']}: `{surface['synced']}` — `{surface['path']}`")
    lines.append("")
    lines.append("## Intentionally not changed")
    lines.append("")
    for path, reason in INTENTIONALLY_NOT_CHANGED.items():
        lines.append(f"- `{path}`: {reason}")
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    lines.extend(f"- {item}" for item in payload["boundary"])
    lines.append("")
    lines.append("## Problems")
    lines.append("")
    lines.extend((f"- {problem}" for problem in problems) if problems else ["- none"])
    lines.append("")
    CONTROL_SYNC_MD.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({"ok": not problems, "json": rel(CONTROL_SYNC_JSON), "markdown": rel(CONTROL_SYNC_MD), "summary": payload["summary"], "problems": problems}, ensure_ascii=False, indent=2))
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
