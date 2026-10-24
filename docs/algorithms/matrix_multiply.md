<div align="center">

# `matrix_multiply` · Matrix Multiplication

**Math & backtracking** · average `O(n^3)` · space `O(n^2)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Standard triple-nested-loop multiplication of two dense matrices.

## Signature

```python
def matrix_multiply_<file>_<block>(left, right):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n^3)` | `O(n^2)` |
| Average | `O(n^3)` | `O(n^2)` |
| Worst | `O(n^3)` | `O(n^2)` |

## In the dataset

- **3,111** implementations across **1,000** files.
- Namespaced as `matrix_multiply_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0003.py` → `matrix_multiply_0003_0004`.

## Example

Loaded from `algorithms/algorithm-0003.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0003", "algorithms/algorithm-0003.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

left = [[1, 2], [3, 4]]
right = [[5, 6], [7, 8]]
result = module.matrix_multiply_0003_0004(left, right)
print(result)
```

Output:

```text
[[19, 22], [43, 50]]
```

## Notes

- The shared dimension comes from the number of rows in the right matrix.
- Returns a new matrix; both inputs are left unchanged.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
