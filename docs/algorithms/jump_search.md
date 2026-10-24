<div align="center">

# `jump_search` · Jump Search

**Search** · average `O(sqrt(n))` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Probes a sorted sequence in blocks of sqrt(n), then performs a linear scan inside the block that may contain the target.

## Signature

```python
def jump_search_<file>_<block>(values, target):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(1)` | `O(1)` |
| Average | `O(sqrt(n))` | `O(1)` |
| Worst | `O(sqrt(n))` | `O(1)` |

## In the dataset

- **3,112** implementations across **1,000** files.
- Namespaced as `jump_search_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0003.py` → `jump_search_0003_0006`.

## Example

Loaded from `algorithms/algorithm-0003.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0003", "algorithms/algorithm-0003.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [1, 3, 5, 7, 9, 11, 13, 15]
result = module.jump_search_0003_0006(values, 11)
print(result)
```

Output:

```text
5
```

## Notes

- Requires sorted input and cheap random access.
- The block size is derived from the length of the sequence.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
