"""Execute notebook(s) top-to-bottom in-place, writing outputs back to the file.

Usage: .venv/bin/python tools/run_nb.py path/to/notebook.ipynb [more.ipynb ...]
"""
import sys
import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

fail = 0
for nb_path in sys.argv[1:]:
    nb = nbformat.read(nb_path, as_version=4)
    try:
        NotebookClient(nb, timeout=600, kernel_name="python3").execute()
        nbformat.write(nb, nb_path)
        print(f"PASS {nb_path}")
    except CellExecutionError as e:
        nbformat.write(nb, nb_path)
        print(f"FAIL {nb_path}: {e}")
        fail = 1

sys.exit(fail)
