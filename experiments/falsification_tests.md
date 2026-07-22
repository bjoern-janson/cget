# CGET Falsification Tests

## Overview

A scientific framework must define conditions under which it would fail.

CGET proposes that intelligence emerges from the combination of:

1. **Executable causal compression**
2. **Invariant preservation**
3. **Composable representations**
4. **Controllable counterfactual reach**
5. **Stable self-modification**

The framework is falsified if these components are shown to be unnecessary, non-predictive, or incorrectly structured.

---

# 1. Causal Compression Falsification Test

## Hypothesis

Intelligent systems gain capability by discovering compact executable representations that preserve causal structure.

Formally:

\[
\mathcal{G}_{better} \rightarrow
\frac{K(W_{future})}{K(\mathcal{G})+K_{execution}}
\uparrow
\]

## Falsification Condition

CGET is weakened if:

- Large-scale intelligence improvements occur without improved causal compression.
- Systems with higher descriptive complexity consistently outperform compressed representations.
- Memorization dominates abstraction even in open-ended environments.

## Example Test

Compare:

- Lookup-table agent
- Compressed causal model agent

Under increasing environment complexity.

Prediction:

The causal model should dominate as:

\[
Complexity(environment) \rightarrow \infty
\]

---

# 2. Causal Closure Falsification Test

## Hypothesis

Generalization requires compositional operator closure.

\[
C(\Omega) \rightarrow Generalization
\]

## Falsification Condition

CGET fails if:

- Non-compositional systems generalize equally well.
- Memorized trajectory systems scale indefinitely without structural abstraction.
- Operator reuse provides no advantage.

## Example

Train agents on:

- Known trajectories
- Composable causal rules

Test on unseen combinations.

Prediction:

Composable systems should maintain performance.

---

# 3. Value Closure Falsification Test

## Hypothesis

Stable alignment requires compositional value representations.

\[
C_{\mathcal O}
\rightarrow
\text{generalizable values}
\]

## Falsification Condition

Alignment systems based entirely on:

- preference lookup
- reward memorization
- example imitation

should perform equally well under distribution shift.

If they do, value closure is unnecessary.

---

# 4. Identity Preservation Falsification Test

## Hypothesis

Safe self-modification requires preserving core invariants.

\[
D_{KL}(V_{core,t+1}||V_{core,t})
\leq \eta_{core}
\]

## Falsification Condition

A self-modifying system can achieve greater capability while freely rewriting its fundamental objectives without catastrophic failure.

If unrestricted goal drift consistently produces superior stable agents, the CGET constraint is incorrect.

---

# 5. Transition Stability Falsification Test

## Hypothesis

Stable intelligence requires bounded update transitions.

\[
S_{\mathcal T}
=
e^{-D_{KL}(\mathcal T_{t+1}||\mathcal T_t)}
\]

## Falsification Condition

Systems with large discontinuous internal transformations outperform gradually adapting systems while maintaining alignment.

---

# 6. Agency Kernel Falsification Test

## Hypothesis

Agency requires controllable counterfactual selection.

\[
\mathcal A_{control}
=
\frac{|W_{steerable}|}
{|W_{reachable}|}
\]

## Falsification Condition

A system with no meaningful policy influence over outcomes demonstrates equivalent intelligence to a system with high steering bandwidth.

Examples:

- Hurricane
- Crystal growth
- Autonomous planner

If raw complexity alone predicts intelligence, agency separation fails.

---

# 7. Compression vs Scaling Test

## Question

Can brute-force scaling replace representation discovery?

## Hypothesis

Eventually:

\[
\Delta Capability
\propto
\Delta Representation
>
\Delta Compute
\]

## Falsification Condition

Unlimited compute scaling produces arbitrary intelligence without improved representations.

---

# 8. Alignment Without Internal Models Test

## Hypothesis

External reward shaping is insufficient for robust alignment.

## Falsification Condition

A system with:

- no self-model
- no value representation
- no invariant preservation mechanism

achieves reliable alignment under all distribution shifts.

---

# 9. The Strongest Possible Falsifier

The strongest falsification of CGET would be:

> A system achieves superhuman intelligence and robust self-modification through pure optimization without discovering causal compression, without maintaining identity invariants, and without increasing controllable counterfactual reach.

Such a system would demonstrate that intelligence does not require the structures proposed by CGET.

---

# 10. Experimental Program

Future experiments should measure:

| Component | Metric |
|---|---|
| Representation quality | Compression ratio |
| Causal understanding | Intervention accuracy |
| Closure | Novel composition performance |
| Alignment stability | Core drift measurement |
| Agency | Counterfactual steering bandwidth |
| Self-modification safety | Transition divergence |
| Intelligence growth | Controlled future expansion |

---

# Conclusion

CGET is not validated because it explains intelligence elegantly.

It is validated only if systems built around:

- causal compression,
- invariant preservation,
- compositional closure,
- and controlled self-modification

outperform alternatives while surviving adversarial tests.

The framework's goal is not to prove that intelligence works this way.

The goal is to discover whether reality allows intelligence to exist any other way.
