#!/usr/bin/env bash
# Goal check: every notebook code cell and every ragkit/agentkit module parses.
# Fast syntax gate (no execution) — catches broken cells before the slower
# notebooks.sh run. Reports the first syntax error per file.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT" || exit 1

.venv/bin/python - <<'PYEOF'
import ast, sys, pathlib, nbformat

fail = 0

# 1. Notebook code cells
for nb_path in sorted(pathlib.Path(".").glob("[0-9][0-9]_*/**/*.ipynb")):
    if ".ipynb_checkpoints" in str(nb_path):
        continue
    nb = nbformat.read(str(nb_path), as_version=4)
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code":
            continue
        src = "".join(
            l for l in cell.source.splitlines(keepends=True)
            if not l.lstrip().startswith(("%", "!"))  # strip magics/shell lines
        )
        try:
            ast.parse(src)
        except SyntaxError as e:
            print(f"FAIL {nb_path} cell {i}: {e}")
            fail = 1

# 2. ragkit + agentkit package modules
for pkg in ("ragkit", "agentkit"):
    for py in sorted(pathlib.Path(pkg).rglob("*.py")):
        try:
            ast.parse(py.read_text())
        except SyntaxError as e:
            print(f"FAIL {py}: {e}")
            fail = 1

if not fail:
    print("PASS lint: all notebook cells and ragkit/agentkit modules parse")
sys.exit(fail)
PYEOF
