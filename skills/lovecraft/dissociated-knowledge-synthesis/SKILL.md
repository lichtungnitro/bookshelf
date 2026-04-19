---
name: dissociated-knowledge-synthesis
description: Correlates separated sources—artifacts, notes, clippings, testimony—into timelines, tag convergence, and same-day multi-source tension checks. Use when investigating multi-document problems, incident reconstruction, research synthesis, or any task where truth may emerge only from piecing dissociated knowledge.
---

# Dissociated knowledge synthesis

## What this encodes (from the manuscript)

In *The Call of Cthulhu*, the breakthrough is not a single proof: it is **accidental correlation** across unrelated media (e.g. a late professor’s notes and a stray newspaper item). The narrator explicitly warns that **piecing dissociated knowledge** can be dangerous—not because synthesis is always wrong, but because convergence can be real.

Your job is to make that synthesis **legible and reviewable**: provenance first, timeline second, convergence third, contradictions last.

## Workflow

1. **Inventory sources** (medium + custody chain): who held it, how it arrived, whether it is primary or derivative.
2. **Normalize claims** as small, falsifiable statements; give each an `id`. Tag recurring entities (`cult`, `figure`, `phrase`, `locale`, etc.).
3. **Date what you can**; keep undated claims separate rather than forcing a guess.
4. **Link related claims** with `relates_to` when one exhibit supports, narrows, or conflicts with another.
5. **Read the machine output as a map, not a verdict**: high tag overlap means “investigate here,” not “confirmed.”

## Executable tool

From `skills/lovecraft/` (uses the repo’s `uv` project):

```bash
uv run lovecraft-tools evidence-matrix path/to/claims.json
```

JSON shape:

```json
{
  "title": "Optional title",
  "claims": [
    {
      "id": "c1",
      "source": "professor_notes",
      "date": "1925-03-01",
      "text": "Short claim text.",
      "tags": ["cthulhu", "bas_relief"],
      "relates_to": ["c2"]
    }
  ]
}
```

- `date` is `YYYY-MM-DD` or omit for undated.
- `tags` power convergence sections; `relates_to` lists other claim ids.

## Example

See [examples/sample-claims.json](examples/sample-claims.json).

## Anti-patterns

- **Narrative glue without sources**: if a link is inference, label it inference in prose—do not tag it as if it were observed.
- **Leading questions**: wide surveys can manufacture patterns; note when your collection method could prime respondents (the manuscript’s narrator worries about exactly this).
