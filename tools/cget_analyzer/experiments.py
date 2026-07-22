from cget_metrics import *
from toy_agents import *


def evaluate(agent):

    return {
        "name":
            agent.name,

        "compression":
            compression_score(
                agent.raw_complexity,
                agent.latent_complexity
            ),

        "causal":
            causal_fidelity(
                agent.interventions_correct,
                agent.interventions_total
            ),

        "closure":
            closure_score(
                agent.compositions_successful,
                agent.compositions_attempted
            ),

        "agency":
            agency_bandwidth(
                agent.steerable,
                agent.reachable
            ),

        "identity":
            identity_preservation(
                agent.identity_change
            ),

        "theta":
            theta_star(
                agent.reachable,
                agency_bandwidth(
                    agent.steerable,
                    agent.reachable
                ),
                agent.identity_change
            )
    }


def run():

    agents = [
        LookupAgent(),
        CausalAgent(),
        SelfModifyingAgent()
    ]

    for agent in agents:

        print("\n", evaluate(agent))


if __name__ == "__main__":
    run()
