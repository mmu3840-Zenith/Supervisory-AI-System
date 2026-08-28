from src.experiments.runner import run_experiment


def test_experiment_is_deterministic():

    first = run_experiment(
        agents=10,
        tasks=20,
        steps=20,
        seed=42,
        supervisory=True,
    )

    second = run_experiment(
        agents=10,
        tasks=20,
        steps=20,
        seed=42,
        supervisory=True,
    )

    assert first == second


def test_experiment_metrics_exist():

    result = run_experiment(
        agents=5,
        tasks=10,
        steps=10,
        seed=42,
    )

    metrics = result["metrics"]

    assert 0.0 <= metrics["completion_rate"] <= 1.0
    assert metrics["failed_agents"] >= 0
    assert metrics["makespan"] >= 1
