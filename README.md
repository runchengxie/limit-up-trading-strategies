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
- [`docs/release/public-release-checklist.md`](docs/release/public-release-checklist.md): release, provenance, licensing and research-validity checklist.

## Research boundary

The public repository is a research record, not a verified live-trading system or investment recommendation. Any result must be revalidated with point-in-time data, realistic fills, fees, slippage, board-specific price-limit rules, rolling out-of-sample tests and multiple-testing controls.

The private source archive is maintained separately at [`limit-up-trading-strategies-archive`](https://github.com/runchengxie/limit-up-trading-strategies-archive).
