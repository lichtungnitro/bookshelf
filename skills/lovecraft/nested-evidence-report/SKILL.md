---
name: nested-evidence-report
description: Structures layered investigations—frame narrator, primary exhibits, secondary accounts, synthesis limits, and disclosure/custody—when conclusions are sensitive or easy to misread. Use for postmortems, journalism, legal memos, security incident reports, or any chain-of-custody narrative.
---

# Nested evidence report

## What this encodes (from the manuscript)

The story is explicitly **documents inside documents**: a late narrator, papers of the dead, police narrative, anthropological meeting minutes, newsprint, and finally a sailor’s manuscript. The closing lines are not melodrama—they are **epistemic ethics**: the author hopes an executor will prefer **caution over audacity** in circulation.

This skill is that architecture stripped of fiction: **who speaks, what is exhibit-grade, what is hearsay, what synthesis is justified, who bears risk if it leaks**.

## Workflow

1. **Frame**: name the responsible narrator (role, conflicts, what they do not know).
2. **Primary exhibits**: artifacts or records that a reader could verify independently.
3. **Secondary accounts**: interviews, press, testimony—treat as evidence about belief and behavior, not automatic truth.
4. **Synthesis**: what links are forced, what would falsify the chain, what coincidence remains unexplained.
5. **Disclosure**: audiences harmed by partial truths; custody; redaction policy; what not to circulate without safeguards.

## Executable tool

```bash
uv run lovecraft-tools report-outline path/to/outline.yaml
```

YAML shape (minimal):

```yaml
title: Investigation title
frame_narrator:
  prompt: Who is writing, under what duty of care?
primary_documents:
  - name: Exhibit A
    note: Custody and why it matters
secondary_accounts:
  - "Interview …"
  - "Press clipping …"
synthesis_and_limits:
  prompt: What is proven vs inferred; falsifiers.
disclosure_and_risk:
  prompt: Who could be harmed; circulation rules.
```

## Example

See [examples/sample-outline.yaml](examples/sample-outline.yaml).

## Anti-patterns

- **Mystery box reporting**: if you withhold conclusions to sound important, say you are withholding and why.
- **Merging voices**: keep each source’s boundaries visible—nested structure is a feature, not clutter.
