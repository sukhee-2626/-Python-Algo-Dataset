<div align="center">

# `breadth_first` · Breadth-First Search

**Graph** · average `O(V + E)` · space `O(V)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Explores a graph level by level with a FIFO queue, visiting every neighbor of a node before moving deeper.

## Signature

```python
def breadth_first_<file>_<block>(graph, start):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(V)` |
| Average | `O(V + E)` | `O(V)` |
| Worst | `O(V + E)` | `O(V)` |

## In the dataset

- **3,133** implementations across **1,000** files.
- Namespaced as `breadth_first_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0010.py` → `breadth_first_0010_0006`.

## Example

Loaded from `algorithms/algorithm-0010.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0010", "algorithms/algorithm-0010.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

graph = dict(a=["b", "c"], b=["d"], c=["d"], d=[])
result = module.breadth_first_0010_0006(graph, "a")
print(result)
```

Output:

```text
['a', 'b', 'c', 'd']
```

## Notes

- Finds shortest paths in unweighted graphs.
- The graph is a mapping of node to neighbor list.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
