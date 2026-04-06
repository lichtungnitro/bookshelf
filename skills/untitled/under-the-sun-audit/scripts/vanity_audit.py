#!/usr/bin/env python3
"""Interactive Ecclesiastes-style 'under the sun' audit; prints Markdown to stdout."""

from __future__ import annotations

import argparse
from datetime import date


QUESTIONS = [
    (
        "credit",
        "If public credit (title, metrics, visibility) were removed, would you still pay the same cost?",
    ),
    (
        "difficulty",
        "If the path doubled in difficulty, would it still be worth who you become?",
    ),
    (
        "legacy",
        "Twenty years after you're gone, does this leave anything beyond others' memory of you?",
    ),
]


def _prompt_answer(label: str) -> str:
    while True:
        raw = input(f"{label} [y/n/u]: ").strip().lower()
        if raw in ("y", "yes", "n", "no", "u", "unsure", ""):
            if raw in ("y", "yes"):
                return "yes"
            if raw in ("n", "no"):
                return "no"
            return "unsure"
        print("Please enter y, n, or u (unsure).")


def run_interactive(domain: str) -> dict[str, str]:
    print(f"\nUnder-the-sun audit: {domain}\n")
    out: dict[str, str] = {}
    for key, text in QUESTIONS:
        print(text)
        out[key] = _prompt_answer("Answer")
    print("\nWhat season is this? (free text, one line)")
    out["season"] = input("Season: ").strip()
    print(
        "\nOne gift you will receive as gift this week (food, rest, relationship, craft) — one line:"
    )
    out["gift"] = input("Gift: ").strip()
    print("\nDoes this pursuit train reverence+fidelity, or grasping? One line:")
    out["closure"] = input("Closure note: ").strip()
    return out


def run_batch(domain: str) -> dict[str, str]:
    return {
        "credit": "unsure",
        "difficulty": "unsure",
        "legacy": "unsure",
        "season": "(fill in)",
        "gift": "(fill in)",
        "closure": "(fill in)",
    }


def to_markdown(domain: str, answers: dict[str, str]) -> str:
    today = date.today().isoformat()
    lines = [
        f"# Under-the-sun audit: {domain}",
        "",
        f"**Date:** {today}",
        "",
        "## Vapor test",
        "",
        f"- **Credit stripped:** {answers['credit']}",
        f"- **Doubled difficulty:** {answers['difficulty']}",
        f"- **Beyond memory:** {answers['legacy']}",
        "",
        "## Season",
        "",
        answers.get("season", "") or "—",
        "",
        "## Gift (received, not grasped)",
        "",
        answers.get("gift", "") or "—",
        "",
        "## Reverence / fidelity vs grasping",
        "",
        answers.get("closure", "") or "—",
        "",
        "## Interpreter notes (for the agent or reader)",
        "",
        "- `no` on credit → reputation may be doing too much work.",
        "- `no` on difficulty → motivation may be conditional on ease.",
        "- `no` on legacy → treat as seasonal; avoid ultimate weight.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser(
        description="Run an under-the-sun audit; prints Markdown to stdout."
    )
    p.add_argument("--domain", required=True, help="Topic being examined (e.g. career move)")
    p.add_argument(
        "--batch",
        action="store_true",
        help="Non-interactive: emit template with unsure/placeholder answers",
    )
    args = p.parse_args()
    domain = args.domain.strip()
    answers = run_batch(domain) if args.batch else run_interactive(domain)
    print("\n---\n")
    print(to_markdown(domain, answers))


if __name__ == "__main__":
    main()
