# OptionForge Strategy Map

Derived from upstream pack metadata, example strategies, and scaffold templates in the OptionForge repository on 2026-03-14.

## First-Pass Heuristics

- Start from `.focus/context.json -> recommended_first_pass` when available. The upstream default points to the `selection` pack.
- Prefer config changes over code changes when the request only tunes thresholds, limits, service activation, or observability knobs.
- Prefer pack-owned tests before broad regression.
- Use backtests for behavior evidence, not for every small refactor.

## Request-To-Surface Matrix

| User intent | Start here | Supporting files | Minimum verification | Common pitfall |
| --- | --- | --- | --- | --- |
| Change trading target, underlying universe, or option-chain selection | `config/general/trading_target.toml`, `config/domain_service/selection`, `src/strategy/domain/domain_service/selection` | `focus/packs/selection/pack.toml`, `tests/strategy/domain/domain_service/test_selection_integration.py` | `validate --json`, selection-focused tests, `focus test --json` | Do not hardcode selection rules in `strategy_entry.py`. |
| Add indicator logic or change signal thresholds | `src/strategy/domain/domain_service/signal`, `config/strategy_config.toml` | `example/*/strategy_contract.toml`, `tests/strategy/application/test_market_workflow_pipeline.py` | `validate --json`, focused signal or workflow tests, `focus test --json` | Do not duplicate signal logic in application workflows. |
| Tune pricing, Greeks, or vol-surface behavior | `src/strategy/domain/domain_service/pricing`, `config/domain_service` | `tests/strategy/domain/domain_service/test_pricing_engine.py`, `tests/strategy/domain/domain_service/test_greeks_calculator.py` | `validate --json`, pricing-focused tests, `focus test --json` | Do not mix pricing rules into gateway or parsing code. |
| Change sizing, stop rules, concentration limits, or combination risk | `src/strategy/domain/domain_service/risk`, `src/strategy/domain/domain_service/combination`, `config/domain_service/risk` | `focus/packs/risk/pack.toml`, `tests/strategy/domain/domain_service/risk`, `tests/strategy/domain/domain_service/combination` | `validate --json`, risk or combination integration tests, `focus test --json` | Do not move risk decisions into CLI or workflow glue. |
| Change smart-order execution or scheduling | `src/strategy/domain/domain_service/execution`, `config/domain_service/execution` | `focus/packs/execution/pack.toml`, `tests/strategy/domain/domain_service/test_execution_integration.py` | `validate --json`, execution integration tests, `focus test --json` | Do not introduce new facade or coordinator layers. |
| Tune Delta or Vega hedging | `src/strategy/domain/domain_service/hedging`, `config/strategy_config.toml` | `focus/packs/hedging/pack.toml`, `tests/strategy/domain/domain_service/test_delta_hedging_service.py`, `tests/strategy/domain/domain_service/test_vega_hedging_service.py` | `validate --json`, hedging tests, `focus test --json`, backtest if behavior changed materially | Do not scatter hedging thresholds through business code. |
| Add monitoring, snapshots, or decision journaling | `src/strategy/infrastructure/monitoring`, `src/strategy/infrastructure/persistence` | `focus/packs/monitoring/pack.toml`, `tests/strategy/infrastructure/monitoring`, `tests/strategy/infrastructure/persistence` | `validate --json`, monitoring or persistence tests, `focus test --json` | Do not push observability responsibilities into domain services. |
| Produce execution evidence or debug parameter effects | `src/backtesting`, `tests/backtesting` | `artifacts/backtest/latest.json`, `tests/backtesting/test_runner.py` | `backtest --json` plus the smallest relevant regression set | Do not duplicate strategy logic just for backtest mode. |
| Scaffold a new strategy or repo | `python -m src.cli.app init ...`, `python -m src.cli.app create ...` | `example/*`, `src/main/scaffold/templates/presets/*` | `validate --json`, `focus test --json` after integrating generated files | Do not invent a contract layout before checking examples and presets. |

## Strategy Contract Levers

The upstream examples use `strategy_contract.toml` to declare strategy wiring. Check examples before building a new contract shape.

- `strategy_contracts.indicator_service`: indicator implementation import path
- `strategy_contracts.signal_service`: signal implementation import path
- `strategy_contracts.*_kwargs`: parameter blocks passed into indicator or signal services
- `service_activation.*`: feature flags for selection, pricing, risk, execution, monitoring, and observability services
- `observability.*`: decision journal and monitoring behavior

Use these levers before changing application orchestration code.

## Strategy-Design Checklist

1. Write the requested behavior in terms of entry, exit, selection, sizing, risk, hedging, and observability.
2. Update `strategy_spec.toml` when the intent, acceptance criteria, or enabled capabilities changed.
3. Decide whether the change belongs in config, a concrete domain service, or only a strategy contract.
4. Extend the nearest pack-owned tests before broad regression.
5. Run structured verification and summarize evidence from JSON artifacts instead of raw console output.
