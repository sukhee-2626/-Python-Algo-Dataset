<div align="center">

# `binary_search` · Binary Search

**Search** · average `O(log n)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Locates a target value in a sorted sequence by repeatedly halving the search interval. Each step compares the middle element and discards the half that cannot contain the target.

## Signature

```python
def binary_search_<file>_<block>(values, target):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(1)` |
| Average | `O(log n)` | `O(1)` |
| Worst | `O(log n)` | `O(1)` |

## In the dataset

- **3,103** implementations across **1,000** files.
- Namespaced as `binary_search_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0017.py` → `binary_search_0017_0005`.

## Example

Loaded from `algorithms/algorithm-0017.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0017", "algorithms/algorithm-0017.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [2, 4, 6, 8, 10, 12]
result = module.binary_search_0017_0005(values, 8)
print(result)
```

Output:

```text
3
```

## Notes

- Requires the input to be sorted in ascending order.
- Returns the index of the target, or -1 when the value is absent.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
