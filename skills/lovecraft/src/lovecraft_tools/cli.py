"""`lovecraft-tools` entrypoint: evidence-matrix | window-clusters | report-outline."""

from __future__ import annotations

import sys

from lovecraft_tools import evidence, outline, windows


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in ("-h", "--help"):
        sys.stdout.write(
            "usage: lovecraft-tools <command> [args]\n\n"
            "commands:\n"
            "  evidence-matrix <claims.json>   timeline + index from dissociated claims\n"
            "  window-clusters <events.csv>    peak overlap window across observers\n"
            "  report-outline <outline.yaml>   nested evidence report skeleton\n"
        )
        return 0 if args else 2
    cmd = args.pop(0)
    if cmd == "evidence-matrix":
        return evidence.main(args)
    if cmd == "window-clusters":
        return windows.main(args)
    if cmd == "report-outline":
        return outline.main(args)
    sys.stderr.write(f"unknown command: {cmd}\n")
    return 2
