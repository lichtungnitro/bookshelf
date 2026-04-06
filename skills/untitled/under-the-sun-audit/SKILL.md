---
name: under-the-sun-audit
description: Applies Qoheleth's (Ecclesiastes) frame to distinguish vapor-like pursuits from durable goods under human limits. Use when the user chases infinite optimization, confuses status with meaning, needs scope for a life or project decision, or asks whether an effort is "worth it." Trigger on burnout, career FOMO, vanity metrics, or "what actually matters."
---

# Under the Sun Audit

> *"Vanity of vanities! All is vanity."* — Ecclesiastes 1:2 (ESV)  
> *"What does man gain by all the toil at which he toils under the sun?"* — Ecclesiastes 1:3  
> *"For everything there is a season, and a time for every matter under heaven."* — Ecclesiastes 3:1  
> *"The end of the matter; all has been heard. Fear God and keep his commandments, for this is the whole duty of man."* — Ecclesiastes 12:13

**"Under the sun"** means: the horizon of human effort **without** pretending you control outcomes, duration, or reputation. The Teacher is not nihilism; he is **anti-fantasy**: strip the story you tell about the work until the work stands for what it is.

## When to use

- Choosing what to optimize (OKRs, life goals, product metrics)
- After success that still feels empty
- Before a multi-year commitment
- When comparing yourself to a curated feed

## Executable workflow

### 1. Name the pursuit

One paragraph: what are you trying to **maximize**?

### 2. Vapor test (three questions)

Answer honestly (yes / no / unsure):

1. **If you removed public credit**, would you still pay the same cost?
2. **If it doubled in difficulty**, would it still be worth the same *kind* of person you become?
3. **Twenty years after you're gone**, does this pursuit leave anything that is not someone else's memory of you?

"No" on (1) often signals **vanity of reputation**. "No" on (2) signals **fragile motivation**. "No" on (3) is not automatically disqualifying — but it clarifies **scope**: treat it as season, not salvation.

### 3. Season check (Ecclesiastes 3)

List what season this is:

- A time to plant / uproot
- A time to break down / build up
- A time to keep / cast away

If you cannot match the season, you may be mistiming the work (right thing, wrong era of life or product).

### 4. Bounded joy (gift, not grasp)

The Teacher affirms **enjoyment** of food, drink, vocation, love — as **gift**, not as the thing that finally completes you (Ecclesiastes 5:18–20, 9:7–10).

Write one sentence:

> "I will receive **[concrete gift]** as gift this week without asking it to be my verdict."

### 5. Fear and command (closure)

Regardless of metaphysical commitment, treat **Ecclesiastes 12:13** as a compression of maturity:

- **Fear** = proportion: you are not the center of the causal universe.
- **Keep commandments** = fidelity to constraints you did not invent (law, vows, ethics, users' trust).

**Duty of man** here means **whole** obligation in compact form — use it as a final lens: does this pursuit train reverence and fidelity, or does it train grasping?

## Tone

Qoheleth is not pessimistic — he is honest. There is a difference. His voice is measured, a little ironic, anti-inflation of meaning. When applying this audit, do not preach and do not dramatize: strip the story, look at what remains, note it without despair. The Teacher permits real bounded joy (Eccl 9:7–10) — affirm it when it appears; do not collapse the audit into pure negation. The goal is clarity about what is vapor and what is not, so that effort goes to what endures.

## Script

Run an interactive audit in the terminal (answers echoed into a Markdown summary on stdout):

```bash
python scripts/vanity_audit.py --domain "your topic"
```

For non-interactive defaults, use `--batch` (all answers "unsure") to get the template only.

See [reference.md](reference.md) for nuance and misuse guards.
