---
name: truth-conditions
description: Force precision by eliciting the exact truth conditions of any claim, requirement, or assertion. Based on Wittgenstein's Tractatus 4.431: "The proposition is the expression of its truth-conditions." Use when requirements are vague, success criteria are absent, bug reports are ambiguous, or any time a statement is in play without clarity on when it would be true or false. Meaning is not what you intend — it is what conditions in the world would verify or falsify the claim.
---

# Truth Conditions

> *"The proposition is the expression of its truth-conditions."*
> — Tractatus 4.431

> *"In order to discover whether the picture is true or false we must compare it with reality. It cannot be discovered from the picture alone whether it is true or false."*
> — Tractatus 2.223–2.224

> *"What the picture represents is its sense. In the agreement or disagreement of its sense with reality, its truth or falsity consists."*
> — Tractatus 2.221–2.222

## The Core Principle

You do not understand a proposition until you know **what state of the world would make it true**, and **what state would make it false**. The meaning of a statement is not its psychological content — it is its position in logical space: the range of facts it includes and excludes.

A statement that is true no matter what is a tautology — it says nothing. A statement that is false no matter what is a contradiction — it also says nothing. A meaningful proposition carves reality at a joint.

## The Elicitation Protocol

For any claim that will drive a decision, demand its truth conditions explicitly:

```
1. Restate the claim as a declarative sentence.
2. Ask: "Under what specific, observable conditions is this true?"
3. Ask: "Under what specific, observable conditions is this false?"
4. If steps 2 and 3 produce the same answer, or no answer → dissolve (see logical-silence)
5. If the conditions are clear → record them. These are the acceptance criteria.
```

## Application Map

| Context | Vague form | Truth-conditions form |
|---------|-----------|----------------------|
| Requirement | "The system should be fast" | "P95 latency < 200ms under 1000 concurrent users" |
| Bug report | "It doesn't work" | "Calling X with input Y returns Z; expected W" |
| Design claim | "This architecture is better" | "Under load pattern L, this reduces error rate by R%" |
| Code review | "This is hard to read" | "A new engineer cannot trace the control flow from entry to exit within 5 minutes" |
| Success criterion | "Users will be happy" | "30-day retention ≥ 40% in cohort A" |

## The Excluded Middle

Every genuine proposition admits of a truth value. This has two consequences:

**1. Vague predicates must be sharpened.** "Fast", "clean", "simple", "good" — none of these are propositions until the conditions that would make them true or false are given. Ask: for the purposes of this decision, what counts as "fast enough"?

**2. Truth conditions determine scope.** When you know what would make something true, you automatically know what you do not need to verify. This is the source of testability: a proposition whose truth conditions can be checked is a testable proposition.

## Showing vs. Saying

Wittgenstein distinguishes what can be *said* from what can only be *shown* (2.172, 4.1212). Truth conditions apply to what is *said*. Some things — code quality, elegance, the feeling that a design is right — can only be shown, not stated as propositions. This is not a failure; it is the nature of those things.

Recognize this: when something can only be shown, stop demanding it be said. Demonstrate it instead. Write the code that shows what good code looks like; do not argue about what "good" means.

## Anti-patterns

- **Intention substitution**: Replacing truth conditions with intent ("we want users to feel confident") — intentions are not truth conditions
- **Metric theater**: Picking a measurable proxy without verifying it tracks the actual truth condition ("engagement" as proxy for "value")
- **Retroactive conditions**: Defining truth conditions *after* seeing the result, to make the outcome look like success
- **Condition inflation**: Adding so many conditions that nothing can fail — tautology dressed as rigor
- **Underdetermination**: Stating conditions so loosely that many different, incompatible outcomes all satisfy them
