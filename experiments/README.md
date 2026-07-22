# CGET Experiments

## Purpose

The purpose of the CGET experimental program is to test whether the proposed principles of **invariant-preserving compression** correspond to measurable improvements in adaptive intelligence.

CGET predicts that intelligence is not equivalent to:

* raw prediction accuracy,
* search depth,
* reachable state-space size,
* or optimization performance alone.

Instead, intelligence emerges from the combination of:

1. **Compressed causal representations**
2. **Executable world models**
3. **Counterfactual steering capability**
4. **Compositional generalization**
5. **Identity-preserving adaptation**

The experiments are designed to separate these factors.

---

# Experimental Hypothesis

The central hypothesis:

> Systems that discover reusable causal structures should achieve greater controllable future reach than systems that rely on memorization, brute-force search, or fixed policies.

Formally:

[
\text{Intelligence} \propto
\frac{
\text{Reachable Future Complexity}
\times
\text{Counterfactual Steering Bandwidth}
}
{
\text{Identity Destruction}
}
]

---

# Experimental Philosophy

CGET experiments are designed around one principle:

> A representation is valuable if it allows a system to preserve invariants while expanding the set of futures it can intentionally select.

Therefore, experiments focus on transitions:

[
(\mathcal{G}*t,\mathcal{O}*t)
\rightarrow
(\mathcal{G}*{t+1},\mathcal{O}*{t+1})
]

rather than static benchmark scores.

---

# Benchmark Categories

## 1. Representation Compression

### Question

Can an agent discover compact structures that preserve future predictions and interventions?

### Test

Compare:

* raw state memorization
* learned latent representations
* causal operator representations

Measure:

[
\frac{
K(\mathcal{W}_{future})
}
{
K(\mathcal{G})
}
]

Expected result:

Causal representations should achieve greater future coverage per unit description complexity.

---

# 2. Causal Generalization

## Question

Does the agent learn mechanisms or only trajectories?

A system that memorizes:

```
State A → Action B
```

should fail when:

* objects are rearranged
* rules change
* environments are expanded

A causal system should preserve:

```
Operator X causes transformation Y
```

across contexts.

---

## Metrics

### Causal Fidelity

[
\mathbb{I}_{causal}(\mathcal{G})
]

Measures whether learned structures preserve intervention outcomes.

---

### Operator Closure

[
C(\Omega)
]

Measures whether learned operations compose into valid unseen combinations.

---

# 3. Counterfactual Steering Experiments

## Question

Does the system merely access possible futures, or can it intentionally select among them?

A hurricane has enormous reachable future complexity.

It does not have agency.

Therefore:

[
\mathcal{A}_{control}
=====================

\frac{
|\mathcal{W}*{steerable}|
}
{
|\mathcal{W}*{reachable}|
}
]

is measured.

---

Expected ordering:

```
Chaotic System

High reachable futures
Low steering bandwidth


Fixed Controller

Limited reachable futures
Moderate steering bandwidth


Adaptive Intelligence

High reachable futures
High steering bandwidth
```

---

# 4. Adaptation and Self-Modification

## Question

Can a system improve itself without destroying the invariants that define it?

The experiment separates:

## Valid Adaptation

[
\Delta V_{adaptive} \neq 0
]

while:

[
\Delta V_{core}=0
]

## Normative Collapse

[
\Delta V_{core}\neq0
]

where the system modifies its evaluator itself to avoid failure.

---

# 5. Viability Kernel Experiments

## Question

Does self-modification remain inside a stable region?

Define:

[
\mathcal{K}_{viable}
====================

{s|\forall t,\mathcal{T}^{t}(s)\in\mathcal{M}^{*}}
]

Test whether agents maintain:

* causal fidelity
* identity constraints
* transition stability

during learning.

---

# Toy Benchmark: MazeWorld

The first experimental environment is a minimal controlled world.

## Agents

### Random Agent

Purpose:

Establish lower bound.

Properties:

* no representation
* no planning
* no causal model

---

### Shortest Path Agent

Purpose:

Test optimization without representation learning.

Properties:

* strong local performance
* limited transfer
* no self-modification

---

### CGET Agent

Purpose:

Test causal compression.

Properties:

* learns reusable operators
* predicts transitions
* adapts representations
* preserves constraints

---

# Metrics Collected

Each experiment records:

| Metric                | Purpose                     |
| --------------------- | --------------------------- |
| Success Rate          | Task completion             |
| Future Complexity     | Raw reachable space         |
| Steering Bandwidth    | Policy control              |
| Causal Fidelity       | Intervention accuracy       |
| Operator Closure      | Generalization              |
| Identity Preservation | Core stability              |
| Transition Stability  | Safe adaptation             |
| (\Psi_{stable})       | Unified score               |
| (\Theta^*)            | Transformation intelligence |

---

# Falsification Criteria

CGET is weakened if experiments show:

## 1. No advantage from causal compression

If memorization performs equally well under distribution shift.

---

## 2. No agency distinction

If systems with zero steering capability score equal to intentional controllers.

---

## 3. No value stability benefit

If unconstrained self-modification improves indefinitely without identity drift.

---

## 4. Metrics are redundant

If all CGET terms collapse into existing measures such as reward optimization or prediction accuracy.

---

# Current Status

## Phase 1: Formalization

Completed:

* core primitives
* mathematical framework
* metrics
* toy agent architecture

---

## Phase 2: Toy Validation

In progress:

* MazeWorld benchmark
* baseline agents
* metric implementation

---

## Phase 3: Scaling

Future:

* complex environments
* multi-agent systems
* self-modifying agents
* long-horizon adaptation

---

# Guiding Principle

The experiments do not attempt to prove that CGET is the final theory of intelligence.

They test a narrower claim:

> Intelligence can be operationally studied as the expansion of controllable counterfactual reach through compressed executable representations while preserving the invariants required for coherent self-transformation.
