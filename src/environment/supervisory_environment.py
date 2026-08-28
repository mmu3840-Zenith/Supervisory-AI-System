"""Multi-agent computational environment."""

from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class Task:
    """One simulated task."""

    task_id: int
    x: float
    y: float
    priority: float = 1.0
    completed: bool = False


class SupervisoryEnvironment:
    """Deterministic grid-like environment for experiments."""

    def __init__(
        self,
        width: int = 100,
        height: int = 100,
        task_count: int = 50,
        seed: int = 42,
    ) -> None:

        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")

        if task_count < 0:
            raise ValueError("task_count cannot be negative")

        self.width = width
        self.height = height
        self.task_count = task_count
        self.seed = seed

        self.random = random.Random(seed)

        self.tasks: list[Task] = []
        self.generate_tasks()

    def generate_tasks(self) -> None:
        """Generate deterministic tasks."""

        self.tasks.clear()

        for task_id in range(self.task_count):
            self.tasks.append(
                Task(
                    task_id=task_id,
                    x=self.random.uniform(0, self.width),
                    y=self.random.uniform(0, self.height),
                    priority=self.random.uniform(0.5, 2.0),
                )
            )

    def remaining_tasks(self) -> int:
        """Return number of unfinished tasks."""
        return sum(
            1 for task in self.tasks
            if not task.completed
        )

    def completion_rate(self) -> float:
        """Return task completion fraction."""

        if not self.tasks:
            return 1.0

        completed = sum(
            1 for task in self.tasks
            if task.completed
        )

        return completed / len(self.tasks)
