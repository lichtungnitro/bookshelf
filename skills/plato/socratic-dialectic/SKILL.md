---
name: socratic-dialectic
description: Apply the Socratic method of elenctic questioning to examine claims rigorously, expose contradictions, and arrive at more defensible positions. Use when evaluating a proposed solution, reviewing an argument, questioning requirements, or when a confident claim needs stress-testing. Trigger on phrases like "we should just...", "obviously...", "everyone knows...", or any assertion accepted without examination.
---

# Socratic Dialectic

> *"The unexamined life is not worth living."*  
> *"The good is something to be prized even more highly than knowledge and truth."*
> — Plato, Republic VI, 508e

## The Method

The Socratic elenchus is not debate — it is collaborative examination. Its goal is not to win but to discover what is true, or to expose that we do not yet know.

Four moves:

1. **State the claim**: Make the position explicit and precise.
2. **Ask for the principle**: What general rule does this claim rely on?
3. **Find the counterexample**: What case would make the principle false?
4. **Refine or abandon**: Revise the claim, or acknowledge ignorance as the honest position.

Repeat until either a defensible claim emerges, or the inquiry reveals the question needs to be reframed entirely.

## Applied to Engineering

### Examining a proposed solution

```
Claim: "We should use a message queue to decouple these services."

Step 1 — State it: Decoupling via async messaging is the right approach here.
Step 2 — Find the principle: Async messaging is preferable when... (when?)
Step 3 — Find the counterexample: What if the consumer must respond before the producer continues?
Step 4 — Refine: This use case requires synchronous acknowledgment. A queue decouples the wrong thing.
```

### Examining a requirement

```
Claim: "Users need real-time updates."

Step 1 — State it: The data must be current within the moment of display.
Step 2 — Find the principle: What harm occurs if data is 5 seconds stale? 60 seconds?
Step 3 — Find the counterexample: Are there cases where stale data is preferable (stability, cost)?
Step 4 — Refine: Users need updates within 30 seconds. Polling suffices. WebSockets are premature.
```

## The Philosopher's Discipline

> *"Those who hold this view are unable to show what knowledge it is. They are compelled, in the end, to say that it is knowledge of the good."*
> — Republic VI, 505b

The elenchus reveals two kinds of ignorance:
- **Simple ignorance**: you do not know, and you know you do not know. This is honest and recoverable.
- **Double ignorance**: you do not know, but believe you do. This is the only truly dangerous state.

The goal of dialectic is to convert double ignorance into simple ignorance. From there, genuine inquiry becomes possible.

## When to Stop

Dialectic is not infinite regress. Stop when:
- A claim survives all counterexamples you can construct (provisionally accept it)
- The question reveals itself as unanswerable with current information (acknowledge the gap)
- The cost of further inquiry exceeds the cost of being wrong (make a reversible decision)

The philosopher-engineer knows when to examine and when to act. Unending examination is its own form of cowardice.

## The Asymmetry of Burden

> *"It is not the same person being talked about all the time."*  
> — Republic IV, 430e

The burden of proof lies with the claim, not with the question. "We should add a cache" must justify itself. "Why?" is never the burden of the questioner.

Default to the simpler position until dialectic forces you toward complexity.
