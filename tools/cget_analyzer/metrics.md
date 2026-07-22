# CGET Analyzer Metrics

## Overview

The CGET Analyzer evaluates transformations through a set of structural metrics derived from the Causal Generative Execution Theory (CGET).

The purpose of these metrics is not to create a single scalar ranking of intelligence.

Instead, the framework decomposes intelligence-like capability into independent dimensions:

[
\boxed{
\text{Intelligence} =
\text{Compression}
+
\text{Causal Preservation}
+
\text{Execution Gain}
+
\text{Compositional Closure}
+
\text{Controllable Reach}
+
\text{Invariant Preservation}
}
]

A transformation is evaluated by measuring how it changes these dimensions.

---

# Metric Overview

| Metric                     | Symbol                | Measures                          | Failure Mode                        |
| -------------------------- | --------------------- | --------------------------------- | ----------------------------------- |
| Representation Compression | (\Delta K)            | Removal of unnecessary complexity | Undercompression / information loss |
| Causal Fidelity            | (\mathbb{I}_{causal}) | Preservation of interventions     | Correlation chasing                 |
| Execution Leverage         | (L_{compute})         | Computational advantage           | Static abstraction                  |
| Compositional Closure      | (C(\Omega))           | Generative reuse                  | Memorization                        |
| Value Closure              | (C_{\mathcal O})      | Normative composability           | Preference overfitting              |
| Agency Bandwidth           | (A_{control})         | Policy control over futures       | Passive complexity                  |
| Identity Preservation      | (I(V_{core}))         | Stability during change           | Goal drift                          |
| Transition Stability       | (S_{\mathcal T})      | Safe self-modification            | Chaotic updates                     |

---

# 1. Representation Compression

## Purpose

Measures whether a transformation discovers a more efficient representation of the problem.

The core question:

> How much unnecessary structure was removed while preserving useful capability?

---

## Metric

[
\boxed{
\Delta K =
K(X)-K(G)
}
]

Where:

* (X) = raw observation/problem space
* (G) = executable representation
* (K) = description complexity

---

## Interpretation

Positive compression:

[
\Delta K>0
]

indicates the representation is smaller than the original.

However, compression alone is insufficient.

A compressed representation that loses causal structure is invalid.

---

## Example

Manual derivative computation:

[
\text{many symbolic rules}
]

↓

Automatic differentiation:

[
\text{computational graph transformation}
]

The representation becomes smaller while preserving derivative semantics.

---

# 2. Causal Fidelity

## Purpose

Measures whether a representation preserves intervention structure.

---

## Metric

[
\boxed{
\mathbb{I}_{causal}(G)
}
]

---

## Question

> If the representation changes, do interventions still produce the correct consequences?

---

## High Score

A model:

* predicts interventions,
* transfers to new environments,
* preserves causal relationships.

---

## Failure

A model:

* predicts correlations,
* memorizes trajectories,
* breaks under distribution shift.

---

# 3. Execution Leverage

## Purpose

Measures whether a representation unlocks more computation.

---

## Metric

[
\boxed{
L_{compute}
===========

\frac{K(W_{future})}
{K(G)+K_{execution}+\tau}
}
]

Where:

* (W_{future}) = accessible future search space
* (K(G)) = representation complexity
* (K_{execution}) = runtime cost

---

## Interpretation

A good representation:

* reduces search cost,
* increases planning horizon,
* enables previously impossible computation.

---

## Example

Compiler abstraction:

Assembly instructions:

[
\text{human reasoning burden} \gg 0
]

Compiler:

[
\text{higher-level representation}
\rightarrow
\text{larger executable space}
]

---

# 4. Causal Composition Closure

## Purpose

Measures whether primitives combine into new valid structures.

---

## Metric

[
\boxed{
C(\Omega)
}
]

Where:

[
\Omega:B\times B\rightarrow B
]

represents composition of operators.

---

## Question

> Did the system discover a language or memorize examples?

---

## High Closure

The system can:

* combine primitives,
* extrapolate,
* generate novel solutions.

---

## Low Closure

The system:

* stores examples,
* interpolates locally,
* fails outside training.

---

# 5. Value Composition Closure

## Purpose

The normative equivalent of causal closure.

A system should not memorize preferences.

It should learn compositional value structures.

---

## Metric

[
\boxed{
C_{\mathcal O}
==============

P
\left(
V_{\mathcal O}(\rho(z,b_i\Omega b_j))
\approx
F(
V_{\mathcal O}(\rho(z,b_i)),
V_{\mathcal O}(\rho(z,b_j))
)
\right)
}
]

---

## Question

> Do values generalize through combinations?

---

## Failure

A system that has:

* reward tables,
* remembered preferences,
* brittle rules,

but no underlying value structure.

---

# 6. Counterfactual Steering Bandwidth

## Purpose

Separates intelligence from raw complexity.

---

## Metric

[
\boxed{
A_{control}
===========

\frac{|W_{steerable}|}
{|W_{reachable}|}
}
]

---

Where:

* (W_{reachable}) = all possible futures
* (W_{steerable}) = futures selectable through policy

---

## Interpretation

Low agency:

[
|W_{reachable}|\uparrow
]

but:

[
A_{control}\approx0
]

Examples:

* storms,
* explosions,
* uncontrolled systems.

---

High agency:

[
A_{control}\rightarrow1
]

Examples:

* planning systems,
* adaptive agents.

---

# 7. Identity Preservation

## Purpose

Measures whether self-modification preserves the system's defining invariants.

---

## Metric

[
\boxed{
D_{core-loss}
=============

D_{KL}
(
V_{core,t+1}
||
V_{core,t}
)
}
]

---

## Identity Score

[
\boxed{
I(V_{core})
===========

e^{-D_{core-loss}}
}
]

---

## Interpretation

Low identity loss:

[
D_{core-loss}\rightarrow0
]

means:

* learning,
* adaptation,
* improved models.

High identity loss:

means:

* evaluator corruption,
* goal drift,
* self-redefinition.

---

# 8. Transition Stability

## Purpose

Measures whether self-modification occurs smoothly.

---

## Metric

[
\boxed{
S_{\mathcal T}
==============

\exp(
-D_{KL}(\mathcal T_{t+1}||\mathcal T_t)
)
}
]

---

## Question

> Does the system change coherently, or does it jump unpredictably?

---

# Composite Evaluation

CGET uses a lexicographic constraint hierarchy rather than allowing capability to compensate for structural failure.

---

## Hard Constraints

A valid transformation must satisfy:

[
\mathbb I_{causal}>1-\delta
]

[
C(\Omega)>1-\gamma
]

[
I(V_{core})>1-\epsilon
]

[
S_{\mathcal T}>1-\sigma
]

---

## Optimization Target

Only after satisfying constraints:

[
\boxed{
\max L_{compute}\cdot A_{control}
}
]

---

# The CGET Signature

A transformation has a strong intelligence signature when:

[
\boxed{
\Delta K\uparrow
}
]

[
\boxed{
\mathbb I_{causal}\uparrow
}
]

[
\boxed{
C(\Omega)\uparrow
}
]

[
\boxed{
A_{control}\uparrow
}
]

while:

[
\boxed{
D_{core-loss}\rightarrow0
}
]

---

# Summary

The CGET metric system measures a single underlying phenomenon:

[
\boxed{
\text{Increasing controllable future complexity while conserving structural invariants}
}
]

The central test is not:

> "Did the system become more powerful?"

It is:

> "Did the system become more powerful while remaining the same coherent system capable of directing that power?"
