#!/usr/bin/env bash
# Goal check: notebook(s) execute top-to-bottom with no errors.
# This is the repo's real "tests green" — every notebook must run clean
# before it is considered done (see CLAUDE.md > Technical conventions).
#
# Usage:
#   .claude/checks/notebooks.sh                      # all tier notebooks (00–06)
#   .claude/checks/notebooks.sh 01_foundations/04_attention_mechanism.ipynb
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT" || exit 1

if [ "$#" -gt 0 ]; then
  set -- "$@"
else
  set -- $(find 0[0-6]_* -name '*.ipynb' -not -path '*/.ipynb_checkpoints/*' | sort)
fi

.venv/bin/python - "$@" <<'PYEOF'
import sys, nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

fail = 0
for nb_path in sys.argv[1:]:
    nb = nbformat.read(nb_path, as_version=4)
    try:
        NotebookClient(nb, timeout=600, kernel_name="python3").execute()
        print(f"PASS {nb_path}")
    except CellExecutionError as e:
        print(f"FAIL {nb_path}: {str(e).splitlines()[-1][:200]}")
        fail = 1
    except Exception as e:
        print(f"ERR  {nb_path}: {type(e).__name__}: {e}")
        fail = 1
sys.exit(fail)
PYEOF
