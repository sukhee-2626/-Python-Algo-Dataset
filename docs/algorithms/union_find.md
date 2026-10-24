<div align="center">

# `UnionFind` · Union-Find (Disjoint Set)

**Data structures & misc** · average `O(alpha(n))` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Disjoint-set forest with path halving and union by rank, supporting near-constant connectivity queries.

## Signature

```python
class UnionFind<file>_<block>:
    def __init__(self, size): ...
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(n)` |
| Average | `O(alpha(n))` | `O(n)` |
| Worst | `O(log n)` | `O(n)` |

## In the dataset

- **3,108** implementations across **1,000** files.
- Namespaced as `UnionFind_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0003.py` → `UnionFind0003_0001`.

## Example

Loaded from `algorithms/algorithm-0003.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0003", "algorithms/algorithm-0003.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

structure = module.UnionFind0003_0001(5)
structure.union(0, 1)
structure.union(3, 4)
result = (structure.find(1), structure.find(4), structure.find(2))
print(result)
```

Output:

```text
(0, 3, 2)
```

## Notes

- Nodes are zero-indexed integers from 0 to size - 1.
- union returns False when the two nodes are already connected.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
