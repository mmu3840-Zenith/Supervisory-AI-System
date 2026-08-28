"""Energy/workload based failure-risk prediction."""

from __future__ import annotations


def predict_failure_risk(
    energy: float,
    workload: float,
    *,
    energy_weight: float = 0.7,
    workload_weight: float = 0.3,
) -> float:
    """Estimate simulated failure risk in [0, 1].

    This is a transparent heuristic model rather than a trained
    clinical, industrial, or physical failure predictor.
    """

    if not 0.0 <= energy <= 100.0:
        raise ValueError("energy must be between 0 and 100")

    if workload < 0.0:
        raise ValueError("workload cannot be negative")

    normalized_energy_risk = 1.0 - energy / 100.0
    normalized_workload_risk = min(1.0, workload / 10.0)

    risk = (
        energy_weight * normalized_energy_risk
        + workload_weight * normalized_workload_risk
    )

    return max(0.0, min(1.0, risk))
