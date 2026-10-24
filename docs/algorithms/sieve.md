<div align="center">

# `sieve` · Sieve of Eratosthenes

**Math & backtracking** · average `O(n log log n)` · space `O(n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Flags multiples of each prime to enumerate every prime up to a limit.

## Signature

```python
def sieve_<file>_<block>(limit=<default>):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n log log n)` | `O(n)` |
| Average | `O(n log log n)` | `O(n)` |
| Worst | `O(n log log n)` | `O(n)` |

## In the dataset

- **3,123** implementations across **1,000** files.
- Namespaced as `sieve_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0004.py` → `sieve_0004_0004`.

## Example

Loaded from `algorithms/algorithm-0004.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0004", "algorithms/algorithm-0004.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.sieve_0004_0004(30)
print(result)
```

Output:

```text
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## Notes

- Each variant bakes a different default limit into its signature.
- Returns the primes as an ascending list.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
