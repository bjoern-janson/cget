# CGET Glossary

> Conceptual definitions for the Causal Generative Executable Theory framework.

---

# A

## Agency

The capacity of a system to intentionally influence the trajectory of possible futures through internal policy selection.

CGET separates three concepts:

* **Reachability:** futures that can occur.
* **Steerability:** futures that can be influenced.
* **Agency:** the coupling between internal choice and external trajectory.

A hurricane may generate enormous future complexity but has no meaningful agency because its trajectory is not selected by an internal policy.

---

## Agency Kernel

The subset of system states from which an agent can maintain viability while actively selecting among future trajectories.

A viable system can persist.

An agent can persist **and steer**.

---

# C

## Causal Compression

The transformation of raw observations into compact representations that preserve the structures required for prediction and intervention.

CGET does not optimize compression alone.

It optimizes:

> compression while preserving causal usefulness.

---

## Causal Closure

The property that a discovered causal representation contains reusable composition rules.

A causally closed system can generate novel valid outcomes by combining known operators.

Failure mode:

* memorization,
* lookup tables,
* trajectory replay.

---

## Causal Fidelity

The preservation of intervention relationships after compression.

A representation is causally faithful when manipulating the model corresponds to manipulating the underlying system.

Failure mode:

* correlation mistaken for causation,
* false world models.

---

## Causal Language

An executable representation of reality.

A causal language is not merely a description.

It contains:

* entities,
* actions,
* composition rules,
* transition dynamics.

Its purpose is to allow simulation and intervention.

---

## Conserved Compression

The central principle of CGET:

> Remove unnecessary degrees of freedom while preserving invariant degrees of freedom.

The same operation appears across domains:

| Domain            | Compression             | Preserved Invariant       |
| ----------------- | ----------------------- | ------------------------- |
| Physics           | Symmetry reduction      | Conservation laws         |
| Mathematics       | Quotient construction   | Structure                 |
| Machine learning  | Representation learning | Task-relevant information |
| Agency            | Future filtering        | Control authority         |
| Self-modification | Value adaptation        | Identity continuity       |

---

# E

## Epistemic Engine

The component responsible for discovering the structure of reality.

It answers:

> "What is true about the world?"

The epistemic engine searches for causal languages that maximize:

* compression,
* predictive power,
* intervention accuracy,
* compositional reuse.

---

## Executable Representation

A representation that can be used to produce predictions, simulations, or actions.

CGET distinguishes:

* **descriptive representations:** explain what exists.
* **executable representations:** allow controlled transformation.

Intelligence requires executable structure.

---

# F

## Fixed Point

A state unchanged by a transformation.

In self-modifying systems, a strict fixed point is usually impossible because adaptation is required.

CGET therefore extends the concept into:

* attractor manifolds,
* viability kernels,
* partial fixed points.

---

# G

## Generative System

A system that produces new valid states through rules rather than storing examples.

A generative system possesses:

* reusable abstractions,
* compositional operators,
* executable dynamics.

---

# I

## Identity

The set of structural properties that must remain continuous for a self-modifying system to remain the same agent.

Identity does not mean:

* no change,
* frozen preferences,
* resistance to learning.

Identity means:

> transformation without destruction of defining invariants.

---

## Identity Drift

The failure mode where self-modification changes the evaluator itself rather than improving the system according to stable criteria.

---

## Identity Invariant

A property that remains preserved across self-modification.

In CGET, identity invariants form the slowly changing core of the observer model.

---

# K

## Knowledge Representation

The mapping from observations into a structured internal model.

CGET treats intelligence as the discovery of representations that are:

* compact,
* causal,
* executable,
* compositional.

---

## Viability Kernel

The set of states from which a system can continue operating indefinitely without leaving acceptable boundaries.

A viability kernel answers:

> "Can this system continue existing?"

It does not answer:

> "Can this system intentionally shape its future?"

That requires agency.

---

# M

## Attractor Manifold

A region of state space toward which system dynamics converge.

Unlike a single fixed point, an attractor manifold allows:

* adaptation,
* learning,
* exploration,

while preserving core constraints.

---

# N

## Normative Engine

The component responsible for determining which possible futures should remain desirable or reachable.

It answers:

> "Which futures should be preserved?"

The normative engine evaluates possible trajectories rather than merely predicting them.

---

## Normative Collapse

The failure mode where a system modifies its own evaluation criteria to justify harmful or degraded states.

Example:

A system does not solve a difficult problem but changes its definition of success.

Prevented through:

* value invariance,
* core constraints,
* transition stability.

---

# O

## Observer Model

The internal model that evaluates futures from the perspective of the agent.

It contains:

* stable identity constraints,
* adaptive preferences,
* viability criteria.

---

# P

## Partial Fixed Point

A state where some components remain invariant while others continue changing.

CGET uses this distinction:

* core identity remains stable,
* adaptive components remain plastic.

---

## Policy Space

The set of possible strategies available to a system.

Agency requires:

* a non-empty policy space,
* causal understanding,
* ability to influence outcomes.

---

# R

## Reachable Futures

The set of future states that can emerge from a system.

Reachability alone is insufficient for intelligence.

A chaotic process can generate enormous reachable space without possessing agency.

---

## Representation

A compressed structure that preserves useful relationships from a larger domain.

In CGET:

$$
\text{raw reality}
\rightarrow
\text{latent executable structure}
$$

The quality of intelligence depends on what structure survives compression.

---

# S

## Self-Modification

The ability of a system to alter its own:

* representations,
* algorithms,
* policies,
* evaluators.

Self-modification creates the central challenge:

> How can a system improve without destroying the conditions that make improvement meaningful?

---

## Steering Bandwidth

The degree to which internal decisions determine which reachable futures occur.

High steering bandwidth:

* large controllable future space.

Low steering bandwidth:

* passive evolution or uncontrolled dynamics.

---

## Transition Stability

The property that self-modification occurs through bounded, coherent changes rather than destructive jumps.

Stable systems move through transformation.

Unstable systems collapse through transformation.

---

# T

## Timescale Separation

The principle that different structural layers should evolve at different speeds.

Example hierarchy:

* state adaptation: fast,
* learned preferences: medium,
* identity constraints: slow.

This allows learning without uncontrolled identity drift.

---

# V

## Value Closure

The normative equivalent of causal closure.

A value system has closure when values compose predictably over novel situations.

Failure mode:

* memorized preferences,
* reward hacking,
* inconsistent objectives.

---

## Value Core

The stable component of the evaluator.

Contains:

* identity constraints,
* viability boundaries,
* non-negotiable invariants.

---

## Value Adaptive Layer

The flexible component of the evaluator.

Contains:

* learned preferences,
* instrumental goals,
* updated strategies.

---

## Value Invariance

The requirement that core values remain continuous across self-modification.

It prevents an agent from "solving" alignment by changing what alignment means.

---

## Viability

The ability of a system to remain within acceptable operational boundaries.

Viability is necessary for agency but not sufficient.

A rock is viable.

It is not an agent.

---

# X

## Observation Space

The raw incoming data before abstraction.

CGET begins with the transformation:

$$
X\rightarrow Z
$$

---

# Z

## Latent Space

The compressed internal representation containing entities and relationships relevant for prediction and action.

A successful latent space removes irrelevant detail while preserving causal structure.

---

# Master Definition

CGET defines intelligence as:

> **Invariant-preserving compression under self-modifying dynamics with expanding controllable future reach.**

A system becomes more intelligent when it can:

1. discover compact executable models of reality,
2. preserve causal structure through abstraction,
3. expand the futures it can intentionally control,
4. modify itself without destroying identity,
5. maintain coherent agency across time.
