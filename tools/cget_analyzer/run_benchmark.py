```python
"""
CGET Benchmark Runner

Runs the complete toy benchmark suite.

Evaluates agents across:

1. Compression
2. Causal Fidelity
3. Operator Closure
4. Agency Bandwidth
5. Identity Preservation
6. Transformation Efficiency (Theta*)

Usage:

    python run_benchmark.py
"""

from experiments import evaluate
from toy_agents import (
    LookupAgent,
    CausalAgent,
    SelfModifyingAgent
)


def print_header():
    print("=" * 70)
    print("CGET BENCHMARK SUITE")
    print("Causal Generative Execution Theory")
    print("=" * 70)


def format_score(value):
    """
    Format metric values consistently.
    """

    if isinstance(value, float):
        return f"{value:.4f}"

    return value


def print_results(results):

    print("\nAgent:", results["name"])
    print("-" * 50)

    for metric, value in results.items():

        if metric == "name":
            continue

        print(
            f"{metric:<25}: "
            f"{format_score(value)}"
        )


def rank_agents(all_results):

    """
    Rank by Theta*.

    Note:
    Future versions may replace scalar ranking
    with lexicographic CGET constraints.
    """

    return sorted(
        all_results,
        key=lambda x: x["theta"],
        reverse=True
    )


def run_benchmark():

    print_header()

    agents = [
        LookupAgent(),
        CausalAgent(),
        SelfModifyingAgent()
    ]

    results = []

    for agent in agents:

        result = evaluate(agent)

        results.append(result)

        print_results(result)


    print("\n")
    print("=" * 70)
    print("CGET TRANSFORMATION RANKING")
    print("=" * 70)

    ranking = rank_agents(results)

    for index, agent in enumerate(ranking, start=1):

        print(
            f"{index}. "
            f"{agent['name']} "
            f"(Theta* = {agent['theta']:.4f})"
        )


def main():

    run_benchmark()


if __name__ == "__main__":
    main()
```
