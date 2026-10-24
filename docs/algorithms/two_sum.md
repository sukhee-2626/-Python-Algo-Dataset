<div align="center">

# `two_sum` · Two Sum

**Data structures & misc** · average `O(n)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Hashes previously seen values to find two indices whose values add up to a target in a single pass.

## Signature

```python
def two_sum_<file>_<block>(values, target):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(n)` |
| Average | `O(n)` | `O(n)` |
| Worst | `O(n)` | `O(n)` |

## In the dataset

- **3,111** implementations across **1,000** files.
- Namespaced as `two_sum_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0006.py` → `two_sum_0006_0001`.

## Example

Loaded from `algorithms/algorithm-0006.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0006", "algorithms/algorithm-0006.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.two_sum_0006_0001([2, 7, 11, 15], 9)
print(result)
```

Output:

```text
(0, 1)
```

## Notes

- Returns the first pair found, or None.
- Indices are returned in ascending order.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
