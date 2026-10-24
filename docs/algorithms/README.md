<div align="center">

# 📚 Algorithm Reference

**40 algorithms · 1,000 modules · 1.74M lines**

[← Dataset README](../../README.md)

</div>

---

Every algorithm used in the dataset has its own reference page with a description,
complexity analysis, signature, variant counts, and a verified example that runs
against a real module from the corpus.

## Loading a module

Files live in `algorithms/` and are named `algorithm-NNNN.py`. Because the names
contain a hyphen, load them through `importlib.util`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("algorithm_0001", "algorithms/algorithm-0001.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

names = [name for name in dir(module) if not name.startswith('_')]
print(len(names), "public symbols")
```

## Families

| Family | Algorithms | Implementations |
| :-- | --: | --: |
| 🔍 Search | 6 | 18,682 |
| 🔀 Sorting | 7 | 21,825 |
| 🕸️ Graph | 7 | 21,851 |
| 🧮 DP & greedy | 5 | 15,622 |
| 🔤 Strings | 4 | 12,446 |
| ➗ Math & backtracking | 5 | 15,608 |
| 🧱 Data structures & misc | 6 | 18,712 |
| **Total** | **40** | **124,746** |

*Totals count the 40 primary templates only. Each `gcd` variant also defines an
`lcm` helper (+3,136), bringing the corpus to 127,882 module-level definitions.*

## 🔍 Search

| Algorithm | Average time | Space | Variants | Reference |
| :-- | :-- | :-- | --: | :-- |
| `binary_search` | `O(log n)` | `O(1)` | 3,103 | [Read →](binary_search.md) |
| `linear_search` | `O(n)` | `O(1)` | 3,113 | [Read →](linear_search.md) |
| `jump_search` | `O(sqrt(n))` | `O(1)` | 3,112 | [Read →](jump_search.md) |
| `interpolation_search` | `O(log log n)` | `O(1)` | 3,128 | [Read →](interpolation_search.md) |
| `exponential_search` | `O(log n)` | `O(1)` | 3,101 | [Read →](exponential_search.md) |
| `ternary_search` | `O(log n)` | `O(1)` | 3,125 | [Read →](ternary_search.md) |

## 🔀 Sorting

| Algorithm | Average time | Space | Variants | Reference |
| :-- | :-- | :-- | --: | :-- |
| `bubble_sort` | `O(n^2)` | `O(n)` | 3,091 | [Read →](bubble_sort.md) |
| `insertion_sort` | `O(n^2)` | `O(n)` | 3,135 | [Read →](insertion_sort.md) |
| `selection_sort` | `O(n^2)` | `O(n)` | 3,113 | [Read →](selection_sort.md) |
| `merge_sort` | `O(n log n)` | `O(n)` | 3,123 | [Read →](merge_sort.md) |
| `quick_sort` | `O(n log n)` | `O(n)` | 3,129 | [Read →](quick_sort.md) |
| `counting_sort` | `O(n + k)` | `O(k)` | 3,123 | [Read →](counting_sort.md) |
| `partition_dutch` | `O(n)` | `O(n)` | 3,111 | [Read →](partition_dutch.md) |

## 🕸️ Graph

| Algorithm | Average time | Space | Variants | Reference |
| :-- | :-- | :-- | --: | :-- |
| `breadth_first` | `O(V + E)` | `O(V)` | 3,133 | [Read →](breadth_first.md) |
| `depth_first` | `O(V + E)` | `O(V)` | 3,138 | [Read →](depth_first.md) |
| `dijkstra` | `O((V + E) log V)` | `O(V)` | 3,123 | [Read →](dijkstra.md) |
| `a_star` | `O(E log V)` | `O(V)` | 3,112 | [Read →](a_star.md) |
| `floyd_warshall` | `O(V^3)` | `O(V^2)` | 3,123 | [Read →](floyd_warshall.md) |
| `topological_sort` | `O(V + E)` | `O(V)` | 3,117 | [Read →](topological_sort.md) |
| `bellman_ford` | `O(V * E)` | `O(V)` | 3,105 | [Read →](bellman_ford.md) |

## 🧮 DP & greedy

| Algorithm | Average time | Space | Variants | Reference |
| :-- | :-- | :-- | --: | :-- |
| `knapsack` | `O(n * capacity)` | `O(capacity)` | 3,119 | [Read →](knapsack.md) |
| `longest_increasing_subsequence` | `O(n log n)` | `O(n)` | 3,129 | [Read →](longest_increasing_subsequence.md) |
| `coin_change` | `O(amount * len(coins))` | `O(amount)` | 3,132 | [Read →](coin_change.md) |
| `activity_selection` | `O(n log n)` | `O(n)` | 3,123 | [Read →](activity_selection.md) |
| `max_subarray` | `O(n)` | `O(1)` | 3,119 | [Read →](max_subarray.md) |

## 🔤 Strings

| Algorithm | Average time | Space | Variants | Reference |
| :-- | :-- | :-- | --: | :-- |
| `longest_common_subsequence` | `O(m * n)` | `O(m * n)` | 3,113 | [Read →](longest_common_subsequence.md) |
| `edit_distance` | `O(m * n)` | `O(n)` | 3,114 | [Read →](edit_distance.md) |
| `kmp_search` | `O(n + m)` | `O(m)` | 3,101 | [Read →](kmp_search.md) |
| `rabin_karp` | `O(n + m)` | `O(1)` | 3,118 | [Read →](rabin_karp.md) |

## ➗ Math & backtracking

| Algorithm | Average time | Space | Variants | Reference |
| :-- | :-- | :-- | --: | :-- |
| `sieve` | `O(n log log n)` | `O(n)` | 3,123 | [Read →](sieve.md) |
| `gcd` | `O(log n)` | `O(1)` | 3,136 | [Read →](gcd.md) |
| `modular_power` | `O(log e)` | `O(1)` | 3,131 | [Read →](modular_power.md) |
| `n_queens` | `O(n!)` | `O(n)` | 3,107 | [Read →](n_queens.md) |
| `matrix_multiply` | `O(n^3)` | `O(n^2)` | 3,111 | [Read →](matrix_multiply.md) |

## 🧱 Data structures & misc

| Algorithm | Average time | Space | Variants | Reference |
| :-- | :-- | :-- | --: | :-- |
| `UnionFind` | `O(alpha(n))` | `O(n)` | 3,108 | [Read →](union_find.md) |
| `Trie` | `O(L)` | `O(total characters)` | 3,143 | [Read →](trie.md) |
| `two_sum` | `O(n)` | `O(n)` | 3,111 | [Read →](two_sum.md) |
| `sliding_window_maximum` | `O(n)` | `O(k)` | 3,119 | [Read →](sliding_window_maximum.md) |
| `permutations` | `O(n! * n)` | `O(n! * n)` | 3,121 | [Read →](permutations.md) |
| `subsets` | `O(n * 2^n)` | `O(n * 2^n)` | 3,110 | [Read →](subsets.md) |

---

<div align="center">

[← Back to the dataset README](../../README.md)

</div>
