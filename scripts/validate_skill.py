#!/usr/bin/env python3
"""Validate the installable quant strategy skill without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SKILL_NAME = "quant-strategy-builder"
REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / SKILL_NAME
REQUIRED_REFERENCES = [
    "backtrader-adapter.md",
    "freqtrade-adapter.md",
    "lean-adapter.md",
    "optionforge-adapter.md",
    "prompt-map.md",
    "strategy-design-workflow.md",
    "validation-matrix.md",
]
FORBIDDEN_CORE_PATTERNS = [
    "strategy_spec.toml",
    ".focus/context.json",
    "src/strategy/",
    "python -m src.cli.app",
]


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def read_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md is missing valid YAML frontmatter.")

    block = match.group(1)
    body = match.group(2)
    frontmatter: dict[str, str] = {}
    for raw_line in block.splitlines():
        if not raw_line.strip():
            continue
        if raw_line.startswith(" "):
            continue
        if ":" not in raw_line:
            raise ValueError(f"Invalid frontmatter line: {raw_line}")
        key, value = raw_line.split(":", 1)
        frontmatter[key.strip()] = strip_quotes(value)
    return frontmatter, body


def read_interface_map(text: str) -> dict[str, str]:
    lines = text.splitlines()
    inside_interface = False
    interface: dict[str, str] = {}

    for line in lines:
        if not inside_interface:
            if line.strip() == "interface:":
                inside_interface = True
            continue

        if line and not line.startswith("  "):
            break
        if not line.strip():
            continue
        if not line.startswith("  ") or ":" not in line:
            raise ValueError(f"Invalid interface line: {line}")
        key, raw_value = line.strip().split(":", 1)
        raw_value = raw_value.strip()
        if not (raw_value.startswith('"') and raw_value.endswith('"')):
            raise ValueError(f"Value for interface.{key} must be quoted.")
        interface[key] = strip_quotes(raw_value)

    if not interface:
        raise ValueError("agents/openai.yaml is missing the interface section.")
    return interface


def validate_skill() -> list[str]:
    errors: list[str] = []

    skill_md = SKILL_DIR / "SKILL.md"
    openai_yaml = SKILL_DIR / "agents" / "openai.yaml"
    references_dir = SKILL_DIR / "references"

    if not skill_md.exists():
        return [f"Missing {skill_md}"]
    if not openai_yaml.exists():
        errors.append(f"Missing {openai_yaml}")
    if not references_dir.exists():
        errors.append(f"Missing {references_dir}")

    try:
        frontmatter, body = read_frontmatter(skill_md.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [str(exc)]

    if frontmatter.get("name") != SKILL_NAME:
        errors.append(f"Frontmatter name must be {SKILL_NAME}.")

    description = frontmatter.get("description", "")
    if not description:
        errors.append("Frontmatter description is required.")

    if not re.fullmatch(r"[a-z0-9-]+", frontmatter.get("name", "")):
        errors.append("Skill name must be hyphen-case.")

    for pattern in FORBIDDEN_CORE_PATTERNS:
        if pattern in body:
            errors.append(
                f"Core SKILL.md should not contain OptionForge-specific marker: {pattern}"
            )

    if openai_yaml.exists():
        try:
            interface = read_interface_map(openai_yaml.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(str(exc))
            interface = {}

        for key in ("display_name", "short_description", "default_prompt"):
            if key not in interface:
                errors.append(f"agents/openai.yaml is missing interface.{key}.")

        short_description = interface.get("short_description", "")
        if short_description and not (25 <= len(short_description) <= 64):
            errors.append("interface.short_description must be 25-64 characters.")

        default_prompt = interface.get("default_prompt", "")
        if default_prompt and f"${SKILL_NAME}" not in default_prompt:
            errors.append("interface.default_prompt must mention $quant-strategy-builder.")

    for reference_name in REQUIRED_REFERENCES:
        reference_path = references_dir / reference_name
        if not reference_path.exists():
            errors.append(f"Missing required reference: {reference_name}")

    return errors


def main() -> int:
    errors = validate_skill()
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed for {SKILL_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
