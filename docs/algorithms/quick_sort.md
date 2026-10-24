<div align="center">

# `quick_sort` · Quick Sort

**Sorting** · average `O(n log n)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Partitions around a middle pivot into lower, equal, and higher groups, then recurses on the outer groups.

## Signature

```python
def quick_sort_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n log n)` | `O(n)` |
| Average | `O(n log n)` | `O(n)` |
| Worst | `O(n^2)` | `O(n)` |

## In the dataset

- **3,129** implementations across **1,000** files.
- Namespaced as `quick_sort_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0009.py` → `quick_sort_0009_0006`.

## Example

Loaded from `algorithms/algorithm-0009.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0009", "algorithms/algorithm-0009.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [5, 3, 9, 1, 7]
result = module.quick_sort_0009_0006(values)
print(result)
```

Output:

```text
[1, 3, 5, 7, 9]
```

## Notes

- This variant allocates new lists rather than sorting in place.
- Degrades to O(n^2) on adversarial pivot choices.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
