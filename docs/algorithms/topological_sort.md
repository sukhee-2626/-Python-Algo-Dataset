<div align="center">

# `topological_sort` · Topological Sort

**Graph** · average `O(V + E)` · space `O(V)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Kahn's algorithm orders a directed acyclic graph so that every edge points forward, repeatedly emitting zero-indegree nodes.

## Signature

```python
def topological_sort_<file>_<block>(graph):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(V + E)` | `O(V)` |
| Average | `O(V + E)` | `O(V)` |
| Worst | `O(V + E)` | `O(V)` |

## In the dataset

- **3,117** implementations across **1,000** files.
- Namespaced as `topological_sort_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0003.py` → `topological_sort_0003_0005`.

## Example

Loaded from `algorithms/algorithm-0003.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0003", "algorithms/algorithm-0003.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

graph = dict(a=["b", "c"], b=["d"], c=["d"], d=[])
result = module.topological_sort_0003_0005(graph)
print(result)
```

Output:

```text
['a', 'b', 'c', 'd']
```

## Notes

- Requires a DAG; cycles leave some nodes unprocessed.
- The graph is a mapping of node to outgoing neighbor list.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
