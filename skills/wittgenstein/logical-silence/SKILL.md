---
name: logical-silence
description: Detect when a question or problem is senseless — not false, but without determinate meaning. Based on Wittgenstein's Tractatus proposition 7: "Whereof one cannot speak, thereof one must be silent." Use when facing circular debates, unanswerable questions, vague requirements with no resolution path, or any time reasoning loops without progress. The method: test whether the question has truth conditions. If not, dissolve it rather than answer it.
---

# Logical Silence

> *"For an answer which cannot be expressed the question too cannot be expressed. The riddle does not exist. If a question can be put at all, then it can also be answered."*
> — Tractatus 6.5

> *"Most questions and propositions of the philosophers result from the fact that we do not understand the logic of our language."*
> — Tractatus 4.003

## The Core Distinction

A genuine question has determinate truth conditions — there is some state of the world that would settle it. A pseudo-question appears grammatically valid but refers to nothing that can be true or false.

| Type | Example | Response |
|------|---------|----------|
| **Genuine question** | "Does this function return nil on empty input?" | Answer it |
| **Vague question** | "Is this code good?" | Dissolve: good *for what*? under what *conditions*? |
| **Category error** | "What is the meaning of this system?" | Dissolve: systems have functions, not meanings |
| **Infinite regress** | "But why is *that* the requirement?" | Stop: requirements are primitive — they ground further questions |

## The Silence Test

Before attempting to answer, run this test:

1. **State the truth conditions**: Under what specific, observable conditions would the answer be "yes"? Under what conditions "no"?
2. **Check for grounding**: Does the question presuppose facts that can be independently verified, or does it float free?
3. **Test the negation**: Can you meaningfully state what it would mean for the answer to be *wrong*?

If step 1 fails — the question dissolves. It was never a question; it was a confusion in language.

## When to Apply

- A debate has run more than two rounds without progress → test for pseudo-question
- A requirement cannot be turned into an acceptance test → it lacks truth conditions
- A bug report says "it feels wrong" or "it's not right" → demand specificity
- Someone asks "what should this really do?" in a circle → the question may be malformed
- An architectural debate reduces to taste, not trade-offs → silence the aesthetic, surface the facts

## The Protocol

```
1. Identify the question being asked.
2. Ask: what would make this true? What would make it false?
3. If no answer → restate: "We are not asking whether X is true, but rather what X means."
4. Reconstruct the question with explicit truth conditions, or declare it dissolved.
5. Proceed only with reconstructed, grounded questions.
```

## What Silence Is Not

Silence does not mean giving up. It means recognizing that the work is **conceptual clarification**, not reasoning toward an answer. Once the question is clarified, the answer often becomes obvious — or the question vanishes entirely (6.521: "The solution of the problem of life is seen in the vanishing of this problem").

## Anti-patterns

- **Answering nonsense**: Providing a confident answer to a question with no truth conditions (hallucinating certainty)
- **Escalating vagueness**: Adding qualifications to a pseudo-question instead of dissolving it
- **Treating silence as failure**: Saying "I don't know" when the correct response is "that question cannot be asked"
- **Debating the unsayable**: Ethics, aesthetics, and values cannot be argued into truth — they can only be shown through action (6.421: "Ethics cannot be expressed")
