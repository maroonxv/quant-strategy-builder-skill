# qteasy Adapter

Load this reference when the workspace uses qteasy for local China-market research, backtesting, or live-trading workflows.

## Workspace Markers

- `import qteasy as qt`
- `qt.configure(...)`
- strategy classes or functions using `realize()` and `get_data()`
- local data stores, parameter optimization, or multi-strategy composition

## Typical Edit Surface

- strategy `realize()` logic and data-window usage
- `qt.configure(...)` settings for asset pool, fees, batch size, and data-cycle behavior
- strategy combination, optimization parameters, and local account settings
- backtest or live-run config that controls T+1, minimum order quantity, and execution assumptions

## Preferred Verification

- focused local backtests that verify the changed signal or risk rule
- checks that `get_data()` and configuration only expose data available at decision time
- explicit verification of batch size, fee model, T+1, and `use_latest_data_cycle` when editing A-share strategies

## Common Pitfalls

- bypassing `get_data()` semantics and accidentally reintroducing lookahead bias
- forgetting A-share batch-size assumptions such as 100-share round lots
- validating signal logic without matching fee, T+1, or order-quantity settings
- changing strategy code while leaving local data or optimization config inconsistent
