"""Computational robotic-agent abstraction.

This model represents simulated agents only. It does not claim
physical robotic deployment.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RobotAgent:
    """State of one simulated robotic agent."""

    agent_id: int
    x: float = 0.0
    y: float = 0.0
    energy: float = 100.0
    workload: float = 0.0
    active: bool = True
    completed_tasks: int = 0

    def position(self) -> tuple[float, float]:
        """Return the current simulated position."""
        return self.x, self.y

    def distance_to(self, target: tuple[float, float]) -> float:
        """Return Euclidean distance to a target."""
        dx = self.x - target[0]
        dy = self.y - target[1]
        return (dx * dx + dy * dy) ** 0.5

    def consume_energy(self, amount: float) -> None:
        """Consume simulated energy."""
        if amount < 0:
            raise ValueError("amount cannot be negative")

        self.energy = max(0.0, self.energy - amount)

        if self.energy <= 0.0:
            self.active = False

    def assign_task(self, workload: float) -> None:
        """Assign simulated workload."""
        if workload < 0:
            raise ValueError("workload cannot be negative")

        self.workload += workload

    def complete_task(self) -> None:
        """Complete one simulated task."""
        if self.workload > 0:
            self.workload -= 1.0

        self.completed_tasks += 1
