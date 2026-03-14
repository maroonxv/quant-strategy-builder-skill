# TqSdk Adapter

Load this reference when the workspace uses TqSdk for China futures or options workflows.

## Workspace Markers

- `from tqsdk import TqApi`
- `TargetPosTask`, `TqBacktest`, `TqSim`, or `get_kline_serial`
- quote subscriptions, order insertion, or task loops driven by TqSdk
- repos focused on futures, options, realtime quotes, or execution loops

## Typical Edit Surface

- quote and K-line acquisition
- target-position or direct order logic
- session filters, stop logic, and execution throttling
- backtest or simulation configuration

## Preferred Verification

- small `TqBacktest` or simulation runs that isolate the changed rule
- inspection of position diffs, order history, and session-aware behavior
- helper tests for signal generation and state transitions outside the API loop

## Common Pitfalls

- assuming stock-style session structure instead of China futures day and night sessions
- blocking the event loop with heavy signal code
- mixing live-trading and backtest-only branches without explicit guards
- skipping realistic fee, slippage, or contract-roll assumptions
