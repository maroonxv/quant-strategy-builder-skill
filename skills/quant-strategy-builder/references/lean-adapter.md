# LEAN Adapter

Load this reference when the workspace is based on QuantConnect LEAN.

## Workspace Markers

- `AlgorithmImports.py`
- `main.py`, `research.ipynb`, or `*.csproj`
- `QCAlgorithm` subclasses
- `QuantConnect/` namespaces or LEAN-specific project layout

## Typical Edit Surface

- strategy class methods such as `Initialize`, `OnData`, scheduled handlers, and helper modules
- universe selection, alpha, portfolio construction, risk, or execution model hooks
- config or parameters passed through LEAN project settings

## China-Market Notes

- if the repo uses mainland China data through custom imports, set `Asia/Shanghai` time assumptions explicitly and verify market hours instead of relying on generic defaults
- model A-share and ETF realities such as 100-share round lots, T+1 sell constraints, price limits, and auction behavior in custom execution, fill, or risk components
- keep China futures or options metadata explicit: multiplier, expiration, roll logic, session boundaries, margin, and exercise handling should live in strategy or model code, not in ad-hoc symbol parsing
- when a venue is only partially supported, state clearly which parts are native LEAN behavior and which parts are custom-data or custom-model simulation

## Preferred Verification

- focused backtests on the changed strategy or algorithm
- deterministic unit tests for helper modules outside `QCAlgorithm`
- inspection of order events, insight generation, portfolio targets, and benchmark comparison

## Common Pitfalls

- putting too much strategy logic directly in `OnData` without reusable helpers
- mixing research-notebook logic with production algorithm code
- ignoring fees, slippage, fill models, or warm-up requirements
- assuming imported China-market data automatically carries the right exchange calendar, trading hours, or execution constraints
