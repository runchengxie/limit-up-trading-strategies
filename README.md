# 涨停事件研究

这是一个面向中国 A 股涨停事件研究的公开仓库，包含可复用的 Python 研究基础组件、研究假设、文献线索和验证路线。

当前代码包名为 `limit-up-event-study`，模块名为 `limit_up_event_study`。项目使用合成输入演示事件校验、成交约束下的收益期望和前瞻收益路径，不包含行情数据，也不构成投资建议。

## 当前功能

- `LimitUpEvent`：记录事件日期、证券标识、信号时间、首次触板时间、价格和市场分段，并提供基础校验。
- `ExecutionAssumption`：记录成交概率、滑点、费用和排队成本。
- `execution_adjusted_expectation`：根据成交概率和交易成本调整原始收益期望。
- `forward_path_metrics`：计算多个持有期限的收益，并给出 MFE 和 MAE。

这些组件用于固定研究口径，避免把信号收益直接当成可成交收益。后续研究需要接入具备时间点一致性的数据，并补充真实撮合、费用、滑点、涨跌幅制度和样本外验证。

## 快速开始

需要 Python 3.11 或更高版本。

```bash
python -m pip install -e ".[test,dev]"
python -m pytest -q
python -m compileall -q src tests
python -m ruff check src tests
```

构造一个事件并计算收益路径：

```python
from datetime import datetime

from limit_up_event_study import (
    ExecutionAssumption,
    LimitUpEvent,
    execution_adjusted_expectation,
    forward_path_metrics,
)

event = LimitUpEvent(
    event_date="2024-01-02",
    security_id="SYNTH-001",
    signal_time=datetime(2024, 1, 2, 10, 30),
    first_touch_time=datetime(2024, 1, 2, 10, 45),
    limit_price=11.0,
    signal_price=10.8,
    market_segment="main",
)
event.validate()

assumption = ExecutionAssumption(
    fill_probability=0.5,
    slippage_bps=10,
    fee_bps=5,
    queue_cost_bps=5,
)
adjusted_return = execution_adjusted_expectation(0.10, assumption)
path = forward_path_metrics(
    100,
    {"next_open": 101, "t_plus_2": 98, "t_plus_5": 103},
)
```

## 文档

- [研究路线](docs/research/strategy-research-roadmap.md)：事件表、成交真实性、分组研究和样本外验证顺序。
- [文献与研究假设](docs/references/literature-and-broker-reports.md)：学术论文、研报线索和可检验假设。
- [维护与验证](docs/maintenance-and-validation.md)：本地检查、CI 和文档站构建方式。
- [公开发布清单](docs/release/public-release-checklist.md)：代码、来源、数据和研究表达的发布检查项。

在线文档见 [GitHub Pages](https://runchengxie.github.io/limit-up-trading-strategies/)。

## 研究边界

仓库内容用于研究和软件开发，不提供投资建议。任何结果都需要使用点时数据重新验证，并明确信号时点、下单时点、首次可成交时点、成交概率、费用、滑点、排队成本、制度分层、滚动样本外区间和多重检验处理。

仓库不存放私有 archive 中的原始策略文本、第三方材料全文、数据供应商导出物、个股交易记录或账户信息。相关背景资料可见 [limit-up-trading-strategies-archive](https://github.com/runchengxie/limit-up-trading-strategies-archive)。
