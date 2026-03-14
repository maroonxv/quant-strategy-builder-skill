# VeighNa / vn.py Adapter

Load this reference when the workspace uses VeighNa / vn.py for China-market trading or backtesting.

## Workspace Markers

- `from vnpy...`
- `CtaTemplate`, `BarGenerator`, or `ArrayManager`
- `vnpy_ctp`, `vnpy_ctastrategy`, `vnpy_ctabacktester`, or gateway packages
- `MainEngine`, `EventEngine`, or VeighNa Trader launch scripts

## Typical Edit Surface

- CTA strategy lifecycle methods such as `on_init`, `on_start`, `on_bar`, `on_tick`, and `on_trade`
- strategy `parameters` and `variables`
- contract metadata, fee or slippage assumptions, and gateway-specific config
- backtester setup, symbol routing, and session-aware filters

## Preferred Verification

- targeted CTA backtests with explicit contract, session, and fee settings
- inspection of order, trade, and position events after strategy changes
- focused tests for signal helpers, roll logic, and risk guards outside the GUI shell

## Common Pitfalls

- ignoring main-contract rolls, price tick, contract multiplier, or fee model
- treating China futures like continuous 24-hour markets and forgetting night sessions
- hiding mutable strategy state outside the framework's expected `variables`
- mixing GUI or gateway boot logic with domain-level trading decisions
