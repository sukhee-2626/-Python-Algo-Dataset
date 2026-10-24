<div align="center">

# `linear_search` · Linear Search

**Search** · average `O(n)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Scans the sequence from left to right and returns the first index whose value matches the target. It makes no assumptions about ordering.

## Signature

```python
def linear_search_<file>_<block>(values, target):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(1)` |
| Average | `O(n)` | `O(1)` |
| Worst | `O(n)` | `O(1)` |

## In the dataset

- **3,113** implementations across **1,000** files.
- Namespaced as `linear_search_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0006.py` → `linear_search_0006_0002`.

## Example

Loaded from `algorithms/algorithm-0006.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0006", "algorithms/algorithm-0006.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [7, 3, 9, 1, 5]
result = module.linear_search_0006_0002(values, 9)
print(result)
```

Output:

```text
2
```

## Notes

- Works on unsorted data, unlike binary and jump search.
- Returns -1 when the target does not appear.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
