#!/usr/bin/env python3
"""Audit raw paper source notes for evidence quality, not just structure.

The structural audit in ``paper_source_audit.py`` proves that required fields
exist. This script catches the failure mode that motivated the paper-card
repair pass: source notes can have the right headings while ``原文短摘`` is only
a keyword, or while the body still says "待精读正文后补" even though a local
extracted Markdown file exists.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PLACEHOLDER_PATTERNS = [
    "待精读正文后补",
    "待精读定位",
    "第一轮只基于 arXiv 摘要",
    "当前只录入摘要级短证据",
    "本轮未保存 PDF，仅用远程 PDF 生成 extracted 文本",
    "本页只保留 `## 需要我读的内容` 中的极短摘录",
]

REQUIRED_HEADINGS = [
    "## 为什么收",
    "## 一句话",
    "## 需要我读的内容",
    "## 论文主张",
    "## 可以拆成概念卡",
    "## 我的疑问",
    "## 边界提醒",
]


def frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    parts = text.split("---", 2)
    return parts[1] if len(parts) >= 3 else ""


def fm_value(fm: str, key: str) -> str:
    match = re.search(
        rf"(?m)^{re.escape(key)}:\s*(?:\"([^\"]*)\"|'([^']*)'|([^\n#]+))",
        fm,
    )
    if not match:
        return ""
    return next(group for group in match.groups() if group is not None).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]", text))


def is_source_paper(fm: str) -> bool:
    return bool(re.search(r"(?m)^type:\s*source\b", fm)) and bool(
        re.search(r"(?m)^source_type:\s*paper\b", fm)
    )


def audit_file(path: Path, min_quote_words: int, max_quote_words: int) -> list[str]:
    text = path.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if not is_source_paper(fm):
        return []

    errors: list[str] = []
    extracted = fm_value(fm, "extracted")
    has_extracted = bool(extracted)

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing heading: {heading}")

    if has_extracted:
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern in text:
                errors.append(f"placeholder remains despite extracted text: {pattern}")

    required_section = re.search(
        r"(?ms)^## 需要我读的内容\n(?P<body>.*?)(?=^## |\Z)", text
    )
    if not required_section:
        errors.append("missing ## 需要我读的内容")
        return errors

    blocks = re.split(r"(?m)^#### 必读块\s+\d+：", required_section.group("body"))[1:]
    if not blocks:
        errors.append("missing required-reading blocks")
        return errors

    for index, body in enumerate(blocks, 1):
        quotes = [
            quote.strip()
            for quote in re.findall(r"(?m)^\s*>\s*(.+)$", body)
            if not quote.strip().startswith("使用规则")
        ]
        if not quotes:
            errors.append(f"block {index} has no excerpt quote")
            continue
        for quote in quotes:
            count = word_count(quote)
            if count < min_quote_words:
                errors.append(
                    f"block {index} quote too short ({count} words/chars): {quote!r}"
                )
            if count > max_quote_words:
                errors.append(
                    f"block {index} quote too long ({count} words/chars > {max_quote_words})"
                )
            if re.search(r"^(Lucky Pass|process-level assessment|Prefix Tree Acceptor)$", quote):
                errors.append(f"block {index} quote is keyword-only: {quote!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="agentic learning/raw/papers")
    parser.add_argument("--min-quote-words", type=int, default=5)
    parser.add_argument("--max-quote-words", type=int, default=45)
    args = parser.parse_args()

    root = Path(args.root)
    paths = sorted(path for path in root.rglob("*.md") if path.is_file())
    failures: dict[Path, list[str]] = {}
    checked = 0

    for path in paths:
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if not is_source_paper(fm):
            continue
        checked += 1
        errors = audit_file(path, args.min_quote_words, args.max_quote_words)
        if errors:
            failures[path] = errors

    print(f"Paper source quality audit: checked {checked} files")
    if failures:
        for path, errors in failures.items():
            print(f"\nFAIL {path}")
            for error in errors:
                print(f"  - {error}")
        return 1

    print("PASS: paper source notes have non-placeholder extracted-backed short excerpts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
