"""Executable research experiment for the Supervisory AI System.

The experiment compares:
1. Greedy allocation
2. Load-balanced allocation
3. Supervisory allocation with failure-risk monitoring

This is a computational simulation and does not establish
physical robotic performance.
"""

from __future__ import annotations

import json
import random
from pathlib import Path

from src.agents.robot_agent import RobotAgent
from src.allocation.strategies import (
    greedy_allocate,
    load_balanced_allocate,
)
from src.environment.supervisory_environment import (
    SupervisoryEnvironment,
)
from src.metrics.research_metrics import ExperimentMetrics
from src.supervisor.supervisor import Supervisor


def run_experiment(
    *,
    agents: int = 20,
    tasks: int = 50,
    steps: int = 100,
    seed: int = 42,
    supervisory: bool = True,
) -> dict:
    """Run one deterministic experiment."""

    if agents < 1:
        raise ValueError("agents must be positive")

    if tasks < 0:
        raise ValueError("tasks cannot be negative")

    if steps < 1:
        raise ValueError("steps must be positive")

    rng = random.Random(seed)

    environment = SupervisoryEnvironment(
        task_count=tasks,
        seed=seed,
    )

    robot_agents = [
        RobotAgent(
            agent_id=i,
            x=rng.uniform(0, environment.width),
            y=rng.uniform(0, environment.height),
        )
        for i in range(agents)
    ]

    supervisor = Supervisor(
        risk_threshold=0.70
    )

    total_risks: list[float] = []
    reassignments = 0
    failed_agents = 0

    for step in range(steps):

        decisions = supervisor.assess_swarm(
            robot_agents
        )

        total_risks.extend(
            decision.risk
            for decision in decisions
        )

        if supervisory:

            for decision in decisions:

                if decision.action == "redistribute":

                    agent = robot_agents[
                        decision.agent_id
                    ]

                    if agent.workload > 0:
                        agent.workload *= 0.5
                        reassignments += 1

        assignments = load_balanced_allocate(
            robot_agents,
            environment.tasks,
        ) if supervisory else greedy_allocate(
            robot_agents,
            environment.tasks,
        )

        for task_id, agent_id in assignments.items():

            task = next(
                task
                for task in environment.tasks
                if task.task_id == task_id
            )

            agent = robot_agents[agent_id]

            if not task.completed:

                agent.assign_task(1.0)

                energy_cost = (
                    0.5
                    + 0.05 * agent.distance_to(
                        (task.x, task.y)
                    )
                )

                agent.consume_energy(
                    min(energy_cost, 5.0)
                )

                if agent.active:
                    task.completed = True
                    agent.complete_task()

        failed_agents = sum(
            1 for agent in robot_agents
            if not agent.active
        )

        if environment.remaining_tasks() == 0:
            break

    metrics = ExperimentMetrics(
        completion_rate=environment.completion_rate(),
        mean_failure_risk=(
            sum(total_risks) / len(total_risks)
            if total_risks
            else 0.0
        ),
        failed_agents=failed_agents,
        task_reassignments=reassignments,
        total_energy=sum(
            agent.energy
            for agent in robot_agents
        ),
        makespan=step + 1,
    )

    return {
        "experiment": "Supervisory AI System",
        "model_type": "computational multi-agent simulation",
        "seed": seed,
        "agents": agents,
        "tasks": tasks,
        "steps_requested": steps,
        "supervisory_enabled": supervisory,
        "metrics": metrics.as_dict(),
    }


def save_result(
    result: dict,
    output: str | Path,
) -> Path:
    """Write one experiment result."""

    path = Path(output)
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        json.dumps(
            result,
            indent=2,
        ),
        encoding="utf-8",
    )

    return path


def main() -> None:
    """Run baseline and supervisory experiments."""

    output_dir = Path(
        "results/raw"
    )

    for seed in [42, 7, 21, 99, 123]:

        baseline = run_experiment(
            seed=seed,
            supervisory=False,
        )

        supervisory = run_experiment(
            seed=seed,
            supervisory=True,
        )

        save_result(
            baseline,
            output_dir
            / f"baseline_seed_{seed}.json",
        )

        save_result(
            supervisory,
            output_dir
            / f"supervisory_seed_{seed}.json",
        )

        print(
            f"Seed {seed}: "
            f"baseline="
            f"{baseline['metrics']['completion_rate']:.3f}, "
            f"supervisory="
            f"{supervisory['metrics']['completion_rate']:.3f}"
        )


if __name__ == "__main__":
    main()
