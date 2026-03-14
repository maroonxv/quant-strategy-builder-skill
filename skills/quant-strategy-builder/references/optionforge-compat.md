# OptionForge Compatibility Notes

Load this reference only when the workspace is clearly an OptionForge checkout or when the user explicitly asks for OptionForge compatibility.

## Workspace Markers

- `strategy_spec.toml`
- `.focus/context.json`
- `src/strategy/`
- `python -m src.cli.app --help`

## Source-Of-Truth Order

1. `strategy_spec.toml`
2. `.focus/context.json`
3. `.focus/*.md`
4. `tests/TEST.md`
5. `artifacts/*/latest.json`

When these disagree, prefer the generator-backed source over generated markdown.

## Preferred Command Entry

- Use `python -m src.cli.app ...` from a source checkout.
- Prefer `--json` whenever the command supports it.

## Default Command Loop

1. Run `python -m src.cli.app forge --json` when strategy intent, focus assets, or AGENT-facing navigation needs refresh.
2. Run `python -m src.cli.app focus show --json` if the current editable surface is unclear.
3. Run `python -m src.cli.app validate --config config/strategy_config.toml --json` after code or config edits.
4. Run `python -m src.cli.app focus test --json` as the default smoke loop.
5. Run `python -m src.cli.app backtest --config config/strategy_config.toml --start 2025-01-01 --end 2025-03-01 --no-chart --json` when behavior changes need execution evidence.

## Boundary Rules

- Stay inside `.focus/context.json -> surfaces.editable` by default.
- Treat `src/main`, `src/backtesting`, `src/web`, and `src/cli` as reference surfaces unless the task directly targets them.
- Explain any editable-surface expansion in the delivery summary.

## Delivery Requirements

State:

- which workflow entrypoints were used
- which source-of-truth assets were consulted
- whether edits stayed inside the editable surface
- which structured verification steps ran
- whether `tests/TEST.md` or `artifacts/*/latest.json` changed
