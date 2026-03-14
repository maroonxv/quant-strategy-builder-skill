---
name: quant-strategy-builder
description: Design, refine, debug, and verify quantitative trading strategies across framework-agnostic research flows and common engines such as LEAN, Freqtrade, Backtrader, and OptionForge. Use when Codex needs to translate a trading idea into strategy logic, configs, backtests, risk rules, framework adapters, or evidence-backed delivery.
---

# Quant Strategy Builder

Turn a trading idea into the smallest safe strategy change set. Prefer the framework's existing seams, keep trading logic explicit, and return verification evidence instead of intuition.

## When To Use

Use this skill when the task involves any of the following:

- turning a strategy idea into code, config, tests, or backtest steps
- refining entry, exit, universe, sizing, risk, hedging, or execution behavior
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

1. Restate the request in strategy terms: instrument, universe, timeframe, signal, entry, exit, sizing, risk, execution, and observability.
2. Identify whether the change is research-only, config-first, code-first, or porting between frameworks.
3. Ask what "done" looks like in evidence terms: unit tests, backtests, parameter tables, benchmark comparison, or dry-run logs.
4. Keep the change surface small. Prefer parameters and existing extension points before inventing new abstractions.

## Detect The Active Framework

Check the workspace before editing:

- **LEAN**: `AlgorithmImports.py`, `*.csproj`, `QuantConnect/`, `Research.ipynb`, or `QCAlgorithm` subclasses
- **Freqtrade**: `freqtrade/`, `user_data/strategies/`, `config.json`, `IStrategy` subclasses
- **Backtrader**: `bt.Strategy`, `Cerebro`, `backtrader` imports, `strategies/` or notebook-based research
- **OptionForge**: repo naming, docs, or task wording clearly indicate OptionForge; then load the dedicated adapter reference before editing
- **Unknown / custom stack**: infer the architecture from strategy classes, config files, and test entrypoints before changing anything

If a framework is detected, load only the matching adapter file. If the workspace is custom, stay framework-agnostic and map behavior to the repo's nearest strategy seams.

## Default Edit Loop

1. Read the strategy source of truth first: strategy module, config, tests, and any task-specific docs.
2. Translate the request into a checklist for universe, signal, sizing, risk, execution, and evidence.
3. Prefer config or strategy-parameter changes when the behavior is already exposed.
4. Put trading decisions in strategy/domain logic, not in CLI glue, notebooks, or unrelated infrastructure.
5. Add or update the smallest focused test or backtest harness near the affected strategy seam.
6. Run the narrowest verification loop that can prove the change.
7. Summarize what changed, what evidence ran, and what assumptions still matter.

## Verification Expectations

Use the smallest combination that proves the behavior:

- unit or component tests for signal, sizing, risk, and adapter logic
- focused backtests when the change affects trading outcomes or parameter sensitivity
- smoke validation for config loading, strategy registration, or framework boot
- artifact summaries with metrics, benchmark deltas, and known data caveats

Prefer structured outputs and saved artifacts over raw console narration.

## Delivery Checklist

Every delivery should state:

- which framework was detected, or that the repo was treated as custom
- which strategy files, configs, and tests were used as source of truth
- whether the change was config-first, code-first, or adapter-focused
- which verification steps ran and whether they passed
- which assumptions, skipped checks, or data limitations remain

## Load References On Demand

Read only the file that matches the job:

1. `references/strategy-design-workflow.md` for framework-agnostic strategy decomposition and implementation planning
2. `references/validation-matrix.md` for matching changes to the cheapest convincing proof
3. `references/prompt-map.md` for common strategy archetypes and reusable prompt starters
4. `references/lean-adapter.md` when the repo is QuantConnect / LEAN based
5. `references/freqtrade-adapter.md` when the repo is Freqtrade based
6. `references/backtrader-adapter.md` when the repo is Backtrader based
7. `references/optionforge-adapter.md` when the repo is clearly OptionForge-shaped
