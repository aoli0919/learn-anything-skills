#!/usr/bin/env python3
"""Install Learn Anything Skills into a local Codex skills directory."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
MANIFEST = ROOT / "skillpack.json"


def default_target() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    return Path.home() / ".codex" / "skills"


def manifest_skill_names() -> list[str]:
    if not MANIFEST.exists():
        raise SystemExit(f"Missing manifest: {MANIFEST}")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    skills = data.get("skills")
    if not isinstance(skills, list) or not skills:
        raise SystemExit("skillpack.json must contain a non-empty skills list.")
    return [str(skill) for skill in skills]


def validate_before_install() -> None:
    result = subprocess.run(
        ["python3", str(ROOT / "scripts" / "validate_skills.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit("Validation failed; install aborted.")


def install(target: Path, dry_run: bool, force: bool, skip_validate: bool) -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Missing skills directory: {SOURCE}")

    if not skip_validate:
        validate_before_install()

    target = target.expanduser().resolve()
    skill_names = manifest_skill_names()
    skill_dirs = [SOURCE / name for name in skill_names]

    print(f"Source: {SOURCE}")
    print(f"Target: {target}")

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            raise SystemExit(f"Missing SKILL.md in {skill_dir}")

        destination = target / skill_dir.name
        print(f"{'Would install' if dry_run else 'Installing'} {skill_dir.name}")

        if dry_run:
            if destination.exists():
                print("  conflict: already installed")
            continue

        target.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            if not force:
                raise SystemExit(
                    f"{destination} already exists. Re-run with --force to back it up and replace it."
                )
            stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            backup = destination.with_name(f"{destination.name}.backup-{stamp}")
            destination.rename(backup)
            print(f"  backed up existing skill to {backup}")

        shutil.copytree(skill_dir, destination)

    print("Done.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=default_target())
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="Replace existing skills after creating timestamped backups.")
    parser.add_argument("--skip-validate", action="store_true", help="Skip validation before installing.")
    args = parser.parse_args()
    install(args.target, args.dry_run, args.force, args.skip_validate)


if __name__ == "__main__":
    main()
