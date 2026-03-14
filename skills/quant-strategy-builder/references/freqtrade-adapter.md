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

## China-Market Notes

- treat Freqtrade as crypto-first. When a repo says "China market," first determine whether it really means mainland assets or crypto strategies operated on China time and workflows
- do not assume Freqtrade natively models A-shares, China futures delivery, ETF options exercise, T+1, round lots, or price-limit rules; if the repo still uses it for those ideas, keep the mismatch explicit
- for China-timezone operation, make candle boundaries, session filters, and reporting timestamps explicit so signals are aligned to `Asia/Shanghai` expectations
- if a strategy borrows mainland-market logic for a crypto proxy, document that translation and keep exchange fees, funding, leverage, and liquidation assumptions visible in config

## Preferred Verification

- strategy-specific backtests
- targeted dry-run checks for order generation and protections
- hyperopt or parameter-sweep evidence only when the user explicitly wants tuning

## Common Pitfalls

- duplicating indicator calculations across entry and exit paths
- tuning many parameters without a baseline or out-of-sample check
- forgetting exchange fees, funding, or leverage constraints
- presenting mainland China market behavior as if it were natively executable in Freqtrade without a custom exchange or simulation layer
