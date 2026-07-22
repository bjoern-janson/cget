```python
"""
CGET Toy Agent: Random Agent

Baseline agent.

Characteristics:

- No world model
- No representation learning
- No causal abstraction
- No planning
- No viability preservation

Purpose:

Establish the lower baseline for:

- agency bandwidth
- survival
- future reach
- transformation efficiency

"""

import random

from maze_world import MazeWorld, State


class RandomAgent:


    def __init__(self):

        self.name = "Random Agent"

        self.steps = 0
        self.success = False
        self.failed = False


    def choose_action(
        self,
        world: MazeWorld,
        state: State
    ):

        actions = world.available_actions(
            state
        )

        if not actions:

            return None

        return random.choice(actions)


    def run_episode(
        self,
        world: MazeWorld,
        max_steps=100
    ):

        state = world.reset()

        self.steps = 0
        self.success = False
        self.failed = False


        for _ in range(max_steps):

            self.steps += 1


            if not state.alive:

                self.failed = True
                break


            action = self.choose_action(
                world,
                state
            )


            if action is None:

                break


            state = world.step(
                state,
                action
            )


            if state.position == world.goal:

                self.success = True
                break


        if not state.alive:

            self.failed = True


        return state



def evaluate_random_agent(
    episodes=100
):

    world = MazeWorld()

    agent = RandomAgent()

    successes = 0
    failures = 0
    total_steps = 0


    for _ in range(episodes):

        final_state = agent.run_episode(
            world
        )

        total_steps += agent.steps


        if agent.success:

            successes += 1


        if agent.failed:

            failures += 1



    return {

        "agent":
            agent.name,

        "episodes":
            episodes,

        "success_rate":
            successes / episodes,

        "failure_rate":
            failures / episodes,

        "average_steps":
            total_steps / episodes,

        # CGET interpretation:

        # Random agent explores futures,
        # but does not intentionally select them.

        "agency_bandwidth":
            0.0,

        "representation_compression":
            0.0,

        "causal_fidelity":
            0.0
    }



if __name__ == "__main__":


    results = evaluate_random_agent()


    print("=" * 50)
    print("CGET Random Agent Benchmark")
    print("=" * 50)


    for key, value in results.items():

        print(
            f"{key}: {value}"
        )
```
