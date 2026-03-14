# Validation Matrix

Use this matrix to match each change to the cheapest convincing proof.

| Change type | Cheapest proof | What to inspect |
| --- | --- | --- |
| Indicator math or feature engineering | Unit tests with fixed fixtures | numerical stability, lookahead bias, NaN handling |
| Entry / exit threshold change | Focused backtest plus one regression test | trade count, hit rate, turnover, benchmark delta |
| Universe or ranking logic | Component test plus sample selection snapshot | symbol inclusion rules, ties, missing data |
| Position sizing or rebalancing | Unit tests plus portfolio-transition integration | leverage, exposure caps, rebalance churn |
| Stop-loss, drawdown, or risk rule | Risk-focused integration test and focused backtest | tail losses, exposure clipping, regime behavior |
| Options logic or Greeks changes | Deterministic pricing tests plus strategy scenario backtest | delta, theta, IV assumptions, assignment path |
| Exchange / broker execution wiring | Dry-run or paper-trading smoke test | order lifecycle, retries, fees, slippage assumptions |
| Cross-framework porting | Adapter smoke test plus one benchmark backtest | config parity, signal equivalence, artifact drift |

## Minimum Reporting Fields

- date range and data resolution used
- benchmark or baseline used for comparison
- key metrics: return, drawdown, Sharpe-like measure, turnover, win rate, or options-specific Greeks exposure
- assumptions that would change the result materially

## Red Flags

- backtests that improve PnL while worsening turnover or exposure with no explanation
- strategy logic duplicated in both framework adapter and core logic
- validation that depends on future data leakage, survivorship-biased universes, or missing fee models
- parameter changes justified only by a single date range
