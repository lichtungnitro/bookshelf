---
name: justice-ordering
description: Apply Plato's concept of justice as right ordering — each part doing its proper work — to evaluate systems, codebases, and architectures. Use when reviewing code structure, system design, team responsibilities, or any arrangement where components may be overstepping or failing their function. Trigger on questions of "who should own this?", "why is this coupled?", or "why does this feel wrong structurally?".
---

# Justice as Right Ordering

> *"He has, quite literally, to put his own house in order — forbidding each of the elements within him to perform tasks other than its own, and not allowing the classes of thing within his soul to interfere with one another."*
> — Plato, Republic IV, 443d

## The Principle

Plato defines justice not as fairness in the external sense, but as **each part fulfilling its proper function** — no more, no less. Injustice is disorder: appetite overruling reason, or reason abdicating and leaving a vacuum.

This maps directly to systems:

| Soul | City | Codebase |
|------|------|----------|
| **Reason** (logos) | Philosopher-rulers | Architecture, domain model, core abstractions |
| **Spirit** (thymos) | Guardians/warriors | Services, enforcement layers, validation |
| **Appetite** (epithymia) | Craftsmen/producers | I/O, persistence, external integrations |

**Justice**: each layer does its work, governed by the layer above.  
**Injustice**: appetite (database concerns) bleeds into reason (business logic); spirit (validation) is absent; reason (architecture) is enslaved to appetite (performance hacks).

## Diagnosing Disorder

Ask three questions about any component:

1. **What is its proper function?** State it in one sentence.
2. **Is it doing only that?** Name anything it does that belongs elsewhere.
3. **Is it governed correctly?** Does higher-order logic control it, or does it control the higher-order logic?

Common injustices:

- **Appetite rules reason**: business logic encoded in SQL queries or HTTP handlers
- **Spirit is absent**: no validation layer; every component trusts every other
- **Reason is tyrannized**: architecture contorted to serve a framework's preferences
- **Classes interfere**: a UI component that mutates shared state it doesn't own

## The Ordering Prescription

To restore justice:

1. Name the three levels in your system (what corresponds to reason, spirit, appetite).
2. Audit one component at a time: does it stay within its function?
3. Move misplaced concerns to their proper home — not by rewriting, but by rehousing.
4. Make the dependency direction flow downward only: reason → spirit → appetite, never upward.

## The Individual Mirror

> *"The just man will be no different from a just city."*
> — Republic IV, 435b

The same principle holds for a person writing code: reason (what needs to be true) must govern spirit (the urge to ship) and appetite (desire for clever solutions). Unjust code is written by appetite — it solves the problem you found pleasure in solving, not the problem that needed solving.

Before writing: let reason state the requirement. Let spirit assess feasibility. Let appetite implement only what reason and spirit have sanctioned.
