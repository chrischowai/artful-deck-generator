#!/usr/bin/env python3
"""Dependency-free validator for the artful-deck-generator skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


MAX_SKILL_NAME_LENGTH = 64
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    if not text.startswith("---\n"):
        return {}, "No YAML frontmatter found"
    match = re.match(r"^---\n(.*?)\n---\n?", text, re.DOTALL)
    if not match:
        return {}, "Invalid frontmatter format"

    data: dict[str, str] = {}
    current_key: str | None = None
    for raw in match.group(1).splitlines():
      if not raw.strip():
          continue
      if raw[0].isspace() and current_key:
          data[current_key] += " " + raw.strip()
          continue
      if ":" not in raw:
          return {}, f"Invalid frontmatter line: {raw}"
      key, value = raw.split(":", 1)
      current_key = key.strip()
      data[current_key] = value.strip().strip('"').strip("'")
    return data, None


def validate_skill(skill_path: str) -> tuple[bool, str]:
    root = Path(skill_path)
    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")
    frontmatter, error = parse_frontmatter(content)
    if error:
        return False, error

    unexpected = set(frontmatter) - ALLOWED_FRONTMATTER
    if unexpected:
        return False, f"Unexpected frontmatter keys: {', '.join(sorted(unexpected))}"

    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()
    if not name:
        return False, "Missing 'name' in frontmatter"
    if not description:
        return False, "Missing 'description' in frontmatter"
    if not re.match(r"^[a-z0-9-]+$", name):
        return False, f"Name '{name}' should be hyphen-case"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
    if len(name) > MAX_SKILL_NAME_LENGTH:
        return False, f"Name is too long ({len(name)} characters)"
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets"
    if len(description) > 1024:
        return False, f"Description is too long ({len(description)} characters)"

    reference = root / "references" / "complete-slide-art-reference.jpg"
    if not reference.exists():
        return False, "Missing references/complete-slide-art-reference.jpg"
    audit_reference = root / "references" / "final-deck-audit.md"
    if not audit_reference.exists():
        return False, "Missing references/final-deck-audit.md"

    required_phrases = [
        "Do not use a multi-panel contact sheet",
        "Create a contact sheet or equivalent all-slide overview",
        "For decks over 20 slides, read `references/layout-variety-reference.md` and inspect every screenshot",
        "Before outlining, drafting copy, or building a deck, confirm the language.",
        "3. Bilingual (English + Traditional Chinese)",
        "Never infer bilingual output or a default language.",
        "GenImage is mandatory for new deck imagery",
        "Style reference controls treatment, never the subject.",
        "Run a content relevance gate before generation",
        "Run a scene-diversity pass across the full brief",
        "deploy a subagent final audit",
        "## Delivery Gate",
    ]
    missing = [phrase for phrase in required_phrases if phrase not in content]
    if missing:
        return False, "Missing required deck guardrail(s): " + "; ".join(missing)

    return True, "Skill is valid"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)

    ok, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if ok else 1)
