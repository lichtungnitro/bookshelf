---
name: distributed-corroboration-window
description: Clusters sparse reports across many observers by overlapping date windows and cohort labels, surfacing peak overlap periods for weak-signal phenomena. Use when analyzing surveys, incident logs, symptom diaries, telemetry outages, or any domain where single witnesses are unreliable but temporal overlap may be informative.
---

# Distributed corroboration window

## What this encodes (from the manuscript)

Professor Angell does not rely on one dreamer: he collects **many independent nightly reports**, then notices a **shared window** (here, intensity spikes while a central case is acute). Separately, global clippings cluster around the same season. The methodological point is universal: **weak signals + time overlap + cohort stratification** can justify a closer look without pretending any single report is decisive.

## Workflow

1. **Define the phenomenon** you are counting (one sentence, operationalizable).
2. **Collect intervals**: for each observer, the date range their report covers (even a one-day window is valid).
3. **Label cohorts** when populations plausibly differ in sensitivity or exposure (in the story: artists vs. “practical” townspeople).
4. **Interpret the peak window** as a *hypothesis generator*: who falls inside it, who falls outside, and what alternative explanations exist (selection bias, publicity effects, shared cause).

## Executable tool

```bash
uv run lovecraft-tools window-clusters path/to/events.csv
```

CSV columns (header row required):

| column | meaning |
|--------|---------|
| `observer_id` | stable id |
| `window_start` | `YYYY-MM-DD` |
| `window_end` | `YYYY-MM-DD`, inclusive |
| `cohort` | optional; defaults to `unknown` |

## Example

See [examples/sample-events.csv](examples/sample-events.csv).

## Anti-patterns

- **Ecological fallacy**: a cohort pattern is not an explanation of mechanism.
- **P-hacking windows**: if you slice many ways, say so and widen uncertainty.
