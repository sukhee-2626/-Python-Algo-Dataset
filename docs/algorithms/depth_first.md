<div align="center">

# `depth_first` · Depth-First Search

**Graph** · average `O(V + E)` · space `O(V)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Explores as deep as possible before backtracking, using an explicit stack instead of recursion.

## Signature

```python
def depth_first_<file>_<block>(graph, start):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(V)` |
| Average | `O(V + E)` | `O(V)` |
| Worst | `O(V + E)` | `O(V)` |

## In the dataset

- **3,138** implementations across **1,000** files.
- Namespaced as `depth_first_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0005.py` → `depth_first_0005_0001`.

## Example

Loaded from `algorithms/algorithm-0005.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0005", "algorithms/algorithm-0005.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

graph = dict(a=["b", "c"], b=["d"], c=["d"], d=[])
result = module.depth_first_0005_0001(graph, "a")
print(result)
```

Output:

```text
['a', 'b', 'd', 'c']
```

## Notes

- The iterative form avoids Python's recursion limit.
- Produces a pre-order traversal of reachable nodes.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
