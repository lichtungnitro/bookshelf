"""Find dense date-window overlap across many observers (weak-signal clustering)."""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path


@dataclass(frozen=True)
class Interval:
    oid: str
    start: date
    end: date
    cohort: str


def _parse_date(s: str) -> date:
    return datetime.strptime(s.strip(), "%Y-%m-%d").date()


def load_intervals(path: Path) -> list[Interval]:
    rows: list[Interval] = []
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        required = {"observer_id", "window_start", "window_end"}
        if not reader.fieldnames or not required.issubset(set(reader.fieldnames)):
            raise ValueError(
                f"CSV must include columns {sorted(required)}; got {reader.fieldnames!r}"
            )
        for raw in reader:
            oid = (raw.get("observer_id") or "").strip()
            if not oid:
                continue
            cohort = (raw.get("cohort") or "").strip() or "unknown"
            rows.append(
                Interval(
                    oid=oid,
                    start=_parse_date(raw["window_start"]),
                    end=_parse_date(raw["window_end"]),
                    cohort=cohort,
                )
            )
    return rows


def max_overlap_window(intervals: list[Interval]) -> tuple[date, date, int]:
    """Return inclusive [start, end] where simultaneous interval count is maximized."""
    if not intervals:
        d = date.today()
        return d, d, 0
    events: list[tuple[date, int]] = []
    for it in intervals:
        events.append((it.start, 1))
        events.append((it.end + timedelta(days=1), -1))
    events.sort(key=lambda x: (x[0], x[1]))
    cur = 0
    best = 0
    for _, delta in events:
        cur += delta
        if cur > best:
            best = cur
    if best == 0:
        d = intervals[0].start
        return d, d, 0
    cur = 0
    seg_start: date | None = None
    first_start: date | None = None
    first_end: date | None = None
    for day, delta in events:
        before = cur
        cur += delta
        if before < best <= cur:
            seg_start = day
        if before == best > cur and seg_start is not None:
            seg_end = day - timedelta(days=1)
            if first_start is None:
                first_start, first_end = seg_start, seg_end
            seg_start = None
    if first_start is None or first_end is None:
        d = intervals[0].start
        return d, d, best
    return first_start, first_end, best


def active_during(intervals: list[Interval], win_start: date, win_end: date) -> list[Interval]:
    out: list[Interval] = []
    for it in intervals:
        if it.end < win_start or it.start > win_end:
            continue
        out.append(it)
    return out


def render_report(path: Path) -> str:
    intervals = load_intervals(path)
    lines: list[str] = []
    lines.append("# Date-window overlap report")
    lines.append("")
    lines.append(f"- Intervals loaded: **{len(intervals)}**")
    w0, w1, k = max_overlap_window(intervals)
    lines.append(
        f"- Maximum simultaneous overlap: **{k}** on **{w0.isoformat()}** → **{w1.isoformat()}**"
    )
    lines.append("")
    active = active_during(intervals, w0, w1)
    by_cohort: dict[str, list[str]] = defaultdict(list)
    for it in active:
        by_cohort[it.cohort].append(it.oid)
    lines.append("## Observers intersecting peak window (by cohort)")
    lines.append("")
    for cohort, oids in sorted(by_cohort.items(), key=lambda x: (-len(x[1]), x[0])):
        uniq = sorted(set(oids))
        lines.append(f"- **{cohort}** ({len(uniq)}): {', '.join(uniq)}")
    lines.append("")
    lines.append("## Interpretation notes")
    lines.append("")
    lines.append(
        "- A peak window is where the count of *simultaneous* reports is highest "
        "(weak-signal correlation across observers)."
    )
    lines.append(
        "- If some cohorts cluster inside the window and others do not, treat that as a "
        "stratification hypothesis—not proof."
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    import sys as _sys

    args = argv if argv is not None else _sys.argv[1:]
    if len(args) != 1:
        print("usage: lovecraft-tools window-clusters <events.csv>", file=_sys.stderr)
        return 2
    path = Path(args[0])
    _sys.stdout.write(render_report(path))
    return 0
