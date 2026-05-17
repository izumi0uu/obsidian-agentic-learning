"""Shared path resolution for project-owned concept taxonomy tooling.

The taxonomy scripts are intentionally project-native. They default to
``reports/concept-card-relation-map``. Set ``CONCEPT_TAXONOMY_OUT_DIR`` when
you need to read or write an alternate scratch report directory.
"""
from __future__ import annotations

import os
from pathlib import Path


def find_repo_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__)).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists() or (candidate / "agentic learning").exists():
            return candidate
    # Fallback for the checked-in layout: scripts/concept_taxonomy/paths.py
    return Path(__file__).resolve().parents[2]


def project_path(value: str | os.PathLike[str]) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


ROOT = find_repo_root()
VAULT_DIR = project_path(os.environ.get("CONCEPT_TAXONOMY_VAULT_DIR", "agentic learning"))
CONCEPT_DIR = project_path(os.environ.get("CONCEPT_TAXONOMY_CONCEPT_DIR", "agentic learning/wiki/concepts"))
DEFAULT_OUT_DIR = project_path("reports/concept-card-relation-map")
OUT_DIR = project_path(os.environ.get("CONCEPT_TAXONOMY_OUT_DIR", str(DEFAULT_OUT_DIR.relative_to(ROOT))))
SCRIPT_DIR = Path(__file__).resolve().parent


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)
