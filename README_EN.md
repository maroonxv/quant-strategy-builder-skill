# Quant Strategy Builder

[![Validate Skill](https://github.com/maroonxv/quant-strategy-builder-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/maroonxv/quant-strategy-builder-skill/actions/workflows/validate-skill.yml)

English version. Chinese-first repo overview lives in [README.md](README.md).

`quant-strategy-builder` is a reusable agent skill for Codex, Claude Code, and other `SKILL.md`-compatible coding agents. It helps turn a vague market idea into a smaller, safer strategy change set with explicit checks for signal logic, position sizing, risk controls, backtests, and delivery evidence.

This repository is the GitHub-facing wrapper for the installable skill in `skills/quant-strategy-builder/`. The current positioning is China-market-first, with prompt examples and delivery guidance centered on A-shares, ETFs, China futures, and exchange-listed options.

## Why This Skill Exists

Most "quant prompts" stop at brainstorming. This skill is built to help agents:

- decompose a strategy into universe, data, signal, entry, exit, sizing, risk, execution, and observability
- detect the active framework before editing code
- prefer config and existing extension points over unnecessary rewrites
- choose the cheapest convincing proof for every change
- deliver structured evidence instead of vague "should work" summaries

## Supported Agents

The same core skill is designed to work across multiple coding agents:

- Codex, via `skills/quant-strategy-builder/agents/openai.yaml`
- Claude Code, via the same `SKILL.md`
- other `SKILL.md`-aware runtimes

## Supported Frameworks

Version 1 ships with a framework-agnostic core workflow plus China-market-first adapters for:

- VeighNa / vn.py
- RQAlpha
- TqSdk
- qteasy
- OptionForge

It also keeps compatibility references for:

- LEAN / QuantConnect
- Freqtrade
- Backtrader

If the repo does not match one of these engines, the skill falls back to a generic design-and-verification workflow.

## Install

### Codex

Copy the installable skill directory into your Codex skills folder:

```powershell
New-Item -ItemType Directory -Force -Path "$env:CODEX_HOME\\skills" | Out-Null
Copy-Item -Recurse -Force ".\\skills\\quant-strategy-builder" "$env:CODEX_HOME\\skills\\quant-strategy-builder"
```

### Claude Code

Copy the same skill directory into your Claude Code user skills folder:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\\.claude\\skills" | Out-Null
Copy-Item -Recurse -Force ".\\skills\\quant-strategy-builder" "$HOME\\.claude\\skills\\quant-strategy-builder"
```

If you want the skill to be project-local for Claude Code, copy it into `.claude/skills/quant-strategy-builder/` inside the target repo instead.

If you prefer to inspect before installing, start with [skills/quant-strategy-builder/SKILL.md](skills/quant-strategy-builder/SKILL.md).

## Copy-Paste Prompts

These prompts are intentionally agent-neutral. In Codex, you can explicitly invoke `$quant-strategy-builder`. In Claude Code, ask Claude to use the `quant-strategy-builder` skill with the same task text.

- `Use the quant-strategy-builder skill to turn a CSI 300 mean-reversion idea into a testable strategy with entry and exit rules, volatility-aware sizing, and a focused validation plan.`
- `Use the quant-strategy-builder skill to adapt my China commodity futures strategy so it handles main-contract rolls, night-session filters, realistic fees, and cleaner risk rules.`
- `Use the quant-strategy-builder skill to build a 50ETF options income strategy with strike selection, assignment handling, and backtest evidence.`
- `Use the quant-strategy-builder skill to review this Backtrader strategy and tell me whether the A-share timing signal, sizing, and analyzer setup are aligned or fighting each other.`
- `Use the quant-strategy-builder skill to port this OptionForge strategy idea into the right domain, config, and test surfaces while keeping the editable surface small.`

More prompts live in [examples/prompt-gallery.md](examples/prompt-gallery.md).

## Repository Layout

```text
.
|-- README.md
|-- README_EN.md
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

## What Makes It Useful

- It is not tied to one engine, but it still respects real framework seams.
- The same core `SKILL.md` travels cleanly between Codex and Claude Code.
- It now speaks more directly to China-market workflows across A-shares, ETFs, futures, and options, including common open-source stacks such as vn.py, RQAlpha, TqSdk, and qteasy.
- It is small enough to install quickly, but opinionated enough to reduce agent drift.
- It keeps human-facing positioning in the repo root and agent-facing rules inside the skill itself.
