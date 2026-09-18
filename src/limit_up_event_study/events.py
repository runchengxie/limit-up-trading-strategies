from dataclasses import dataclass
from datetime import datetime

SUPPORTED_MARKET_SEGMENTS = frozenset({"main", "chinext", "star", "st"})


@dataclass
class LimitUpEvent:
    event_date: str
    security_id: str
    signal_time: datetime
    first_touch_time: datetime
    limit_price: float
    signal_price: float
    market_segment: str

    def validate(self) -> None:
        if not self.event_date:
            raise ValueError("event_date must be non-empty")
        if not self.security_id:
            raise ValueError("security_id must be non-empty")
        if self.signal_time > self.first_touch_time:
            raise ValueError("signal_time cannot be after first_touch_time")
        if self.limit_price <= 0 or self.signal_price <= 0:
            raise ValueError("prices must be positive")
        if self.market_segment not in SUPPORTED_MARKET_SEGMENTS:
            raise ValueError("market_segment is not supported")
