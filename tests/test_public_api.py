from limit_up_event_study import (
    ExecutionAssumption,
    LimitUpEvent,
    execution_adjusted_expectation,
    forward_path_metrics,
)


def test_public_api_exports_event_and_return_primitives() -> None:
    assert LimitUpEvent.__name__ == "LimitUpEvent"
    assert ExecutionAssumption.__name__ == "ExecutionAssumption"
    assert callable(execution_adjusted_expectation)
    assert callable(forward_path_metrics)
