<div align="center">

# `n_queens` · N-Queens

**Math & backtracking** · average `O(n!)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Backtracking search that places one queen per row while pruning attacked columns and diagonals.

## Signature

```python
def n_queens_<file>_<block>(size=<default>):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n!)` | `O(n)` |
| Average | `O(n!)` | `O(n)` |
| Worst | `O(n!)` | `O(n)` |

## In the dataset

- **3,107** implementations across **1,000** files.
- Namespaced as `n_queens_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0005.py` → `n_queens_0005_0002`.

## Example

Loaded from `algorithms/algorithm-0005.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0005", "algorithms/algorithm-0005.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.n_queens_0005_0002(6)
print(result)
```

Output:

```text
4
```

## Notes

- Counts complete solutions rather than returning boards.
- The board size is baked into each variant's default argument.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
