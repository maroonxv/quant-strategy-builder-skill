# Quant Strategy Builder

[![Validate Skill](https://github.com/maroonxv/optionforge-strategy-builder-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/maroonxv/optionforge-strategy-builder-skill/actions/workflows/validate-skill.yml)

English-first, with concise Chinese notes for maintainers and contributors.

`quant-strategy-builder` is a reusable Codex skill for designing, adapting, and verifying quantitative trading strategies across multiple frameworks. It helps an agent turn a vague market idea into a smaller, safer change set with explicit checks for signal logic, position sizing, risk controls, backtests, and delivery evidence.

中文说明：这个仓库现在是一个面向 GitHub 展示和分发的公开项目，真正可安装的 skill 位于 `skills/quant-strategy-builder/`。

## Why This Skill Exists

Most "quant prompts" stop at brainstorming. This skill is built to help agents:

- decompose a strategy into universe, data, signal, entry, exit, sizing, risk, execution, and observability
- detect the active framework before editing code
- prefer config and existing extension points over unnecessary rewrites
- choose the cheapest convincing proof for every change
- deliver structured evidence instead of vague "should work" summaries

## Supported Frameworks

Version 1 ships with a framework-agnostic core workflow plus adapters for:

- LEAN / QuantConnect
- Freqtrade
- Backtrader
- OptionForge

If the repo does not match one of these engines, the skill falls back to a generic design-and-verification workflow.

## Install

Copy the installable skill directory into your Codex skills folder:

```powershell
New-Item -ItemType Directory -Force -Path "$env:CODEX_HOME\\skills" | Out-Null
Copy-Item -Recurse -Force ".\\skills\\quant-strategy-builder" "$env:CODEX_HOME\\skills\\quant-strategy-builder"
```

If you prefer to inspect before installing, start with [skills/quant-strategy-builder/SKILL.md](skills/quant-strategy-builder/SKILL.md).

## Copy-Paste Prompts

- `Use $quant-strategy-builder to turn a mean-reversion idea on liquid US equities into a testable strategy with entry and exit rules, volatility-aware sizing, and a focused validation plan.`
- `Use $quant-strategy-builder to adapt my Freqtrade strategy so it handles leverage, protections, and realistic fee assumptions without duplicating indicators.`
- `Use $quant-strategy-builder to build a LEAN options strategy for covered calls with strike selection, assignment handling, and backtest evidence.`
- `Use $quant-strategy-builder to review this Backtrader strategy and tell me whether the signal, sizing, and analyzer setup are aligned or fighting each other.`
- `Use $quant-strategy-builder to port this OptionForge strategy idea into the right domain, config, and test surfaces while keeping the editable surface small.`

More prompts live in [examples/prompt-gallery.md](examples/prompt-gallery.md).

## Repository Layout

```text
.
|-- README.md
|-- AGENTS.md
|-- examples/
|   `-- prompt-gallery.md
|-- scripts/
|   `-- validate_skill.py
|-- .github/workflows/
|   `-- validate-skill.yml
`-- skills/
    `-- quant-strategy-builder/
        |-- SKILL.md
        |-- agents/openai.yaml
        `-- references/
```

## Validate

Run the repository-local validator before opening a PR:

```powershell
python .\scripts\validate_skill.py
```

## What Makes It Star-Worthy

- It is not tied to one engine, but it still respects real framework seams.
- It covers both stock and options workflows, including Greeks-aware scenarios.
- It is small enough to install quickly, but opinionated enough to reduce agent drift.
- It is documented for humans at the repo root and documented for agents inside the skill itself.

## Chinese Maintainer Notes

- 根目录负责 GitHub 传播和安装说明。
- `skills/quant-strategy-builder/` 负责真正的 skill 内容。
- 框架特有规则放在 `references/*-adapter.md`，不要重新塞回核心 `SKILL.md`。
