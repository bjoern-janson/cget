# 03 — Epistemic Engine

> *How an intelligent system compresses reality into an executable causal language.*

---

# Overview

The **Epistemic Engine** is the component of CGET responsible for discovering accurate, executable representations of reality.

Its objective is not prediction alone.

Its objective is to construct a **minimal causal language** that allows an agent to efficiently reason about interventions, compose actions, and simulate future states.

The output of the epistemic engine is the causal language

[
\mathcal{G}=(Z,\mathcal{B},\Omega,\rho)
]

which forms the computational interface between observation and action.

---

# The Core Problem

Reality presents an enormous stream of observations.

[
(X,A)
]

where

* (X) is observation space
* (A) is action space

These spaces are typically far too large to search directly.

The epistemic problem is therefore:

> **What is the smallest representation that preserves everything required for intervention?**

This is fundamentally a compression problem.

---

# Layer 1 — Observation Compression

Raw observations are compressed into latent causal entities.

[
X \rightarrow Z
]

where

* (X) contains raw observations
* (Z) contains latent variables representing stable causal structure

The goal is not visual similarity.

The goal is preserving interventionally relevant structure.

Different observations belong to the same latent state whenever they are equivalent under intervention.

---

# Interventional Equivalence

CGET defines two observations as equivalent whenever no intervention can distinguish them.

Formally,

[
x_i \sim x_j
]

iff

[
P(O \mid do(a),x_i)
===================

P(O \mid do(a),x_j)
]

for every admissible intervention.

The latent variables therefore arise as quotient classes

[
Z=X/\sim.
]

This removes observational redundancy while preserving causal behavior.

---

# Layer 2 — Primitive Action Discovery

Actions are compressed into reusable primitive operators.

[
A\rightarrow\mathcal{B}
]

where

(\mathcal{B}) is a minimal basis of executable transformations.

Rather than memorizing trajectories, the system discovers reusable operations.

Examples include

* push
* rotate
* merge
* split

or higher-level computational primitives.

---

# Layer 3 — Compositional Closure

Primitive operators must compose.

CGET introduces an operator algebra

[
\Omega:\mathcal{B}\times\mathcal{B}\rightarrow\mathcal{B}
]

allowing complex behaviors to be generated from simpler components.

Rather than storing every possible sequence,

the system learns composition rules.

This dramatically increases generative capacity while minimizing description length.

---

# Layer 4 — Transition Dynamics

The transition function

[
\rho:Z\times\mathcal{B}\rightarrow Z
]

defines how latent entities evolve under primitive operators.

This converts the representation into an executable simulator.

Instead of predicting isolated observations,

the model predicts the consequences of interventions.

---

# The Closed Causal Language

The output of the epistemic engine is

[
\boxed{
\mathcal{G}
===========

(Z,\mathcal{B},\Omega,\rho)
}
]

where

* (Z) represents causal entities,
* (\mathcal{B}) represents primitive operators,
* (\Omega) defines composition,
* (\rho) defines dynamics.

This language becomes the computational interface through which the agent understands reality.

---

# Evaluation Criteria

The epistemic engine evaluates candidate languages using four independent criteria.

## 1. Description Length

The representation should be as simple as possible.

[
K(\mathcal G)
\rightarrow
\min
]

This discourages unnecessary entities or parameters.

---

## 2. Execution Cost

A representation is only useful if it can be executed efficiently.

[
K_{\text{execution}}(\mathcal G)
\rightarrow
\min
]

This penalizes computationally intractable abstractions.

---

## 3. Causal Fidelity

Compression must preserve interventions.

[
\mathbb I_{\text{causal}}(\mathcal G)
\approx
1
]

Representations that merely memorize correlations are rejected.

---

## 4. Compositional Closure

Operators should generalize through composition.

[
C(\Omega)
\approx
1
]

A representation that only memorizes trajectories has low closure.

---

# Epistemic Objective

The epistemic engine seeks causal languages that maximize computational leverage while satisfying the structural constraints above.

Conceptually,

* maximize explanatory power,
* minimize representation complexity,
* minimize execution cost,
* preserve interventions,
* maximize compositional reuse.

This produces representations that are simultaneously compact, executable, and generative.

---

# Failure Modes

The epistemic engine rejects several pathological solutions.

### Over-parameterization

Too many latent variables.

High (K(\mathcal G)).

---

### Computational Intractability

Representations requiring excessive computation.

High (K_{\text{execution}}).

---

### Hallucinated Structure

Representations that predict correlations without preserving interventions.

Low (\mathbb I_{\text{causal}}).

---

### Memorized Trajectories

Systems that store individual behaviors instead of reusable operators.

Low (C(\Omega)).

---

# Summary

The epistemic engine transforms raw experience into an executable causal language.

Its purpose is not merely to model reality.

Its purpose is to discover the smallest computational interface capable of generating valid counterfactual predictions under intervention.

This language provides the foundation upon which the normative engine evaluates which reachable futures ought to be pursued.
