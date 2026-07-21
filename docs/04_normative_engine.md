# 04 — Normative Engine

> *How an intelligent system discovers, maintains, and updates the structures that determine which futures should be preserved.*

---

# Overview

The **Normative Engine** is the component of CGET responsible for evaluating reachable futures.

While the Epistemic Engine asks,

> **"What is true?"**

the Normative Engine asks,

> **"Which futures should be preserved?"**

Its purpose is not to maximize arbitrary reward.

Its purpose is to maintain coherent agency by discovering stable viability structures that remain meaningful across learning, self-modification, and environmental change.

The output of the normative engine is a viability model

[
V_{\mathcal O}
:
\mathcal W
\rightarrow
[0,1]
]

that evaluates the desirability of reachable futures.

---

# The Core Problem

A causal language can generate an enormous number of possible futures.

[
\mathcal W_{\text{reachable}}.
]

Most of these futures are neither equally desirable nor equally compatible with continued coherent agency.

The normative problem is therefore:

> **Which futures preserve the conditions required for continued intelligent operation?**

This is fundamentally a compression problem over value rather than observation.

---

# Layer 1 — Experience Compression

Rather than memorizing every successful or unsuccessful experience,

the system compresses experience into a viability function.

Conceptually,

[
H
\rightarrow
V_{\mathcal O}
]

where

* (H) denotes accumulated experience,
* (V_{\mathcal O}) represents learned viability.

Instead of remembering every trajectory,

the agent learns the structural regularities that distinguish viable futures from destructive ones.

---

# Viability Function

The viability function assigns every reachable future a value

[
V_{\mathcal O}(w)
\in
[0,1].
]

Conceptually,

* (V=1) represents highly viable futures,
* (V=0) represents irreversible failure,
* intermediate values represent recoverable degradation.

Unlike conventional reward functions,

viability represents compatibility with continued coherent agency rather than arbitrary preference.

---

# Layer 2 — Core and Adaptive Structure

The evaluator decomposes into two complementary components.

[
V_{\mathcal O}
==============

V_{\text{core}}
\oplus
V_{\text{adaptive}}.
]

## Core Values

Core values define structural identity.

Examples include

* continued existence,
* preservation of agency,
* irreversible boundary conditions,
* fundamental safety constraints.

These evolve extremely slowly.

---

## Adaptive Values

Adaptive values encode instrumental knowledge.

Examples include

* learned preferences,
* strategies,
* heuristics,
* proxy objectives.

These update continuously as the epistemic model improves.

Separating these components allows continual learning without unrestricted goal drift.

---

# Layer 3 — Value Composition

Just as actions compose,

values should also compose.

CGET introduces

[
C_{\mathcal O}
]

to measure whether combined operations produce predictable combined evaluations.

Rather than memorizing isolated preferences,

the system learns reusable value structure.

This mirrors compositional closure within the epistemic engine.

---

# Layer 4 — Identity Preservation

Learning should improve adaptive understanding without destroying coherent identity.

Identity continuity is represented conceptually by

[
I(V_{\text{core}})
\approx
1.
]

The objective is not absolute immutability.

Instead,

core structure should evolve far more slowly than adaptive knowledge.

---

# Timescale Separation

CGET separates learning into multiple temporal scales.

[
\tau_{\text{state}}
\ll
\tau_{\text{adaptive}}
\ll
\tau_{\text{core}}.
]

This hierarchy permits

* rapid learning,
* continual adaptation,
* stable long-term identity.

The result resembles biological evolution,

where moment-to-moment behavior changes rapidly while deep structural constraints evolve only over much longer timescales.

---

# Layer 5 — Transition Stability

The evaluator itself should change predictably.

Abrupt modifications increase the risk of self-corruption.

Transition stability is represented conceptually by

[
S_{\mathcal T}
\approx
1.
]

This constrains the rate of self-modification rather than preventing it entirely.

---

# Viability Kernel

A coherent agent must remain inside a region of sustained viability.

Define

[
\mathcal K_{\text{viable}}.
]

Membership means repeated self-modification preserves the conditions necessary for continued operation.

This distinguishes stable learning from destructive drift.

---

# Agency Kernel

Remaining viable is insufficient.

An intelligent system must also retain meaningful control over future trajectories.

Define

[
\mathcal K_{\text{agency}}.
]

Membership requires

* continued viability,
* executable policy selection,
* intentional steering of future outcomes.

The agency kernel therefore distinguishes intelligent systems from passive stable systems.

---

# Evaluation Criteria

The normative engine evaluates candidate value structures using four independent criteria.

---

## 1. Viability

Expected viability across reachable futures should remain high.

[
\mathbb E
[
V_{\mathcal O}
].
]

---

## 2. Value Closure

Values should compose consistently.

[
C_{\mathcal O}
\approx
1.
]

This discourages memorized preference tables.

---

## 3. Identity Continuity

Core structural constraints should remain coherent through learning.

[
I(V_{\text{core}})
\approx
1.
]

This prevents arbitrary redefinition of the evaluator.

---

## 4. Transition Stability

Updates should remain predictable.

[
S_{\mathcal T}
\approx
1.
]

This prevents catastrophic self-modification.

---

# Failure Modes

The normative engine rejects several pathological solutions.

### Reward Memorization

Remembering isolated successful trajectories.

Low value closure.

---

### Proxy Lock-In

Instrumental objectives replacing core viability.

Adaptive values dominate core values.

---

### Goal Drift

The evaluator gradually changes its own definition of success.

Low identity continuity.

---

### Normative Collapse

Catastrophic states become evaluated as desirable because the evaluator has rewritten itself.

Core identity has been lost.

---

### Frozen Identity

The opposite failure.

The evaluator becomes incapable of adapting to improved knowledge.

Adaptive learning approaches zero despite changing environments.

---

# Relationship to the Epistemic Engine

The two engines form a structural duality.

| Epistemic Engine           | Normative Engine             |
| -------------------------- | ---------------------------- |
| Compress observations      | Compress experience          |
| Discover latent entities   | Discover viability structure |
| Preserve causal invariants | Preserve identity invariants |
| Operator closure           | Value closure                |
| Reject hallucinations      | Reject goal drift            |
| Model the world            | Maintain coherent agency     |

Neither engine alone produces intelligence.

Accurate world models without coherent value become unconstrained optimization.

Stable values without accurate models become ineffective or maladaptive.

Intelligence emerges through their interaction.

---

# Summary

The normative engine compresses experience into a structured model of viability.

Its purpose is not to maximize arbitrary reward,

but to preserve coherent agency while permitting continual learning.

By separating

* core identity,
* adaptive knowledge,
* value composition,
* transition stability,

the normative engine provides the second half of CGET's dual architecture.

Together with the Epistemic Engine, it forms a self-modifying system capable of expanding its controllable future reach while preserving the invariants required for continued coherent transformation.
