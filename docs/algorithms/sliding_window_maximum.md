<div align="center">

# `sliding_window_maximum` · Sliding Window Maximum

**Data structures & misc** · average `O(n)` · space `O(k)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Maintains a monotonic deque of candidates so each fixed-width window maximum is available in constant time.

## Signature

```python
def sliding_window_maximum_<file>_<block>(values, width=<default>):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(n)` | `O(k)` |
| Average | `O(n)` | `O(k)` |
| Worst | `O(n)` | `O(k)` |

## In the dataset

- **3,119** implementations across **1,000** files.
- Namespaced as `sliding_window_maximum_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0001.py` → `sliding_window_maximum_0001_0002`.

## Example

Loaded from `algorithms/algorithm-0001.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0001", "algorithms/algorithm-0001.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.sliding_window_maximum_0001_0002([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)
```

Output:

```text
[3, 3, 5, 5, 6, 7]
```

## Notes

- The window width is baked into each variant's default argument.
- Each index enters and leaves the deque at most once.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
