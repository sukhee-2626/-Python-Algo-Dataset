<div align="center">

# `a_star` · A* Search

**Graph** · average `O(E log V)` · space `O(V)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Best-first grid search that orders the frontier by path cost plus a Manhattan-distance heuristic.

## Signature

```python
def a_star_<file>_<block>(grid, start, goal):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(V)` |
| Average | `O(E log V)` | `O(V)` |
| Worst | `O(E log V)` | `O(V)` |

## In the dataset

- **3,112** implementations across **1,000** files.
- Namespaced as `a_star_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0002.py` → `a_star_0002_0004`.

## Example

Loaded from `algorithms/algorithm-0002.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0002", "algorithms/algorithm-0002.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
result = module.a_star_0002_0004(grid, (0, 0), (2, 2))
print(result)
```

Output:

```text
4
```

## Notes

- The heuristic is admissible for four-direction grid movement.
- Truthy grid cells are treated as blocked; zero cells are walkable.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
