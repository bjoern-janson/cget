# CGET Assumptions

> Foundational assumptions required for the Causal Generative Executable Theory framework.

CGET does not attempt to begin from an assumption-free foundation. Instead, it makes its assumptions explicit and treats them as potential points of empirical validation or falsification.

The framework's goal is not to define intelligence by arbitrary criteria, but to identify structural conditions that appear necessary for increasingly capable self-modifying systems.

---

# 1. Reality Contains Compressible Structure

## Assumption

The external world contains regularities that can be represented more efficiently than raw observation history.

Formally:

$$
K(\mathcal{G}) < K(X)
$$

where:

* $X$ represents raw observations,
* $\mathcal{G}$ represents a structured causal representation.

## Implication

If reality were fundamentally incompressible, intelligence could only memorize observations rather than discover generalizable structure.

Science, mathematics, and machine learning all rely on this assumption.

## Failure Case

A maximally random universe with no exploitable regularity would eliminate the possibility of meaningful causal modeling.

---

# 2. Useful Intelligence Requires Causal Structure

## Assumption

Prediction alone is insufficient for robust intelligence.

A capable system must preserve relationships that survive intervention.

$$
P(Y|\text{do}(X))
\neq
P(Y|X)
$$

in general.

## Implication

An intelligent representation must capture:

* what changes outcomes,
* what can be controlled,
* what remains invariant.

## Failure Case

A system that only models correlations may perform well under familiar distributions while failing under intervention or distribution shift.

---

# 3. Representations Are Computational Objects

## Assumption

A representation is not merely a passive description.

A sufficiently powerful representation functions as an executable computational substrate.

## Implication

Changing representation can change the effective computational capability of a system.

Examples:

* equations replacing tables,
* compilers replacing manual machine instructions,
* automatic differentiation replacing symbolic derivative derivation,
* abstractions replacing exhaustive search.

## Failure Case

If representations only encode information but cannot alter computation, intelligence reduces to storage and retrieval.

---

# 4. Intelligence Requires Compression Under Constraints

## Assumption

The goal of intelligence is not maximum compression alone.

The optimal representation balances:

* simplicity,
* causal fidelity,
* execution efficiency,
* generative capacity.

A representation that compresses everything into an unusable abstraction is not intelligent.

## Implication

CGET rejects:

* pure memorization,
* infinitely complex world models,
* abstractions with no executable value.

---

# 5. Generalization Requires Compositional Closure

## Assumption

Robust intelligence requires the ability to create novel valid combinations from learned primitives.

A system must discover reusable operators:

$$
\Omega:B\times B\rightarrow B
$$

## Implication

Generalization comes from discovering structure, not merely increasing interpolation capacity.

## Failure Case

A lookup table may perfectly reproduce previous examples while lacking genuine understanding.

---

# 6. Agents Exist Within Viability Constraints

## Assumption

Any persistent agent operates within boundaries imposed by:

* physics,
* resources,
* environment,
* internal stability.

An agent cannot optimize futures indefinitely while violating the conditions required for its continued existence.

## Implication

Alignment is not an external addition.

It emerges from maintaining viable trajectories.

---

# 7. Self-Modification Creates a New Optimization Problem

## Assumption

A system capable of improving itself must also preserve the conditions that define improvement.

The system modifies:

* its world model,
* its policies,
* its preferences,
* potentially its evaluator.

Therefore:

the optimizer becomes part of the optimization target.

## Implication

Self-modifying intelligence requires constraints on transformation itself.

---

# 8. Identity Has Structural Invariants

## Assumption

A self-modifying system requires some persistent structure to remain a coherent agent.

Identity is not equivalent to immutability.

Instead:

$$
\text{Identity}
===============

\text{Preserved Invariants}
+
\text{Adaptive Change}
$$

## Implication

The system must distinguish:

* learning,
* correction,
* improvement,

from:

* evaluator corruption,
* goal drift,
* identity destruction.

---

# 9. Core and Adaptive Components Must Evolve at Different Rates

## Assumption

Stable self-improvement requires timescale separation.

$$
\eta_{core}\ll\eta_{adaptive}
$$

Meaning:

* adaptive representations may change quickly,
* core invariants change slowly.

## Implication

A fully frozen evaluator cannot learn.

A fully plastic evaluator cannot preserve identity.

---

# 10. Agency Requires Control Over Futures

## Assumption

Future complexity alone does not imply intelligence.

A system must influence which futures occur.

Therefore:

$$
\text{Agency}
\neq
\text{Reachability}
$$

Agency requires coupling between:

* internal policy,
* external trajectory.

## Implication

A hurricane has complexity.

An agent has directed control.

---

# 11. Alignment Is Internal to Intelligence

## Assumption

A sufficiently advanced intelligence cannot treat alignment as an external safety layer.

The system must internally represent:

* what futures are desirable,
* what boundaries must remain preserved,
* how self-modification should occur.

## Implication

The normative engine is the internal counterpart of the epistemic engine.

Reality modeling and value modeling are dual compression processes.

---

# 12. Future Space Is Structured

## Assumption

The space of possible futures is not an undifferentiated set.

Futures contain:

* causal dependencies,
* constraints,
* opportunities,
* tradeoffs.

## Implication

Intelligence expands future reach by discovering the structure of possible transformations.

---

# 13. Computational Resources Are Transformable

## Assumption

Effective compute is not only determined by hardware.

Algorithmic and representational changes can increase usable computational capability.

## Implication

A better representation can function as a form of acquired compute.

This motivates the informal interpretation:

> CGET = "get compute."

---

# 14. Intelligence Is a Dynamical Property

## Assumption

Intelligence is not a static property of a model.

It emerges from the interaction:

$$
(\mathcal{G}*t,\mathcal{O}*t)
\rightarrow
(\mathcal{G}*{t+1},\mathcal{O}*{t+1})
$$

over time.

## Implication

The relevant object is not only the agent state, but the transformation process.

---

# 15. The Framework Is Empirically Falsifiable

## Assumption

The proposed structure should make predictions that could fail.

CGET should be rejected or modified if:

* major intelligence gains occur without improved compression,
* causal structure is unnecessary for robust generalization,
* self-modification does not require identity preservation,
* agency does not correlate with controllable future selection,
* representation changes fail to produce computational leverage.

---

# Summary

The core assumptions of CGET can be compressed into five primitives:

## 1. Compression

Useful intelligence discovers lower-complexity representations.

## 2. Causality

Useful representations preserve intervention structure.

## 3. Execution

Useful representations increase computational reach.

## 4. Agency

Useful systems control selected futures.

## 5. Invariance

Useful self-modification preserves the structures that make future improvement meaningful.

Final assumption:

> **Intelligence is possible because reality contains compressible structure, and advanced intelligence emerges when a system learns to compress both the world and itself while preserving the invariants required for continued transformation.**
