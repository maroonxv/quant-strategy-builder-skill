---
name: optionforge-strategy-builder
description: Build, refine, debug, and verify quantitative or options strategies on top of the OptionForge framework. Use when Codex needs to work in an OptionForge repository or adapt its architecture for strategy_spec.toml updates, .focus-guided edits, config tuning, src/strategy domain-service changes, pack-aware tests, or validate/focus test/backtest evidence.
---

# OptionForge Strategy Builder

Translate a trading idea into the smallest safe OptionForge change set. Prefer the repository's agent-first protocol, keep edits inside the active surface, and return structured verification evidence instead of informal guesses.

## Start From The Source Of Truth

1. Confirm the workspace is OptionForge-shaped. Look for `strategy_spec.toml`, `.focus/context.json`, `src/strategy`, and `python -m src.cli.app --help`.
2. Read `strategy_spec.toml` first for strategy intent, enabled capabilities, and acceptance checks.
3. Read `.focus/context.json` next for editable surfaces, recommended first-pass pack, and test selectors.
4. Read `.focus/*.md`, `tests/TEST.md`, and `artifacts/*/latest.json` only as supporting context.
5. Run `python -m src.cli.app forge --json` before editing when the task changes strategy intent, focus assets, pack ownership, or AGENT-facing navigation.
6. Use the upstream layout only as a reference pattern when the current workspace is not an actual OptionForge checkout. Call out any path assumptions explicitly.

## Keep Layering Honest

1. Edit `src/strategy/domain/**` for trading rules such as selection, signal, pricing, risk, execution, and hedging logic.
2. Edit `config/**` first when a requested behavior is already parameterized.
3. Edit `src/strategy/application/**` or `src/strategy/strategy_entry.py` only when orchestration or event flow must change.
4. Edit `src/strategy/infrastructure/**` for monitoring, persistence, gateway, subscription, or parsing concerns.
5. Avoid adding facade or coordinator layers. Let the application layer call concrete domain services and infrastructure directly.
6. Avoid hand-editing generated `.focus/*` files unless the task is specifically about the generator or focus rendering logic.

## Use The Default Edit Loop

1. Restate the requested strategy change in terms of selection, signal, sizing, risk, hedging, execution, and observability.
2. Decide whether the change is config-first or code-first.
3. Keep the change inside the active editable surface unless the task clearly requires more.
4. Update or add focused tests next to the affected pack before broad regression.
5. Run `python -m src.cli.app validate --config config/strategy_config.toml --json`.
6. Run `python -m src.cli.app focus test --json`.
7. Run `python -m src.cli.app backtest --config config/strategy_config.toml --start 2025-01-01 --end 2025-03-01 --no-chart --json` when behavior or parameter effects need execution evidence.
8. Inspect `artifacts/validate/latest.json`, `artifacts/backtest/latest.json`, and `tests/TEST.md` before summarizing outcomes.

## Reuse Existing Scaffolds

1. Use `python -m src.cli.app init <strategy_name> --destination <dir>` when the user wants a new strategy starter.
2. Use `python -m src.cli.app create <repo_name>` when the user wants a fresh full OptionForge-style repository scaffold.
3. Inspect `example/*` and `src/main/scaffold/templates/presets/*` before inventing a contract shape, example README, or service activation layout from scratch.
4. Prefer `python -m src.cli.app ...` from a source checkout. Use `optionforge ...` only if the package is installed and the workspace already relies on that alias.

## Delivery Requirements

1. State which workflow entrypoints were used: `forge`, `validate`, `focus test`, `backtest`, or `run`.
2. State which source-of-truth assets were consulted.
3. State whether edits stayed inside the editable surface or why scope expanded.
4. State which structured verification steps ran and whether they passed.
5. State whether `.focus/*`, `tests/TEST.md`, or `artifacts/*/latest.json` changed.
6. State remaining risks, skipped checks, or data assumptions.

## Load References On Demand

1. Read `references/optionforge-agent-workflow.md` for the canonical command loop, artifact paths, editing boundaries, and delivery checklist.
2. Read `references/optionforge-strategy-map.md` to map a trading idea to the right OptionForge files, config knobs, tests, and common pitfalls.
