<div align="center">

# `gcd` · Greatest Common Divisor

**Math & backtracking** · average `O(log n)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Euclidean algorithm that repeatedly replaces the pair with (right, left mod right) until the remainder is zero.

## Signature

```python
def gcd_<file>_<block>(left, right):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(log n)` | `O(1)` |
| Average | `O(log n)` | `O(1)` |
| Worst | `O(log n)` | `O(1)` |

## In the dataset

- **3,136** implementations across **1,000** files.
- Namespaced as `gcd_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0012.py` → `gcd_0012_0006`.

## Example

Loaded from `algorithms/algorithm-0012.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0012", "algorithms/algorithm-0012.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.gcd_0012_0006(48, 18)
print(result)
```

Output:

```text
6
```

## Notes

- Every block also defines a paired lcm helper.
- Returns the absolute value of the divisor.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
