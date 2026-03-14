# OptionForge Agent Workflow

Derived from the upstream OptionForge repository on 2026-03-14, mainly from `README_EN.md`, `AGENTS_FOCUS.md`, `strategy_spec.toml`, `.focus/context.json`, and `tests/TEST.md`.

## Workspace Markers

- `strategy_spec.toml`: high-level strategy intent, enabled capabilities, and acceptance checks
- `.focus/context.json`: machine-readable current-context contract, editable/reference/frozen surfaces, and test selectors
- `focus/packs/*/pack.toml`: pack ownership, config keys, CLI hints, and common mistakes
- `tests/TEST.md`: current test plan and latest acceptance summary
- `artifacts/validate/latest.json` and `artifacts/backtest/latest.json`: latest structured validation and backtest evidence

## Preferred Command Entry

- Use `python -m src.cli.app ...` from a source checkout.
- Use `optionforge ...` only when the package is installed into the active environment and the workspace already uses that alias.
- Prefer `--json` whenever the command supports it.

## Default Command Loop

1. Run `python -m src.cli.app forge --json` when strategy intent, focus assets, or AGENT-facing navigation needs refresh.
2. Run `python -m src.cli.app focus show --json` if the current surface or pack routing is unclear.
3. Run `python -m src.cli.app validate --config config/strategy_config.toml --json` after code or config edits.
4. Run `python -m src.cli.app focus test --json` as the default smoke loop.
5. Run `python -m src.cli.app backtest --config config/strategy_config.toml --start 2025-01-01 --end 2025-03-01 --no-chart --json` when behavior or parameter effects need execution evidence.
6. Run `python -m src.cli.app run --mode standalone --config config/strategy_config.toml --paper --json` only for runtime lifecycle, monitoring, or live-loop work.
7. Run `python -m src.cli.app doctor --json` when environment health, dependency setup, or runtime prerequisites are in doubt.

## Source-Of-Truth Order

1. `strategy_spec.toml`
2. `.focus/context.json`
3. `.focus/*.md`
4. `tests/TEST.md`
5. `artifacts/*/latest.json`

When these disagree, prefer the generator-backed source over generated markdown and regenerate instead of hand-maintaining drift.

## Typical Editable Surface In Upstream OptionForge

The upstream `.focus/context.json` currently marks these as editable:

- `src/strategy/strategy_entry.py`
- `src/strategy/application`
- `src/strategy/domain`
- `config/strategy_config.toml`
- `config/general/trading_target.toml`
- `config/domain_service`
- `tests/strategy`
- `tests/web`

Read the local `.focus/context.json` before assuming the same list still applies in another checkout.

## Boundary Rules

- Stay inside `surfaces.editable` by default.
- Treat `src/main`, `src/backtesting`, `src/web`, `src/cli`, `deploy`, and `doc` as reference surfaces unless the task directly targets them.
- Treat `.codex`, `.git`, caches, virtualenvs, and license files as frozen unless the task explicitly requires otherwise.
- Explain any surface expansion in the delivery summary.

## Delivery Checklist

Every delivery should state:

- which workflow entrypoints were used
- which source-of-truth assets were consulted
- which surface was edited
- which structured verification steps ran
- whether `tests/TEST.md` or `artifacts/*/latest.json` changed
- which risks, skips, or data assumptions remain

## License Note

Upstream OptionForge is licensed under AGPL-3.0. When using this skill outside an OptionForge checkout, prefer architecture notes, command patterns, and file mapping over verbatim code copying, and ask before porting protected source into a different project.
