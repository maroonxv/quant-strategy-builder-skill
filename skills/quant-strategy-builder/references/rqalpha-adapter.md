# RQAlpha Adapter

Load this reference when the workspace is based on RQAlpha or Ricequant-style strategy files.

## Workspace Markers

- `rqalpha` imports or CLI usage such as `rqalpha run`
- strategy functions like `init`, `before_trading`, `handle_bar`, or `after_trading`
- `__config__`, mod settings, or references to `sys_accounts`, `sys_risk`, `sys_scheduler`, or `sys_analyser`
- project layout centered on standalone strategy scripts plus config

## Typical Edit Surface

- strategy lifecycle hooks and scheduler callbacks
- account, commission, slippage, and risk-mod configuration
- stock or futures-specific portfolio logic
- analyzer outputs and artifact export settings

## Preferred Verification

- focused `rqalpha run` backtests with the smallest time range that proves the change
- inspection of analyzer outputs, trade logs, positions, and risk metrics
- unit tests for pure signal or sizing helpers outside the runtime

## Common Pitfalls

- changing strategy behavior without updating matching mod or account configuration
- mixing stock and futures assumptions without checking the active account model
- relying on narrative summaries instead of analyser artifacts and risk outputs
- overlooking scheduler timing, rebalance cadence, or order-risk checks
