<div align="center">

# `selection_sort` · Selection Sort

**Sorting** · average `O(n^2)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Scans for the smallest remaining element and swaps it into the next position of the output.

## Signature

```python
def selection_sort_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n^2)` | `O(n)` |
| Average | `O(n^2)` | `O(n)` |
| Worst | `O(n^2)` | `O(n)` |

## In the dataset

- **3,113** implementations across **1,000** files.
- Namespaced as `selection_sort_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0007.py` → `selection_sort_0007_0007`.

## Example

Loaded from `algorithms/algorithm-0007.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0007", "algorithms/algorithm-0007.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [5, 3, 9, 1, 7]
result = module.selection_sort_0007_0007(values)
print(result)
```

Output:

```text
[1, 3, 5, 7, 9]
```

## Notes

- Performs at most n - 1 swaps, which matters when writes are expensive.
- Not stable relative to equal keys.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
