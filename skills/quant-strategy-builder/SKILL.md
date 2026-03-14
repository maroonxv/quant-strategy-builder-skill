---
name: quant-strategy-builder
description: Design, refine, debug, and verify China-market-first quantitative trading strategies across framework-agnostic research flows and common engines such as vn.py, RQAlpha, TqSdk, qteasy, LEAN, Freqtrade, Backtrader, and OptionForge. Use when an agent needs to translate a trading idea into strategy logic, configs, backtests, risk rules, framework adapters, or evidence-backed delivery.
---

# Quant Strategy Builder

Portable skill for Codex, Claude Code, and other `SKILL.md`-aware coding agents.

Turn a trading idea into the smallest safe strategy change set. Prefer the framework's existing seams, keep trading logic explicit, and return verification evidence instead of intuition.

Default stance: be China-market-first unless the repo or task clearly targets another venue. Start from A-shares, ETFs, China futures, and exchange-listed options assumptions before reaching for US-market defaults.

## When To Use

Use this skill when the task involves any of the following:

- turning a strategy idea into code, config, tests, or backtest steps
- refining entry, exit, universe, sizing, risk, hedging, or execution behavior
- adapting a strategy to exchange rules such as T+1, lot size, price limits, contract rolls, margin, or exercise handling
- porting a strategy between research or execution frameworks
- debugging a backtest mismatch, signal regression, or risk-rule bug
- producing structured delivery notes with assumptions, evidence, and next checks

## When Not To Use

Do not use this skill as the primary workflow for:

- discretionary market predictions with no code or research artifact
- broker account actions, live capital allocation, or compliance/legal advice
- data engineering work that does not affect strategy behavior
- generic portfolio commentary that does not require strategy design

## Start From Intent

1. Restate the request in strategy terms: market, exchange, instrument, universe, timeframe, signal, entry, exit, sizing, risk, execution, and observability.
2. For China-market tasks, explicitly capture microstructure: T+1 vs T+0, round-lot or contract-multiplier rules, price limits, auctions, night sessions, margin, roll rules, and exercise or assignment handling.
3. Identify whether the change is research-only, config-first, code-first, data-pipeline-first, or porting between frameworks.
4. Ask what "done" looks like in evidence terms: unit tests, backtests, parameter tables, benchmark comparison, or dry-run logs.
5. Keep the change surface small. Prefer parameters and existing extension points before inventing new abstractions.

## China-Market Checkpoints

When the task touches mainland China markets, treat these as first-class design inputs rather than afterthoughts:

- **A-shares / ETFs**: trading calendar, opening and closing auctions, 100-share round lots, T+1 selling constraints, suspensions, ST treatment, and limit-up or limit-down behavior
- **China futures**: dominant-contract choice, roll trigger, day and night sessions, multiplier, margin, fee model, delivery month boundaries, and exchange-specific sessions
- **Exchange-listed options**: underlying mapping, contract multiplier, expiration ladder, strike filtering, covered vs margin requirements, exercise style, assignment or exercise flow, and hedge linkage to ETF or futures underlyings
- **Data stack**: source, adjustment method, dominant-contract stitching, survivorship handling, and whether the backtest only sees data available at decision time
- **Execution realism**: commissions, slippage, queueing, price-limit behavior, and whether validation distinguishes research assumptions from executable production behavior

## Detect The Active Framework

Check the workspace before editing:

- **VeighNa / vn.py**: `from vnpy...`, `CtaTemplate`, `BarGenerator`, `ArrayManager`, `vnpy_ctp`, `vnpy_ctastrategy`, or `MainEngine`
- **RQAlpha**: `rqalpha`, `__config__`, `init`, `before_trading`, `handle_bar`, `scheduler`, or `rqalpha run`
- **TqSdk**: `from tqsdk import TqApi`, `TargetPosTask`, `get_kline_serial`, `insert_order`, `TqBacktest`, or `TqSim`
- **qteasy**: `import qteasy as qt`, `qt.configure`, `realize()`, `get_data()`, local data stores, or strategy-combination configs
- **AKShare / Tushare / RQData research stack**: data-fetch notebooks or research scripts with no execution engine; treat these as custom research repos and identify where execution logic is supposed to live before editing
- **OptionForge**: repo naming, docs, or task wording clearly indicate OptionForge; then load the dedicated adapter reference before editing
- **LEAN**: `AlgorithmImports.py`, `*.csproj`, `QuantConnect/`, `Research.ipynb`, or `QCAlgorithm` subclasses
- **Freqtrade**: `freqtrade/`, `user_data/strategies/`, `config.json`, `IStrategy` subclasses
- **Backtrader**: `bt.Strategy`, `Cerebro`, `backtrader` imports, `strategies/` or notebook-based research
- **Unknown / custom stack**: infer the architecture from strategy classes, config files, and test entrypoints before changing anything

If a framework is detected, load only the matching adapter file. If the workspace is custom, stay framework-agnostic and map behavior to the repo's nearest strategy seams.

## Default Edit Loop

1. Read the strategy source of truth first: strategy module, config, tests, and any task-specific docs.
2. Translate the request into a checklist for market structure, universe, data, signal, sizing, risk, execution, and evidence.
3. Verify the market-specific constraints before changing signal logic: session boundaries, lot size or multiplier, T+1, price limits, margin, roll, and exercise assumptions.
4. Prefer config or strategy-parameter changes when the behavior is already exposed.
5. Keep data-source assumptions explicit, especially when using AKShare, Tushare, RQData, or stitched continuous futures data.
6. Put trading decisions in strategy or domain logic, not in CLI glue, notebooks, or unrelated infrastructure.
7. Add or update the smallest focused test or backtest harness near the affected strategy seam.
8. Run the narrowest verification loop that can prove the change.
9. Summarize what changed, what evidence ran, and what assumptions still matter.

## Verification Expectations

Use the smallest combination that proves the behavior:

- unit or component tests for signal, sizing, risk, and adapter logic
- focused backtests when the change affects trading outcomes or parameter sensitivity
- smoke validation for config loading, strategy registration, or framework boot
- market-structure checks for T+1, lot size, roll logic, session filters, exercise handling, or price-limit behavior when relevant
- artifact summaries with metrics, benchmark deltas, and known data caveats

Prefer structured outputs and saved artifacts over raw console narration.

## Delivery Checklist

Every delivery should state:

- which framework was detected, or that the repo was treated as custom
- which market, exchange, data source, and adjustment or continuous-contract assumptions were used
- which strategy files, configs, and tests were used as source of truth
- whether the change was config-first, code-first, or adapter-focused
- which verification steps ran and whether they passed
- which assumptions, skipped checks, or data limitations remain

## Load References On Demand

Read only the file that matches the job:

1. `references/strategy-design-workflow.md` for framework-agnostic strategy decomposition and implementation planning
2. `references/validation-matrix.md` for matching changes to the cheapest convincing proof
3. `references/prompt-map.md` for China-market-first strategy archetypes and reusable prompt starters
4. `references/vnpy-adapter.md` when the repo is VeighNa / vn.py based
5. `references/rqalpha-adapter.md` when the repo is RQAlpha based
6. `references/tqsdk-adapter.md` when the repo is TqSdk based
7. `references/qteasy-adapter.md` when the repo is qteasy based
8. `references/optionforge-adapter.md` when the repo is clearly OptionForge-shaped
9. `references/lean-adapter.md` when the repo is QuantConnect / LEAN based
10. `references/freqtrade-adapter.md` when the repo is Freqtrade based
11. `references/backtrader-adapter.md` when the repo is Backtrader based
