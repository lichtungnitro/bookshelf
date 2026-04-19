"""Build a timeline and claim table from dissociated source snippets (JSON)."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Claim:
    cid: str
    source: str
    occurred: date | None
    text: str
    tags: tuple[str, ...]
    relates_to: tuple[str, ...]


def _parse_date(s: str | None) -> date | None:
    if not s:
        return None
    y, m, d = (int(x) for x in s.split("-", 2))
    return date(y, m, d)


def load_claims(path: Path) -> tuple[str | None, list[Claim]]:
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    title = data.get("title")
    claims: list[Claim] = []
    for raw in data.get("claims", []):
        claims.append(
            Claim(
                cid=str(raw["id"]),
                source=str(raw.get("source", "")),
                occurred=_parse_date(raw.get("date")),
                text=str(raw.get("text", "")).strip(),
                tags=tuple(str(t) for t in raw.get("tags", []) if t is not None),
                relates_to=tuple(str(x) for x in raw.get("relates_to", []) if x is not None),
            )
        )
    return (title if isinstance(title, str) else None), claims


def render_markdown(title: str | None, claims: list[Claim]) -> str:
    lines: list[str] = []
    if title:
        lines.append(f"# {title}")
        lines.append("")
    lines.append("## Timeline (dated claims)")
    lines.append("")
    dated = [(c.occurred, c) for c in claims if c.occurred is not None]
    undated = [c for c in claims if c.occurred is None]
    dated.sort(key=lambda x: x[0])
    if not dated and not undated:
        lines.append("_No claims._")
        lines.append("")
    else:
        for d, c in dated:
            tag = f" `[{', '.join(c.tags)}]`" if c.tags else ""
            rel = f" → relates: {', '.join(c.relates_to)}" if c.relates_to else ""
            lines.append(f"- **{d.isoformat()}** — `{c.cid}` ({c.source}){tag}{rel}")
            lines.append(f"  - {c.text}")
        lines.append("")
    if undated:
        lines.append("### Undated")
        lines.append("")
        for c in undated:
            tag = f" `[{', '.join(c.tags)}]`" if c.tags else ""
            lines.append(f"- `{c.cid}` ({c.source}){tag}: {c.text}")
        lines.append("")

    lines.append("## Claim index")
    lines.append("")
    lines.append("| id | source | date | tags |")
    lines.append("|---|-----|-----|-----|")
    for c in sorted(claims, key=lambda x: x.cid):
        ds = c.occurred.isoformat() if c.occurred else ""
        tags = ", ".join(c.tags)
        lines.append(f"| {c.cid} | {c.source} | {ds} | {tags} |")
    lines.append("")

    by_tag: dict[str, list[str]] = defaultdict(list)
    for c in claims:
        if not c.tags:
            by_tag["(untagged)"].append(c.cid)
        for t in c.tags:
            by_tag[t].append(c.cid)
    lines.append("## Tag co-occurrence (possible convergence)")
    lines.append("")
    for tag, ids in sorted(by_tag.items(), key=lambda x: (-len(x[1]), x[0])):
        uniq = sorted(set(ids))
        lines.append(f"- **{tag}**: {len(uniq)} — {', '.join(uniq)}")
    lines.append("")

    # Simple contradiction / tension hints: same tag, different sources, same date
    lines.append("## Same-day multi-source tag overlap (review for tension)")
    lines.append("")
    bucket: dict[tuple[date, str], list[str]] = defaultdict(list)
    for c in claims:
        if c.occurred is None:
            continue
        for t in c.tags:
            bucket[(c.occurred, t)].append(f"{c.cid}:{c.source}")
    printed = False
    for (d, t), refs in sorted(bucket.items()):
        if len(set(r.split(":", 1)[1] for r in refs)) < 2:
            continue
        printed = True
        lines.append(f"- {d.isoformat()} / `{t}`: {', '.join(sorted(set(refs)))}")
    if not printed:
        lines.append("_None detected from tags + dates._")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("usage: lovecraft-tools evidence-matrix <claims.json>", file=sys.stderr)
        return 2
    path = Path(args[0])
    title, claims = load_claims(path)
    sys.stdout.write(render_markdown(title, claims))
    return 0
