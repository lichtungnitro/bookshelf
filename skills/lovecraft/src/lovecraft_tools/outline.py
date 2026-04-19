"""Emit a nested-evidence report skeleton from a small YAML file."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


def _load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("YAML root must be a mapping")
    return data


def _section_lines(title: str, key: str, body: str | None) -> list[str]:
    lines = [f"## {title}", ""]
    if body:
        lines.append(body.rstrip())
        lines.append("")
    else:
        lines.append(f"<!-- Fill `{key}` -->")
        lines.append("")
    return lines


def render_outline(data: dict[str, Any]) -> str:
    title = str(data.get("title", "Untitled report"))
    lines: list[str] = [f"# {title}", ""]

    frame = data.get("frame_narrator")
    if isinstance(frame, dict):
        lines.extend(_section_lines("Frame / responsible narrator", "frame_narrator", frame.get("prompt")))
    primary = data.get("primary_documents")
    if isinstance(primary, list):
        lines.append("## Primary documents (linked exhibits)")
        lines.append("")
        for i, item in enumerate(primary, start=1):
            if isinstance(item, dict):
                name = str(item.get("name", f"Document {i}"))
                note = item.get("note")
                lines.append(f"{i}. **{name}**")
                if note:
                    lines.append(f"   - {note}")
            else:
                lines.append(f"{i}. {item}")
        lines.append("")
    secondary = data.get("secondary_accounts")
    if isinstance(secondary, list):
        lines.append("## Secondary accounts (testimony, press, interviews)")
        lines.append("")
        for i, item in enumerate(secondary, start=1):
            lines.append(f"{i}. {item}")
        lines.append("")
    synthesis = data.get("synthesis_and_limits")
    if isinstance(synthesis, dict):
        lines.extend(
            _section_lines(
                "Synthesis, limits, and what would falsify this chain",
                "synthesis_and_limits",
                synthesis.get("prompt"),
            )
        )
    disclosure = data.get("disclosure_and_risk")
    if isinstance(disclosure, dict):
        lines.extend(
            _section_lines(
                "Disclosure, audience risk, and custody",
                "disclosure_and_risk",
                disclosure.get("prompt"),
            )
        )
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("usage: lovecraft-tools report-outline <outline.yaml>", file=sys.stderr)
        return 2
    path = Path(args[0])
    data = _load_yaml(path)
    sys.stdout.write(render_outline(data))
    return 0
