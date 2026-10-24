<div align="center">

# `subsets` · Subsets (Power Set)

**Data structures & misc** · average `O(n * 2^n)` · space `O(n * 2^n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Bitmask enumeration of the power set: each mask selects a subset of the input positions.

## Signature

```python
def subsets_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n * 2^n)` | `O(n * 2^n)` |
| Average | `O(n * 2^n)` | `O(n * 2^n)` |
| Worst | `O(n * 2^n)` | `O(n * 2^n)` |

## In the dataset

- **3,110** implementations across **1,000** files.
- Namespaced as `subsets_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0015.py` → `subsets_0015_0010`.

## Example

Loaded from `algorithms/algorithm-0015.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0015", "algorithms/algorithm-0015.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.subsets_0015_0010([1, 2])
print(result)
```

Output:

```text
[[], [1], [2], [1, 2]]
```

## Notes

- Generates 2^n subsets, including the empty set.
- Order follows the ascending mask value.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
