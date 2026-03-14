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

## Preferred Verification

- focused backtests on the changed strategy or algorithm
- deterministic unit tests for helper modules outside `QCAlgorithm`
- inspection of order events, insight generation, portfolio targets, and benchmark comparison

## Common Pitfalls

- putting too much strategy logic directly in `OnData` without reusable helpers
- mixing research-notebook logic with production algorithm code
- ignoring fees, slippage, fill models, or warm-up requirements
