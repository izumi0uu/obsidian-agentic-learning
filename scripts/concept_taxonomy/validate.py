#!/usr/bin/env python3
"""Validate the concept-card relationship pipeline and plugin compatibility."""
from __future__ import annotations

import paths
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

from boundary_policy import FORBIDDEN_UP_PAIRS

ROOT = paths.ROOT
CONCEPT_DIR = paths.CONCEPT_DIR
OUT_DIR = paths.OUT_DIR
JSON_OUT = OUT_DIR / "concept-relations-temp.json"
MD_OUT = OUT_DIR / "concept-relations-temp.md"
LEDGER_JSON = OUT_DIR / "relation-decision-ledger.json"
LEDGER_MD = OUT_DIR / "relation-decision-ledger.md"
DRY_JSON = OUT_DIR / "writeback-dry-run.json"
DRY_MD = OUT_DIR / "writeback-dry-run.md"
APPLY_JSON = OUT_DIR / "writeback-apply-report.json"
PLUGIN_JSON = OUT_DIR / "plugin-compat-validation.json"
PLUGIN_MD = OUT_DIR / "plugin-compat-validation.md"
TAXONOMY_REVIEW_JSON = OUT_DIR / "concept-hierarchy-placement-review.json"
TAXONOMY_APPLY_JSON = OUT_DIR / "concept-hierarchy-placement-apply-report.json"
TAXONOMY_DRY_RUN_JSON = OUT_DIR / "concept-hierarchy-placement-writeback-dry-run.json"
TAXONOMY_STEP10_JSON = OUT_DIR / "concept-hierarchy-placement-closure.json"


def load_fm(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    return yaml.safe_load(text[4:end]) or {}


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def clean_link(value: Any) -> str | None:
    if value is None or isinstance(value, dict):
        return None
    s = str(value).strip().strip('"').strip("'")
    if s.startswith("[[") and "]]" in s:
        s = s[2:s.find("]]")]
    s = s.split("|")[0].split("#")[0].strip()
    if "/" in s:
        s = Path(s).stem
    return s or None


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def require(path: Path) -> None:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")


def validate_map() -> tuple[dict[str, Any], list[Path]]:
    require(JSON_OUT)
    require(MD_OUT)
    data = json.loads(JSON_OUT.read_text(encoding="utf-8"))
    concept_files = sorted(p for p in CONCEPT_DIR.glob("*.md") if load_fm(p).get("type") == "concept")
    nodes = data.get("nodes", [])
    node_ids = [n.get("id") for n in nodes]
    if len(nodes) != len(concept_files):
        fail(f"node count {len(nodes)} != concept file count {len(concept_files)}")
    if len(set(node_ids)) != len(node_ids):
        fail("duplicate node ids")
    if data.get("summary", {}).get("total_concepts") != len(concept_files):
        fail("summary.total_concepts mismatch")
    if not data.get("edges"):
        fail("no edges extracted")
    edge_counts = data.get("summary", {}).get("edge_counts", {})
    for required in ["taxonomy", "typed_relation", "related_link"]:
        if required not in edge_counts:
            fail(f"missing edge count for {required}")
    md = MD_OUT.read_text(encoding="utf-8")
    for heading in ["## Summary", "## Existing taxonomy edges", "## Existing typed relations", "## Candidate edges for review", "## Concepts without `up`"]:
        if heading not in md:
            fail(f"missing markdown heading {heading}")
    return data, concept_files


def validate_ledger(data: dict[str, Any]) -> dict[str, Any]:
    require(LEDGER_JSON)
    require(LEDGER_MD)
    ledger = json.loads(LEDGER_JSON.read_text(encoding="utf-8"))
    input_map = ROOT / ledger.get("input_map", str(JSON_OUT.relative_to(ROOT)))
    if input_map.exists():
        ledger_source_data = json.loads(input_map.read_text(encoding="utf-8"))
    else:
        ledger_source_data = data
    candidates = ledger_source_data.get("candidate_edges", [])
    decisions = ledger.get("decisions", [])
    policy_pairs = {(p.get("source"), p.get("target")) for p in ledger.get("non_taxonomy_boundary_policy", [])}
    missing_policy = FORBIDDEN_UP_PAIRS - policy_pairs
    if missing_policy:
        fail(f"ledger non_taxonomy_boundary_policy missing forbidden pair(s): {sorted(missing_policy)}")
    if len(decisions) != len(candidates):
        fail(f"ledger decision count {len(decisions)} != candidate count {len(candidates)}")
    seen = set()
    open_review_items: list[tuple[str, str, str]] = []
    open_writeback_items: list[tuple[str, str, str]] = []
    terminal_non_writeback = 0
    for d in decisions:
        key = (d.get("source"), d.get("target"), d.get("candidate_type"))
        if key in seen:
            fail(f"duplicate ledger decision {key}")
        seen.add(key)
        status = d.get("resolution_status")
        if d.get("writeback_action") == "add_up":
            open_writeback_items.append((str(d.get("source")), str(d.get("target")), str(d.get("decision"))))
            if status != "open_writeback":
                fail(f"writeback candidate missing open_writeback resolution status: {key}")
        elif d.get("decision") in {"needs_review", "defer_taxonomy"}:
            open_review_items.append((str(d.get("source")), str(d.get("target")), str(d.get("decision"))))
            if status != "open_review":
                fail(f"review tail missing open_review resolution status: {key}")
        elif d.get("decision") in {"reject_taxonomy", "adjacency_only", "duplicate_signal"}:
            terminal_non_writeback += 1
            if status != "terminal_non_writeback":
                fail(f"terminal non-writeback decision has wrong resolution status: {key} -> {status}")
        if d.get("candidate_type") == "topic_family_review" and d.get("writeback_action") != "none":
            fail(f"topic_family_review has writeback action: {key}")
        pair = (d.get("source"), d.get("target"))
        if pair in FORBIDDEN_UP_PAIRS:
            if d.get("writeback_action") != "none":
                fail(f"forbidden non-taxonomy boundary has writeback action: {pair}")
            if d.get("decision") not in {"reject_taxonomy", "adjacency_only", "defer_taxonomy"}:
                fail(f"forbidden non-taxonomy boundary has unsafe decision: {pair} -> {d.get('decision')}")
            if not d.get("boundary_guardrail_applied"):
                fail(f"forbidden non-taxonomy boundary missing explicit guardrail marker: {pair}")
        if d.get("writeback_action") == "add_up":
            if d.get("decision") != "accept_taxonomy":
                fail(f"writeback action without accept_taxonomy: {key}")
            if d.get("candidate_type") != "taxonomy_candidate":
                fail(f"writeback action from non-taxonomy candidate: {key}")
            if d.get("proposed_field") != "up":
                fail(f"writeback action targets non-up field: {key}")
    summary = ledger.get("summary", {})
    if summary.get("open_review_items", len(open_review_items)) != len(open_review_items):
        fail("ledger summary.open_review_items mismatch")
    if summary.get("open_writeback_items", len(open_writeback_items)) != len(open_writeback_items):
        fail("ledger summary.open_writeback_items mismatch")
    if summary.get("terminal_non_writeback_decisions", terminal_non_writeback) != terminal_non_writeback:
        fail("ledger summary.terminal_non_writeback_decisions mismatch")
    if open_review_items:
        fail(f"unresolved review tail(s) remain: {open_review_items}")
    return ledger


def validate_dry_run(ledger: dict[str, Any]) -> dict[str, Any]:
    require(DRY_JSON)
    require(DRY_MD)
    dry = json.loads(DRY_JSON.read_text(encoding="utf-8"))
    accepted = {(d["source"], d["target"]) for d in ledger.get("decisions", []) if d.get("decision") == "accept_taxonomy"}
    planned = {(r["source"], r["target"]) for r in dry.get("planned", [])}
    if not planned.issubset(accepted):
        fail("dry-run includes rows not accepted by ledger")
    forbidden = planned & FORBIDDEN_UP_PAIRS
    if forbidden:
        fail(f"dry-run includes forbidden non-taxonomy up pair(s): {sorted(forbidden)}")
    expected_writebacks = ledger.get("summary", {}).get("writeback_candidates", len(accepted))
    if not planned and expected_writebacks == 0:
        return dry
    if not planned:
        fail("dry-run contains no planned rows despite remaining writeback candidates")
    if dry.get("summary", {}).get("ready", 0) <= 0:
        fail("dry-run has no ready rows")
    return dry


def validate_apply_report(ledger: dict[str, Any]) -> dict[str, Any] | None:
    if not APPLY_JSON.exists():
        return None
    apply = json.loads(APPLY_JSON.read_text(encoding="utf-8"))
    accepted = {(d["source"], d["target"]) for d in ledger.get("decisions", []) if d.get("decision") == "accept_taxonomy"}
    applied_pairs = set()
    historical_or_already_present: list[tuple[str, str]] = []
    for row in apply.get("applied", []):
        pair = (row.get("source"), row.get("target"))
        if pair in FORBIDDEN_UP_PAIRS:
            fail(f"apply report includes forbidden non-taxonomy up pair: {pair}")
        path = CONCEPT_DIR / f"{row['source']}.md"
        fm = load_fm(path) if path.exists() else {}
        up = [x for x in (clean_link(v) for v in as_list(fm.get("up"))) if x]
        if pair not in accepted:
            # After a successful small-batch writeback, rebuilding the temporary
            # map removes those child cards from the current candidate list
            # because they now already have `up`. The apply report is still a
            # valid historical artifact if the applied edge is present on the
            # source card and remains non-forbidden.
            if row.get("result") in {"applied", "already_present"} and row.get("target") in up:
                historical_or_already_present.append(pair)
            else:
                fail(f"apply report includes row not accepted by current ledger and not present as historical up: {pair}")
        if row.get("result") == "applied":
            applied_pairs.add(pair)
            if not path.exists():
                fail(f"applied source missing: {path}")
            if row["target"] not in up:
                fail(f"{row['source']} missing applied up target {row['target']}")
            if "down" in fm:
                fail(f"{row['source']} has manual down field; Breadcrumbs should infer down")
            if "children" in fm:
                fail(f"{row['source']} has manual children field; Abstract Folder/Breadcrumbs should infer children")
    if historical_or_already_present:
        apply.setdefault("validation_warnings", []).append({
            "type": "historical_apply_rows_not_in_current_ledger",
            "pairs": [list(p) for p in historical_or_already_present],
            "note": "Rows already applied in an earlier small batch disappear from the regenerated candidate list once the source card has up; validation checked that the up edge is still present and non-forbidden.",
        })
    changed = subprocess.run(["git", "diff", "--name-only", "--", "agentic learning/wiki/concepts"], cwd=ROOT, text=True, capture_output=True, check=False).stdout.splitlines()
    changed_stems = {Path(p).stem for p in changed}
    external = sorted(changed_stems - {s for s, _t in applied_pairs})
    if external:
        # The vault may already contain unrelated concept edits from earlier wiki
        # maintenance. Report them as a boundary instead of failing this pipeline;
        # every row applied by this script is still required to be present in the
        # apply report and to contain the target up edge.
        apply.setdefault("validation_warnings", []).append({
            "type": "pre_existing_or_external_concept_diffs",
            "files": external,
            "note": "Concept diffs outside this apply report were left untouched by relation writeback validation.",
        })
    return apply


def validate_taxonomy_placement_apply(data: dict[str, Any]) -> dict[str, Any] | None:
    """Validate the concept hierarchy audit concept-hierarchy-placement apply artifact when present.

    This is separate from the older relation-decision writeback report: Limited apply
    consumes the specialized concept-hierarchy-placement dry-run and may apply rows that
    are no longer present in the regenerated candidate ledger after the child
    card receives `up`.
    """
    if not TAXONOMY_REVIEW_JSON.exists():
        return None

    review = json.loads(TAXONOMY_REVIEW_JSON.read_text(encoding="utf-8"))
    if review.get("artifact_type") != "taxonomy_placement_review":
        fail("concept hierarchy placement review artifact_type mismatch")
    if len(review.get("rows", [])) != len(data.get("nodes", [])):
        fail("concept hierarchy placement review row count does not match temp map node count")

    stage = review.get("classification_stage")
    if stage not in {"limited_apply", "audit_closure"}:
        return {
            "classification_stage": stage,
            "applied": 0,
            "post_apply_dry_run_planned": review.get("summary", {}).get("dry_run_planned"),
        }

    require(TAXONOMY_APPLY_JSON)
    require(TAXONOMY_DRY_RUN_JSON)
    apply = json.loads(TAXONOMY_APPLY_JSON.read_text(encoding="utf-8"))
    dry = json.loads(TAXONOMY_DRY_RUN_JSON.read_text(encoding="utf-8"))
    if apply.get("artifact_type") != "taxonomy_placement_apply_report":
        fail("concept hierarchy placement apply artifact_type mismatch")
    if apply.get("classification_stage") != "limited_apply":
        fail("concept hierarchy placement apply classification_stage mismatch")
    if dry.get("artifact_type") != "taxonomy_placement_writeback_dry_run":
        fail("concept hierarchy placement post-apply dry-run artifact_type mismatch")

    summary = apply.get("summary", {})
    applied = apply.get("applied", [])
    selected = apply.get("planned", [])
    if summary.get("selected") != len(selected):
        fail("concept hierarchy placement Limited apply selected count mismatch")
    if summary.get("concept_card_writes") != sum(1 for row in applied if row.get("result") == "applied"):
        fail("concept hierarchy placement Limited apply concept_card_writes mismatch")
    if summary.get("post_apply_dry_run_planned") != dry.get("summary", {}).get("planned"):
        fail("concept hierarchy placement Limited apply post-apply dry-run planned mismatch")
    if summary.get("post_apply_dry_run_ready") != dry.get("summary", {}).get("ready"):
        fail("concept hierarchy placement Limited apply post-apply dry-run ready mismatch")
    if review.get("summary", {}).get("limited_apply_applied") != summary.get("applied"):
        fail("concept hierarchy placement Limited apply review/apply applied summary mismatch")
    if review.get("summary", {}).get("limited_apply_post_apply_dry_run_planned") != summary.get("post_apply_dry_run_planned"):
        fail("concept hierarchy placement Limited apply review/apply post-apply dry-run mismatch")

    applied_pairs = {(row.get("source"), row.get("target")) for row in applied}
    excluded_pairs = {(row.get("source"), row.get("target")) for row in apply.get("excluded_from_input_dry_run", [])}
    overlap = applied_pairs & excluded_pairs
    if overlap:
        fail(f"concept hierarchy placement Limited apply applied rows overlap excluded rows: {sorted(overlap)}")
    for pair in applied_pairs:
        if pair in FORBIDDEN_UP_PAIRS:
            fail(f"concept hierarchy placement Limited apply applied forbidden non-taxonomy up pair: {pair}")

    for row in applied:
        source = str(row.get("source") or "")
        target = str(row.get("target") or "")
        if not source or not target:
            fail(f"concept hierarchy placement Limited apply applied row missing source/target: {row}")
        source_file = ROOT / str(row.get("source_file") or f"agentic learning/wiki/concepts/{source}.md")
        if not source_file.exists():
            fail(f"concept hierarchy placement Limited apply source file missing: {source_file.relative_to(ROOT)}")
        fm = load_fm(source_file)
        up = [x for x in (clean_link(v) for v in as_list(fm.get("up"))) if x]
        if target not in up:
            fail(f"concept hierarchy placement Limited apply target missing from source up: {source} -> {target}")
        if "down" in fm:
            fail(f"concept hierarchy placement Limited apply source has manual down field: {source}")
        if "children" in fm:
            fail(f"concept hierarchy placement Limited apply source has manual children field: {source}")

    result = {
        "classification_stage": stage,
        "applied": sum(1 for row in applied if row.get("result") == "applied"),
        "already_present": sum(1 for row in applied if row.get("result") == "already_present"),
        "post_apply_dry_run_planned": dry.get("summary", {}).get("planned"),
        "post_apply_dry_run_ready": dry.get("summary", {}).get("ready"),
        "apply_report": str(TAXONOMY_APPLY_JSON.relative_to(ROOT)),
    }
    if stage == "audit_closure":
        require(TAXONOMY_STEP10_JSON)
        closure = json.loads(TAXONOMY_STEP10_JSON.read_text(encoding="utf-8"))
        if closure.get("artifact_type") != "taxonomy_placement_audit_closure":
            fail("concept hierarchy placement Audit closure artifact_type mismatch")
        if closure.get("classification_stage") != "audit_closure":
            fail("concept hierarchy placement Audit closure classification_stage mismatch")
        tax_summary = review.get("summary", {})
        if tax_summary.get("open_review") != 0:
            fail("concept hierarchy placement Audit closure must leave open_review at 0")
        if tax_summary.get("open_writeback") != 0:
            fail("concept hierarchy placement Audit closure must leave open_writeback at 0")
        if tax_summary.get("dry_run_planned") != 0:
            fail("concept hierarchy placement Audit closure must leave dry_run_planned at 0")
        deferred_rows = [row for row in review.get("rows", []) if row.get("decision") == "defer_boundary_review"]
        if any(row.get("review_status") != "deferred_with_backlog" for row in deferred_rows):
            fail("concept hierarchy placement Audit closure deferred rows missing deferred_with_backlog status")
        if closure.get("summary", {}).get("deferred_with_backlog") != len(deferred_rows):
            fail("concept hierarchy placement Audit closure deferred_with_backlog count mismatch")
        if closure.get("summary", {}).get("concept_card_writes") != 0:
            fail("concept hierarchy placement Audit closure must not edit concept cards")
        completion = closure.get("completion_definition") or {}
        checks = completion.get("checks") or {}
        if not completion.get("met") or not all(value is True for value in checks.values()):
            fail(f"concept hierarchy placement Audit closure completion definition not met: {checks}")
        result["audit_closure_report"] = str(TAXONOMY_STEP10_JSON.relative_to(ROOT))
        result["deferred_with_backlog"] = closure.get("summary", {}).get("deferred_with_backlog")
    return result


def validate_plugin_compat(concept_files: list[Path], apply: dict[str, Any] | None) -> None:
    problems: list[str] = []
    checked_up_edges = 0
    forbidden_up_edges: list[str] = []
    for path in concept_files:
        fm = load_fm(path)
        up_values = as_list(fm.get("up"))
        for value in up_values:
            target = clean_link(value)
            checked_up_edges += 1
            if not target:
                problems.append(f"{path.relative_to(ROOT)} has unparsable up value {value!r}")
                continue
            if not (CONCEPT_DIR / f"{target}.md").exists():
                problems.append(f"{path.relative_to(ROOT)} up target missing: {target}")
            pair = (path.stem, target)
            if pair in FORBIDDEN_UP_PAIRS:
                msg = f"{path.relative_to(ROOT)} has forbidden non-taxonomy up target: {target}"
                problems.append(msg)
                forbidden_up_edges.append(msg)
        if "down" in fm:
            problems.append(f"{path.relative_to(ROOT)} has manual down field")
        if "children" in fm:
            problems.append(f"{path.relative_to(ROOT)} has manual children field")
    applied_count = 0
    if apply:
        applied_count = sum(1 for row in apply.get("applied", []) if row.get("result") == "applied")
    payload = {
        "schema_version": 1,
        "artifact_type": "breadcrumbs_abstract_folder_compat_validation",
        "summary": {
            "concept_cards_checked": len(concept_files),
            "up_edges_checked": checked_up_edges,
            "applied_rows_checked": applied_count,
            "problems": len(problems),
            "abstract_folder_contract": "parent property = up; no physical folder conversion required",
            "breadcrumbs_contract": "top-level up edge field only; down is implied; relations remains nested explanation layer",
            "juggl_contract": "retired; no Juggl mirror fields validated or required",
            "non_taxonomy_boundary_guardrails_checked": len(FORBIDDEN_UP_PAIRS),
            "forbidden_up_edges": len(forbidden_up_edges),
        },
        "problems": problems,
    }
    PLUGIN_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = ["# Breadcrumbs / Abstract Folder Compatibility Validation", ""]
    for k, v in payload["summary"].items():
        md.append(f"- {k}: {v}")
    md.append("")
    if problems:
        md.append("## Problems")
        md.extend([f"- {p}" for p in problems])
    else:
        md.append("## Problems")
        md.append("- none")
    md.append("")
    PLUGIN_MD.write_text("\n".join(md), encoding="utf-8")
    if problems:
        fail("plugin compatibility problems:\n" + "\n".join(problems))


def main() -> None:
    data, concept_files = validate_map()
    ledger = validate_ledger(data)
    dry = validate_dry_run(ledger)
    apply = validate_apply_report(ledger)
    taxonomy = validate_taxonomy_placement_apply(data)
    validate_plugin_compat(concept_files, apply)
    diff_check = subprocess.run(["git", "diff", "--check"], cwd=ROOT, text=True, capture_output=True, check=False)
    if diff_check.returncode != 0:
        fail("git diff --check failed:\n" + diff_check.stdout + diff_check.stderr)
    result = {
        "ok": True,
        "concepts": len(concept_files),
        "edges": len(data.get("edges", [])),
        "candidates": len(data.get("candidate_edges", [])),
        "ledger_decisions": len(ledger.get("decisions", [])),
        "open_review_items": ledger.get("summary", {}).get("open_review_items"),
        "open_writeback_items": ledger.get("summary", {}).get("open_writeback_items"),
        "relation_tail_status": ledger.get("summary", {}).get("relation_tail_status"),
        "dry_run_planned": len(dry.get("planned", [])),
        "applied": 0 if not apply else sum(1 for row in apply.get("applied", []) if row.get("result") == "applied"),
        "taxonomy_placement": taxonomy,
        "plugin_compat": str(PLUGIN_MD.relative_to(ROOT)),
    }
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
