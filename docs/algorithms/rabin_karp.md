<div align="center">

# `rabin_karp` · Rabin-Karp Search

**Strings** · average `O(n + m)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Uses a rolling hash to find the pattern, verifying each candidate character by character.

## Signature

```python
def rabin_karp_<file>_<block>(text, pattern, base=257, modulus=1000000007):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n + m)` | `O(1)` |
| Average | `O(n + m)` | `O(1)` |
| Worst | `O(n * m)` | `O(1)` |

## In the dataset

- **3,118** implementations across **1,000** files.
- Namespaced as `rabin_karp_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0002.py` → `rabin_karp_0002_0005`.

## Example

Loaded from `algorithms/algorithm-0002.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0002", "algorithms/algorithm-0002.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.rabin_karp_0002_0005("abxabcabcaby", "abcaby")
print(result)
```

Output:

```text
[6]
```

## Notes

- Returns the first match only, as a single-element list.
- Hash collisions are resolved with a direct string comparison.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
