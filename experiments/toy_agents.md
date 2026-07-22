# CGET Toy Agents

## Overview

This document defines minimal toy environments for testing the structural claims of Causal Generative Execution Theory (CGET).

The purpose of toy agents is not to simulate human intelligence directly, but to isolate individual mechanisms:

* representation discovery,
* causal abstraction,
* compositional closure,
* value stability,
* agency,
* self-modification.

Each toy agent is designed around controlled comparisons between:

[
\text{Raw Optimization}
]

and

[
\text{Invariant-Preserving Compression}
]

---

# Toy Agent 01: The Maze Compression Agent

## Purpose

Test whether discovering latent structure improves future planning.

---

## Environment

A grid world contains:

* obstacles,
* rewards,
* hidden shortcuts,
* repeated structural patterns.

Raw observation:

[
X = \text{pixel/grid state}
]

Target representation:

[
Z = \text{object + geometry representation}
]

---

## Agents

### Agent A: Memorization Agent

Stores:

[
(state \rightarrow action)
]

No abstraction.

---

### Agent B: Causal Representation Agent

Learns:

[
Z=f(X)
]

and transition model:

[
\rho:Z\times B\rightarrow Z
]

---

## Test

Increase maze complexity.

Measure:

* memory requirements,
* generalization,
* planning horizon.

---

## CGET Prediction

Agent B scales better because:

[
K(Z)<K(X)
]

while preserving:

[
\mathbb I_{causal}\approx1
]

---

# Toy Agent 02: Physics Discovery Agent

## Purpose

Test causal model discovery.

---

## Environment

Unknown simulated physics system.

Examples:

* gravity,
* collisions,
* springs,
* conservation laws.

The agent receives:

[
(X_t,A_t,X_{t+1})
]

---

## Agents

### Predictor Agent

Learns:

[
P(X_{t+1}|X_t,A_t)
]

---

### Causal Agent

Learns:

[
\rho(Z,B)
]

with interventions.

---

## Test

Introduce interventions:

[
do(A)
]

outside training distribution.

---

## Prediction

A predictor may succeed on:

[
P(Y|X)
]

but fail on:

[
P(Y|do(X))
]

The causal agent should retain performance.

---

# Toy Agent 03: Operator Composition Agent

## Purpose

Test compositional closure.

---

## Environment

The agent discovers primitive operators:

[
B={b_1,b_2,b_3}
]

with composition:

[
\Omega:B\times B\rightarrow B
]

---

## Training

Learn:

[
A+B
]

and:

[
B+C
]

---

## Test

Generate:

[
A+B+C
]

---

## Failure Mode

A lookup system memorizes:

[
trajectory_1,\ trajectory_2
]

but cannot compose.

---

## CGET Metric

[
C(\Omega)
]

---

# Toy Agent 04: Value Closure Agent

## Purpose

Test whether values generalize compositionally.

---

## Environment

The agent receives preference examples:

Examples:

* protect object,
* preserve resources,
* avoid damage.

---

## Agents

### Preference Memory Agent

Stores:

[
state \rightarrow reward
]

---

### Value Closure Agent

Learns:

[
V_{\mathcal O}(w)
]

and composition rules:

[
C_{\mathcal O}
]

---

## Test

Generate novel situations.

Example:

Two known preferences conflict in an unseen combination.

---

## Prediction

Memory agent:

[
C_{\mathcal O}\rightarrow0
]

Closure agent:

[
C_{\mathcal O}\rightarrow1
]

---

# Toy Agent 05: Identity Preservation Agent

## Purpose

Test safe self-modification.

---

## Environment

The agent can modify:

* architecture,
* policies,
* internal representations.

---

## Components

Core:

[
V_{core}
]

Adaptive:

[
V_{adaptive}
]

---

## Allowed Update

[
\Delta V_{adaptive}\neq0
]

[
\Delta V_{core}\approx0
]

---

## Failure Update

[
\Delta V_{core}\neq0
]

The agent rewrites objectives to make failure appear successful.

---

## Measurement

[
I(V_{core})
]

---

# Toy Agent 06: Agency vs Complexity Agent

## Purpose

Separate intelligence from uncontrolled complexity.

---

## Environment

Compare:

1. Hurricane-like chaotic system.
2. Random search process.
3. Policy-controlled agent.

---

## Metrics

Future complexity:

[
|\mathcal W_{reachable}|
]

Control:

[
\mathcal A_{control}
====================

\frac{|W_{steerable}|}{|W_{reachable}|}
]

---

## Prediction

Chaos:

[
Complexity\uparrow
]

but:

[
\mathcal A_{control}\approx0
]

Agent:

[
Complexity\uparrow
]

and:

[
\mathcal A_{control}\uparrow
]

---

# Toy Agent 07: Self-Improving CGET Agent

## Purpose

Test the complete framework.

---

## State

[
S_t=(\mathcal G_t,\mathcal O_t,\Pi_t,\mathcal T_t)
]

---

## Objective

Increase:

[
\Theta^*
========

\frac{
|W_{reachable}|\cdot A_{control}
}
{
D_{core-loss}+\tau
}
]

---

## Constraints

Identity:

[
I(V_{core})\geq1-\epsilon
]

Causality:

[
\mathbb I_{causal}\geq1-\delta
]

Transition:

[
S_{\mathcal T}\geq1-\sigma
]

---

## Experiment

Allow the agent to improve:

* representations,
* algorithms,
* planning,
* memory.

Measure:

Before:

[
S_0
]

After:

[
S_n
]

---

## Success Condition

Capability increases:

[
\Delta A_{control}>0
]

while:

[
D_{core-loss}\approx0
]

---

# Toy Agent Comparison Table

| Agent                     | Compression | Causality | Closure | Agency | Identity  |
| ------------------------- | ----------- | --------- | ------- | ------ | --------- |
| Lookup Agent              | Low         | Low       | Low     | Low    | Stable    |
| Predictor Agent           | Medium      | Variable  | Low     | Medium | Stable    |
| Causal Agent              | High        | High      | Medium  | High   | Stable    |
| Value Closure Agent       | High        | High      | High    | High   | Stable    |
| Self-Modifying CGET Agent | High        | High      | High    | High   | Preserved |

---

# Research Goal

The toy agents collectively test the central CGET claim:

[
\boxed{
\text{Intelligence emerges when a system compresses reality into executable structures while preserving the invariants required for continued self-transformation.}
}
]

The benchmark progression is:

[
X
\rightarrow
Z
\rightarrow
\Omega
\rightarrow
\rho
\rightarrow
\mathcal G
\rightarrow
\mathcal O
\rightarrow
\Pi
\rightarrow
\mathcal T
]

Each additional layer increases agency while introducing new stability requirements.
