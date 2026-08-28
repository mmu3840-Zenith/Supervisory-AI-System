"""Task allocation strategies used as experimental baselines."""

from __future__ import annotations

from src.agents.robot_agent import RobotAgent
from src.environment.supervisory_environment import Task


def greedy_allocate(
    agents: list[RobotAgent],
    tasks: list[Task],
) -> dict[int, int]:
    """Assign each task to the closest active agent."""

    assignments: dict[int, int] = {}

    active_agents = [
        agent for agent in agents
        if agent.active
    ]

    if not active_agents:
        return assignments

    for task in tasks:
        if task.completed:
            continue

        selected = min(
            active_agents,
            key=lambda agent: (
                agent.distance_to((task.x, task.y)),
                agent.agent_id,
            ),
        )

        assignments[task.task_id] = selected.agent_id

    return assignments


def load_balanced_allocate(
    agents: list[RobotAgent],
    tasks: list[Task],
) -> dict[int, int]:
    """Allocate tasks using current workload and distance."""

    assignments: dict[int, int] = {}

    active_agents = [
        agent for agent in agents
        if agent.active
    ]

    if not active_agents:
        return assignments

    for task in tasks:
        if task.completed:
            continue

        selected = min(
            active_agents,
            key=lambda agent: (
                agent.workload
                + 0.01
                * agent.distance_to((task.x, task.y)),
                agent.agent_id,
            ),
        )

        assignments[task.task_id] = selected.agent_id

    return assignments
