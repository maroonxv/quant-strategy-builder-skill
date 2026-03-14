# Strategy Delivery Checklist

Use this checklist when the repo does not clearly map to a supported framework yet, or when the user wants a framework-agnostic design pass before implementation.

## 1. Clarify The Trading Hypothesis

- Market and instrument type: equities, futures, crypto, options, or multi-asset
- Universe selection rule
- Timeframe and bar resolution
- Signal drivers: indicators, spreads, regimes, events, or vol structure
- Entry and exit conditions
- Position sizing and capital constraints
- Risk controls: stops, exposure limits, concentration, volatility, Greeks
- Execution assumptions: market, limit, scheduled, smart routing, or paper-only

## 2. Map The Request To The Smallest Change

- **Config-first** when the behavior is already parameterized
- **Strategy-logic first** when the entry, exit, or risk rule changes
- **Adapter first** when the task is about porting or framework-specific wiring
- **Research first** when the user needs hypothesis shaping before code edits

## 3. Keep The Architecture Honest

- Put signal logic near the strategy or domain layer that already owns it
- Keep risk and sizing close to the position-management seam
- Keep execution details in broker/exchange adapters or scheduling layers
- Avoid scattering trading rules across notebooks, CLI wrappers, and data loaders

## 4. Choose Evidence Before Editing

Pick the minimum proof needed:

- unit tests for deterministic rules
- walk-forward or focused backtests for PnL-sensitive changes
- dry-run or paper-trading smoke checks for execution or lifecycle work
- artifact summaries for parameter sweeps and benchmark comparisons

## 5. Summarize The Result

Always report:

- what changed in strategy behavior
- what evidence ran
- what assumptions the result depends on
- what should be tested next before live usage
