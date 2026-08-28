"""Research metrics for supervisory-control experiments."""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean


@dataclass
class ExperimentMetrics:
    """Aggregate metrics for one experimental run."""

    completion_rate: float
    mean_failure_risk: float
    failed_agents: int
    task_reassignments: int
    total_energy: float
    makespan: int

    def as_dict(self) -> dict[str, float | int]:
        """Return JSON-compatible metrics."""

        return {
            "completion_rate": self.completion_rate,
            "mean_failure_risk": self.mean_failure_risk,
            "failed_agents": self.failed_agents,
            "task_reassignments": self.task_reassignments,
            "total_energy": self.total_energy,
            "makespan": self.makespan,
        }


def mean_risk(risks: list[float]) -> float:
    """Return mean risk."""

    if not risks:
        return 0.0

    return mean(risks)
