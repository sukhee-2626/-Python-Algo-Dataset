<div align="center">

# `partition_dutch` · Dutch National Flag Partition

**Sorting** · average `O(n)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Three-way partition that groups values below, equal to, and above a pivot in a single pass.

## Signature

```python
def partition_dutch_<file>_<block>(values, pivot):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n)` | `O(n)` |
| Average | `O(n)` | `O(n)` |
| Worst | `O(n)` | `O(n)` |

## In the dataset

- **3,111** implementations across **1,000** files.
- Namespaced as `partition_dutch_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0002.py` → `partition_dutch_0002_0006`.

## Example

Loaded from `algorithms/algorithm-0002.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0002", "algorithms/algorithm-0002.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

values = [3, 1, 4, 1, 5, 9, 2, 6]
result = module.partition_dutch_0002_0006(values, 4)
print(result)
```

Output:

```text
[3, 1, 1, 2, 4, 9, 6, 5]
```

## Notes

- Forms the core of three-way quicksort on duplicate-heavy data.
- Returns a new list; the input is untouched.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
