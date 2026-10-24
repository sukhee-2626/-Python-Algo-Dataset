<div align="center">

# `counting_sort` · Counting Sort

**Sorting** · average `O(n + k)` · space `O(k)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Counts how often each key occurs, then rebuilds the sequence in order without comparing elements.

## Signature

```python
def counting_sort_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n + k)` | `O(k)` |
| Average | `O(n + k)` | `O(k)` |
| Worst | `O(n + k)` | `O(k)` |

## In the dataset

- **3,123** implementations across **1,000** files.
- Namespaced as `counting_sort_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0007.py` → `counting_sort_0007_0002`.

## Example

Loaded from `algorithms/algorithm-0007.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0007", "algorithms/algorithm-0007.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [4, 2, 2, 8, 3, 3, 1]
result = module.counting_sort_0007_0002(values)
print(result)
```

Output:

```text
[1, 2, 2, 3, 3, 4, 8]
```

## Notes

- Efficient when keys are small integers spanning a narrow range.
- Not comparison-based, so the usual O(n log n) bound does not apply.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
