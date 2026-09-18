from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class ExecutionAssumption:
    fill_probability: float
    slippage_bps: float
    fee_bps: float
    queue_cost_bps: float

    def __post_init__(self) -> None:
        if not 0 <= self.fill_probability <= 1:
            raise ValueError("fill_probability must be between 0 and 1")
        if any(value < 0 for value in (self.slippage_bps, self.fee_bps, self.queue_cost_bps)):
            raise ValueError("execution costs must be non-negative")


def execution_adjusted_expectation(
    raw_return: float,
    assumption: ExecutionAssumption,
) -> float:
    total_cost = (
        assumption.slippage_bps + assumption.fee_bps + assumption.queue_cost_bps
    ) / 10_000
    return assumption.fill_probability * (raw_return - total_cost)


def forward_path_metrics(entry_price: float, prices: Mapping[str, float]) -> dict[str, float]:
    if entry_price <= 0:
        raise ValueError("entry_price must be positive")
    if not prices:
        raise ValueError("prices must not be empty")
    if any(price <= 0 for price in prices.values()):
        raise ValueError("prices must be positive")

    returns = {horizon: price / entry_price - 1 for horizon, price in prices.items()}
    returns["mfe"] = max(returns.values())
    returns["mae"] = min(returns.values())
    return returns
