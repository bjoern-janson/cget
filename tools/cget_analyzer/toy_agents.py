"""
Minimal CGET toy agents.
"""


class Agent:

    def __init__(self, name):
        self.name = name

        self.raw_complexity = 100
        self.latent_complexity = 100

        self.interventions_correct = 0
        self.interventions_total = 0

        self.compositions_successful = 0
        self.compositions_attempted = 0

        self.steerable = 0
        self.reachable = 0

        self.identity_change = 0


class LookupAgent(Agent):

    def __init__(self):
        super().__init__("Lookup Agent")

        self.latent_complexity = 100

        self.interventions_correct = 5
        self.interventions_total = 20

        self.compositions_successful = 1
        self.compositions_attempted = 20

        self.steerable = 5
        self.reachable = 100


class CausalAgent(Agent):

    def __init__(self):
        super().__init__("Causal Agent")

        self.latent_complexity = 20

        self.interventions_correct = 18
        self.interventions_total = 20

        self.compositions_successful = 17
        self.compositions_attempted = 20

        self.steerable = 70
        self.reachable = 100

        self.identity_change = 0.02


class SelfModifyingAgent(Agent):

    def __init__(self):
        super().__init__("CGET Agent")

        self.latent_complexity = 10

        self.interventions_correct = 20
        self.interventions_total = 20

        self.compositions_successful = 20
        self.compositions_attempted = 20

        self.steerable = 95
        self.reachable = 100

        self.identity_change = 0.001
