#!/usr/bin/env python3
"""Export concept-card review prompts as True Recall Import Studio blocks.

The script does not modify the True Recall SQLite database. It reads stable
concept-card sections and writes an editable Markdown import draft using the
block format accepted by True Recall Import Studio:

    #type/basic
    Front: Question
    Back: Answer
    ---
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
CONCEPT_DIR = ROOT / "agentic learning" / "wiki" / "concepts"
DEFAULT_OUTPUT = ROOT / "reports" / "true-recall-concept-cards.md"

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.S)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
COMMENT_RE = re.compile(r"<!--[\s\S]*?-->")

CARD_PRIORITY = (
    ("一句话", "用一句话解释 {title}。"),
    ("它不是什么", "{title} 最容易被误认为哪些相邻概念？"),
    ("边界细节", "判断 {title} 是否适用时，最小边界是什么？"),
    ("现代性状态", "{title} 在现代系统里的状态是什么？"),
    ("常见误解", "{title} 的常见误解或风险是什么？"),
    ("常见误解 / 风险", "{title} 的常见误解或风险是什么？"),
)


@dataclass(frozen=True)
class ImportCard:
    title: str
    front: str
    back: str
    source_anchor: str
    source_path: str


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def first_heading(body: str, fallback: str) -> str:
    for line in body.splitlines():
        match = HEADING_RE.match(line)
        if match and len(match.group(1)) == 1:
            return match.group(2).strip()
    return fallback


def slug_to_concept_path(value: str) -> Path | None:
    candidate = Path(value)
    if candidate.exists():
        return candidate if candidate.is_absolute() else ROOT / candidate

    if candidate.suffix == ".md":
        path = CONCEPT_DIR / candidate.name
    else:
        path = CONCEPT_DIR / f"{value}.md"
    return path if path.exists() else None


def iter_concept_paths(values: list[str]) -> list[Path]:
    if not values:
        return sorted(CONCEPT_DIR.glob("*.md"))

    paths: list[Path] = []
    missing: list[str] = []
    for value in values:
        path = slug_to_concept_path(value)
        if path is None:
            missing.append(value)
        else:
            paths.append(path)

    if missing:
        joined = ", ".join(missing)
        raise SystemExit(f"Could not resolve concept card(s): {joined}")
    return sorted(dict.fromkeys(paths))


def parse_sections(body: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None

    for line in body.splitlines():
        match = HEADING_RE.match(line)
        if match and len(match.group(1)) == 2:
            current = match.group(2).strip()
            sections.setdefault(current, [])
            continue
        if current:
            sections[current].append(line)

    return {heading: "\n".join(lines).strip() for heading, lines in sections.items()}


def normalize_inline_markdown(text: str, *, max_chars: int) -> str:
    text = COMMENT_RE.sub("", text)
    text = WIKILINK_RE.sub(lambda m: m.group(2) or m.group(1), text)
    text = MARKDOWN_LINK_RE.sub(lambda m: m.group(1), text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)

    parts: list[str] = []
    for line in text.splitlines():
        cleaned = line.strip()
        if not cleaned or cleaned.startswith(">"):
            continue
        cleaned = re.sub(r"^\s*[-*+]\s+", "", cleaned)
        cleaned = re.sub(r"^\s*\d+[.)]\s+", "", cleaned)
        cleaned = cleaned.strip()
        if cleaned:
            parts.append(cleaned)

    joined = "；".join(parts)
    joined = re.sub(r"([。.!?！？])；", r"\1 ", joined)
    joined = re.sub(r"\s+", " ", joined).strip()
    joined = joined.replace("\t", " ")
    if len(joined) > max_chars:
        joined = joined[: max_chars - 1].rstrip(" ，,;；。") + "…"
    return joined


def normalize_question(text: str) -> str:
    text = normalize_inline_markdown(text, max_chars=180)
    text = text.rstrip("。.")
    if not text.endswith(("?", "？")):
        text += "？"
    return text


def anchor_link(title: str, section: str) -> str:
    return f"[[{title}#{section}]]"


def trigger_questions(section_text: str) -> list[str]:
    questions: list[str] = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = re.match(r"^(?:[-*+]|\d+[.)])\s+(.*)$", stripped)
        if not match:
            continue
        question = normalize_question(match.group(1))
        if question and not question.startswith("如果我答错"):
            questions.append(question)
    return questions


def build_cards_for_path(
    path: Path,
    *,
    max_cards_per_note: int,
    max_back_chars: int,
    include_triggers: bool,
) -> list[ImportCard]:
    text = path.read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    title = first_heading(body, path.stem)
    sections = parse_sections(body)
    cards: list[ImportCard] = []

    for section, front_template in CARD_PRIORITY:
        if len(cards) >= max_cards_per_note:
            break
        content = sections.get(section)
        if not content:
            continue
        back = normalize_inline_markdown(content, max_chars=max_back_chars)
        if not back:
            continue
        cards.append(
            ImportCard(
                title=title,
                front=front_template.format(title=title),
                back=back,
                source_anchor=anchor_link(title, section),
                source_path=str(path.relative_to(ROOT)),
            )
        )

    if include_triggers and len(cards) < max_cards_per_note:
        for question in trigger_questions(sections.get("复习触发", "")):
            if len(cards) >= max_cards_per_note:
                break
            cards.append(
                ImportCard(
                    title=title,
                    front=question,
                    back=f"先自行作答；答错回看 {anchor_link(title, '复习触发')} 和概念卡的边界 section。",
                    source_anchor=anchor_link(title, "复习触发"),
                    source_path=str(path.relative_to(ROOT)),
                )
            )

    return cards


def render_import(cards: list[ImportCard]) -> str:
    lines = [
        "# True Recall concept-card import draft",
        "",
        "> Generated by `scripts/export_true_recall_concept_cards.py`.",
        "> Review/delete cards before saving them in True Recall Import Studio.",
        "",
    ]

    for card in cards:
        lines.extend(
            [
                "#type/basic",
                f"Front: {card.front}",
                f"Back: {card.back}",
                f"<!-- source: {card.source_anchor}; file: {card.source_path} -->",
                "---",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_summary(cards: list[ImportCard], paths: Iterable[Path]) -> dict[str, object]:
    by_note: dict[str, int] = {}
    for card in cards:
        by_note[card.source_path] = by_note.get(card.source_path, 0) + 1
    return {
        "concept_files": len(list(paths)),
        "cards": len(cards),
        "notes_with_cards": len(by_note),
        "by_note": by_note,
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "concepts",
        nargs="*",
        help="Concept titles or Markdown paths. Defaults to all wiki/concepts/*.md.",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT.relative_to(ROOT)),
        help="Markdown import draft path, relative to repo root by default.",
    )
    parser.add_argument("--max-cards-per-note", type=int, default=3)
    parser.add_argument("--max-back-chars", type=int, default=420)
    parser.add_argument(
        "--include-triggers",
        action="store_true",
        help="Also convert ## 复习触发 questions into self-test cards.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print summary JSON without writing the import draft.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.max_cards_per_note < 1:
        raise SystemExit("--max-cards-per-note must be >= 1")
    if args.max_back_chars < 80:
        raise SystemExit("--max-back-chars must be >= 80")

    paths = iter_concept_paths(args.concepts)
    cards: list[ImportCard] = []
    for path in paths:
        cards.extend(
            build_cards_for_path(
                path,
                max_cards_per_note=args.max_cards_per_note,
                max_back_chars=args.max_back_chars,
                include_triggers=args.include_triggers,
            )
        )

    summary = write_summary(cards, paths)
    if args.dry_run:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_import(cards), encoding="utf-8")
    print(json.dumps({**summary, "output": str(output.relative_to(ROOT))}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
