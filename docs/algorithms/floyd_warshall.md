<div align="center">

# `floyd_warshall` · Floyd-Warshall

**Graph** · average `O(V^3)` · space `O(V^2)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Computes all-pairs shortest paths by relaxing every pair through each intermediate vertex in turn.

## Signature

```python
def floyd_warshall_<file>_<block>(matrix):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(V^3)` | `O(V^2)` |
| Average | `O(V^3)` | `O(V^2)` |
| Worst | `O(V^3)` | `O(V^2)` |

## In the dataset

- **3,123** implementations across **1,000** files.
- Namespaced as `floyd_warshall_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0006.py` → `floyd_warshall_0006_0004`.

## Example

Loaded from `algorithms/algorithm-0006.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0006", "algorithms/algorithm-0006.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

matrix = [[0, 3, 9], [10 ** 9, 0, 1], [10 ** 9, 10 ** 9, 0]]
result = module.floyd_warshall_0006_0004(matrix)
print(result)
```

Output:

```text
[[0, 3, 4], [1000000000, 0, 1], [1000000000, 1000000000, 0]]
```

## Notes

- Works on dense graphs given as an adjacency matrix.
- Infinity is represented by a large sentinel value in the matrix.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
