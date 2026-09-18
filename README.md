# Limit-up Trading Strategies

Research notes and reproducibility guidance for Chinese A-share limit-up, first-board, continuation and sentiment-regime studies.

This is the public-facing research index. It intentionally does not include the private archive's raw Excel/CSV exports, backtest logs, notebooks with execution outputs, third-party strategy source text, or historical Git objects.

## Scope

- Event-level research design for first limit-up, next-day continuation and multi-board events.
- Execution-aware evaluation: signal time, order time, first executable time, fill probability, fees, slippage and queue costs.
- Market-regime conditioning using limit-up counts, broken-board rate, next-day premium, board height and promotion rate.
- Literature and broker-report references mapped to testable research hypotheses.

## Documents

- [`docs/references/literature-and-broker-reports.md`](docs/references/literature-and-broker-reports.md): peer-reviewed papers, broker-report leads and project hypotheses.
- [`docs/research/strategy-research-roadmap.md`](docs/research/strategy-research-roadmap.md): strategy decomposition, research priorities, event-level backtest design and validation sequence.
- [`docs/release/public-release-checklist.md`](docs/release/public-release-checklist.md): release, provenance, licensing and research-validity checklist.

## Research boundary

The public repository is a research record, not a verified live-trading system or investment recommendation. Any result must be revalidated with point-in-time data, realistic fills, fees, slippage, board-specific price-limit rules, rolling out-of-sample tests and multiple-testing controls.

The private source archive is maintained separately at [`limit-up-trading-strategies-archive`](https://github.com/runchengxie/limit-up-trading-strategies-archive).

## Local development

Requires Python 3.11 or newer. Install the package with its test dependencies and run the same checks used by CI:

```bash
python -m pip install -e ".[test]"
python -m pytest -q
python -m compileall -q src tests
```

The first implementation uses synthetic inputs only. It provides typed event validation, execution-adjusted return expectations, forward-horizon returns, MFE and MAE; it does not download or bundle market data.
