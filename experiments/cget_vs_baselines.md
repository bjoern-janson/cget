# CGET vs Baselines

## Experimental Comparison Framework

This document defines the baseline comparisons used to evaluate whether CGET captures capabilities that are not explained by existing optimization, prediction, or control paradigms.

The goal is not to demonstrate that CGET replaces existing approaches, but to identify whether **invariant-preserving compression and controllable future reach** explain measurable differences between systems.

---

# Core Experimental Question

The central question:

> Does learning compact executable causal structures produce greater adaptive intelligence than systems optimized only for prediction, reward maximization, search, or fixed control?

CGET predicts that strong intelligence requires simultaneous optimization of:

1. Representation efficiency
2. Causal fidelity
3. Compositional closure
4. Counterfactual steering ability
5. Identity-preserving adaptation

---

# Baseline Categories

## 1. Random Agent

## Description

A policy with no learned representation or planning mechanism.

[
\pi(a|s)=Uniform(A)
]

## Purpose

Establish the minimum capability baseline.

## Expected Behavior

Strengths:

* zero computational overhead
* no model assumptions

Weaknesses:

* no causal understanding
* no generalization
* no future steering

Expected CGET profile:

| Metric                  | Expected            |
| ----------------------- | ------------------- |
| (K(\mathcal{G}))        | Minimal             |
| (\mathbb{I}_{causal})   | ~0                  |
| (C(\Omega))             | 0                   |
| (\mathcal{A}_{control}) | Low                 |
| (I(V_{core}))           | Undefined / trivial |

---

# 2. Fixed Policy Agent

## Description

A hand-designed controller optimized for a known environment.

Examples:

* scripted rules
* heuristic controller
* lookup policy

## Purpose

Tests whether performance comes from memorized solutions rather than discovered structure.

## Expected Behavior

Strengths:

* high performance in known environments
* low inference cost

Weaknesses:

* poor transfer
* no structural discovery
* limited adaptation

Expected CGET profile:

| Metric                  | Expected              |
| ----------------------- | --------------------- |
| (K(\mathcal{G}))        | Low                   |
| (\mathbb{I}_{causal})   | Environment-dependent |
| (C(\Omega))             | Low                   |
| (\mathcal{A}_{control}) | Moderate              |
| Adaptation              | Poor                  |

---

# 3. Search-Based Agent

## Description

A planning system that explores possible actions directly.

Examples:

* breadth-first search
* A*
* Monte Carlo Tree Search

## Purpose

Separates intelligence from brute-force future exploration.

## Expected Behavior

Strengths:

* strong short-horizon control
* accurate local planning

Weaknesses:

* computational explosion
* limited abstraction
* weak transfer

CGET prediction:

Search increases reachable futures but does not necessarily increase compressed future reach.

The distinction:

[
\text{Future Exploration}
\neq
\text{Future Understanding}
]

Expected profile:

| Metric             | Expected                 |
| ------------------ | ------------------------ |
| Reachable futures  | High                     |
| Steering bandwidth | High locally             |
| Compression        | Low                      |
| Runtime efficiency | Degrades with complexity |

---

# 4. Reinforcement Learning Agent

## Description

A learned policy optimized through environmental reward.

General form:

[
\max_\pi E[\sum_t \gamma^t r_t]
]

## Purpose

Compare reward optimization against CGET's viability optimization.

## Strengths

* adaptive behavior
* policy discovery
* strong task performance

## Weaknesses

Potential failure modes:

* reward hacking
* proxy optimization
* distribution shift
* unstable self-modification

CGET interpretation:

RL optimizes:

[
\text{Reward}
]

CGET attempts to optimize:

[
\text{Reachable controllable futures}
+
\text{Invariant preservation}
]

Expected profile:

| Metric                | Expected               |
| --------------------- | ---------------------- |
| Task reward           | High                   |
| Causal fidelity       | Variable               |
| Value closure         | Variable               |
| Identity preservation | Depends on constraints |

---

# 5. World Model Agent

## Description

An agent that learns an internal predictive model.

Examples:

* latent dynamics models
* predictive representation learning

## Purpose

Tests the epistemic half of CGET.

## Strengths

* compressed representations
* improved planning
* transfer capability

## Weaknesses

Prediction alone does not guarantee:

* causal validity
* agency
* alignment

CGET prediction:

A world model without normative closure creates capable but potentially uncontrolled optimization.

Expected profile:

| Metric              | Expected  |
| ------------------- | --------- |
| Compression         | High      |
| Prediction          | High      |
| Causal fidelity     | Variable  |
| Normative stability | Undefined |

---

# 6. CGET Agent

## Description

A system explicitly optimized for:

[
\Psi_{stable}
]

with:

[
\mathcal{G}
===========

(Z,\mathcal{B},\Omega,\rho)
]

and:

[
V_{\mathcal O}
==============

V_{core}
\oplus
V_{adaptive}
]

---

# Expected CGET Advantages

## 1. Distribution Shift

Scenario:

Training environment:

```
A → B → C
```

Testing environment:

```
A → X → C
```

Memorization fails.

Causal operators transfer.

Prediction:

[
CGET > Fixed\ Policy
]

---

## 2. Compositional Generalization

Scenario:

Learn:

[
A \circ B
]

Test:

[
A \circ B \circ C
]

Systems with operator closure should outperform trajectory learners.

Prediction:

[
C(\Omega) \uparrow
\Rightarrow
Generalization \uparrow
]

---

## 3. Self-Modification

Scenario:

Agent improves its own architecture.

Compare:

### Unconstrained Self-Modification

Potential:

[
Capability \uparrow
]

but:

[
I(V_{core}) \downarrow
]

### CGET-Constrained Modification

Expected:

[
Capability \uparrow
]

while:

[
I(V_{core}) \approx 1
]

---

# Comparison Matrix

| System            | Compression | Causal Model | Control | Adaptation | Identity Preservation |
| ----------------- | ----------- | ------------ | ------- | ---------- | --------------------- |
| Random            | ❌           | ❌            | ❌       | ❌          | N/A                   |
| Fixed Policy      | Low         | Low          | Medium  | Low        | Fixed                 |
| Search Agent      | Low         | Medium       | High    | Low        | Fixed                 |
| RL Agent          | Medium      | Variable     | Medium  | Medium     | Variable              |
| World Model Agent | High        | Variable     | High    | Medium     | Variable              |
| CGET Agent        | High        | High         | High    | High       | Explicit              |

---

# Primary Falsification Test

CGET fails as a useful framework if:

1. Causal compression provides no advantage over memorization.
2. Steering bandwidth does not distinguish agency from uncontrolled complexity.
3. Identity constraints provide no benefit during self-modification.
4. The combined metric predicts no outcomes better than existing measures.

---

# Final Hypothesis

CGET predicts:

> The most capable adaptive systems will not be those that maximize reachable futures alone, but those that maximize controllable future reach while preserving the invariants that make continued agency possible.

The benchmark suite therefore evaluates not only whether an agent can reach futures, but whether it can intentionally choose, preserve, and continue navigating them.
