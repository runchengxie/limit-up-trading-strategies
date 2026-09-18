# Event Study v1 and CI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a small, dependency-light event-study library with execution-aware return calculations, tests, and GitHub Actions CI.

**Architecture:** Use a typed Python package under `src/limit_up_event_study` with immutable dataclasses for observed events and execution assumptions. Keep calculations pure and deterministic: validation rejects future-looking fields, execution-adjusted return is separate from raw return paths, and MFE/MAE are computed from supplied forward prices. Tests use synthetic data only.

**Tech Stack:** Python 3.11+, standard library (`dataclasses`, `datetime`, `typing`), pytest, GitHub Actions.

**Spec:** `docs/research/strategy-research-roadmap.md`

## Global Constraints

- Do not import or copy third-party strategy code from the private archive.
- Do not require network access or real market data for unit tests.
- Do not use future observations to validate event fields or calculate the signal-time record.
- CI must run on Python 3.11 and 3.12 for pushes and pull requests.

---

### Task 1: Package metadata and event model

**Files:**
- Create: `pyproject.toml`
- Create: `src/limit_up_event_study/__init__.py`
- Create: `src/limit_up_event_study/events.py`
- Test: `tests/test_events.py`

**Interfaces:**
- `LimitUpEvent` dataclass with `event_date`, `security_id`, `signal_time`, `first_touch_time`, `limit_price`, `signal_price`, `market_segment`.
- `LimitUpEvent.validate() -> None` raises `ValueError` for missing identity, signal time after first touch, non-positive prices, or unsupported segment.

- [ ] Write failing validation tests.
- [ ] Run `python -m pytest tests/test_events.py -q` and verify failure because the package is absent.
- [ ] Implement the dataclass and validation.
- [ ] Run the focused tests and verify they pass.

### Task 2: Execution-adjusted returns and path metrics

**Files:**
- Create: `src/limit_up_event_study/returns.py`
- Test: `tests/test_returns.py`

**Interfaces:**
- `ExecutionAssumption(fill_probability: float, slippage_bps: float, fee_bps: float, queue_cost_bps: float)`.
- `execution_adjusted_expectation(raw_return: float, assumption: ExecutionAssumption) -> float`.
- `forward_path_metrics(entry_price: float, prices: Mapping[str, float]) -> dict[str, float]` returning `mfe`, `mae`, and the supplied horizon returns.

- [ ] Write failing tests for fill probability, costs, invalid assumptions, MFE and MAE.
- [ ] Run the focused tests and verify expected failures.
- [ ] Implement the pure calculations with explicit validation.
- [ ] Run all tests and verify they pass.

### Task 3: Documentation and CI

**Files:**
- Create: `.github/workflows/ci.yml`
- Create: `tests/test_public_api.py`
- Modify: `README.md`

**Interfaces:**
- CI runs pytest against Python 3.11 and 3.12 on push and pull request.
- README documents local setup and the synthetic-data test boundary.

- [ ] Write a public API smoke test.
- [ ] Run the complete local test suite.
- [ ] Add the GitHub Actions matrix and README usage instructions.
- [ ] Validate the workflow YAML and run the same commands locally.

### Task 4: Final verification

- [ ] Run `python -m pytest -q`.
- [ ] Run `python -m compileall -q src tests`.
- [ ] Run `git diff --check`.
- [ ] Scan the diff for private paths, credentials, and third-party archive imports.
- [ ] Commit the feature branch only after all checks pass.
