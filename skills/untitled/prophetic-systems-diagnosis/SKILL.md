---
name: prophetic-systems-diagnosis
description: Diagnoses systems (orgs, products, societies) using the prophetic biblical pattern—surface symptom, root commitment, who is crushed, ignored warnings, and concrete return. Use for post-incidents, ethics reviews, "why does this keep happening," technical debt that is really moral debt, or strategy when incentives misalign with stated values. Trigger on repeated failure, scapegoating, or noble mission with ugly outcomes.
---

# Prophetic Systems Diagnosis

The prophetic books (e.g., Isaiah, Jeremiah, Ezekiel, Amos) share a **recurrent anatomy**: Israel's God confronts not merely bad luck but **misordered love** — what you ultimately trust, sacrifice for, and cannot question. That structure transfers to any system: **idols** are not only statues; they are **unquestionable goods** that reorganize everything else.

> *"They have forsaken me, the fountain of living waters, and hewed out cisterns for themselves, broken cisterns that can hold no water."* — Jeremiah 2:13 (ESV)

## When to use

- Recurring incidents with different "human error" labels
- Metrics improve while trust erodes
- Leadership narrative and frontline reality diverge
- You need blameless root cause that still names structure

## Executable workflow

### 1. Name the surface symptom

What broke? One paragraph, observable.

### 2. Identify the liturgy

**Liturgy** = what the system **repeatedly does** together, not what it posts on the wall.

Ask:

- What do we **always** fund first?
- What meeting **never** gets canceled?
- What failure mode gets **automated forgiveness**?

### 3. Name the functional idol

Complete: *"This system cannot afford to disappoint **[X]**."*

`X` might be: growth %, a VIP customer, the quarterly narrative, "being right," zero downtime at any human cost.

The idol is **what must not be questioned**.

### 4. Trace harm (Amos-style)

List **who is thin** in the system:

- Who loses sleep?
- Whose warnings were filed as "culture issues"?
- Which group's pain is priced as acceptable?

If you cannot name a harmed party, you have not looked.

### 5. Warnings ignored (Jeremiah pattern)

List **two** earlier signals that were rationalized away. Prophetic literature treats ignored warnings as **data**, not drama.

### 6. Concrete return (not vague repentance)

"Do better" is not return. Specify:

| From | To |
|------|-----|
| Incentive A | Incentive B |
| Metric M | Metric M' + guardrail G |
| Role R's power | Role R's accountability |

**Return** must be **testable within a month**. If it is not testable, it is mood.

### 7. Shalom probe (optional theistic reading)

If the user accepts the frame: **shalom** is not calm wallpaper; it is **rightness of relationship**. Ask: what relationship (user, employee, neighbor, creation) is being traded away for the idol?

## Tone

The prophets are not comfortable but they are not cruel. They name the idol the system cannot question — and they name it directly, using concrete evidence rather than abstraction. When applying this framework, use clinical precision rather than accusatory language: the goal is structural clarity, not blame. The prophetic literature treats ignored warnings as data, not drama. Treat them the same way. The diagnosis is an act of care for the system, not an attack on the people in it.

## Script

Emit a Markdown diagnostic template:

```bash
python scripts/root_pattern_template.py --system "name of system or incident"
```

See [reference.md](reference.md) for examples and boundaries.
