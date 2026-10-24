<div align="center">

# `longest_increasing_subsequence` · Longest Increasing Subsequence

**DP & greedy** · average `O(n log n)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Maintains the smallest possible tail for each subsequence length, the patience-sorting approach to LIS.

## Signature

```python
def longest_increasing_subsequence_<file>_<block>(values):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n log n)` | `O(n)` |
| Average | `O(n log n)` | `O(n)` |
| Worst | `O(n log n)` | `O(n)` |

## In the dataset

- **3,129** implementations across **1,000** files.
- Namespaced as `longest_increasing_subsequence_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0003.py` → `longest_increasing_subsequence_0003_0002`.

## Example

Loaded from `algorithms/algorithm-0003.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0003", "algorithms/algorithm-0003.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [10, 9, 2, 5, 3, 7, 101, 18]
result = module.longest_increasing_subsequence_0003_0002(values)
print(result)
```

Output:

```text
4
```

## Notes

- Returns the length, not the subsequence itself.
- Uses bisect to keep the tails array sorted.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
