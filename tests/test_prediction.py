from src.prediction.failure_predictor import (
    predict_failure_risk,
)


def test_failure_risk_range():
    risk = predict_failure_risk(
        energy=50,
        workload=2,
    )

    assert 0.0 <= risk <= 1.0


def test_low_energy_increases_risk():
    low = predict_failure_risk(
        energy=10,
        workload=1,
    )

    high = predict_failure_risk(
        energy=90,
        workload=1,
    )

    assert low > high
