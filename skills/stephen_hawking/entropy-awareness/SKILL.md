---
name: entropy-awareness
description: Recognize that all systems drift toward disorder by default. Entropy always increases in closed systems. Use when reviewing code for complexity creep, assessing technical debt, designing for longevity, or understanding why systems degrade over time without active effort.
---

# Entropy Awareness

*Inspired by Hawking's Chapter 9: "The Arrow of Time" — disorder increases because there are vastly more disordered states than ordered ones.*

## The Law, Applied

Entropy is not a metaphor. In software, as in physics:

- **Complexity accumulates** because there are more complex states than simple ones
- **Order requires energy** — every refactor, every cleanup, every simplification costs effort
- **Decay is passive; order is active**

If a system is not being actively maintained, it is degrading. This is not failure — it is physics.

## What Entropy Looks Like in Code

- Functions that do more than they did last year
- Dependencies that have grown without pruning
- Documentation that hasn't kept pace with behavior  
- Naming that no longer reflects meaning
- Tests that test the old design, not the current one
- Configuration spread across multiple locations

Each of these is entropy. Not bad engineering — inevitable drift.

## Designing Against Entropy

1. **Small surfaces** — Less surface area means less entropy accumulation. Prefer small, focused functions, modules, and APIs.
2. **Reversibility** — Design decisions that can be undone accumulate less irreversible complexity.
3. **The second law budget** — Every system has a budget for how much disorder it can absorb before becoming unmaintainable. Spend it deliberately.
4. **Periodic negentropy** — Deliberate reduction of disorder: refactoring, deleting dead code, consolidating, renaming.

## The Irreversibility Principle

Some entropy is irreversible. In physics: you cannot unscramble an egg. In software:

- A public API, once released, is nearly irreversible
- A database schema change that loses data is irreversible
- A leaked secret is irreversible

Treat irreversible decisions with disproportionate care. All other decisions: make them, observe, adjust.

## When Reviewing or Designing

Ask: *In one year, without any maintenance, what does this become?*

If the answer is "a mess" — the design is not fighting entropy. Add structure that resists degradation, not just structure that works today.
