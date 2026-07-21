# 01 – Core Primitives

# Core Primitives

Causal Generative Equilibrium Theory (CGET) is built from a small collection of primitives intended to be orthogonal. Each primitive captures a distinct aspect of intelligence, and together they define the language used throughout the framework.

The goal is to minimize conceptual overlap while maximizing explanatory power.

---

# Design Principles

The primitives are chosen according to four criteria:

1. **Minimal** — each primitive should represent a single idea.
2. **Composable** — primitives should combine into larger structures.
3. **Operational** — each primitive should admit measurable or computable interpretations.
4. **Replaceable** — future mathematical refinements should modify individual primitives without changing the overall architecture.

---

# Primitive 1 — World State

[
X
]

The observable state of the environment.

This is the highest-dimensional description available to the agent and contains both relevant and irrelevant variation.

Examples include:

* sensor observations,
* simulator states,
* physical measurements,
* database records.

The purpose of intelligence is **not** to memorize (X), but to discover a more useful representation.

---

# Primitive 2 — Latent Representation

[
Z=f(X)
]

A compressed representation of the world that preserves the causal distinctions necessary for reasoning and intervention.

A useful latent representation should satisfy three properties:

* lower complexity than the original observations,
* preservation of interventionally relevant structure,
* support for composition and prediction.

The mapping

[
X\rightarrow Z
]

is one of the central operations in CGET.

---

# Primitive 3 — Primitive Operators

[
\mathcal B
]

The basic executable transformations available to the agent.

These correspond to actions, operations, or elementary interventions.

Examples include:

* robot motor commands,
* software functions,
* mathematical operators,
* planning actions.

Primitive operators serve as the alphabet from which larger behaviors are constructed.

---

# Primitive 4 — Composition Algebra

[
\Omega
]

A rule for composing primitive operators into larger executable programs.

Rather than treating actions independently, CGET assumes useful intelligence discovers reusable composition rules.

This distinguishes generalization from memorization.

A learned system should discover:

[
b_i\Omega b_j
]

rather than separately memorizing every possible action sequence.

---

# Primitive 5 — Transition Dynamics

[
\rho
:
Z\times\mathcal B
\rightarrow
Z
]

The transition function describing how operators transform latent states.

Together,

[
(Z,\mathcal B,\Omega,\rho)
]

form an executable causal language.

This language should support simulation, planning, and counterfactual reasoning.

---

# Primitive 6 — Causal Language

[
\mathcal G
==========

(Z,\mathcal B,\Omega,\rho)
]

The central object of the epistemic engine.

A causal language is more than a predictive model.

It is an executable representation capable of generating valid counterfactual trajectories.

The quality of a causal language is evaluated using several structural constraints introduced later in the framework, including:

* compression,
* causal fidelity,
* execution efficiency,
* compositional closure.

---

# Primitive 7 — Viability Function

[
V_{\mathcal O}
:
\mathcal W
\rightarrow
[0,1]
]

Maps reachable futures onto a measure of viability.

Rather than assigning arbitrary rewards, the viability function estimates how compatible a future is with continued coherent operation.

Conceptually,

* (V=1) represents highly viable futures,
* (V=0) represents irreversible failure.

---

# Primitive 8 — Core and Adaptive Values

The viability function decomposes into two components:

[
V_{\mathcal O}
==============

V_{\text{core}}
\oplus
V_{\text{adaptive}}
]

## Core Values

The slowly changing structural constraints defining the identity of the agent.

Examples include:

* physical survival,
* preservation of agency,
* irreversible failure boundaries.

## Adaptive Values

Rapidly changing instrumental preferences.

These include:

* strategies,
* heuristics,
* learned proxies,
* environment-specific objectives.

This decomposition separates identity preservation from continual learning.

---

# Primitive 9 — Policy

[
\pi\in\Pi
]

A policy selects operators according to the current latent state.

Policies determine which futures become realized.

Without policy selection, future complexity alone does not imply agency.

---

# Primitive 10 — Reachable Futures

[
\mathcal W_{\text{reachable}}
]

The set of futures consistent with the current causal language.

This represents possibility.

It does **not** represent control.

---

# Primitive 11 — Steerable Futures

[
\mathcal W_{\text{steerable}}
]

The subset of reachable futures that can be intentionally selected through policy.

The distinction between reachable and steerable futures is central to CGET's definition of agency.

---

# Primitive 12 — Counterfactual Steering Bandwidth

[
\mathcal A_{\text{control}}
===========================

\frac
{
|\mathcal W_{\text{steerable}}|
}
{
|\mathcal W_{\text{reachable}}|
}
]

This measures how strongly internal decisions influence future outcomes.

High future complexity without steering ability corresponds to uncontrolled dynamics rather than intelligence.

---

# Primitive 13 — Self-Modification Operator

[
\mathcal T
:
(\mathcal G_t,\mathcal O_t)
\rightarrow
(\mathcal G_{t+1},\mathcal O_{t+1})
]

The transformation governing both learning and self-improvement.

Rather than treating intelligence as static optimization, CGET models intelligent systems as dynamical processes operating under repeated self-modification.

---

# Primitive 14 — Viability Kernel

[
\mathcal K_{\text{viable}}
]

The set of states from which the system can remain inside acceptable operating conditions indefinitely.

Membership in the viability kernel represents sustained coherence under repeated updates.

---

# Primitive 15 — Agency Kernel

[
\mathcal K_{\text{agency}}
]

The subset of viable states from which the system possesses at least one executable policy capable of intentionally steering future trajectories.

This distinguishes passive persistence from active agency.

---

# Primitive Relationships

The primitives interact through the following dependency structure:

```text
World
  X
  │
  ▼
Latents
  Z
  │
  ▼
Operators
  B
  │
  ▼
Composition
  Ω
  │
  ▼
Dynamics
  ρ
  │
  ▼
Causal Language
  G
  │
  ├──────────────┐
  ▼              ▼
Reachable     Policies
Futures       Π
  │              │
  └──────┬───────┘
         ▼
Steerable Futures
         │
         ▼
Viability
V_O
         │
         ▼
Self Modification
T
         │
         ▼
Agency
```

---

# Summary

The remainder of CGET is built by imposing structural constraints on these primitives rather than introducing fundamentally new objects.

Subsequent sections formalize:

* how causal languages are evaluated,
* how value structures remain coherent,
* how agency emerges from controllable counterfactual reach,
* and how self-modifying systems preserve identity while increasing capability.
