# Prompt Gallery

These prompts are written for direct reuse in skill-aware coding agents such as Codex and Claude Code. The default framing is China-market-first; replace framework, exchange, and contract details to match your repo.

If you want explicit invocation, use `$quant-strategy-builder` in Codex or ask Claude Code to use the `quant-strategy-builder` skill with the same task text.

## Generic Research

- `使用 quant-strategy-builder skill，把一个沪深300成分股均值回归想法整理成具体方案，补齐标的池、z-score 进出场、T+1 约束、仓位规则和最小回测计划。`
- `使用 quant-strategy-builder skill，审查这个策略仓库，判断标的池、数据、信号、仓位和执行逻辑是否清晰分层，还是混在一起。`
- `使用 quant-strategy-builder skill，把这个商品期货突破策略从 notebook 迁移成可维护的策略代码，并补上明确测试和验证步骤。`

## VeighNa / vn.py

- `使用 quant-strategy-builder skill，为 vn.py CTA 策略实现一套螺纹钢主力合约趋势跟随逻辑，明确主力切换、夜盘过滤、手续费、滑点和风控参数。`
- `使用 quant-strategy-builder skill，改造这个 vn.py 项目里的 50ETF 期权策略，补齐行权价筛选、到期梯度、备兑约束和回测证据。`

## RQAlpha

- `使用 quant-strategy-builder skill，在这个 RQAlpha 项目里做一个 A 股 ETF 轮动策略，要求明确 scheduler、sys_risk 约束和 analyser 输出。`
- `使用 quant-strategy-builder skill，把这个 RQAlpha 股票策略扩展成股票加股指期货对冲方案，并验证账户模型、调仓节奏和风险指标。`

## TqSdk

- `使用 quant-strategy-builder skill，为这个 TqSdk 期货策略加上夜盘过滤、开平仓节奏和 TqBacktest 验证，并检查 TargetPosTask 是否适合当前执行逻辑。`
- `使用 quant-strategy-builder skill，基于 TqSdk 给中证1000股指期货做一个日内突破策略，要求包含交易时段、止损、手续费和回测证据。`

## qteasy

- `使用 quant-strategy-builder skill，改造这个 qteasy A 股策略，让它显式处理 T+1、trade_batch_size=100、费用模型和 use_latest_data_cycle 设定。`
- `使用 quant-strategy-builder skill，为这个 qteasy 项目组合两个 A 股选股策略，并说明多策略信号如何合并、回测如何验证。`

## OptionForge

- `使用 quant-strategy-builder skill，在 OptionForge 中落地一个上证50ETF期权收入策略，保持在可编辑范围内，并报告 validate、focus test 和 backtest 证据。`
- `使用 quant-strategy-builder skill，把这个中国 ETF 期权思路映射到正确的 OptionForge config、domain-service 和 test surfaces，再开始修改。`

## Compatibility Engines

- `Use the quant-strategy-builder skill to adapt this Backtrader A-share timing strategy so it respects round lots, T+1 assumptions, and explicit analyzer output.`
- `Use the quant-strategy-builder skill to port a China-market ETF options idea into LEAN while keeping strike selection, exercise handling, and evidence explicit.`
