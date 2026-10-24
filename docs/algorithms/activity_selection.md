<div align="center">

# `activity_selection` · Activity Selection

**DP & greedy** · average `O(n log n)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Greedily selects the maximum number of non-overlapping intervals by always taking the one that finishes earliest.

## Signature

```python
def activity_selection_<file>_<block>(activities):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n log n)` | `O(n)` |
| Average | `O(n log n)` | `O(n)` |
| Worst | `O(n log n)` | `O(n)` |

## In the dataset

- **3,123** implementations across **1,000** files.
- Namespaced as `activity_selection_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0010.py` → `activity_selection_0010_0001`.

## Example

Loaded from `algorithms/algorithm-0010.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0010", "algorithms/algorithm-0010.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
result = module.activity_selection_0010_0001(activities)
print(result)
```

Output:

```text
[(1, 4), (5, 7), (8, 11), (12, 16)]
```

## Notes

- Activities are (start, end) tuples.
- Sorting by finish time is the key greedy step.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
