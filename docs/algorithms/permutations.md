<div align="center">

# `permutations` · Permutations

**Data structures & misc** · average `O(n! * n)` · space `O(n! * n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Backtracking enumeration of every ordering of the input values, tracking which positions are already used.

## Signature

```python
def permutations_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n!)` | `O(n! * n)` |
| Average | `O(n! * n)` | `O(n! * n)` |
| Worst | `O(n! * n)` | `O(n! * n)` |

## In the dataset

- **3,121** implementations across **1,000** files.
- Namespaced as `permutations_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0001.py` → `permutations_0001_0001`.

## Example

Loaded from `algorithms/algorithm-0001.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0001", "algorithms/algorithm-0001.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.permutations_0001_0001([1, 2])
print(result)
```

Output:

```text
[(1, 2), (2, 1)]
```

## Notes

- Produces n! tuples.
- Duplicate values are treated as distinct positions.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
