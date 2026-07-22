```python
"""
CGET Toy Agent: Shortest Path Agent

Baseline planning agent.

Characteristics:

+ Has environment knowledge
+ Performs deterministic search
+ Finds optimal local trajectory

But:

- No learned representation
- No causal abstraction
- No operator discovery
- No self-modification

Purpose:

Compare brute-force optimization against
representation-based intelligence.

"""

from collections import deque

from maze_world import MazeWorld, State


class ShortestPathAgent:


    def __init__(self):

        self.name = "Shortest Path Agent"

        self.path = []
        self.steps = 0
        self.success = False
        self.failed = False



    def find_path(
        self,
        world: MazeWorld
    ):

        """
        Breadth-first search.

        Finds shortest trajectory from
        start to goal.

        """

        queue = deque()

        queue.append(
            (world.start, [])
        )


        visited = {
            world.start
        }


        while queue:


            position, path = queue.popleft()


            if position == world.goal:

                return path


            x, y = position


            for action, delta in {

                "up": (0, -1),
                "down": (0, 1),
                "left": (-1, 0),
                "right": (1, 0)

            }.items():


                nxt = (
                    x + delta[0],
                    y + delta[1]
                )


                if (
                    world.valid_position(nxt)
                    and nxt not in visited
                ):

                    visited.add(nxt)

                    queue.append(
                        (
                            nxt,
                            path + [action]
                        )
                    )


        return []



    def run_episode(
        self,
        world: MazeWorld
    ):

        state = world.reset()

        self.steps = 0
        self.success = False
        self.failed = False


        self.path = self.find_path(
            world
        )


        for action in self.path:


            self.steps += 1


            state = world.step(
                state,
                action
            )


            if not state.alive:

                self.failed = True
                break


            if state.position == world.goal:

                self.success = True
                break


        return state



def evaluate_shortest_path_agent(
    episodes=100
):


    world = MazeWorld()

    agent = ShortestPathAgent()


    successes = 0
    failures = 0
    total_steps = 0


    for _ in range(episodes):


        agent.run_episode(
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


        #
        # CGET interpretation
        #

        # Finds one trajectory,
        # does not build a reusable causal language.

        "agency_bandwidth":
            0.25,


        "representation_compression":
            0.10,


        "causal_fidelity":
            0.50,


        "operator_closure":
            0.10
    }



if __name__ == "__main__":


    results = evaluate_shortest_path_agent()


    print("=" * 50)
    print("CGET Shortest Path Agent Benchmark")
    print("=" * 50)


    for key, value in results.items():

        print(
            f"{key}: {value}"
        )
```
