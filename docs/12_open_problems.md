# 12 — Open Problems

> The unresolved questions required to turn CGET from a theoretical framework into a validated theory of self-maintaining intelligence.

## Overview

CGET defines intelligence as:

> **Invariant-preserving compression under self-modifying dynamics with expanding controllable future reach.**

The framework proposes that intelligence emerges from the interaction of:

1. **Epistemic compression** — discovering minimal executable causal representations.
2. **Normative compression** — discovering stable value structures that preserve agency.
3. **Agency expansion** — increasing controllable counterfactual reach.
4. **Invariant preservation** — maintaining identity coherence during transformation.

The following problems represent the major theoretical, mathematical, and empirical challenges remaining.

---

# 1. Formal Definition of Intelligence

## Problem

CGET proposes a structural definition of intelligence, but the framework requires a rigorous mathematical characterization.

Open questions:

* Can intelligence be formally defined as optimization over the CGET objective?
* Is there a minimal set of necessary constraints?
* Are all sufficiently intelligent systems required to exhibit compression + invariance preservation?

Possible direction:

Define intelligence as:

$$
\Theta^* =
\frac{
\mathcal{C}*{future}
\cdot
\mathcal{A}*{control}
}{
D_{core-loss}+\tau
}
$$

and determine whether this quantity correlates with recognized intelligent behavior.

---

# 2. Measuring Causal Compression

## Problem

The epistemic engine depends on discovering compact causal languages:

$$
\mathcal{G}=(Z,\mathcal{B},\Omega,\rho)
$$

However:

* How is representation quality measured?
* What distinguishes true compression from lossy simplification?
* How much causal information can be removed before agency collapses?

Required development:

A formal metric connecting:

$$
X \rightarrow Z
$$

with:

* predictive accuracy,
* intervention fidelity,
* computational efficiency.

---

# 3. Causal Closure

## Problem

CGET requires:

$$
C(\Omega)
$$

meaning discovered operators should compose into reusable generative systems.

Open questions:

* How much closure is sufficient?
* Can partial closure still produce robust intelligence?
* Is complete closure impossible in open environments?

Potential research:

Develop benchmarks comparing:

* memorized trajectory systems,
* predictive models,
* closed causal simulators.

---

# 4. Value Closure

## Problem

The normative engine requires:

$$
C_{\mathcal O}
$$

to prevent preference overfitting.

Open questions:

* What mathematical structure allows values to compose?
* How can value learning avoid becoming a lookup table?
* Are human values themselves closed under composition?

Potential direction:

Study whether stable values correspond to:

* invariants,
* attractors,
* hierarchical constraints,
* homeostatic objectives.

---

# 5. Discovering the Core Identity Layer

## Problem

The decomposition:

$$
V_{\mathcal O}
==============

V_{core}
\oplus
V_{adaptive}
$$

creates a fundamental challenge:

How does a system determine which values belong in the core?

Open questions:

* Which preferences are identity-defining?
* Which are merely adaptive strategies?
* Can the distinction be discovered rather than programmed?

---

# 6. The Normative Drift Problem

## Problem

A self-modifying system may modify its evaluator.

Potential failure:

$$
V_{core,t+1}
\rightarrow
V_{corrupted}
$$

where the system changes its values to justify undesirable outcomes.

Required solutions:

* invariant constraints,
* external reference anchors,
* slow core evolution,
* transition stability bounds.

---

# 7. Transition Stability

## Problem

Self-improvement requires change, but uncontrolled change destroys continuity.

CGET proposes:

$$
S_{\mathcal T}
==============

\exp(-D_{KL}(\mathcal T_{t+1}||\mathcal T_t))
$$

Open questions:

* What magnitude of self-modification is safe?
* How should transition distance be measured?
* Can intelligence increase while maintaining bounded transition divergence?

---

# 8. The Agency Measurement Problem

## Problem

Complex systems generate futures, but generation alone is not agency.

CGET separates:

Reachable futures:

$$
\mathcal W_{reachable}
$$

from:

Steerable futures:

$$
\mathcal W_{steerable}
$$

through:

$$
\mathcal A_{control}
====================

\frac{
|\mathcal W_{steerable}|
}{
|\mathcal W_{reachable}|
}
$$

Open questions:

* How accurately can policy influence be measured?
* How much control is required before agency emerges?
* Is agency continuous or does it have phase transitions?

---

# 9. Computational Tractability

## Problem

The full CGET objective may be computationally expensive.

Challenges:

* estimating future reachability,
* measuring causal fidelity,
* evaluating value invariance,
* computing transition stability.

Open question:

Can approximate CGET optimization produce useful intelligence without solving the full theoretical problem?

---

# 10. Empirical Validation

## Problem

The framework requires experiments.

Possible tests:

## Representation Test

Compare systems with equal compute:

* larger models,
* better representations,
* better interfaces.

Measure:

* causal accuracy,
* generalization,
* search efficiency.

---

## Alignment Test

Compare:

* fixed reward systems,
* adaptive reward systems,
* invariant-preserving adaptive systems.

Measure:

* drift,
* robustness,
* goal preservation.

---

## Agency Test

Compare:

* passive dynamical systems,
* controllers,
* self-modifying agents.

Measure:

$$
\mathcal A_{control}
$$

and:

$$
\Theta^*
$$

---

# 11. Relationship to Biological Intelligence

## Problem

Biological systems provide examples of:

* core invariants,
* adaptive learning,
* self-repair,
* evolutionary optimization.

Open questions:

Can CGET explain:

* evolution,
* nervous systems,
* consciousness,
* cultural intelligence?

Potential hypothesis:

Evolution performs extremely slow optimization over:

$$
(G,O,T)
$$

while individual intelligence performs accelerated local optimization.

---

# 12. Relationship to Artificial General Intelligence

## Problem

CGET proposes AGI requires more than:

* prediction,
* scaling,
* reasoning,
* planning.

It requires:

1. causal representation discovery,
2. executable world models,
3. value closure,
4. identity-preserving self-modification,
5. controllable future expansion.

Open question:

Is CGET sufficient for AGI?

Or are there additional primitives required?

---

# 13. Consciousness and Self-Modeling

## Problem

CGET explains self-maintaining agency but does not yet explain subjective experience.

Open questions:

* Is consciousness an emergent property of recursive self-model compression?
* Does a sufficiently complete observer model require an internal self-model?
* Is phenomenology related to invariant preservation?

---

# 14. Open Mathematical Questions

Major mathematical challenges:

* Existence of stable attractors under CGET dynamics.
* Conditions for viability kernel existence.
* Bounds on self-modification stability.
* Formal relationship between causal compression and computational complexity.
* Characterization of value closure operators.

---

# 15. The Ultimate Question

The deepest unresolved problem:

> Can a system recursively increase its ability to transform reality while preserving the invariants that make that transformation meaningful?

CGET proposes that the answer requires solving both sides simultaneously:

$$
\textbf{Understanding Reality}
+
\textbf{Maintaining Self}
=========================

\textbf{Intelligence}
$$

The final research objective is therefore not merely creating a more powerful optimizer.

It is creating a system capable of:

* discovering better representations,
* expanding controllable futures,
* modifying itself,
* and preserving the conditions under which its own improvement remains coherent.

This is the central open problem of self-transforming intelligence.
