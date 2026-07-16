#!/usr/bin/env python3
"""Create a dated learning log from the repository template."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "learning-log.md"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", default="Untitled topic")
    parser.add_argument("--output-dir", type=Path, default=Path(".learning-logs"))
    args = parser.parse_args()

    if not TEMPLATE.exists():
        raise SystemExit(f"Missing template: {TEMPLATE}")

    text = TEMPLATE.read_text(encoding="utf-8")
    today = date.today().isoformat()
    text = text.replace("{{date}}", today).replace("{{topic}}", args.topic)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    path = args.output_dir / f"{today}-{args.topic.lower().replace(' ', '-')}.md"
    path.write_text(text, encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()

