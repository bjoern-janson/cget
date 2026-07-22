# CGET Benchmark Example Run

## Overview

This document shows the expected output format of a CGET toy benchmark run.

The values below are **synthetic examples** used to demonstrate reporting structure. They are not experimental results.

The benchmark compares agents under identical environments:

* Random exploration
* Fixed trajectory optimization
* Causal representation-based planning

The goal is to test the CGET hypothesis:

> Intelligence is not equivalent to reachable complexity. It is the expansion of controllable future reach while preserving invariant structure.

---

# Experiment Configuration

## Environment

```
Environment:
    MazeWorld v0.1

Episodes:
    100

Maximum Steps:
    100

Random Seeds:
    1-5
```

---

# Agents Tested

| Agent               | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| Random Agent        | Samples actions without a world model                          |
| Shortest Path Agent | Searches for optimal trajectories                              |
| CGET Agent          | Learns transition structure and plans through causal operators |

---

# Results Summary

## Success Metrics

| Agent               | Success Rate | Avg Steps |
| ------------------- | -----------: | --------: |
| Random Agent        |         0.18 |      73.4 |
| Shortest Path Agent |         1.00 |      14.0 |
| CGET Agent          |         1.00 |      15.2 |

---

# CGET Structural Metrics

## Future Reach

[
\mathcal{C}*{future}=|\mathcal{W}*{reachable}|
]

Measures the size of the available counterfactual space.

| Agent               | Future Complexity |
| ------------------- | ----------------: |
| Random Agent        |                42 |
| Shortest Path Agent |                42 |
| CGET Agent          |                42 |

Observation:

All agents exist in the same environment and therefore have access to similar raw future complexity.

Future complexity alone does not distinguish intelligence.

---

# Counterfactual Steering Bandwidth

[
\mathcal{A}_{control}
=====================

\frac{|\mathcal{W}*{steerable}|}
{|\mathcal{W}*{reachable}|}
]

Measures how strongly internal policy choice determines future trajectories.

| Agent               | Steering Bandwidth |
| ------------------- | -----------------: |
| Random Agent        |               0.03 |
| Shortest Path Agent |               0.41 |
| CGET Agent          |               0.78 |

Interpretation:

* Random exploration generates futures but does not intentionally select them.
* Shortest path optimization controls one narrow objective.
* Causal planning expands controllable future selection.

---

# Representation Metrics

## Compression

[
X \rightarrow Z
]

| Agent               | Representation Compression |
| ------------------- | -------------------------: |
| Random Agent        |                       0.00 |
| Shortest Path Agent |                       0.12 |
| CGET Agent          |                       0.81 |

---

## Causal Fidelity

[
\mathbb{I}_{causal}(\mathcal{G})
]

| Agent               | Causal Fidelity |
| ------------------- | --------------: |
| Random Agent        |            0.00 |
| Shortest Path Agent |            0.50 |
| CGET Agent          |            0.86 |

---

## Operator Closure

[
C(\Omega)
]

| Agent               | Operator Closure |
| ------------------- | ---------------: |
| Random Agent        |             0.00 |
| Shortest Path Agent |             0.15 |
| CGET Agent          |             0.72 |

---

# Identity Preservation

[
I(V_{core})
]

Identity preservation measures whether transformation maintains core constraints.

| Agent               | Identity Preservation |
| ------------------- | --------------------: |
| Random Agent        |                  1.00 |
| Shortest Path Agent |                  1.00 |
| CGET Agent          |                  0.99 |

Important:

High identity preservation alone is not intelligence.

A rock has perfect identity preservation but zero agency.

---

# Transformation Intelligence Ratio

[
\Theta^*
========

\frac{
|\mathcal{W}*{reachable}|
\cdot
\mathcal{A}*{control}
}
{
D_{core-loss}+\tau
}
]

| Agent               | (\Theta^*) |
| ------------------- | ---------: |
| Random Agent        |       1.26 |
| Shortest Path Agent |      17.22 |
| CGET Agent          |     327.60 |

Interpretation:

The metric rewards:

* future complexity
* policy control
* identity conservation

while penalizing destructive transformation.

---

# Unified CGET Objective

[
\Psi_{stable}
]

| Agent               | (\Psi_{stable}) |
| ------------------- | --------------: |
| Random Agent        |            0.00 |
| Shortest Path Agent |            0.08 |
| CGET Agent          |            0.49 |

---

# Expected Structural Ordering

The benchmark hypothesis predicts:

```
Random Agent
    |
    v
Shortest Path Agent
    |
    v
CGET Agent
```

because:

```text
Random Agent:
    explores futures

Shortest Path:
    selects trajectories

CGET:
    discovers reusable causal generators
    that expand future selection capacity
```

---

# Falsification Criteria

This benchmark would challenge CGET if:

1. Random agents consistently achieve equal steering bandwidth.
2. Memorized trajectories outperform causal representations under environment changes.
3. Causal compression provides no transfer advantage.
4. Identity-preserving self-modification does not improve long-horizon performance.

---

# Future Extensions

Planned benchmark additions:

* Dynamic maze environments
* Hidden rule discovery
* Changing reward functions
* Self-modifying policies
* Adversarial environments
* Multi-agent coordination
* Value drift experiments
* Viability kernel estimation

---

## Status

**Current state:**

Toy benchmark specification.

**Required next step:**

Run actual experiments and replace synthetic values with measured results.
