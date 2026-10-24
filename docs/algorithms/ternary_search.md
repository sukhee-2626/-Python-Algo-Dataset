<div align="center">

# `ternary_search` · Ternary Search

**Search** · average `O(log n)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Narrows a sorted range by comparing two interior pivots, discarding a third of the remaining space on each step.

## Signature

```python
def ternary_search_<file>_<block>(values, target):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(1)` |
| Average | `O(log n)` | `O(1)` |
| Worst | `O(log n)` | `O(1)` |

## In the dataset

- **3,125** implementations across **1,000** files.
- Namespaced as `ternary_search_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0004.py` → `ternary_search_0004_0001`.

## Example

Loaded from `algorithms/algorithm-0004.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0004", "algorithms/algorithm-0004.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [1, 3, 5, 7, 9, 11, 13, 15, 17]
result = module.ternary_search_0004_0001(values, 13)
print(result)
```

Output:

```text
6
```

## Notes

- Uses more comparisons per step than binary search.
- Also used for unimodal function optimization.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
