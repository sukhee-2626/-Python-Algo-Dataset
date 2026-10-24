<div align="center">

# `bubble_sort` · Bubble Sort

**Sorting** · average `O(n^2)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Repeatedly swaps adjacent out-of-order pairs, bubbling the largest remaining value to the end of the list on each pass.

## Signature

```python
def bubble_sort_<file>_<block>(values, early_exit=True):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n)` | `O(n)` |
| Average | `O(n^2)` | `O(n)` |
| Worst | `O(n^2)` | `O(n)` |

## In the dataset

- **3,091** implementations across **1,000** files.
- Namespaced as `bubble_sort_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0003.py` → `bubble_sort_0003_0003`.

## Example

Loaded from `algorithms/algorithm-0003.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0003", "algorithms/algorithm-0003.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [5, 3, 9, 1, 7]
result = module.bubble_sort_0003_0003(values)
print(result)
```

Output:

```text
[1, 3, 5, 7, 9]
```

## Notes

- An early-exit flag makes nearly sorted input O(n).
- Stable, and copies the input instead of mutating it.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
