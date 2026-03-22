---
name: model-thinking
description: Reason about systems as provisional models, not as reality itself. A model is valid if it is elegant and makes correct predictions — not because it "is" true. When a model breaks at the edges, replace it. Use when approaching unfamiliar codebases, debugging, architecture decisions, or any situation where assumptions need to be tested.
---

# Model Thinking

*Inspired by Hawking's opening argument: "any physical theory is always provisional, in the sense that it is only a hypothesis: you can never prove it, right, only disprove it."*

## The Core Discipline

Before reasoning about a system, explicitly state your current model:

1. **Name the model** — What do you currently believe about this system?
2. **Derive predictions** — What should be true if your model is correct?
3. **Test the edges** — Where would the model break down? Check those places first.
4. **Update or replace** — When evidence contradicts the model, revise it. Don't defend it.

## Applied to Software

| Situation | Model-Thinking Approach |
|-----------|------------------------|
| Debugging | State your hypothesis explicitly before looking. Test the prediction, not your belief. |
| Architecture | Name the assumptions your design depends on. What breaks when they're wrong? |
| Unfamiliar code | Build a working model before changing anything. Verify by predicting behavior. |
| Code review | Ask: what model of the problem does this code encode? Is it correct? |

## The Turtle Warning

> *"What is the tortoise standing on?" — "It's turtles all the way down."*

When you trace a causal chain, recognize when you've hit the foundation of your model. Don't keep digging — that's where models stop and axioms begin. Know the difference between **explaining** and **naming**.

## Signs Your Model Needs Updating

- Predictions are consistently wrong
- You keep adding patches and exceptions
- The model requires more assumptions than it explains
- Two observations contradict each other at the edge

## What a Good Model Does

A good model is:
- **Predictive** — it says something testable about the world
- **Minimal** — it explains the observations without unnecessary complexity  
- **Bounded** — it knows its own limits; it doesn't pretend to explain everything

A model that explains everything explains nothing.
