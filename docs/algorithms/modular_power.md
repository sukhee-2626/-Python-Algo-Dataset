<div align="center">

# `modular_power` · Modular Exponentiation

**Math & backtracking** · average `O(log e)` · space `O(1)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Binary exponentiation that squares the base each bit of the exponent and keeps every intermediate value under a modulus.

## Signature

```python
def modular_power_<file>_<block>(base, exponent, modulus=<default>):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(log e)` | `O(1)` |
| Average | `O(log e)` | `O(1)` |
| Worst | `O(log e)` | `O(1)` |

## In the dataset

- **3,131** implementations across **1,000** files.
- Namespaced as `modular_power_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0005.py` → `modular_power_0005_0004`.

## Example

Loaded from `algorithms/algorithm-0005.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0005", "algorithms/algorithm-0005.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

result = module.modular_power_0005_0004(2, 10)
print(result)
```

Output:

```text
1024
```

## Notes

- The modulus is baked into each variant's default argument.
- Runs in logarithmic time in the exponent.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
