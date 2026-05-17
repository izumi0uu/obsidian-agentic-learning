#!/usr/bin/env python3
"""Validate the vault-readable concept hierarchy placement baseline mirror."""
from __future__ import annotations

import paths
import json
import sys
from pathlib import Path

ROOT = paths.ROOT
OUT_DIR = paths.OUT_DIR
REVIEW = OUT_DIR / "concept-hierarchy-placement-review.json"
CLOSURE = OUT_DIR / "concept-hierarchy-placement-closure.json"
BASELINE = ROOT / "agentic learning" / "maps" / "09 概念层级审计基线.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    review = json.loads(REVIEW.read_text(encoding="utf-8"))
    closure = json.loads(CLOSURE.read_text(encoding="utf-8"))
    text = BASELINE.read_text(encoding="utf-8")
    summary = review["summary"]

    required_literals = [
        "# 09 概念层级审计基线",
        f"classification_stage: `{review['classification_stage']}`",
        f"total_concepts: `{summary['total_concepts']}`",
        f"reviewed_concepts: `{summary['reviewed_concepts']}`",
        f"concepts_with_up: `{summary['concepts_with_up']}`",
        f"concepts_without_up: `{summary['concepts_without_up']}`",
        f"open_review: `{summary['open_review']}`",
        f"open_writeback: `{summary['open_writeback']}`",
        f"dry_run_planned: `{summary['dry_run_planned']}`",
        f"deferred_with_backlog: `{summary['deferred_with_backlog']}`",
        "[[06 Wiki 健康检查#2026-05-17 概念层级审计边界队列]]",
    ]
    for literal in required_literals:
        if literal not in text:
            fail(f"baseline map missing literal: {literal}")

    for row in review["rows"]:
        link = f"[[{row['concept']}]]"
        if link not in text:
            fail(f"baseline map missing concept link: {link}")

    deferred = closure.get("deferred_with_backlog", [])
    if len(deferred) != summary.get("deferred_with_backlog"):
        fail("closure deferred count does not match review summary")
    for item in deferred:
        if f"[[{item['concept']}]]" not in text:
            fail(f"baseline map missing deferred concept: {item['concept']}")
        if item.get("suppressed_signal_type") and f"`{item['suppressed_signal_type']}`" not in text:
            fail(f"baseline map missing deferred signal: {item['concept']}")

    print(json.dumps({
        "ok": True,
        "baseline": str(BASELINE.relative_to(ROOT)),
        "total_concepts": summary["total_concepts"],
        "deferred_with_backlog": summary["deferred_with_backlog"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
