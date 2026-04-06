---
name: many-counselors-deliberation
description: Structures important decisions using the Proverbs pattern of many advisers, ordered testimony, and faithful correction rather than flattery. Use when the user faces a high-stakes fork (hire/fire, architecture, strategy, personal life), wants a second opinion workflow, or asks for wisdom-style deliberation. Trigger on release planning, "should we", committee decisions, or reducing blind spots.
---

# Many Counselors Deliberation

> *"Where there is no guidance, a people falls, but in an abundance of counselors there is safety."* — Proverbs 11:14 (ESV)  
> *"Without counsel plans fail, but with many advisers they succeed."* — Proverbs 15:22  
> *"The first to plead his case seems right, until another comes and examines him."* — Proverbs 18:17  
> *"Faithful are the wounds of a friend; profuse are the kisses of an enemy."* — Proverbs 27:6

This is not voting-by-committee. It is **structured epistemic humility**: plans fail when guidance is thin; the opening story is never the whole story; the voice that stings may be the one that saves.

## When to use

- Irreversible or expensive decisions
- Strong disagreement among stakeholders
- You feel rushed, clever, or uniquely enlightened
- Post-incident: why did the plan look good before it failed?

## Executable workflow

### 1. Frame the decision (one sentence)

Write **one** crisp decision question. If you cannot, you are not ready to deliberate.

### 2. Enroll diverse counselors (minimum three roles)

Not three people who agree with you. Three **roles** that see different failure modes:

| Role | Sees |
|------|------|
| Operator | Execution load, on-call, edge cases |
| Skeptic | Incentives, gaming, abuse, second-order effects |
| Stakeholder / user | Value delivered, trust, accessibility |

If a role is missing, the deliberation is incomplete.

### 3. First speech / second speech (Prov 18:17)

- **Round A**: Each counselor states the strongest case **for** the leading option *without* rebuttal yet.
- **Round B**: Each counselor states the strongest case **against** that option, referencing concrete scenarios.

Do not "synthesize" before Round B finishes.

### 4. Wound check (Prov 27:6)

Ask explicitly:

- Who loses if we are wrong?
- Which uncomfortable fact are we not placing on the table?
- What would a **faithful enemy** say we are pretending not to know?

If no one can name a wound, you have filtered for flattery.

### 5. Decide with a written dissent

Record:

1. **Decision**
2. **Counsel summary** (one line per role)
3. **Named risk** we are accepting
4. **Dissent** (best argument *against* the chosen path, preserved verbatim)

The dissent is not disloyalty; it is insurance against future self-deception.

## Tone

Proverbs is aphoristic and direct — it does not argue, it strikes. When guiding deliberation, be orderly and unhurried: do not compress Round B before it finishes, and do not synthesize before the wound has been named. Preserve the second speech as if it has equal standing with the first, because it does (Prov 18:17). Name uncomfortable facts plainly rather than softening them. The Proverbs teacher aims at wisdom, not comfort.

## Quick micro-patterns (Proverbs cluster)

- **Slow to anger** in debate: heat correlates with hidden stakes (Prov 14:29).
- **Plans** belong to man; **steps** belong to factors you do not control — build reversibility where you cannot know (Prov 16:9 — apply as humility about forecasts, not fatalism).
- **Boasting about tomorrow** is a red flag (Prov 27:1): prefer dated assumptions and kill criteria.

## Script

Generate a blank deliberation sheet (Markdown):

```bash
python scripts/deliberation_sheet.py --title "Your decision"
```

See [reference.md](reference.md) for verse pointers and anti-patterns.
