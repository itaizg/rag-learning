"""Programmatic notebook builder used to generate this repo's notebooks.

Usage:
    from nbgen import md, code, write_nb
    cells = [md("# Title\n..."), code("print('hi')"), ...]
    write_nb(cells, "01_foundations/01_neural_networks.ipynb")
"""
import nbformat


def md(source: str) -> dict:
    return nbformat.v4.new_markdown_cell(source)


def code(source: str) -> dict:
    return nbformat.v4.new_code_cell(source)


def write_nb(cells: list, path: str) -> None:
    nb = nbformat.v4.new_notebook()
    for i, cell in enumerate(cells, start=1):
        cell["id"] = f"cell{i:03d}"
    nb["cells"] = cells
    nb["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.13.7",
        },
    }
    nbformat.write(nb, path)
    print(f"wrote {path} ({len(cells)} cells)")
