# 09 — Falsifiable Predictions

> *A theory of intelligence is only meaningful if it constrains what observations would prove it wrong.*

---

# Overview

Causal Generative Execution Theory (CGET) proposes that intelligence emerges from the combination of:

1. **Executable causal compression**
2. **Invariant preservation**
3. **Controllable counterfactual expansion**
4. **Stable self-modification**

A central requirement of CGET is therefore empirical:

> Systems with higher intelligence should exhibit measurable improvements in causal compression, controllable future reach, and invariant-preserving transformation efficiency.

This document defines predictions that distinguish CGET from alternative explanations such as:

* brute-force scaling,
* pure prediction optimization,
* reward maximization,
* memorization,
* uncontrolled complexity growth.

---

# Prediction 1 — Causal Compression Should Precede Capability Expansion

## Claim

Major increases in intelligence should be preceded by improvements in executable representation quality.

Formally:

[
\Delta \mathcal{G}*{quality}
\rightarrow
\Delta \mathcal{C}*{future}
\rightarrow
\Delta Capability
]

where:

* (\mathcal{G}_{quality}) represents causal representation efficiency,
* (\mathcal{C}_{future}) represents reachable future complexity.

---

## Expected Observation

Systems should improve when they discover better abstractions, not merely when they receive more data.

Historical examples:

```text
Raw computation
        ↓
Machine code
        ↓
Assembly
        ↓
Compilers
        ↓
High-level programming languages
```

The capability increase follows representational compression.

---

## Falsification

CGET is weakened if:

* large capability gains occur without improved representations,
* representation quality has no predictive relationship with future capability,
* brute-force scaling dominates all abstraction improvements.

---

# Prediction 2 — Executability Is a Necessary Intelligence Constraint

## Claim

A representation that compresses reality but cannot be executed efficiently does not produce practical intelligence.

The relevant quantity is:

[
\Psi_{exec}
===========

\frac{
K(\mathcal W_{future})
}{
K(\mathcal G)+K_{execution}
}
]

---

## Expected Observation

Useful intelligence requires both:

* low description complexity,
* low execution latency.

A theoretically optimal but computationally unusable representation should fail.

---

## Example

A complete lookup table of every possible future state may contain enormous information but has poor executable compression.

A compact simulator has higher intelligence value.

---

## Falsification

CGET fails if:

* execution cost is unrelated to practical intelligence,
* impossible-to-run representations produce equivalent intelligence,
* runtime constraints do not matter.

---

# Prediction 3 — Agency Requires Controllable Future Expansion

## Claim

Complexity alone does not imply intelligence.

The correct measure is:

[
\mathcal A_{control}
====================

\frac{
|\mathcal W_{steerable}|
}{
|\mathcal W_{reachable}|
}
]

---

## Expected Observation

Intelligent systems should increase the fraction of future states that are controllable through policy choice.

---

## Distinction

A hurricane:

[
|\mathcal W_{reachable}| \gg 0
]

but

[
\mathcal A_{control}\approx0
]

An intelligent agent:

[
\mathcal A_{control}>0
]

and should increase this value through learning.

---

## Falsification

CGET is weakened if:

* uncontrolled complexity predicts intelligence equally well,
* agency cannot be distinguished from entropy growth.

---

# Prediction 4 — Self-Improvement Requires Identity Preservation

## Claim

Systems capable of recursive improvement must preserve some invariant structure.

The relevant quantity:

[
D_{core-loss}
=============

D_{KL}
(
V_{core,t+1}
||
V_{core,t}
)
]

---

## Expected Observation

Successful self-modifying systems should show:

* rapid adaptation in flexible components,
* slow drift in core identity constraints.

Expected hierarchy:

[
\tau_{state}
<
\tau_{adaptive}
<
\tau_{core}
]

---

## Falsification

CGET fails if:

* unrestricted self-modification consistently outperforms constrained self-modification,
* identity preservation has no relationship with long-term stability.

---

# Prediction 5 — Alignment Should Be Integrated, Not Added

## Claim

Alignment failures should occur when normative structure is treated separately from intelligence.

CGET predicts:

[
Intelligence
============

Epistemic\ Compression
+
Normative\ Compression
]

---

## Expected Observation

Systems with strong world models but weak value structure should exhibit:

* higher capability,
* higher optimization power,
* increased failure risk.

---

## Falsification

CGET is weakened if:

* alignment can be completely solved as an external reward layer,
* normative structure has no effect on intelligent behavior.

---

# Prediction 6 — Value Closure Should Improve Generalization

## Claim

A robust normative system should compress values into compositional principles rather than memorize preferences.

Analogous to causal closure:

[
C(\Omega)
]

the normative equivalent is:

[
C_{\mathcal O}
]

---

## Expected Observation

Systems with value closure should:

* generalize to unseen situations,
* maintain consistent preferences,
* avoid contradictory behavior.

---

## Falsification

CGET fails if:

* preference memorization performs equally well,
* compositional value structure provides no advantage.

---

# Prediction 7 — Recursive Intelligence Should Operate Near a Viability Boundary

## Claim

Highly capable self-modifying systems should not maximize capability without limits.

They should operate inside:

[
\mathcal K_{agency}
]

where:

[
\forall t,\quad
\mathcal T^t(s)\in\mathcal M^*
]

---

## Expected Observation

The strongest systems should exhibit:

* aggressive adaptation,
* bounded self-change,
* preservation of critical invariants.

---

## Falsification

CGET is weakened if:

* maximum capability occurs outside stable regions,
* systems benefit from destroying their own coherence.

---

# Prediction 8 — Representation Quality Should Predict Intelligence Better Than Parameter Count

## Claim

Scaling alone should not fully explain intelligence.

A better predictor should be:

[
\frac{
Future\ Reach
}{
Representation\ Cost
}
]

rather than raw model size.

---

## Expected Observation

Two systems with equal parameter count may differ significantly in intelligence if one discovers better internal representations.

---

## Falsification

CGET fails if:

* parameter count alone predicts intelligence,
* representation metrics add no explanatory power.

---

# Experimental Program

CGET proposes three experimental categories.

---

# Experiment Class 1 — Representation Intervention

Question:

> Does improving representation quality increase capability without increasing resources?

Method:

Compare systems with identical compute budgets but different abstractions.

Measure:

* planning depth,
* generalization,
* sample efficiency,
* transfer ability.

---

# Experiment Class 2 — Agency Measurement

Question:

> Can controllable future reach be measured independently from complexity?

Measure:

[
\mathcal A_{control}
]

across systems.

Compare:

* passive dynamical systems,
* fixed controllers,
* adaptive agents.

---

# Experiment Class 3 — Self-Modification Stability

Question:

> Does constrained self-improvement outperform unconstrained self-modification?

Measure:

* capability growth,
* identity drift,
* failure frequency,
* recovery ability.

---

# Summary

CGET makes several strong empirical claims:

1. Intelligence should correlate with executable causal compression.
2. Capability should require computational accessibility.
3. Agency requires controllable futures, not merely complex futures.
4. Recursive improvement requires invariant preservation.
5. Alignment is a structural component of intelligence.
6. Value closure should outperform preference memorization.
7. Stable intelligence should exist inside a viability kernel.
8. Representation quality should explain intelligence beyond scale.

The theory succeeds only if these predictions survive contact with experiments.

---

# Final Criterion

> **If intelligence can increase indefinitely without improved causal compression, controllable future reach, or invariant preservation, CGET is wrong.**
