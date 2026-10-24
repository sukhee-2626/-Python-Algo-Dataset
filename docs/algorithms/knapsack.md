<div align="center">

# `knapsack` · 0/1 Knapsack

**DP & greedy** · average `O(n * capacity)` · space `O(capacity)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Dynamic program over capacity that decides whether to take each item, maximizing total value without exceeding the weight limit.

## Signature

```python
def knapsack_<file>_<block>(weights, values, capacity):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n * capacity)` | `O(capacity)` |
| Average | `O(n * capacity)` | `O(capacity)` |
| Worst | `O(n * capacity)` | `O(capacity)` |

## In the dataset

- **3,119** implementations across **1,000** files.
- Namespaced as `knapsack_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0012.py` → `knapsack_0012_0004`.

## Example

Loaded from `algorithms/algorithm-0012.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0012", "algorithms/algorithm-0012.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
result = module.knapsack_0012_0004(weights, values, 7)
print(result)
```

Output:

```text
9
```

## Notes

- Uses a one-dimensional table iterated from high to low capacity.
- Each item can be chosen at most once.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
