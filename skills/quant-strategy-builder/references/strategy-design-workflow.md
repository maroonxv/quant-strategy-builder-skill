# Strategy Design Workflow

Use this reference when the user starts from an idea, a market thesis, or a partially specified strategy and needs a reusable implementation path.

## 1. Frame The Edge

- Instrument class: equities, futures, crypto, options, or multi-asset
- Trading horizon: intraday, swing, daily, weekly, or event-driven
- Edge hypothesis: mean reversion, breakout, trend, carry, dispersion, volatility, or cross-sectional spread
- Constraints: exchange hours, liquidity, borrow, margin, assignment, or hedging requirements

## 2. Translate The Idea Into Strategy Parts

- **Universe**: what can be traded and how symbols are selected
- **Data**: bars, fundamentals, options chains, alternative data, or derived factors
- **Signal**: features, thresholds, regimes, or ranking logic
- **Entry / exit**: timing rules, cooldowns, holds, and profit-taking
- **Sizing**: fixed size, volatility targeting, Kelly-inspired fractions, or risk parity
- **Risk**: stop logic, max drawdown, gross/net exposure, factor limits, or Greeks
- **Execution**: market, limit, schedule, slicing, slippage, and fill assumptions
- **Observability**: logs, metrics, journals, and saved artifacts

## 3. Choose The Smallest Safe Change

- Prefer config-first changes when a strategy already exposes the needed threshold or toggle.
- Prefer extending the existing strategy seam over creating a new abstraction layer.
- Split framework wiring from trading logic so the strategy can be tested without live infrastructure.
- Keep backtest-only helpers out of live execution paths unless the repo already shares them.

## 4. Decide The Proof Up Front

- Unit tests for deterministic signals, filters, and sizing rules
- Integration tests for order generation, portfolio transitions, and framework adapters
- Backtests for PnL-sensitive changes, parameter sensitivity, and benchmark comparison
- Dry-run or paper mode for execution lifecycle, scheduling, and logging behavior

## 5. Summarize Like A Research Engineer

Always report:

- what changed in strategy behavior
- what evidence supports the change
- what assumptions depend on data quality or market regime
- what the next safest validation step should be
