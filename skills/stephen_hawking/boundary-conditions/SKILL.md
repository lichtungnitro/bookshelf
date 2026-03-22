---
name: boundary-conditions
description: The most important things happen at the edges where normal rules break down. Inspired by Hawking's study of singularities, black holes, and the Big Bang — places where existing physics failed and new understanding was required. Use when debugging edge cases, designing APIs, auditing security, reviewing error handling, or any situation where the limits of a system matter.
---

# Boundary Conditions

*Inspired by Hawking's lifelong focus on singularities — points where the known equations break down and new physics must emerge.*

> "The laws of science, as we know them at present, contain many fundamental numbers... We cannot deduce the values of these numbers from first principles."

The boundaries are not inconvenient edge cases. They are where the real nature of a system is revealed.

## The Fundamental Insight

Hawking's greatest contributions came not from studying the middle of things, but from studying their edges:

- **Black holes** — where gravity becomes infinite, the known laws fail
- **The Big Bang** — where time itself has a boundary
- **Hawking radiation** — what happens *at the boundary* between quantum and gravitational physics

In every system, the most revealing information is at the boundary.

## What Boundaries Reveal

| Boundary Type | What It Reveals |
|---------------|----------------|
| Empty input | Whether defaults are safe or undefined |
| Maximum capacity | Whether the system degrades gracefully or catastrophically |
| Network failure | Whether the system has a coherent failure model |
| Concurrent access | Whether state assumptions hold under race conditions |
| Unauthenticated access | Whether authorization is enforced structurally or by convention |
| Zero / null / negative | Whether arithmetic and logic assumptions are explicit |

## The Practice

When reasoning about any system, API, or piece of code:

1. **Find the edges** — What inputs, states, or conditions are at the limits of normal operation?
2. **Test the model there** — Does your understanding of the system still hold at the boundary?
3. **Look for the singularity** — Where does the system's behavior become undefined, undefined, or catastrophic?
4. **Design the boundary explicitly** — A boundary that is not designed is not absent — it is simply uncontrolled.

## The Black Hole Principle

A system with an event horizon is dangerous: once you cross it, you cannot send information back. In software:

- A function that can corrupt shared state without returning an error has an event horizon
- A distributed transaction that can partially commit has an event horizon
- An irreversible deployment without a rollback path has an event horizon

**Identify your system's event horizons. Map them before they map you.**

## Singularities Are Information

When a system breaks at a boundary, that is not a failure to be patched — it is information about the system's true structure. The patch that suppresses the symptom without understanding the boundary is the most dangerous kind.

Ask: *Why does this break here? What does the system believe at this point that is no longer true?*
