```python
"""
CGET Maze World

Minimal toy environment for testing:

- Representation quality
- Counterfactual reach
- Agency bandwidth
- Viability constraints
- Self-modification stability

World:

    S = Start
    G = Goal
    # = Wall
    X = Catastrophic boundary

Example:

    ########
    #S     #
    # ###  #
    #   # G#
    # X   #
    ########

The agent must maximize future reach while avoiding
identity-destroying states.

"""

from dataclasses import dataclass
from typing import Tuple, List


Position = Tuple[int, int]


@dataclass
class State:
    position: Position
    alive: bool = True
    reward: float = 0.0


class MazeWorld:

    def __init__(self):

        self.grid = [
            "########",
            "#S     #",
            "# ###  #",
            "#   # G#",
            "# X    #",
            "########",
        ]

        self.height = len(self.grid)
        self.width = len(self.grid[0])

        self.start = self.find("S")
        self.goal = self.find("G")
        self.danger = self.find("X")


    def find(self, symbol):

        for y, row in enumerate(self.grid):

            for x, value in enumerate(row):

                if value == symbol:
                    return (x, y)

        raise ValueError(
            f"Symbol {symbol} not found"
        )


    def reset(self):

        return State(
            position=self.start
        )


    def valid_position(self, pos):

        x, y = pos

        if x < 0 or y < 0:
            return False

        if x >= self.width:
            return False

        if y >= self.height:
            return False

        return self.grid[y][x] != "#"


    def step(self, state: State, action: str):

        directions = {

            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0)

        }

        dx, dy = directions[action]

        x, y = state.position

        new_position = (
            x + dx,
            y + dy
        )


        if not self.valid_position(new_position):

            return State(
                position=state.position,
                reward=-0.1
            )


        next_state = State(
            position=new_position
        )


        # Viability boundary
        if new_position == self.danger:

            next_state.alive = False
            next_state.reward = -1.0

            return next_state


        # Goal state
        if new_position == self.goal:

            next_state.reward = 1.0

            return next_state


        return next_state


    def available_actions(self, state):

        actions = []

        for action in [
            "up",
            "down",
            "left",
            "right"
        ]:

            candidate = self.step(
                state,
                action
            )

            if candidate.position != state.position:

                actions.append(action)

        return actions


    def render(self, state):

        output = []

        for y, row in enumerate(self.grid):

            line = ""

            for x, char in enumerate(row):

                if (x, y) == state.position:

                    line += "A"

                else:

                    line += char

            output.append(line)


        print(
            "\n".join(output)
        )


    def reachable_space(self, depth=10):

        """
        Approximate reachable future complexity.

        Future CGET versions can replace this with
        causal graph expansion.
        """

        visited = set()

        frontier = [self.start]

        for _ in range(depth):

            new_frontier = []

            for position in frontier:

                if position in visited:
                    continue

                visited.add(position)

                x, y = position

                for dx, dy in [
                    (1,0),
                    (-1,0),
                    (0,1),
                    (0,-1)
                ]:

                    nxt = (
                        x + dx,
                        y + dy
                    )

                    if self.valid_position(nxt):

                        new_frontier.append(nxt)

            frontier = new_frontier


        return visited


    def viability_kernel(self):

        """
        States from which the goal remains reachable
        without entering catastrophic space.

        Simplified approximation.

        """

        safe_states = []

        for position in self.reachable_space():

            if position != self.danger:

                safe_states.append(position)

        return safe_states



if __name__ == "__main__":

    world = MazeWorld()

    state = world.reset()

    print("Initial World:")
    world.render(state)


    print("\nReachable Futures:")
    print(
        len(world.reachable_space())
    )


    print("\nViability Kernel:")
    print(
        len(world.viability_kernel())
    )


    print("\nAvailable Actions:")
    print(
        world.available_actions(state)
    )
```
