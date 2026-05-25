#!/usr/bin/env python3
"""Import True Recall block-format cards into the local plugin database.

This is intentionally local and conservative:

- reads editable `#type/basic` Import Studio drafts;
- creates a database backup before writing unless `--no-backup` is passed;
- adds `flashcard_uid` to source Markdown files when needed;
- skips duplicate cards for the same source note.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sqlite3
import sys
import time
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "agentic learning" / ".true-recall" / "true-recall-g5rak3l5.db"
DEFAULT_IMPORT = ROOT / "reports" / "true-recall-transformer-import.md"
BACKUP_DIR = ROOT / "agentic learning" / ".true-recall" / "backups" / "codex"

BLOCK_RE = re.compile(r"(?ms)^#type/basic\s*\n(.*?)(?=^---\s*$|\Z)")
FIELD_RE = re.compile(r"^([A-Za-z][A-Za-z0-9 _-]*):\s*(.*)$")
SOURCE_FILE_RE = re.compile(r"file:\s*([^<>;\n]+)")
UID_RE = re.compile(r"^flashcard_uid:\s*[\"']?([a-f0-9]+)[\"']?\s*$", re.M)
FRONTMATTER_RE = re.compile(r"^---\n([\s\S]*?)\n---\n?")


@dataclass(frozen=True)
class DraftCard:
    front: str
    back: str
    source_path: Path


def now_ms() -> int:
    return int(time.time() * 1000)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def parse_blocks(text: str) -> list[DraftCard]:
    cards: list[DraftCard] = []
    for match in BLOCK_RE.finditer(text):
        block = match.group(1).strip()
        if not block:
            continue
        fields: dict[str, str] = {}
        current: str | None = None
        for line in block.splitlines():
            if line.strip().startswith("<!--"):
                source_match = SOURCE_FILE_RE.search(line)
                if source_match:
                    fields["__source_path"] = source_match.group(1).strip().removesuffix("--").strip()
                current = None
                continue
            field_match = FIELD_RE.match(line)
            if field_match:
                current = field_match.group(1).strip()
                fields[current] = field_match.group(2).strip()
                continue
            if current:
                fields[current] = f"{fields[current]}\n{line}".strip()

        front = fields.get("Front", "").strip()
        back = fields.get("Back", "").strip()
        source = fields.get("__source_path", "").strip()
        if front and back and source:
            path = Path(source)
            if not path.is_absolute():
                path = ROOT / path
            cards.append(DraftCard(front=front, back=back, source_path=path))
    return cards


def generate_source_uid() -> str:
    return uuid.uuid4().hex[:8]


def ensure_source_uid(path: Path, *, write: bool) -> tuple[str, bool]:
    text = path.read_text(encoding="utf-8")
    existing = UID_RE.search(text)
    if existing:
        return existing.group(1), False

    uid = generate_source_uid()
    match = FRONTMATTER_RE.match(text)
    if not match:
        new_text = f"---\nflashcard_uid: {uid}\n---\n\n{text}"
    else:
        frontmatter = match.group(1)
        body = text[match.end() :]
        lines = frontmatter.splitlines()
        insert_at = len(lines)
        for index, line in enumerate(lines):
            if re.match(r"^(related|up|relations|last_checked|freshness|conflicts):", line):
                insert_at = index
                break
        lines.insert(insert_at, f"flashcard_uid: {uid}")
        new_text = "---\n" + "\n".join(lines) + "\n---\n" + body

    if write:
        path.write_text(new_text, encoding="utf-8")
    return uid, write


def backup_database(db_path: Path) -> Path:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    backup = BACKUP_DIR / f"true-recall-backup-{stamp}.db"
    shutil.copy2(db_path, backup)
    return backup


def insert_cards(db_path: Path, cards: list[DraftCard], *, dry_run: bool) -> dict[str, object]:
    uid_by_path: dict[Path, str] = {}
    frontmatter_updates: list[str] = []
    created: list[str] = []
    skipped: list[str] = []

    conn = sqlite3.connect(db_path)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        for card in cards:
            source_uid = uid_by_path.get(card.source_path)
            if source_uid is None:
                source_uid, changed = ensure_source_uid(card.source_path, write=not dry_run)
                uid_by_path[card.source_path] = source_uid
                if changed:
                    frontmatter_updates.append(str(card.source_path.relative_to(ROOT)))

            fields_json = json.dumps({"Front": card.front, "Back": card.back}, ensure_ascii=False, separators=(",", ":"))
            duplicate = conn.execute(
                """
                SELECT n.id
                FROM notes n
                WHERE n.note_type_id = ?
                  AND n.fields_json = ?
                  AND n.source_uid = ?
                  AND n.deleted_at IS NULL
                """,
                ("builtin-basic", fields_json, source_uid),
            ).fetchone()
            if duplicate:
                skipped.append(card.front)
                continue

            if dry_run:
                created.append(card.front)
                continue

            timestamp = now_ms()
            due = now_iso()
            note_id = str(uuid.uuid4())
            card_id = str(uuid.uuid4())
            conn.execute(
                """
                INSERT INTO notes (
                    id, note_type_id, fields_json, tags, source_uid, source_text,
                    created_via, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    note_id,
                    "builtin-basic",
                    fields_json,
                    "",
                    source_uid,
                    str(card.source_path.relative_to(ROOT)),
                    "manual",
                    timestamp,
                    timestamp,
                ),
            )
            conn.execute(
                """
                INSERT INTO cards (
                    id, note_id, template_ord, due, stability, difficulty,
                    reps, lapses, state, last_review, scheduled_days,
                    learning_step, suspended, buried_until,
                    created_at, updated_at, source_uid
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    card_id,
                    note_id,
                    0,
                    due,
                    0,
                    0,
                    0,
                    0,
                    0,
                    None,
                    0,
                    0,
                    0,
                    None,
                    timestamp,
                    timestamp,
                    source_uid,
                ),
            )
            created.append(card.front)

        if dry_run:
            conn.rollback()
        else:
            conn.commit()
    finally:
        conn.close()

    return {
        "input_cards": len(cards),
        "created": len(created),
        "skipped_duplicates": len(skipped),
        "source_notes": len(uid_by_path),
        "frontmatter_updates": frontmatter_updates,
        "created_fronts": created,
        "skipped_fronts": skipped,
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(DEFAULT_IMPORT.relative_to(ROOT)))
    parser.add_argument("--db", default=str(DEFAULT_DB.relative_to(ROOT)))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = ROOT / input_path
    db_path = Path(args.db)
    if not db_path.is_absolute():
        db_path = ROOT / db_path

    cards = parse_blocks(input_path.read_text(encoding="utf-8"))
    if not cards:
        raise SystemExit(f"No importable #type/basic cards found in {input_path.relative_to(ROOT)}")

    backup = None
    if not args.dry_run and not args.no_backup:
        backup = backup_database(db_path)

    result = insert_cards(db_path, cards, dry_run=args.dry_run)
    if backup:
        result["backup"] = str(backup.relative_to(ROOT))
    result["input"] = str(input_path.relative_to(ROOT))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
