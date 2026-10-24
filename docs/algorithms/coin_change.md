<div align="center">

# `coin_change` · Coin Change

**DP & greedy** · average `O(amount * len(coins))` · space `O(amount)`

[← Algorithm index](README.md) · [Dataset README](../../README.md)

</div>

---

## Overview

Computes the minimum number of coins needed to reach an amount, with unlimited reuse of each coin.

## Signature

```python
def coin_change_<file>_<block>(coins, amount):
```

## Complexity

| Case | Time | Space |
| :-- | :-- | :-- |
| Best | `O(amount * len(coins))` | `O(amount)` |
| Average | `O(amount * len(coins))` | `O(amount)` |
| Worst | `O(amount * len(coins))` | `O(amount)` |

## In the dataset

- **3,132** implementations across **1,000** files.
- Namespaced as `coin_change_<file>_<block>`, so every symbol in the corpus is unique.
- First occurrence: `algorithms/algorithm-0004.py` → `coin_change_0004_0002`.

## Example

Loaded from `algorithms/algorithm-0004.py`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0004", "algorithms/algorithm-0004.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

coins = [1, 2, 5]
result = module.coin_change_0004_0002(coins, 11)
print(result)
```

Output:

```text
3
```

## Notes

- Returns -1 when the amount cannot be formed.
- Coins may be used any number of times.

---

<div align="center">

[← Back to the algorithm index](README.md)

</div>
