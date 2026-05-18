#!/usr/bin/env python3
"""Build a deterministic JSON search index for the public GitHub vault.

The index is intentionally dependency-free so it can run in GitHub Actions and
on a fresh machine. It indexes Markdown knowledge assets, keeps enough metadata
for filtering, and truncates body text to keep the committed JSON reviewable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "search-index.json"
REPOSITORY_URL = "https://github.com/izumi0uu/obsidian-agentic-learning"
MAX_TEXT_CHARS = 8000

INCLUDE_PREFIXES = (
    "README.md",
    "AGENTS.md",
    "agentic learning/",
)

EXCLUDE_PARTS = {
    ".obsidian",
    "templates",
    "Excalidraw",
}

LIST_FIELDS = {
    "aliases",
    "evidence",
    "related",
    "source",
    "topic",
    "up",
}


def run_git_ls_files() -> list[str]:
    cmd = [
        "git",
        "-c",
        "core.quotePath=false",
        "ls-files",
        "--cached",
        "--others",
        "--exclude-standard",
        "*.md",
    ]
    try:
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return []
    return [line for line in result.stdout.splitlines() if line]


def fallback_markdown_files() -> list[str]:
    return sorted(str(path.relative_to(ROOT)) for path in ROOT.rglob("*.md"))


def should_index(relative_path: str) -> bool:
    if not relative_path.startswith(INCLUDE_PREFIXES):
        return False
    parts = set(Path(relative_path).parts)
    if parts & EXCLUDE_PARTS:
        return False
    return True


def markdown_files() -> list[Path]:
    files = run_git_ls_files() or fallback_markdown_files()
    return [ROOT / path for path in sorted(files) if should_index(path)]


def split_frontmatter(content: str) -> tuple[dict[str, object], str]:
    if not content.startswith("---\n"):
        return {}, content

    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content

    raw_frontmatter = content[4:end]
    body = content[end + 5 :]
    return parse_frontmatter(raw_frontmatter), body


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def parse_inline_list(value: str) -> list[str] | None:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return None
    inner = value[1:-1].strip()
    if not inner:
        return []
    return [strip_quotes(part.strip()) for part in inner.split(",") if part.strip()]


def parse_frontmatter(raw: str) -> dict[str, object]:
    fields: dict[str, object] = {}
    current_key: str | None = None

    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        list_item = re.match(r"^\s*-\s+(.*)$", line)
        if list_item and current_key:
            fields.setdefault(current_key, [])
            if isinstance(fields[current_key], list):
                fields[current_key].append(strip_quotes(list_item.group(1)))
            continue

        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not match:
            current_key = None
            continue

        key, value = match.group(1), match.group(2).strip()
        current_key = key if value == "" else None

        if value == "":
            fields[key] = []
            continue

        inline_list = parse_inline_list(value)
        if inline_list is not None:
            fields[key] = inline_list
        elif key in LIST_FIELDS:
            fields[key] = [strip_quotes(value)]
        else:
            fields[key] = strip_quotes(value)

    return fields


def as_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return None


def headings(body: str) -> list[str]:
    found: list[str] = []
    for line in body.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            found.append(match.group(2).strip())
    return found


def normalize_wikilinks(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        target = match.group(1)
        return target.split("|", 1)[-1]

    return re.sub(r"\[\[([^\]]+)\]\]", replace, text)


def normalize_markdown(text: str) -> str:
    text = normalize_wikilinks(text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"[*_~>#|-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def file_kind(relative_path: str, frontmatter: dict[str, object]) -> str:
    explicit = str(frontmatter.get("type", "")).strip()
    if explicit:
        return explicit
    if relative_path == "README.md":
        return "readme"
    if relative_path == "AGENTS.md":
        return "agent-guidance"
    return "markdown"


def github_url(relative_path: str) -> str:
    return f"{REPOSITORY_URL}/blob/main/{quote(relative_path)}"


def build_document(path: Path) -> dict[str, object]:
    relative_path = path.relative_to(ROOT).as_posix()
    content = path.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(content)
    title = first_heading(body) or str(frontmatter.get("title", "")).strip() or path.stem
    normalized_text = normalize_markdown(body)
    truncated_text = normalized_text[:MAX_TEXT_CHARS]

    document = {
        "title": title,
        "path": relative_path,
        "url": github_url(relative_path),
        "type": file_kind(relative_path, frontmatter),
        "status": str(frontmatter.get("status", "")).strip(),
        "updated": str(frontmatter.get("updated", "")).strip(),
        "topic": as_list(frontmatter.get("topic")),
        "aliases": as_list(frontmatter.get("aliases")),
        "related": as_list(frontmatter.get("related")),
        "headings": headings(body)[:40],
        "excerpt": truncated_text[:500],
        "text": truncated_text,
        "truncated": len(normalized_text) > MAX_TEXT_CHARS,
        "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
    }

    return {key: value for key, value in document.items() if value not in ("", [], None)}


def build_index(paths: Iterable[Path]) -> dict[str, object]:
    documents = [build_document(path) for path in paths]
    type_counts: dict[str, int] = {}
    for document in documents:
        doc_type = str(document.get("type", "markdown"))
        type_counts[doc_type] = type_counts.get(doc_type, 0) + 1

    return {
        "schema_version": 1,
        "repository": "izumi0uu/obsidian-agentic-learning",
        "source": "Markdown files tracked in the public vault",
        "generated_by": "scripts/build_search_index.py",
        "document_count": len(documents),
        "type_counts": dict(sorted(type_counts.items())),
        "max_text_chars": MAX_TEXT_CHARS,
        "documents": documents,
    }


def render_index(index: dict[str, object]) -> str:
    return json.dumps(index, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSON path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the output file is missing or not up to date.",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = ROOT / output_path

    rendered = render_index(build_index(markdown_files()))

    if args.check:
        if not output_path.exists():
            print(f"{output_path.relative_to(ROOT)} is missing; run scripts/build_search_index.py", file=sys.stderr)
            return 1
        current = output_path.read_text(encoding="utf-8")
        if current != rendered:
            print(f"{output_path.relative_to(ROOT)} is stale; run scripts/build_search_index.py", file=sys.stderr)
            return 1
        print(f"{output_path.relative_to(ROOT)} is up to date")
        return 0

    output_path.write_text(rendered, encoding="utf-8")
    print(f"Wrote {output_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
