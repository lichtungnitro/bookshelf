# Untitled — skills distilled from the Bible (ESV)

Three agent skills live in subfolders. Each has a `SKILL.md` and optional `scripts/`.

## Skills

| Skill | Source emphasis |
|-------|-----------------|
| [many-counselors-deliberation](many-counselors-deliberation/SKILL.md) | Proverbs: plurality of advisers, order of testimony, faithful correction |
| [under-the-sun-audit](under-the-sun-audit/SKILL.md) | Ecclesiastes: vanity vs durable good, bounded optimization |
| [prophetic-systems-diagnosis](prophetic-systems-diagnosis/SKILL.md) | Prophetic literature: idol → incentive → harm → return |

## Python helpers

Optional dev tooling (lint) from this directory:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
```

Run scripts (examples; use `python3` on macOS if needed):

```bash
python many-counselors-deliberation/scripts/deliberation_sheet.py --title "Release go/no-go"
python under-the-sun-audit/scripts/vanity_audit.py --domain "career pivot"
python prophetic-systems-diagnosis/scripts/root_pattern_template.py --system "payments pipeline"
```

No third-party runtime dependencies are required for the scripts.
