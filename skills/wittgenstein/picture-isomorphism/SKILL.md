---
name: picture-isomorphism
description: Verify that a model shares logical structure with what it models. Based on Wittgenstein's Tractatus picture theory (2.1–2.19): "A picture must have in common with reality its logical form." Use when designing or evaluating data models, APIs, schemas, domain abstractions, or documentation. When a model's structure diverges from the domain's structure, all complexity built on top compounds the error.
---

# Picture Isomorphism

> *"We make to ourselves pictures of facts."*
> — Tractatus 2.1

> *"What every picture must have in common with reality in order to be able to represent it at all — rightly or falsely — is the logical form, that is, the form of reality."*
> — Tractatus 2.18

> *"We must not say, 'The complex sign aRb says a stands in relation R to b'; but we must say, that 'a' stands in a certain relation to 'b' says that aRb."*
> — Tractatus 3.1432

## The Core Principle

A picture (model, schema, API, abstraction) represents reality by sharing its **logical structure** — the same objects in the same possible relations. The representation can be true or false, but it can only *picture* something if it first shares the form.

**Corollary**: If a model cannot be wrong, it is not a model — it is a tautology. If it cannot be right, it is a contradiction. A useful model occupies the space between.

## The Structure Test

When evaluating any model, ask:

| Question | Failure mode |
|----------|-------------|
| Does each element of the model correspond to an element of the domain? | Ghost elements — concepts with no referent |
| Does each relation in the model correspond to a relation in the domain? | Phantom relations — structure imposed on the domain, not drawn from it |
| Does each constraint in the model correspond to a real constraint? | False invariants — rules that break in real cases |
| Is every domain element represented? | Blind spots — real things the model cannot express |

## When to Apply

- **Data model design**: Does the schema's table/column structure mirror the actual entity/attribute structure of the domain?
- **API design**: Does the API's resource/action structure mirror the domain's object/operation structure, or is it a bureaucratic artifact?
- **Abstraction layers**: Does the abstraction preserve the operations that matter and suppress only what is irrelevant?
- **Documentation**: Does the document's structure mirror the structure of the system it describes?
- **Code architecture**: Do module boundaries correspond to domain boundaries, or to incidental implementation details?

## The Isomorphism Protocol

```
1. Name the domain: what facts exist? what objects? what relations between them?
2. Name the model: what elements? what relations between them?
3. Construct the mapping: model element → domain element (one-to-one where possible)
4. Check completeness: every domain element has a model element
5. Check faithfulness: every model relation corresponds to a real domain relation
6. Identify failures: ghost elements, phantom relations, false invariants, blind spots
7. Restructure the model to restore isomorphism, or explicitly mark the abstraction boundaries
```

## The Projection Principle

Wittgenstein's analogy: a geometrical figure can be projected in many ways, but projective properties remain. Different models (projections) of the same domain are all valid as long as they preserve the structural relations. The choice of projection is arbitrary; the structure it must preserve is not.

This means: there is no single "correct" model, but there are *incorrect* models — those that assert relations that do not exist in the domain, or deny relations that do.

## Anti-patterns

- **The leaky abstraction**: A model that exposes implementation structure rather than domain structure — callers must know the internals to use it correctly
- **The God object**: A model element that "represents" too many distinct domain concepts — the mapping is no longer one-to-one
- **Wishful modeling**: A schema designed for the system you wish you had, not the domain you actually have — ghost relations everywhere
- **Premature normalization**: Restructuring a model for storage efficiency before verifying it accurately pictures the domain
- **The name without a referent**: A concept in the model that has no corresponding fact in the world — it cannot be true or false, so it contributes nothing (2.0201: "Every statement about complexes can be analysed into a statement about their constituent parts")
