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

## Preferred Verification

- small backtests with explicit analyzer outputs
- unit tests for custom indicators and sizing helpers
- inspection of broker cash, trades, and analyzer summaries after strategy changes

## Common Pitfalls

- burying reusable signal logic inside `next`
- mixing analyzer/reporting concerns with trading rules
- validating only one data feed or market regime
