# Quant Strategy Builder

[![Validate Skill](https://github.com/maroonxv/quant-strategy-builder-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/maroonxv/quant-strategy-builder-skill/actions/workflows/validate-skill.yml)

中文说明为主，英文版本见 [README_EN.md](README_EN.md)。

`quant-strategy-builder` 是一个可复用的 agent skill，适用于 Codex、Claude Code 和其他兼容 `SKILL.md` 的编码代理。它帮助代理把模糊的市场想法收敛为更小、更安全的策略改动，并明确覆盖信号逻辑、仓位管理、风险控制、回测验证和交付证据。

这个仓库主要用于 GitHub 展示、分发和安装说明，真正可安装的 skill 位于 `skills/quant-strategy-builder/`。当前版本以中国市场场景为主，优先面向 A 股、ETF、国内商品期货、股指期货与场内期权策略设计。

## 这个 Skill 解决什么问题

很多“量化提示词”只停留在策略脑暴阶段，这个 skill 更关注把想法落到可验证的最小改动上。它会引导代理：

- 把策略拆成标的池、数据、信号、开平仓、仓位、风险、执行和可观测性
- 改代码前先识别当前框架和已有扩展点
- 优先复用参数和现有结构，而不是盲目重写
- 为每次改动匹配成本最低但足够有说服力的验证方式
- 最终交付带证据的结果，而不是“应该可以”的口头判断

## 适用代理

同一套核心 skill 可以复用于多种编码代理：

- Codex：通过 `skills/quant-strategy-builder/agents/openai.yaml`
- Claude Code：复用同一个 `SKILL.md`
- 其他兼容 `SKILL.md` 的 agent runtime

## 适用框架

当前版本提供一个框架无关的核心流程，并优先附带以下中国市场相关适配参考：

- VeighNa / vn.py
- RQAlpha
- TqSdk
- qteasy
- OptionForge

同时保留以下通用或国际框架参考：

- LEAN / QuantConnect
- Freqtrade
- Backtrader

如果仓库不属于上述框架，skill 会退回到通用的策略设计与验证流程。

## 安装

### Codex

把可安装 skill 目录复制到 Codex 的 skills 目录：

```powershell
New-Item -ItemType Directory -Force -Path "$env:CODEX_HOME\\skills" | Out-Null
Copy-Item -Recurse -Force ".\\skills\\quant-strategy-builder" "$env:CODEX_HOME\\skills\\quant-strategy-builder"
```

### Claude Code

把同一个 skill 目录复制到 Claude Code 的用户 skills 目录：

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\\.claude\\skills" | Out-Null
Copy-Item -Recurse -Force ".\\skills\\quant-strategy-builder" "$HOME\\.claude\\skills\\quant-strategy-builder"
```

如果你希望只在某个项目内使用，也可以把它复制到目标仓库的 `.claude/skills/quant-strategy-builder/`。

如果想先看说明，再决定是否安装，可以先阅读 [skills/quant-strategy-builder/SKILL.md](skills/quant-strategy-builder/SKILL.md)。

## 可直接复用的提示词

这些提示词尽量保持 agent-neutral。在 Codex 中可以显式调用 `$quant-strategy-builder`；在 Claude Code 中可以直接要求使用 `quant-strategy-builder` skill。

- `使用 quant-strategy-builder skill，把一个沪深300成分股均值回归想法整理成可测试策略，补齐入场、出场、波动率约束仓位和最小可行验证计划。`
- `使用 quant-strategy-builder skill，改造我的中国商品期货趋势策略，让它支持主力合约切换、夜盘过滤、手续费假设和更清晰的风险规则。`
- `使用 quant-strategy-builder skill，为上证50ETF期权设计一个备兑或轮动卖方策略，明确行权价筛选、到期日选择、指派处理和回测证据。`
- `使用 quant-strategy-builder skill，审查这个 Backtrader 策略，判断 A 股择时信号、仓位控制和分析器配置是否协调。`
- `使用 quant-strategy-builder skill，把这个 OptionForge 策略想法映射到正确的领域层、配置层和测试层，并保持最小改动面。`

更多示例见 [examples/prompt-gallery.md](examples/prompt-gallery.md)。

## 仓库结构

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

## 校验

提交 PR 前，先运行仓库内置校验脚本：

```powershell
python .\scripts\validate_skill.py
```

## 这个仓库的特点

- 不绑定单一引擎，但尊重真实框架边界和扩展点。
- 同一份核心 `SKILL.md` 可以在 Codex 和 Claude Code 间复用。
- 从文案到提示词都优先贴近中国市场，并补入 vn.py、RQAlpha、TqSdk、qteasy 这些常见开源工作流。
- 安装体积小，但对策略拆解、验证和交付有明确约束，能减少 agent 漂移。
- 根目录面向人类读者，skill 目录面向 agent，两层职责分离清晰。

## 维护说明

- 根目录负责 GitHub 展示、安装说明和公共定位。
- `skills/quant-strategy-builder/` 负责真正可安装的 skill 内容。
- 框架特有规则放在 `references/*-adapter.md`，不要重新堆回核心 `SKILL.md`。
