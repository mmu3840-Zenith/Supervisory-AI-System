from src.environment.supervisory_environment import (
    SupervisoryEnvironment,
)


def test_environment_determinism():
    first = SupervisoryEnvironment(
        task_count=20,
        seed=42,
    )

    second = SupervisoryEnvironment(
        task_count=20,
        seed=42,
    )

    first_positions = [
        (task.x, task.y)
        for task in first.tasks
    ]

    second_positions = [
        (task.x, task.y)
        for task in second.tasks
    ]

    assert first_positions == second_positions


def test_completion_rate():
    environment = SupervisoryEnvironment(
        task_count=2,
        seed=42,
    )

    assert environment.completion_rate() == 0.0

    environment.tasks[0].completed = True

    assert environment.completion_rate() == 0.5
