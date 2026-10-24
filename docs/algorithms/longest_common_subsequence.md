<div align="center">

# `longest_common_subsequence` · Longest Common Subsequence

**Strings** · average `O(m * n)` · space `O(m * n)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Fills a two-dimensional table over string prefixes to measure the longest shared subsequence.

## Signature

```python
def longest_common_subsequence_<file>_<block>(left, right):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(m * n)` | `O(m * n)` |
| Average | `O(m * n)` | `O(m * n)` |
| Worst | `O(m * n)` | `O(m * n)` |

## In the dataset

- **3,113** implementations across **1,000** files.
- Namespaced as `longest_common_subsequence_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0001.py` → `longest_common_subsequence_0001_0003`.

## Example

Loaded from `algorithms/algorithm-0001.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0001", "algorithms/algorithm-0001.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.longest_common_subsequence_0001_0003("ABCBDAB", "BDCABA")
print(result)
```

Output:

```text
4
```

## Notes

- A subsequence need not be contiguous, unlike a substring.
- Returns the length, not the reconstructed sequence.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
