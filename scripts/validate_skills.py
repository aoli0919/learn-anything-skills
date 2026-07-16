#!/usr/bin/env python3
"""Validate repository structure and skill metadata."""

from __future__ import annotations

import re
import sys
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MANIFEST = ROOT / "skillpack.json"

REQUIRED_SECTIONS = [
    "When To Use",
    "Core Behavior",
    "Output",
]

LEARNING_CONTRACT_TERMS = [
    "next action",
    "visible artifact",
    "check question",
    "what to ignore",
    "resource cap",
    "reflection",
]

AGENT_KEYS = [
    "display_name",
    "short_description",
    "default_prompt",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def read_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter.")
    end = text.find("\n---", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed.")
    block = text[4:end].strip()
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def read_simple_yaml(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def manifest_skill_names() -> list[str]:
    if not MANIFEST.exists():
        fail(f"Missing manifest: {MANIFEST}")
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    skills = data.get("skills")
    if not isinstance(skills, list):
        fail("skillpack.json must contain a skills list.")
    return [str(skill) for skill in skills]


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    try:
        meta = read_frontmatter(text)
    except SystemExit:
        return [f"{path}: invalid frontmatter"]

    for key in ("name", "description"):
        if not meta.get(key):
            errors.append(f"{path}: missing frontmatter key {key}")

    if meta.get("name") != path.parent.name:
        errors.append(f"{path}: frontmatter name must match directory name")

    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", path.parent.name):
        errors.append(f"{path}: skill directory must be kebab-case")

    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in text:
            errors.append(f"{path}: missing section ## {section}")

    if "TODO" in text:
        errors.append(f"{path}: contains TODO")

    description = meta.get("description", "")
    if len(description) < 40:
        errors.append(f"{path}: description is too short")

    if not re.search(r"beginner|初学者|learner", text, re.IGNORECASE):
        errors.append(f"{path}: should mention beginner/learner behavior")

    lower_text = text.lower()
    for term in LEARNING_CONTRACT_TERMS:
        if term not in lower_text:
            errors.append(f"{path}: learning contract missing '{term}'")

    agent_path = path.parent / "agents" / "openai.yaml"
    if not agent_path.exists():
        errors.append(f"{path.parent}: missing agents/openai.yaml")
    else:
        agent_data = read_simple_yaml(agent_path)
        for key in AGENT_KEYS:
            if not agent_data.get(key):
                errors.append(f"{agent_path}: missing {key}")
        prompt = agent_data.get("default_prompt", "")
        if f"${path.parent.name}" not in prompt:
            errors.append(f"{agent_path}: default_prompt should include ${path.parent.name}")

    return errors


def main() -> None:
    if not SKILLS.exists():
        fail(f"Missing skills directory: {SKILLS}")

    manifest_names = manifest_skill_names()
    manifest_set = set(manifest_names)
    dir_set = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    if manifest_set != dir_set:
        fail(f"skillpack.json skills do not match skills/ directories: manifest={sorted(manifest_set)} dirs={sorted(dir_set)}")

    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    if len(skill_files) < 14:
        fail("Expected at least fourteen skills.")

    errors: list[str] = []
    for skill_file in skill_files:
        errors.extend(validate_skill(skill_file))

    for required in ("README.md", "README.zh-CN.md", "LICENSE", "CONTRIBUTING.md"):
        if not (ROOT / required).exists():
            errors.append(f"Missing {required}")

    if errors:
        print("\n".join(errors))
        raise SystemExit(1)

    print(f"Validated {len(skill_files)} skills.")


if __name__ == "__main__":
    main()
