"""
CGET Core Metrics

Toy implementations of:
- compression
- causal fidelity
- closure
- agency bandwidth
- identity preservation
- transition stability
"""

import math


def compression_score(raw_complexity, latent_complexity):
    """
    Measures reduction in representation complexity.
    """
    if raw_complexity == 0:
        return 0

    return max(
        0,
        (raw_complexity - latent_complexity) / raw_complexity
    )


def causal_fidelity(intervention_success, total_interventions):
    """
    Fraction of interventions correctly predicted.
    """

    if total_interventions == 0:
        return 0

    return intervention_success / total_interventions


def closure_score(successful_compositions, attempted_compositions):
    """
    Measures whether learned operators compose.
    """

    if attempted_compositions == 0:
        return 0

    return successful_compositions / attempted_compositions


def agency_bandwidth(steerable_futures, reachable_futures):
    """
    A_control = W_steerable / W_reachable
    """

    if reachable_futures == 0:
        return 0

    return steerable_futures / reachable_futures


def identity_preservation(core_change):
    """
    Simplified:

    I(V_core)=exp(-D_KL)

    """

    return math.exp(-core_change)


def transition_stability(operator_change):
    """
    S_T = exp(-D_KL(T_next||T))
    """

    return math.exp(-operator_change)


def theta_star(
    future_complexity,
    agency,
    identity_loss,
    epsilon=1e-9
):
    """
    Final transformation efficiency:

    controllable future expansion /
    identity destruction
    """

    return (
        future_complexity * agency
    ) / (
        identity_loss + epsilon
    )
