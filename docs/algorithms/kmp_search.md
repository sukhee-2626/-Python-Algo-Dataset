<div align="center">

# `kmp_search` · Knuth-Morris-Pratt Search

**Strings** · average `O(n + m)` · space `O(m)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Precomputes a prefix-function table so mismatches skip ahead without rescanning text characters.

## Signature

```python
def kmp_search_<file>_<block>(text, pattern):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n + m)` | `O(m)` |
| Average | `O(n + m)` | `O(m)` |
| Worst | `O(n + m)` | `O(m)` |

## In the dataset

- **3,101** implementations across **1,000** files.
- Namespaced as `kmp_search_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0001.py` → `kmp_search_0001_0005`.

## Example

Loaded from `algorithms/algorithm-0001.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0001", "algorithms/algorithm-0001.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.kmp_search_0001_0005("abxabcabcaby", "abcaby")
print(result)
```

Output:

```text
[6]
```

## Notes

- Guaranteed linear time in the combined input length.
- Returns every starting index where the pattern matches.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
