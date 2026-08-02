#!/usr/bin/env bash
# Creates the isolated .venv-frameworks used by 04_agents/20b_agent_framework_tradeoffs.ipynb.
# These third-party frameworks (crewai in particular) pin rich<15, which conflicts with this
# repo's main .venv (rich>=15.0.0, used by ragkit.pretty). Keeping them in a separate venv means
# the other 60+ notebooks are never touched by this dependency.
set -euo pipefail
cd "$(dirname "$0")/.."

uv venv .venv-frameworks --python 3.13
uv pip install --python .venv-frameworks \
  crewai autogen-agentchat "autogen-ext[anthropic]" "openai-agents[litellm]" \
  anthropic python-dotenv fastapi uvicorn httpx

echo "Isolated frameworks venv ready at .venv-frameworks/"
