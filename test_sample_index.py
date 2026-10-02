"""Exercise the notebook's row bounds check without loading a model."""
import ast
import json
from pathlib import Path

notebook = json.loads((Path(__file__).parent / "notebooks" / "tabular-load-saved-model-single-training.ipynb").read_text(encoding="utf-8"))
cell = next(cell for cell in notebook["cells"] if "sample_row = input_df.iloc" in "".join(cell["source"]))
tree = ast.parse("".join(cell["source"]))
guard = next(node for node in tree.body if isinstance(node, ast.If) and "SAMPLE_ROW_INDEX" in ast.unparse(node.test))
code = compile(ast.Module(body=[guard], type_ignores=[]), "notebook-index-check", "exec")
for index, valid in [(-1, False), (0, True), (2, True), (3, False)]:
    try:
        exec(code, {"SAMPLE_ROW_INDEX": index, "input_df": [0, 1, 2]})
    except IndexError:
        assert not valid, index
    else:
        assert valid, index
print("Sample index bounds passed.")
