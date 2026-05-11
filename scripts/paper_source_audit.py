#!/usr/bin/env python3
"""Audit raw paper source notes for the vault's paper-card evidence template.

This is a structural audit only: it verifies that each `raw/papers/*.md`
contains the required sections and evidence-block fields. It does not prove the
scientific accuracy of summaries or replace human/source review.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "## 为什么收",
    "## 一句话",
    "## 需要我读的内容",
    "## 论文主张",
    "## 可以拆成概念卡",
    "## 我的疑问",
    "## 边界提醒",
]

REQUIRED_BLOCK_FIELDS = [
    "位置",
    "为什么必读",
    "原文短摘",
    "中文概括",
    "我需要理解的机制",
    "支撑概念",
    "证据边界",
]


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    return parts[1]


def section_after(text: str, heading: str) -> str:
    pattern = re.compile(rf"^{re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)", re.M | re.S)
    match = pattern.search(text)
    return match.group("body") if match else ""


def word_count(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]", s))


def audit_file(path: Path, max_quote_words: int) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    fm = frontmatter(text)
    if not fm:
        errors.append("missing YAML frontmatter")
    else:
        if not re.search(r"(?m)^type:\s*source\b", fm):
            errors.append("frontmatter type is not source")
        if not re.search(r"(?m)^source_type:\s*paper\b", fm):
            errors.append("frontmatter source_type is not paper")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing heading: {heading}")

    required = section_after(text, "## 需要我读的内容")
    if "### 必读" not in required:
        errors.append("missing ### 必读 under ## 需要我读的内容")
        return errors

    blocks = re.split(r"(?m)^#### 必读块\s+\d+：", required)
    block_bodies = blocks[1:]
    if not block_bodies:
        errors.append("missing #### 必读块")
        return errors

    for index, body in enumerate(block_bodies, 1):
        for field in REQUIRED_BLOCK_FIELDS:
            if field not in body:
                errors.append(f"block {index} missing field: {field}")
        quotes = re.findall(r"(?m)^\s*>\s*(.+)$", body)
        if not quotes:
            errors.append(f"block {index} missing blockquote short excerpt")
        for quote in quotes:
            if "待精读" not in quote and word_count(quote) > max_quote_words:
                errors.append(
                    f"block {index} quote too long ({word_count(quote)} words/chars > {max_quote_words})"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="agentic learning/raw/papers",
        help="Directory containing paper source notes.",
    )
    parser.add_argument("--max-quote-words", type=int, default=45)
    args = parser.parse_args()

    root = Path(args.root)
    paths = sorted(p for p in root.glob("*.md") if p.is_file())
    all_errors: dict[Path, list[str]] = {}
    for path in paths:
        errors = audit_file(path, args.max_quote_words)
        if errors:
            all_errors[path] = errors

    print(f"Paper source audit: checked {len(paths)} files")
    if all_errors:
        for path, errors in all_errors.items():
            print(f"\nFAIL {path}")
            for error in errors:
                print(f"  - {error}")
        return 1
    print("PASS: all paper source notes satisfy required-reading evidence structure")
    return 0


if __name__ == "__main__":
    sys.exit(main())
