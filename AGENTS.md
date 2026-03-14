# Repository Routing

This repository is a GitHub-facing wrapper around one installable skill.

## For Agents

- Start with [skills/quant-strategy-builder/SKILL.md](skills/quant-strategy-builder/SKILL.md) when the task is about quantitative strategy design, backtests, framework adaptation, or verification.
- Use [README.md](README.md) for the Chinese-first project positioning, installation steps, and prompt examples.
- Use [README_EN.md](README_EN.md) when the user explicitly needs English-facing copy.
- Use [examples/prompt-gallery.md](examples/prompt-gallery.md) when the user needs copy-paste prompts or trigger phrases.

## Editing Rules

- Keep the installable skill under `skills/quant-strategy-builder/`.
- Keep framework-specific guidance in adapter references, not in the root README.
- If the public positioning changes, update both `README.md` and `skills/quant-strategy-builder/agents/openai.yaml`.
