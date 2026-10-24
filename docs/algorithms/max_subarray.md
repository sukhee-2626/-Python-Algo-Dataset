<div align="center">

# `max_subarray` · Maximum Subarray (Kadane)

**DP & greedy** · average `O(n)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Kadane's algorithm tracks the best sum ending at each position and the best sum seen so far.

## Signature

```python
def max_subarray_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n)` | `O(1)` |
| Average | `O(n)` | `O(1)` |
| Worst | `O(n)` | `O(1)` |

## In the dataset

- **3,119** implementations across **1,000** files.
- Namespaced as `max_subarray_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0010.py` → `max_subarray_0010_0003`.

## Example

Loaded from `algorithms/algorithm-0010.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0010", "algorithms/algorithm-0010.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = module.max_subarray_0010_0003(values)
print(result)
```

Output:

```text
6
```

## Notes

- Runs in a single pass with constant extra space.
- Works when every value is negative.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
