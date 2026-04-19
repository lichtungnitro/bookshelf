---
name: disguise-and-proof
description: Defers public identity until tests have run—gathering ground truth, sorting allies from performers, and revealing authority only when proof is cheap and irreversible harm is unlikely. Use when rolling out sensitive changes, joining hostile or politicized contexts, incident response, M&A integrations, or when the user says "trust but verify," "phased rollout," or "they need to show me first." Trigger on security incidents, leadership transitions, and high-stakes negotiations.
---

# Disguise and Proof

> In Ithaca, Odysseus returns **not as king** but as what will be overlooked: a beggar can listen; a king cannot. Proof is staged—the bow, the tree, the scar—so that **truth is demonstrated**, not announced. This skill is not deception for sport; it is **latency of recognition** until evidence has done its work.

## When to use

- Announcing role or intent too early would distort behavior (Hawthorne effect at civilization scale)
- You must distinguish loyalty from convenience before committing resources
- Reveal order matters: some truths destroy cover before tests complete

## Executable workflow

### 1. Name what must stay latent

One sentence: **what identity or capability stays veiled**, and until when (event or condition).

### 2. Map observers

Who must **not** know yet, who can **help** without full knowledge, who must be **tested** without knowing they are in a trial?

### 3. Design proofs (cheap → costly)

| Stage | Proof | What failure means |
|-------|-------|---------------------|
| 1 | | |
| 2 | | |
| 3 | | |

Proofs should be **falsifiable**: a bad ally should fail a fair test.

### 4. Reveal rule

Write the single rule: **We reveal X only after Y is true.** If you cannot state Y, you are hoarding secrecy, not running a proof.

### 5. Harm check

Disguise that protects the vulnerable is one thing; disguise that **steals consent** is another. Name who bears risk while truth is delayed.

## Tone

Patient, unsentimental, allergic to dramatic "gotchas." The epic’s patience is ethical when it prevents slaughter; when it becomes cruelty, the poem punishes it.

## Script

Emit a phased proof worksheet (Markdown):

```bash
python skills/homer/disguise-and-proof/scripts/phase_reveal.py --context "Short label for this situation"
```

For episode anchors and PDF limits, see [reference.md](reference.md).
