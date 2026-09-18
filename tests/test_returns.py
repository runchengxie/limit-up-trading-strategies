import pytest

from limit_up_event_study.returns import (
    ExecutionAssumption,
    execution_adjusted_expectation,
    forward_path_metrics,
)


def test_execution_adjusted_expectation_applies_fill_probability_and_costs() -> None:
    assumption = ExecutionAssumption(
        fill_probability=0.5,
        slippage_bps=10,
        fee_bps=5,
        queue_cost_bps=5,
    )

    result = execution_adjusted_expectation(0.10, assumption)

    assert result == pytest.approx(0.049)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"fill_probability": -0.1, "slippage_bps": 0, "fee_bps": 0, "queue_cost_bps": 0},
        {"fill_probability": 1.1, "slippage_bps": 0, "fee_bps": 0, "queue_cost_bps": 0},
        {"fill_probability": 1, "slippage_bps": -1, "fee_bps": 0, "queue_cost_bps": 0},
    ],
)
def test_execution_assumption_rejects_invalid_values(kwargs: dict[str, float]) -> None:
    with pytest.raises(ValueError):
        ExecutionAssumption(**kwargs)


def test_forward_path_metrics_returns_horizon_returns_and_mfe_mae() -> None:
    metrics = forward_path_metrics(
        100,
        {"next_open": 101, "t_plus_2": 98, "t_plus_5": 103},
    )

    assert metrics["next_open"] == pytest.approx(0.01)
    assert metrics["t_plus_2"] == pytest.approx(-0.02)
    assert metrics["t_plus_5"] == pytest.approx(0.03)
    assert metrics["mfe"] == pytest.approx(0.03)
    assert metrics["mae"] == pytest.approx(-0.02)


def test_forward_path_metrics_rejects_non_positive_prices() -> None:
    with pytest.raises(ValueError, match="prices"):
        forward_path_metrics(100, {"next_open": 0})
