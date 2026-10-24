<div align="center">

# `insertion_sort` · Insertion Sort

**Sorting** · average `O(n^2)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Builds the sorted list one element at a time, shifting larger elements right until the current value finds its place.

## Signature

```python
def insertion_sort_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n)` | `O(n)` |
| Average | `O(n^2)` | `O(n)` |
| Worst | `O(n^2)` | `O(n)` |

## In the dataset

- **3,135** implementations across **1,000** files.
- Namespaced as `insertion_sort_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0002.py` → `insertion_sort_0002_0001`.

## Example

Loaded from `algorithms/algorithm-0002.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0002", "algorithms/algorithm-0002.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [5, 3, 9, 1, 7]
result = module.insertion_sort_0002_0001(values)
print(result)
```

Output:

```text
[1, 3, 5, 7, 9]
```

## Notes

- Excellent for small or nearly sorted lists.
- Stable, with a copy of the input returned.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
