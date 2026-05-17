#!/usr/bin/env python3
"""Plugin-contract verification for concept taxonomy tooling.

This report intentionally does not read or mutate live Obsidian plugin state.
The repository keeps `.obsidian/` out of scope, so plugin-contract validates the durable
contract: concept-card frontmatter, generated relation artifacts, and documented
Abstract Folder / Breadcrumbs boundaries.
"""
from __future__ import annotations

import paths
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = paths.ROOT
CONCEPT_DIR = paths.CONCEPT_DIR
OUT_DIR = paths.OUT_DIR
MAP_JSON = OUT_DIR / "concept-relations-temp.json"
LEDGER_JSON = OUT_DIR / "relation-decision-ledger.json"
REL_DRY_JSON = OUT_DIR / "writeback-dry-run.json"
REL_APPLY_JSON = OUT_DIR / "writeback-apply-report.json"
TAX_REVIEW_JSON = OUT_DIR / "concept-hierarchy-placement-review.json"
TAX_APPLY_JSON = OUT_DIR / "concept-hierarchy-placement-apply-report.json"
TAX_DRY_JSON = OUT_DIR / "concept-hierarchy-placement-writeback-dry-run.json"
TAX_STEP10_JSON = OUT_DIR / "concept-hierarchy-placement-closure.json"
PLUGIN_JSON = OUT_DIR / "plugin-compat-validation.json"
PLUGIN_CONTRACT_JSON = OUT_DIR / "plugin-contract-verification.json"
PLUGIN_CONTRACT_MD = OUT_DIR / "plugin-contract-verification.md"
WORKFLOW = ROOT / "agentic learning" / "maps" / "LLM Wiki 工作流.md"
FIELD_SPEC = ROOT / "agentic learning" / "maps" / "字段规范.md"

FORBIDDEN_TOP_LEVEL_FIELDS = {
    "down",
    "children",
    "parent",
    "parents",
    "same",
    "next",
    "prev",
    # Breadcrumbs mirror fields deliberately not enabled in v1.
    "based_on",
    "represents",
    "representative_of",
    "composes_with",
    "composed_into",
    "related_to",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def clean_link(value: Any) -> str | None:
    """Normalize an Obsidian wikilink/frontmatter value to a concept title."""
    if value is None or isinstance(value, dict):
        return None
    text = str(value).strip().strip('"').strip("'")
    if text.startswith("[[") and "]]" in text:
        text = text[2:text.find("]]")]
    text = text.split("|")[0].split("#")[0].strip()
    if "/" in text:
        text = Path(text).stem
    return text or None


def collect_concept_cards() -> list[Path]:
    return sorted(p for p in CONCEPT_DIR.glob("*.md") if frontmatter(p).get("type") == "concept")


def main() -> None:
    map_data = load_json(MAP_JSON)
    ledger = load_json(LEDGER_JSON)
    rel_dry = load_json(REL_DRY_JSON)
    rel_apply = load_json(REL_APPLY_JSON) if REL_APPLY_JSON.exists() else {}
    tax_review = load_json(TAX_REVIEW_JSON)
    tax_apply = load_json(TAX_APPLY_JSON)
    tax_dry = load_json(TAX_DRY_JSON)
    plugin = load_json(PLUGIN_JSON)
    concept_files = collect_concept_cards()

    top_level_field_hits: dict[str, list[str]] = {field: [] for field in sorted(FORBIDDEN_TOP_LEVEL_FIELDS)}
    up_edges: list[tuple[str, str]] = []
    missing_up_targets: list[dict[str, str]] = []
    relation_mirror_hits: list[dict[str, str]] = []
    for path in concept_files:
        fm = frontmatter(path)
        for field in FORBIDDEN_TOP_LEVEL_FIELDS:
            if field in fm:
                top_level_field_hits[field].append(path.name)
        for value in as_list(fm.get("up")):
            target = clean_link(value)
            if not target:
                missing_up_targets.append({"source": path.stem, "target": str(value), "reason": "unparsable"})
                continue
            up_edges.append((path.stem, target))
            if not (CONCEPT_DIR / f"{target}.md").exists():
                missing_up_targets.append({"source": path.stem, "target": target, "reason": "target file missing"})
        for item in as_list(fm.get("relations")):
            if isinstance(item, dict) and item.get("type") in FORBIDDEN_TOP_LEVEL_FIELDS:
                # This is allowed because it is nested `relations[]`, not a Breadcrumbs top-level edge.
                relation_mirror_hits.append({"source": path.stem, "type": str(item.get("type")), "target": str(item.get("target"))})

    tax_applied_pairs = [(row.get("source"), row.get("target")) for row in tax_apply.get("applied", []) if row.get("result") in {"applied", "already_present"}]
    relation_applied_pairs = [(row.get("source"), row.get("target")) for row in rel_apply.get("applied", []) if row.get("result") in {"applied", "already_present"}]
    all_applied_pairs = set(tax_applied_pairs) | set(relation_applied_pairs)
    missing_applied_up = [pair for pair in sorted(all_applied_pairs) if pair not in set(up_edges)]

    docs = {
        "workflow": WORKFLOW.read_text(encoding="utf-8"),
        "field_spec": FIELD_SPEC.read_text(encoding="utf-8"),
    }
    durable_contract_docs = docs["field_spec"] + docs["workflow"]
    doc_checks = {
        "abstract_folder_up_contract": all(s in durable_contract_docs for s in ["Abstract Folder", "up"]),
        "breadcrumbs_top_level_up_contract": all(s in durable_contract_docs for s in ["Breadcrumbs", "up"]),
        "relations_not_breadcrumbs_edge_field": "relations" in docs["field_spec"] and "不是 Breadcrumbs" in docs["field_spec"],
        "juggl_retired_documented": "Juggl" in durable_contract_docs and any(term in durable_contract_docs for term in ["retired", "退役", "已退役"]),
        "plugin_contract_gate_documented": all(
            [
                "plugin-contract" in docs["workflow"] or "重建与验证" in docs["workflow"],
                "plugin_contract_verification.py" in docs["workflow"],
                "scripts/concept_taxonomy/" in docs["workflow"],
            ]
        ),
    }

    obsidian_dir = ROOT / ".obsidian"
    problems: list[str] = []
    if len(concept_files) != map_data.get("summary", {}).get("total_concepts"):
        problems.append("concept file count does not match temp map total_concepts")
    if map_data.get("summary", {}).get("edge_counts", {}).get("taxonomy") != len(up_edges):
        problems.append("taxonomy edge count does not match concept-card top-level up count")
    if missing_up_targets:
        problems.append("some up targets are missing or unparsable")
    active_forbidden_hits = {k: v for k, v in top_level_field_hits.items() if v}
    if active_forbidden_hits:
        problems.append("forbidden top-level plugin/mirror fields found on concept cards")
    if missing_applied_up:
        problems.append("applied rows are missing from concept-card up fields")
    if rel_dry.get("summary", {}).get("planned") != 0:
        problems.append("relation writeback dry-run still has planned rows")
    if ledger.get("summary", {}).get("open_review_items") != 0 or ledger.get("summary", {}).get("open_writeback_items") != 0:
        problems.append("relation ledger still has open review/writeback items")
    if tax_review.get("classification_stage") not in {"limited_apply", "audit_closure"}:
        problems.append("concept hierarchy placement review is not at a post-limited-apply state before plugin-contract verification")
    if tax_dry.get("summary", {}).get("planned") != 0 or tax_dry.get("summary", {}).get("ready") != 0:
        problems.append("concept hierarchy placement post-apply dry-run is not empty")
    if tax_apply.get("summary", {}).get("post_apply_dry_run_planned") != 0:
        problems.append("concept hierarchy placement apply report does not record empty post-apply dry-run")
    if plugin.get("summary", {}).get("problems") != 0 or plugin.get("summary", {}).get("forbidden_up_edges") != 0:
        problems.append("plugin compatibility validation has problems or forbidden up edges")
    failed_doc_checks = [name for name, ok in doc_checks.items() if not ok]
    if failed_doc_checks:
        problems.append(f"documentation contract checks failed: {failed_doc_checks}")

    payload = {
        "schema_version": 1,
        "artifact_type": "plugin_contract_verification",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "input_artifacts": {
            "temp_map": rel(MAP_JSON),
            "relation_ledger": rel(LEDGER_JSON),
            "relation_dry_run": rel(REL_DRY_JSON),
            "relation_apply_report": rel(REL_APPLY_JSON),
            "taxonomy_review": rel(TAX_REVIEW_JSON),
            "taxonomy_apply_report": rel(TAX_APPLY_JSON),
            "taxonomy_dry_run": rel(TAX_DRY_JSON),
            "taxonomy_audit_closure": rel(TAX_STEP10_JSON) if TAX_STEP10_JSON.exists() else None,
            "plugin_validation": rel(PLUGIN_JSON),
        },
        "summary": {
            "concept_cards_checked": len(concept_files),
            "top_level_up_edges": len(up_edges),
            "temp_map_taxonomy_edges": map_data.get("summary", {}).get("edge_counts", {}).get("taxonomy"),
            "relation_writeback_dry_run_planned": rel_dry.get("summary", {}).get("planned"),
            "taxonomy_post_apply_dry_run_planned": tax_dry.get("summary", {}).get("planned"),
            "taxonomy_post_apply_dry_run_ready": tax_dry.get("summary", {}).get("ready"),
            "taxonomy_limited_apply_rows": tax_apply.get("summary", {}).get("applied"),
            "taxonomy_placement_open_review": tax_review.get("summary", {}).get("open_review"),
            "taxonomy_placement_defer_boundary_review": tax_review.get("summary", {}).get("defer_boundary_review"),
            "taxonomy_placement_deferred_with_backlog": tax_review.get("summary", {}).get("deferred_with_backlog", 0),
            "taxonomy_placement_open_writeback": tax_review.get("summary", {}).get("open_writeback"),
            "relation_apply_rows_checked": len(relation_applied_pairs),
            "taxonomy_apply_rows_checked": len(tax_applied_pairs),
            "plugin_problems": plugin.get("summary", {}).get("problems"),
            "forbidden_up_edges": plugin.get("summary", {}).get("forbidden_up_edges"),
            "forbidden_top_level_fields": sum(len(v) for v in top_level_field_hits.values()),
            "nested_relation_records_with_mirror-like_types": len(relation_mirror_hits),
            "obsidian_plugin_config_present": obsidian_dir.exists(),
            "problems": len(problems),
        },
        "plugin_contract": {
            "abstract_folder": "Contract-only verification: parent property remains `up`; no physical folder conversion or `children` writeback is required.",
            "breadcrumbs": "Contract-only verification: top-level `up` is the only hierarchy edge field; `down` is implied; nested `relations` is not promoted to edge fields.",
            "juggl": "Retired; no Juggl plugin state, field, or mirror edge is required or validated.",
            "live_obsidian_config": "absent" if not obsidian_dir.exists() else "present_but_not_mutated",
        },
        "doc_checks": doc_checks,
        "forbidden_top_level_field_hits": active_forbidden_hits,
        "missing_up_targets": missing_up_targets,
        "missing_applied_up": [list(pair) for pair in missing_applied_up],
        "nested_relations_note": "Nested relations with types such as representative_of/composes_with are allowed because they are not top-level Breadcrumbs edge fields.",
        "problems": problems,
    }
    PLUGIN_CONTRACT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = ["# Plugin Contract Verification", "", f"Generated: `{payload['generated_at']}`", ""]
    lines.append("## Summary")
    lines.append("")
    for key, value in payload["summary"].items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    lines.append("## Plugin contract")
    lines.append("")
    for key, value in payload["plugin_contract"].items():
        lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("## Doc checks")
    lines.append("")
    for key, value in doc_checks.items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    lines.append("## Problems")
    lines.append("")
    if problems:
        lines.extend(f"- {problem}" for problem in problems)
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Boundary")
    lines.append("")
    lines.append("- Plugin contract verification is verification-only; it does not write concept-card fields.")
    lines.append("- `concepts_without_up` may remain > 0; this check proves plugin and writeback contracts after bounded apply.")
    lines.append("- Taxonomy-placement `open_review` may remain > 0; this check is not the whole-audit closure gate.")
    lines.append("- `.obsidian/` is absent in this repo, so live plugin settings are not mutated or asserted beyond durable contract checks.")
    lines.append("")
    PLUGIN_CONTRACT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({"ok": not problems, "json": rel(PLUGIN_CONTRACT_JSON), "markdown": rel(PLUGIN_CONTRACT_MD), "summary": payload["summary"], "problems": problems}, ensure_ascii=False, indent=2))
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
