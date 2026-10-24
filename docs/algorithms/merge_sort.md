<div align="center">

# `merge_sort` · Merge Sort

**Sorting** · average `O(n log n)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Splits the list in half, sorts each half recursively, then merges the two sorted halves into one sequence.

## Signature

```python
def merge_sort_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n log n)` | `O(n)` |
| Average | `O(n log n)` | `O(n)` |
| Worst | `O(n log n)` | `O(n)` |

## In the dataset

- **3,123** implementations across **1,000** files.
- Namespaced as `merge_sort_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0003.py` → `merge_sort_0003_0007`.

## Example

Loaded from `algorithms/algorithm-0003.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0003", "algorithms/algorithm-0003.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [5, 3, 9, 1, 7]
result = module.merge_sort_0003_0007(values)
print(result)
```

Output:

```text
[1, 3, 5, 7, 9]
```

## Notes

- Stable with a guaranteed O(n log n) worst case.
- Needs O(n) auxiliary space for the merge step.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
