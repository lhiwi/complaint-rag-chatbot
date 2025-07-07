#!/usr/bin/env python3
import nbformat, glob, os

for path in glob.glob("notebooks/*.ipynb"):
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    # Remove top-level widgets metadata
    nb.metadata.pop("widgets", None)
    # Remove any cell-level widgets metadata
    for cell in nb.cells:
        cell.metadata.pop("widgets", None)
    # Write back
    with open(path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)
    print("Cleaned:", path)
