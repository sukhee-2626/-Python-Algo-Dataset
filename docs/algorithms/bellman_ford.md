<div align="center">

# `bellman_ford` · Bellman-Ford

**Graph** · average `O(V * E)` · space `O(V)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Relaxes every edge V - 1 times to compute single-source shortest paths, including graphs with negative edge weights.

## Signature

```python
def bellman_ford_<file>_<block>(edges, node_count, source):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(V * E)` | `O(V)` |
| Average | `O(V * E)` | `O(V)` |
| Worst | `O(V * E)` | `O(V)` |

## In the dataset

- **3,105** implementations across **1,000** files.
- Namespaced as `bellman_ford_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0002.py` → `bellman_ford_0002_0002`.

## Example

Loaded from `algorithms/algorithm-0002.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0002", "algorithms/algorithm-0002.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

edges = [(0, 1, 1), (1, 2, 2), (0, 2, 4)]
result = module.bellman_ford_0002_0002(edges, 3, 0)
print(result)
```

Output:

```text
[0, 1, 3]
```

## Notes

- Handles negative weights, unlike Dijkstra.
- Returns the distance list; negative cycles are not detected.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
