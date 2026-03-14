# Backtrader Adapter

Load this reference when the workspace uses Backtrader.

## Workspace Markers

- `import backtrader as bt`
- classes inheriting from `bt.Strategy`
- `Cerebro()` setup
- analyzers, sizers, or observers configured in Python scripts or notebooks

## Typical Edit Surface

- `__init__`, `next`, `notify_order`, and helper indicators
- sizers, analyzers, commission schemes, and broker setup
- parameter tuples exposed on the strategy class

## China-Market Notes

- make the data assumptions explicit before editing strategy logic: adjusted vs unadjusted equities, suspended trading days, ST handling, and dominant-contract stitching can all change China-market results materially
- encode mainland execution constraints in the right seams, such as 100-share round lots, T+1 selling limits, price limits, auction behavior, margin, and fee models
- for China futures, separate day and night sessions deliberately and verify multiplier, roll trigger, margin, and contract-specific fee schedules
- prefer analyzers or saved artifacts that compare raw signal behavior against friction-aware China-market assumptions, so users can see which constraint changed the outcome

## Preferred Verification

- small backtests with explicit analyzer outputs
- unit tests for custom indicators and sizing helpers
- inspection of broker cash, trades, and analyzer summaries after strategy changes

## Common Pitfalls

- burying reusable signal logic inside `next`
- mixing analyzer/reporting concerns with trading rules
- validating only one data feed or market regime
- backtesting China equities or futures on cleaned continuous data without checking how suspensions, rolls, or price limits were represented
