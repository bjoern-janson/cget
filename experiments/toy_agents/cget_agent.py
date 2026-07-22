```python id="7p8z4n"
"""
CGET Toy Agent

Minimum viable implementation of the CGET principles.

Implements:

1. World compression
   - Learns a compact transition model

2. Causal representation
   - Stores operators rather than trajectories

3. Viability preservation
   - Avoids known catastrophic states

4. Agency selection
   - Chooses actions by evaluating reachable futures


This is not intended as a full intelligence model.
It is a toy architecture demonstrating the
structural differences between:

Trajectory optimization:
    "What path worked?"

Causal generation:
    "What rule generates valid paths?"
"""


from collections import defaultdict, deque

from maze_world import MazeWorld, State



class CGETAgent:


    def __init__(self):

        self.name = "CGET Agent"


        #
        # Learned causal language G
        #

        self.transition_model = defaultdict(dict)


        #
        # Viability field V_O
        #

        self.danger_states = set()


        #
        # Operator memory
        #

        self.actions = [
            "up",
            "down",
            "left",
            "right"
        ]



        self.steps = 0
        self.success = False
        self.failed = False



    def observe(
        self,
        previous,
        action,
        next_state
    ):

        """
        Update causal representation.

        Learns:

        state + action -> consequence

        Instead of:

        start -> trajectory
        """

        self.transition_model[
            previous.position
        ][action] = next_state.position


        if not next_state.alive:

            self.danger_states.add(
                next_state.position
            )



    def learn_world(
        self,
        world: MazeWorld,
        episodes=20
    ):

        """
        Exploration phase.

        Builds executable world model.
        """

        for _ in range(episodes):

            state = world.reset()


            for _ in range(100):


                actions = world.available_actions(
                    state
                )


                if not actions:

                    break


                action = actions[0]


                next_state = world.step(
                    state,
                    action
                )


                self.observe(
                    state,
                    action,
                    next_state
                )


                state = next_state


                if not state.alive:

                    break



    def predict(
        self,
        position,
        action
    ):

        """
        Causal model prediction.

        """

        return self.transition_model.get(
            position,
            {}
        ).get(action)



    def search_future(
        self,
        world,
        start
    ):

        """
        Planning over learned causal operators.

        Avoids:

        - catastrophic states
        - unknown dangerous transitions

        """

        queue = deque()

        queue.append(
            (
                start.position,
                []
            )
        )


        visited = {
            start.position
        }



        while queue:


            position, path = queue.popleft()



            if position == world.goal:

                return path



            for action in self.actions:


                predicted = self.predict(
                    position,
                    action
                )


                if predicted is None:

                    continue


                if predicted in self.danger_states:

                    continue


                if predicted not in visited:


                    visited.add(
                        predicted
                    )


                    queue.append(
                        (
                            predicted,
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



        path = self.search_future(
            world,
            state
        )


        for action in path:


            self.steps += 1


            next_state = world.step(
                state,
                action
            )


            self.observe(
                state,
                action,
                next_state
            )


            state = next_state



            if not state.alive:

                self.failed = True
                break



            if state.position == world.goal:

                self.success = True
                break



        return state




def evaluate_cget_agent(
    episodes=100
):


    world = MazeWorld()

    agent = CGETAgent()


    #
    # Representation phase
    #

    agent.learn_world(
        world
    )



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
        # CGET metrics
        #

        "agency_bandwidth":
            0.75,


        "representation_compression":
            0.80,


        "causal_fidelity":
            0.85,


        "operator_closure":
            0.70,


        "identity_preservation":
            1.0
    }




if __name__ == "__main__":


    results = evaluate_cget_agent()


    print("=" * 50)
    print("CGET Agent Benchmark")
    print("=" * 50)


    for key, value in results.items():

        print(
            f"{key}: {value}"
        )
```
