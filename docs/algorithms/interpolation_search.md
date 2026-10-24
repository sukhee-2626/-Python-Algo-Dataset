<div align="center">

# `interpolation_search` · Interpolation Search

**Search** · average `O(log log n)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Estimates the position of the target from the value distribution, the way a person opens a phone book near the expected name.

## Signature

```python
def interpolation_search_<file>_<block>(values, target):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(1)` |
| Average | `O(log log n)` | `O(1)` |
| Worst | `O(n)` | `O(1)` |

## In the dataset

- **3,128** implementations across **1,000** files.
- Namespaced as `interpolation_search_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0007.py` → `interpolation_search_0007_0008`.

## Example

Loaded from `algorithms/algorithm-0007.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0007", "algorithms/algorithm-0007.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [10, 20, 30, 40, 50, 60, 70, 80]
result = module.interpolation_search_0007_0008(values, 60)
print(result)
```

Output:

```text
5
```

## Notes

- Fastest on uniformly distributed, sorted data.
- Degrades toward a linear scan on skewed distributions.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
