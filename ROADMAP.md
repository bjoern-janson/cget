# CGET Research Roadmap

## Computational Geometry of Executable Thought (CGET)

## Purpose

This document defines the progression from the current theoretical framework toward experimentally testable implementations.

CGET proposes that intelligence can be studied as:

\[
\textbf{Invariant-preserving compression under self-modifying dynamics}
\]

A system becomes more intelligent when it can:

1. Compress reality into executable representations.
2. Preserve causal and identity invariants.
3. Expand controllable future reach.
4. Improve itself without destroying the structures that make improvement meaningful.

---

# Phase 0 — Formal Foundation

## Completed

Core concepts:

- Causal Language:

\[
\mathcal{G}=(Z,\mathcal{B},\Omega,\rho)
\]

- Causal Closure:

\[
C(\Omega)
\]

- Value Closure:

\[
C_{\mathcal O}
\]

- Core / Adaptive Value Separation:

\[
V_{\mathcal O}
=
V_{core}
\oplus
V_{adaptive}
\]

- Viability Kernel:

\[
\mathcal K_{viable}
\]

- Agency Kernel:

\[
\mathcal K_{agency}
\]

- Counterfactual Steering Bandwidth:

\[
\mathcal A_{control}
\]

- Transformation Intelligence Ratio:

\[
\Theta^*
\]

---

# Phase 1 — Toy Benchmark Validation

## Goal

Test whether causal representations provide measurable advantages over trajectory optimization.

## Environment

Initial benchmark:

\[
\text{MazeWorld}
\]

## Agents

### Random Agent

Tests:

- raw exploration
- uncontrolled future generation

Expected:

\[
\mathcal A_{control}\approx0
\]

---

### Shortest Path Agent

Tests:

- optimization without abstraction

Expected:

- high immediate performance
- low transfer ability

---

### CGET Agent

Tests:

- learned transition operators
- reusable causal representations

Expected:

- improved transfer
- higher steering bandwidth

---

# Phase 2 — Representation Transfer Experiments

## Question

Does a compact causal model outperform memorized policies under distribution shift?

Experiments:

- New maze layouts
- Different obstacle patterns
- Changed action costs
- Hidden environment rules

Success criterion:

A representation-based agent should preserve performance while requiring fewer learned parameters.

---

# Phase 3 — Self-Modification Experiments

## Question

Can a system improve itself while preserving identity constraints?

Implement:

\[
\mathcal T:
(\mathcal G_t,\mathcal O_t)
\rightarrow
(\mathcal G_{t+1},\mathcal O_{t+1})
\]

Measure:

### Identity Preservation

\[
I(V_{core})
\]

### Transition Stability

\[
S_{\mathcal T}
\]

### Agency Expansion

\[
\Delta\mathcal A_{control}
\]

---

# Phase 4 — Value Learning

## Goal

Move from static rewards toward dynamic viability modeling.

Implement:

\[
V_{\mathcal O}(w)
\]

as a learned viability field.

Test:

- proxy correction
- preference updates
- value drift
- boundary preservation

---

# Phase 5 — Alignment Experiments

## Core Question

Can capability increase without destroying evaluator coherence?

Test:

### Safe Adaptation

\[
\Delta V_{adaptive}\neq0
\]

while:

\[
\Delta V_{core}\approx0
\]

---

### Normative Collapse

Failure condition:

\[
V_{core,t+1}
\rightarrow
V_{corrupted}
\]

where catastrophic states become evaluated as optimal.

---

# Phase 6 — Larger Systems

Potential research directions:

## Reinforcement Learning

Compare:

- reward maximization
- representation learning
- viability-constrained agency

---

## Language Models

Study:

- latent representations
- tool use
- reasoning chains
- self-correction

---

## Autonomous Agents

Measure:

- future search efficiency
- controllable reach
- identity stability

---

# Major Open Questions

## 1. What exactly constitutes a core invariant?

Can identity constraints be discovered, specified, or only approximated?

---

## 2. Can value closure be measured objectively?

Does a coherent value structure require:

- consistency?
- survival?
- human preference alignment?
- another invariant?

---

## 3. Is causal compression sufficient?

Or are there additional primitives required for intelligence?

---

## 4. What is the relationship between agency and intelligence?

Possible hypothesis:

\[
\text{Intelligence}
\approx
\text{Compression}
\times
\text{Control}
\times
\text{Invariant Preservation}
\]

---

# Long-Term Vision

CGET aims to provide a mathematical language for studying systems that:

- understand environments,
- modify themselves,
- maintain coherent identity,
- and expand their influence over possible futures.

The central research question:

> How can a system increase its power over reality without destroying the invariants that define what that power is for?

---

# Current Status

Repository stage:

**Theoretical framework + toy benchmark specification**

Next milestone:

**Run experiments and replace conceptual metrics with measured quantities.**
