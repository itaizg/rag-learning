#!/usr/bin/env bash
# Goal check: the core notebook stack imports cleanly in the uv venv.
# Use this as the "done" check when fixing an environment/dependency problem.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT" || exit 1

.venv/bin/python - <<'PYEOF'
import importlib, sys

mods = [
    "torch", "transformers", "sentence_transformers", "sklearn",
    "numpy", "pandas", "matplotlib", "plotly", "datasets",
    "anthropic", "openai", "dotenv",
    "langgraph", "langchain_anthropic", "langsmith",
]
fail = 0
for m in mods:
    try:
        importlib.import_module(m)
    except Exception as e:
        print(f"FAIL import {m}: {type(e).__name__}: {e}")
        fail = 1
if not fail:
    print(f"PASS imports: {len(mods)} core packages import clean")
sys.exit(fail)
PYEOF
