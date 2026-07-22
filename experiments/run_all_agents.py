```python
"""
CGET Benchmark Runner

Runs all toy agents on identical environments
and evaluates them using CGET metrics.

Pipeline:

Environment
      |
      v
Agent Policy
      |
      v
Trajectory
      |
      v
CGET Metrics
      |
      v
Comparison Report


This is a toy validation framework,
not a claim of measuring general intelligence.
"""


from maze_world import MazeWorld

from random_agent import RandomAgent
from shortest_path_agent import ShortestPathAgent
from cget_agent import CGETAgent

from metrics import (
    reachable_future_complexity,
    counterfactual_steering_bandwidth,
    agency_ratio,
    core_identity_preservation,
    transition_stability,
    cget_score,
    generate_report
)



# ============================================================
# Experiment Configuration
# ============================================================


GRID_SIZE = 10
MAX_STEPS = 100

SEEDS = [
    1,
    2,
    3,
    4,
    5
]



# ============================================================
# Evaluation Helpers
# ============================================================


def evaluate_agent(
    agent,
    seed
):

    env = MazeWorld(
        size=GRID_SIZE,
        seed=seed
    )


    trajectory = []


    state = env.reset()


    done = False


    while not done:

        action = agent.act(
            state,
            env
        )

        state, reward, done = env.step(
            action
        )

        trajectory.append(
            state
        )



    return {

        "trajectory": trajectory,

        "success":
            reward > 0

    }




def estimate_reachable_space(
    env
):
    """
    Approximate future state space.

    Small exhaustive search for toy worlds.
    """

    return env.enumerate_future_states()




def estimate_steerable_space(
    agent,
    env
):
    """
    Approximate states reachable through
    deliberate policy selection.

    """

    return agent.enumerate_controlled_states(
        env
    )



# ============================================================
# CGET Evaluation
# ============================================================


def evaluate_cget(
    agent,
    seed
):

    env = MazeWorld(
        size=GRID_SIZE,
        seed=seed
    )


    result = evaluate_agent(
        agent,
        seed
    )


    reachable = (
        estimate_reachable_space(
            env
        )
    )


    steerable = (
        estimate_steerable_space(
            agent,
            env
        )
    )


    bandwidth = (
        counterfactual_steering_bandwidth(
            steerable,
            reachable
        )
    )


    future_complexity = (
        reachable_future_complexity(
            reachable
        )
    )


    identity = (
        core_identity_preservation(
            1.0,
            1.0
        )
    )


    transition = (
        transition_stability(
            0.1,
            0.1
        )
    )


    theta = (
        agency_ratio(
            future_complexity,
            bandwidth,
            0.001
        )
    )


    score = (
        cget_score(
            epistemic_leverage=1.0,
            causal_fidelity_score=(
                1.0 if result["success"]
                else 0.0
            ),
            closure=bandwidth,
            viability=(
                1.0 if result["success"]
                else 0.5
            ),
            identity=identity,
            transition=transition
        )
    )


    return {

        "success":
            result["success"],

        "future_complexity":
            future_complexity,

        "steering_bandwidth":
            bandwidth,

        "Theta_star":
            theta,

        "Psi_stable":
            score

    }



# ============================================================
# Main Benchmark
# ============================================================


def run_agent(
    name,
    agent
):

    results = []


    for seed in SEEDS:

        metrics = evaluate_cget(
            agent,
            seed
        )

        results.append(
            metrics
        )


    average = {}


    keys = results[0].keys()


    for key in keys:

        average[key] = (
            sum(
                r[key]
                for r in results
            )
            /
            len(results)
        )


    generate_report(
        name,
        average
    )


    return average




def main():

    agents = {

        "Random Agent":
            RandomAgent(),

        "Shortest Path Agent":
            ShortestPathAgent(),

        "CGET Agent":
            CGETAgent()

    }


    all_results = {}


    for name, agent in agents.items():

        all_results[name] = run_agent(
            name,
            agent
        )


    print("\nFINAL CGET COMPARISON\n")


    for name, result in all_results.items():

        print(
            name,
            "=>",
            round(
                result["Psi_stable"],
                4
            )
        )



if __name__ == "__main__":

    main()
```
