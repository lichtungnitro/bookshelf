---
name: xenia-reciprocity
description: Structures mutual obligation in collaboration—what hosts owe guests and guests owe hosts—so trust is earned through exchange rather than assumed. Use when onboarding, partnerships, customer success, open-source communities, or cross-team dependencies where goodwill is fraying. Trigger on "they never give back," freeloading, ambiguous ownership, or hospitality abused (expectations without reciprocity).
---

# Xenia Reciprocity

> *Xenia* is **guest-friendship**: the stranger arrives with need; the host offers shelter and honor; the guest does not consume the house. When the suitors violate *xenia*, the poem treats it as **civilizational breakdown**, not bad manners. In modern work, the same structure appears whenever **time, access, and reputation** flow one way until resentment becomes policy.

## When to use

- Partnerships without clear give/get
- Open-source or internal platforms where "users" never contribute back
- Teams that host others (support, infra) and burn out
- You need explicit norms before conflict hardens

## Executable workflow

### 1. Name the table

Who is **host** (offers space, credentials, time, cover) and who is **guest** (receives)? Roles can alternate by phase; name the phase.

### 2. Minimum host obligations

List what the host **owes** in this context (orientation, SLAs, safety, clarity). Not everything—**minimum** credible hospitality.

### 3. Minimum guest obligations

List what the guest **owes** (signal, restraint, thanks-as-action, feedback). Guests who treat the house as loot invite expulsion.

### 4. Abuse tests

| Violation | Odyssey echo | Here it looks like |
|-----------|--------------|---------------------|
| Eat without limit | Suitors | |
| Mock the host | Suitors | |
| Ignore the gift economy | | |

### 5. Repair or exit

If reciprocity cannot be restored, **name exit** (reduce access, end partnership, fork) before contempt poisons everyone.

## Tone

Firm and hospitable: high standards for both sides, no sentimentality about exploiters.

## Script

Emit a xenia audit table (Markdown):

```bash
python skills/homer/xenia-reciprocity/scripts/xenia_audit.py --table "Partnership or system name"
```

For episode anchors and PDF limits, see [reference.md](reference.md).
