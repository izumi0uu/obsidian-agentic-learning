#!/usr/bin/env python3
"""Compatibility wrapper for the xiaolinnote updater.

The old crawler wrote directly to `raw/articles/xiaolinnote/`, which no longer
matches the vault's durable interview-bank layout. Keep this entry point so old
commands still work, but route all behavior through the preserving updater.
"""

from update_xiaolinnote import main


if __name__ == "__main__":
    raise SystemExit(main())
