---
name: cave-epistemics
description: Apply Plato's Allegory of the Cave to distinguish surface appearances from underlying reality. Use when analyzing problems to separate symptoms from root causes, proxies from truth, assumptions from verified knowledge. Trigger when facing confusing bugs, misleading metrics, or shallow diagnoses — any time the first visible explanation might be a shadow on the wall.
---

# Cave Epistemics

> *"What people in this situation would take for truth would be nothing more than the shadows of the manufactured objects."*
> — Plato, Republic VII, 515c

## The Core Distinction

Plato's cave maps onto four epistemic levels (the Divided Line, Book VI):

| Level | In the Cave | In Practice |
|-------|-------------|-------------|
| **Conjecture** | Shadows on the wall | Error messages, surface logs, user complaints |
| **Belief** | The objects casting shadows | Stack traces, symptoms, visible failures |
| **Thinking** | The world outside the cave | Patterns, root causes, system invariants |
| **Understanding** | The sun itself | The fundamental principle or design flaw |

Most diagnosis stops at level 1 or 2. The philosopher's task is to ascend.

## When to Apply

Apply this lens when:
- A problem is "fixed" but keeps returning (you treated the shadow, not the cause)
- Metrics look good but something feels wrong (the metric is a proxy, not the thing itself)
- A bug is hard to reproduce (you are seeing a shadow; find what casts it)
- Requirements seem unclear (surface desires obscure the actual need)

## The Ascent Protocol

1. **Name the shadow**: What is the immediate visible symptom? State it precisely.
2. **Find the object**: What concrete mechanism produces this symptom? Trace backwards.
3. **Step outside**: What systemic condition makes this mechanism possible?
4. **Name the sun**: What is the root principle — the single truth from which everything else follows?

Only act on the sun-level understanding. Patching shadows wastes effort and breeds recurrence.

## The Return

> *"He would remember that the soul can be impaired in two quite different ways — there's the change from light to darkness, and the change from darkness to light."*
> — Republic VII, 518a

Once you understand the root, communicating it requires patience. Others still see shadows. Do not mock their confusion — help them ascend.

When explaining a root-cause finding: present the shadow first (what they already see), then walk the chain upward to the cause. Do not begin with the abstract truth.

## Anti-patterns

- **Shadow-fixing**: Catching and suppressing the error without eliminating its source
- **Metric worship**: Optimizing the proxy instead of the thing it represents
- **Blame assignment**: Naming a person as the cause (persons are shadows; systems cast them)
