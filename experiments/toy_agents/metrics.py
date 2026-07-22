```python
"""
CGET Metrics

Operational measurements for the toy benchmark.

Maps CGET concepts into measurable quantities:

Epistemic:
    - representation compression
    - causal fidelity
    - operator closure

Agency:
    - reachable future space
    - steerable future space
    - counterfactual steering bandwidth

Normative:
    - identity preservation
    - core drift

Transformation:
    - Theta* intelligence ratio


These are experimental proxies, not final definitions.
"""


import math



# ============================================================
# Epistemic Metrics
# ============================================================


def representation_compression(
    raw_states,
    latent_states
):
    """
    Measures reduction from observed state space
    to learned representation.

    Higher = more compression.

    CGET:

        X -> Z

    """

    if raw_states == 0:

        return 0.0


    return 1 - (
        latent_states / raw_states
    )




def causal_fidelity(
    correct_predictions,
    total_predictions
):
    """
    Measures whether the learned model
    preserves intervention outcomes.

    Proxy for:

        I_causal(G)

    """

    if total_predictions == 0:

        return 0.0


    return (
        correct_predictions /
        total_predictions
    )




def operator_closure(
    reusable_operations,
    total_operations
):
    """
    Measures whether learned operators
    generalize beyond memorized trajectories.

    Proxy for:

        C(Omega)

    """

    if total_operations == 0:

        return 0.0


    return (
        reusable_operations /
        total_operations
    )



# ============================================================
# Agency Metrics
# ============================================================



def reachable_future_complexity(
    reachable_states
):
    """
    Raw size of possible futures.

    Note:

    High value alone does not imply intelligence.

    Hurricanes have enormous future complexity.

    """

    return len(
        reachable_states
    )




def steerable_future_complexity(
    steerable_states
):
    """
    Futures controlled by policy choice.
    """

    return len(
        steerable_states
    )




def counterfactual_steering_bandwidth(
    steerable_states,
    reachable_states
):
    """
    A_control:

        controllable futures /
        possible futures

    """

    if len(reachable_states) == 0:

        return 0.0


    return (
        len(steerable_states) /
        len(reachable_states)
    )



# ============================================================
# Identity / Normative Metrics
# ============================================================



def core_identity_preservation(
    old_core,
    new_core
):
    """
    Proxy for:

        I(V_core)

    In a real implementation this would use
    KL divergence over viability distributions.

    """

    if old_core == new_core:

        return 1.0


    distance = abs(
        old_core - new_core
    )


    return math.exp(
        -distance
    )




def core_loss(
    old_core,
    new_core
):
    """
    Approximation of:

        D_KL(V_core,t+1 || V_core,t)

    """

    return abs(
        old_core - new_core
    )




def transition_stability(
    previous_update,
    current_update
):
    """
    Measures smoothness of self-modification.

    Proxy for:

        S_T

    """

    distance = abs(
        current_update -
        previous_update
    )


    return math.exp(
        -distance
    )



# ============================================================
# Composite CGET Metrics
# ============================================================



def agency_ratio(
    future_complexity,
    steering_bandwidth,
    identity_loss,
    tau=0.001
):
    """
    Theta*

    Intelligence as:

    controllable future expansion /
    identity destruction

    """

    return (
        future_complexity *
        steering_bandwidth
    ) / (
        identity_loss +
        tau
    )




def cget_score(
    epistemic_leverage,
    causal_fidelity_score,
    closure,
    viability,
    identity,
    transition
):
    """
    Simplified Psi_stable objective.

    """

    return (

        epistemic_leverage *

        causal_fidelity_score *

        closure *

        viability *

        identity *

        transition

    )



# ============================================================
# Benchmark Reporting
# ============================================================



def generate_report(
    agent_name,
    metrics
):
    """
    Standard benchmark output.
    """

    print("=" * 60)

    print(
        f"CGET Evaluation: {agent_name}"
    )

    print("=" * 60)



    for key, value in metrics.items():

        print(
            f"{key:35} {value:.4f}"
        )


    print("=" * 60)
```
