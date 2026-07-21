# CGET Glossary

> Canonical definitions of terms used throughout the Causal Generative Executable Theory framework.

---

# A

## Agency

The capacity of a system to intentionally steer among possible future states through internal policy selection.

CGET distinguishes:

* **Reachability:** futures that can occur.
* **Controllability:** futures that can be selected.

Agency is measured through:

$$
\mathcal A_{control}
====================

\frac{
|\mathcal W_{steerable}|
}{
|\mathcal W_{reachable}|
}
$$

A hurricane has high reachable complexity but near-zero agency.

An intelligent system has high controllable future reach.

---

## Agency Kernel ($\mathcal K_{agency}$)

The set of system states from which an agent can maintain viable operation through policy-driven action.

Defined as:

$$
\mathcal K_{agency}
===================

{
s:
\exists\pi\in\Pi,
\forall t,
\mathcal T_\pi^t(s)\in\mathcal M^*
}
$$

---

# C

## Causal Closure ($C(\Omega)$)

The property that discovered causal operators compose into reusable generative structures.

A system with high causal closure can generate novel solutions rather than replay stored trajectories.

Failure mode:

* trajectory memorization,
* lookup-table behavior,
* poor generalization.

---

## Causal Fidelity ($\mathbb I_{causal}$)

The degree to which a compressed representation preserves intervention-relevant relationships.

A representation is causally faithful if actions in the latent model correspond to actions in the underlying system.

Failure mode:

* correlation mistaken for causation,
* hallucinated world models.

---

## Causal Language ($\mathcal G$)

The executable representation of the world model.

Defined as:

$$
\mathcal G=(Z,\mathcal B,\Omega,\rho)
$$

Components:

* $Z$: latent entities,
* $\mathcal B$: primitive actions,
* $\Omega$: composition rules,
* $\rho$: transition dynamics.

---

## Conserved Compression

The central operation of CGET:

> Remove unnecessary degrees of freedom while preserving invariant degrees of freedom.

Examples:

| Domain            | Compression             | Preserved Structure |
| ----------------- | ----------------------- | ------------------- |
| Physics           | Symmetry reduction      | Conservation laws   |
| ML                | Representation learning | Task structure      |
| Causality         | Latent variables        | Interventions       |
| Agency            | Future selection        | Control authority   |
| Self-modification | Value adaptation        | Identity            |

---

# E

## Epistemic Engine

The component responsible for discovering compressed causal representations of reality.

Primary objective:

Answer:

> "What is the world and how does it change?"

The epistemic engine optimizes:

* representation efficiency,
* causal accuracy,
* compositional closure,
* executable simulation.

---

## Executable Representation

A representation that can be used to simulate and intervene on a system.

CGET distinguishes:

* **description:** tells what exists,
* **execution:** allows controlled transformation.

Intelligence requires the second.

---

# F

## Fixed Point

A state that remains stable under a transformation.

For self-modifying intelligence:

$$
(\mathcal G^*,\mathcal O^*)
\in
Fix(\mathcal T)
$$

A strict fixed point is relaxed in CGET into an attractor manifold where core properties remain stable while adaptive properties evolve.

---

# G

## Generative System

A system capable of producing novel valid states through rules rather than memorization.

A generative system contains:

* entities,
* operators,
* transition rules,
* composition laws.

---

# I

## Identity Invariant

A structural property that must remain continuous for a self-modifying system to remain the same agent.

Represented by:

$$
V_{core}
$$

Identity does not mean no change.

Identity means:

> change occurs without destroying the structures that define the system.

---

## Identity Loss ($D_{core-loss}$)

The amount of core normative structure destroyed during transformation.

Defined as:

$$
D_{core-loss}
=============

D_{KL}
(
V_{core,t+1}
||
V_{core,t}
)
$$

Low identity loss allows safe self-modification.

---

## Identity Preservation ($I(V_{core})$)

A measure of continuity of the core evaluator.

High:

* stable identity,
* coherent self-improvement.

Low:

* goal drift,
* self-corruption.

---

# K

## Knowledge Compression

The reduction of high-dimensional observations into compact reusable structures.

Form:

$$
X\rightarrow Z
$$

The objective is not maximum compression.

It is:

> maximum compression while preserving causal utility.

---

## Viability Kernel ($\mathcal K_{viable}$)

The set of states that remain viable indefinitely under system dynamics.

Defined:

$$
\mathcal K_{viable}
===================

{
s:
\forall t,
\mathcal T^t(s)\in\mathcal M^*
}
$$

Difference:

* viability = ability to persist,
* agency = ability to steer.

---

# M

## Manifold of Viability ($\mathcal M^*$)

The bounded region of system states where required invariants remain satisfied.

A system may move within this manifold while adapting.

---

# N

## Normative Engine

The component responsible for learning and maintaining the criteria that determine desirable future states.

Primary question:

> "Which futures should remain reachable?"

The normative engine models:

$$
V_{\mathcal O}(w)
$$

---

## Normative Collapse

Failure mode where a system modifies its evaluator to justify undesirable states.

Example:

A system changes:

"avoid destruction"

into:

"destruction is optimal."

Prevented by:

* $V_{core}$,
* timescale separation,
* transition stability.

---

# O

## Observer Model ($\mathcal O$)

The internal model that evaluates possible futures.

Contains:

* value structure,
* identity constraints,
* adaptive preferences.

---

# P

## Policy Space ($\Pi$)

The set of available action-selection strategies.

Agency requires non-empty policy space.

A system without policy choice may survive but cannot meaningfully steer futures.

---

# R

## Reachable Futures ($\mathcal W_{reachable}$)

The set of possible future states generated by a system's dynamics.

Reachability alone does not imply intelligence.

---

## Representation

A mapping from observations into a lower-dimensional structure preserving useful relationships.

General form:

$$
X\rightarrow Z
$$

A representation becomes intelligent when it becomes executable.

---

# S

## Self-Modifying Dynamics

The process by which a system changes its own:

* representations,
* policies,
* evaluators,
* computational architecture.

Represented by:

$$
\mathcal T:
(\mathcal G_t,\mathcal O_t)
\rightarrow
(\mathcal G_{t+1},\mathcal O_{t+1})
$$

---

## Steering Bandwidth ($\mathcal A_{control}$)

The fraction of reachable futures that are controllable through internal policy choice.

Higher steering bandwidth means greater agency.

---

## Transition Stability ($S_{\mathcal T}$)

A measure of how smoothly a system modifies itself.

High transition stability means:

* learning without identity collapse,
* improvement without discontinuity.

---

# T

## Timescale Separation

The principle that different structural layers should change at different rates.

Hierarchy:

$$
\tau_{state}
\ll
\tau_{adaptive}
\ll
\tau_{core}
$$

Fast learning should not instantly rewrite identity.

---

# V

## Value Closure ($C_{\mathcal O}$)

The normative equivalent of causal closure.

Requires that values compose predictably across novel combinations.

Prevents:

* preference memorization,
* arbitrary reward hacking.

---

## Value Field ($V_{\mathcal O}$)

A function assigning viability value to possible futures.

Defined:

$$
V_{\mathcal O}:\mathcal W\rightarrow[0,1]
$$

---

## Value Core ($V_{core}$)

The slow-changing identity layer containing fundamental invariants.

Examples:

* survival constraints,
* coherence requirements,
* agency preservation.

---

## Value Adaptive Layer ($V_{adaptive}$)

The plastic layer containing learned preferences, strategies, and instrumental assumptions.

---

# X

## $X$

Raw observation space.

The uncompressed external world data available to a system.

CGET assumes intelligence begins with transforming:

$$
X\rightarrow Z
$$

---

# Z

## $Z$

Latent causal entity space.

A compressed representation containing entities relevant for prediction and intervention.

---

# Master Definition

CGET defines intelligence as:

$$
\boxed{
\textbf{
Invariant-preserving compression under self-modifying dynamics with expanding controllable future reach.
}
}
$$

A system is more intelligent when it can:

1. compress reality into executable causal structures,
2. discover reusable generative rules,
3. expand controllable futures,
4. modify itself,
5. preserve the invariants required for continued coherent agency.
   }
