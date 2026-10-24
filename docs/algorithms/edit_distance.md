<div align="center">

# `edit_distance` · Edit Distance (Levenshtein)

**Strings** · average `O(m * n)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Computes the minimum number of inserts, deletes, and substitutions needed to turn one string into another.

## Signature

```python
def edit_distance_<file>_<block>(left, right):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(m * n)` | `O(n)` |
| Average | `O(m * n)` | `O(n)` |
| Worst | `O(m * n)` | `O(n)` |

## In the dataset

- **3,114** implementations across **1,000** files.
- Namespaced as `edit_distance_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0013.py` → `edit_distance_0013_0008`.

## Example

Loaded from `algorithms/algorithm-0013.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0013", "algorithms/algorithm-0013.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.edit_distance_0013_0008("kitten", "sitting")
print(result)
```

Output:

```text
3
```

## Notes

- A rolling row keeps auxiliary space linear in the shorter input.
- Comparison is case-sensitive.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
