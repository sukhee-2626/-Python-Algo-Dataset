<div align="center">

# `exponential_search` · Exponential Search

**Search** · average `O(log n)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Doubles the search bound until it passes the target, then binary-searches the bracketed range. Useful when the target is likely near the front.

## Signature

```python
def exponential_search_<file>_<block>(values, target):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(1)` |
| Average | `O(log n)` | `O(1)` |
| Worst | `O(log n)` | `O(1)` |

## In the dataset

- **3,101** implementations across **1,000** files.
- Namespaced as `exponential_search_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0004.py` → `exponential_search_0004_0003`.

## Example

Loaded from `algorithms/algorithm-0004.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0004", "algorithms/algorithm-0004.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = module.exponential_search_0004_0003(values, 9)
print(result)
```

Output:

```text
8
```

## Notes

- Requires sorted input.
- Well suited to unbounded or streaming sequences.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
