from datetime import datetime

import pytest

from limit_up_event_study.events import LimitUpEvent


def valid_event() -> LimitUpEvent:
    return LimitUpEvent(
        event_date="2024-01-02",
        security_id="SYNTH-001",
        signal_time=datetime(2024, 1, 2, 10, 30),
        first_touch_time=datetime(2024, 1, 2, 10, 45),
        limit_price=11.0,
        signal_price=10.8,
        market_segment="main",
    )


def test_valid_event_passes_validation() -> None:
    valid_event().validate()


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("security_id", ""),
        ("limit_price", 0),
        ("signal_price", -1),
    ],
)
def test_event_rejects_missing_identity_or_non_positive_prices(field: str, value: object) -> None:
    event = valid_event()
    setattr(event, field, value)

    with pytest.raises(ValueError):
        event.validate()


def test_event_rejects_signal_after_first_touch() -> None:
    event = valid_event()
    event.signal_time = datetime(2024, 1, 2, 11, 0)

    with pytest.raises(ValueError, match="signal_time"):
        event.validate()


def test_event_rejects_unknown_market_segment() -> None:
    event = valid_event()
    event.market_segment = "unknown"

    with pytest.raises(ValueError, match="market_segment"):
        event.validate()
