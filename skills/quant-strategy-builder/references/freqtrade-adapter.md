# Freqtrade Adapter

Load this reference when the workspace is based on Freqtrade.

## Workspace Markers

- `user_data/strategies/`
- `config.json` or `config_full.example.json`
- classes inheriting from `IStrategy`
- hyperopt, protections, or pairlist configuration

## Typical Edit Surface

- `populate_indicators`, `populate_entry_trend`, and `populate_exit_trend`
- strategy attributes for timeframe, minimal ROI, stoploss, trailing stop, and protections
- pairlist, informative pairs, leverage, and hyperopt parameter definitions

## Preferred Verification

- strategy-specific backtests
- targeted dry-run checks for order generation and protections
- hyperopt or parameter-sweep evidence only when the user explicitly wants tuning

## Common Pitfalls

- duplicating indicator calculations across entry and exit paths
- tuning many parameters without a baseline or out-of-sample check
- forgetting exchange fees, funding, or leverage constraints
