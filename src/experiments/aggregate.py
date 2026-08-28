"""Aggregate repeated experimental runs."""

from __future__ import annotations

import json
from pathlib import Path
from statistics import mean, stdev


def aggregate_metric(
    files: list[Path],
    metric: str,
) -> dict[str, float | int]:
    """Calculate mean and sample standard deviation."""

    values: list[float] = []

    for path in files:

        data = json.loads(
            path.read_text(
                encoding="utf-8"
            )
        )

        values.append(
            float(data["metrics"][metric])
        )

    if not values:
        raise ValueError(
            "No experiment files supplied"
        )

    return {
        "n": len(values),
        "mean": mean(values),
        "std": (
            stdev(values)
            if len(values) > 1
            else 0.0
        ),
        "min": min(values),
        "max": max(values),
    }


def main() -> None:
    """Aggregate baseline and supervisory results."""

    root = Path("results/raw")

    baseline_files = sorted(
        root.glob("baseline_seed_*.json")
    )

    supervisory_files = sorted(
        root.glob("supervisory_seed_*.json")
    )

    metrics = [
        "completion_rate",
        "mean_failure_risk",
        "failed_agents",
        "task_reassignments",
        "total_energy",
        "makespan",
    ]

    output = {
        "baseline": {},
        "supervisory": {},
    }

    for metric in metrics:

        output["baseline"][metric] = aggregate_metric(
            baseline_files,
            metric,
        )

        output["supervisory"][metric] = aggregate_metric(
            supervisory_files,
            metric,
        )

    output_path = Path(
        "results/processed/summary.json"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path.write_text(
        json.dumps(
            output,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        f"Research summary written to {output_path}"
    )


if __name__ == "__main__":
    main()
