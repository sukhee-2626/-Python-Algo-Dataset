<div align="center">

# `Trie` · Trie (Prefix Tree)

**Data structures & misc** · average `O(L)` · space `O(total characters)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Prefix tree that stores characters in nested dictionaries and marks the end of inserted words.

## Signature

```python
class Trie<file>_<block>:
    def __init__(self): ...
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(L)` | `O(total characters)` |
| Average | `O(L)` | `O(total characters)` |
| Worst | `O(L)` | `O(total characters)` |

## In the dataset

- **3,143** implementations across **1,000** files.
- Namespaced as `Trie_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0004.py` → `Trie0004_0008`.

## Example

Loaded from `algorithms/algorithm-0004.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0004", "algorithms/algorithm-0004.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

structure = module.Trie0004_0008()
structure.insert("dataset")
result = (structure.contains("dataset"), structure.contains("data"))
print(result)
```

Output:

```text
(True, False)
```

## Notes

- insert and contains each run in time proportional to word length.
- Matching is case-sensitive.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
