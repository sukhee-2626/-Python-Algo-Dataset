<div align="center">

# `dijkstra` · Dijkstra's Algorithm

**Graph** · average `O((V + E) log V)` · space `O(V)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Grows shortest-path distances from a source node using a min-heap of frontier nodes and weighted edges.

## Signature

```python
def dijkstra_<file>_<block>(graph, source):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O((V + E) log V)` | `O(V)` |
| Average | `O((V + E) log V)` | `O(V)` |
| Worst | `O((V + E) log V)` | `O(V)` |

## In the dataset

- **3,123** implementations across **1,000** files.
- Namespaced as `dijkstra_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0001.py` → `dijkstra_0001_0004`.

## Example

Loaded from `algorithms/algorithm-0001.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0001", "algorithms/algorithm-0001.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

graph = dict(a=[("b", 1), ("c", 4)], b=[("c", 2)], c=[])
result = module.dijkstra_0001_0004(graph, "a")
print(result)
```

Output:

```text
{'a': 0, 'b': 1, 'c': 3}
```

## Notes

- Requires non-negative edge weights.
- Each adjacency entry is a (neighbor, weight) pair.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
