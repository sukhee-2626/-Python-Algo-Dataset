<div align="center">

# 🐍 Python Algorithms Dataset

**A 1,000-file synthetic corpus of Python algorithm implementations,
built to train and evaluate code language models.**

[![Files](https://img.shields.io/badge/Files-1%2C000-2563eb?style=for-the-badge)](#at-a-glance)
[![Lines](https://img.shields.io/badge/Lines-1.74M-16a34a?style=for-the-badge)](#at-a-glance)
[![Size](https://img.shields.io/badge/Size-53_MB-7c3aed?style=for-the-badge)](#at-a-glance)
[![Definitions](https://img.shields.io/badge/Definitions-127.9k-db2777?style=for-the-badge)](#at-a-glance)

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Compile Check](https://img.shields.io/badge/Compile_Check-100%25-22c55e?style=for-the-badge)](#quality-gates)
[![Text](https://img.shields.io/badge/Prose_%2F_Comments-0-lightgrey?style=for-the-badge)](#quality-gates)

</div>

---

> **Synthetic dataset.** Every module in this repository is machine-generated from
> a template bank of algorithm implementations. It is intended as training data
> for a custom code model, not as production library code.

## Overview

`VersionControlData` is a code-only dataset containing **1,000 standalone Python
modules** (`.py`), each ranging from **100 to 4,000 lines**. The corpus totals
**1,739,445 lines** and **127,882 module-level function and class definitions**,
covering classic search, sorting, graph, dynamic-programming, string, math, and
data-structure algorithms.

The dataset was assembled by a deterministic generator: templates are shuffled
per file with a seeded RNG, every module is compiled before being written, and
symbol names are namespaced so the entire corpus can be imported side by side.

## At a glance

| Property | Value |
| :-- | --: |
| Files (`.py`) | **1,000** |
| Total lines | **1,739,445** |
| Total size | **53 MiB** (55,548,897 bytes) |
| Module-level definitions | **127,882** |
| Lines per file | **100 – 4,000** |
| Mean / median file length | **1,739 / 1,603** lines |
| Distinct algorithm templates | **40** |
| Copies per algorithm | **≈ 3,100** |
| Language / runtime | **Python 3** (validated on 3.14) |
| Encoding / newlines | **UTF-8 / LF** |
| Compile pass rate | **1,000 / 1,000 (100%)** |
| Version | **1.0** · commit `e1536be` |

## Dataset composition

Implementations are grouped into seven families. Counts below are the number of
module-level definitions across all 1,000 files.

| Family | Algorithms | Definitions |
| :-- | :-- | --: |
| 🔍 **Search** | binary, linear, jump, interpolation, exponential, ternary | 18,682 |
| 🔀 **Sorting** | bubble, insertion, selection, merge, quick, counting, Dutch partition | 21,825 |
| 🕸️ **Graph** | BFS, DFS, Dijkstra, A*, Floyd–Warshall, topological sort, Bellman–Ford | 21,851 |
| 🧮 **DP & greedy** | 0/1 knapsack, LIS, coin change, activity selection, Kadane | 15,622 |
| 🔤 **Strings** | LCS, edit distance, KMP, Rabin–Karp | 12,446 |
| ➗ **Math & backtracking** | sieve, GCD/LCM, modular exponentiation, N-Queens, matrix multiply | 15,608 |
| 🧱 **Structures & misc** | union-find, trie, two-sum, sliding-window max, permutations, subsets | 18,712 |
| | **Total (incl. 3,136 LCM helpers)** | **127,882** |

<details>
<summary><b>Per-algorithm variant counts</b></summary>

| Algorithm | Count | Algorithm | Count |
| :-- | --: | :-- | --: |
| bubble_sort | 3,091 | binary_search | 3,103 |
| insertion_sort | 3,135 | linear_search | 3,113 |
| selection_sort | 3,113 | jump_search | 3,112 |
| merge_sort | 3,123 | interpolation_search | 3,128 |
| quick_sort | 3,129 | exponential_search | 3,101 |
| counting_sort | 3,123 | ternary_search | 3,125 |
| partition_dutch | 3,111 | breadth_first | 3,133 |
| depth_first | 3,138 | dijkstra | 3,123 |
| a_star | 3,112 | floyd_warshall | 3,123 |
| topological_sort | 3,117 | bellman_ford | 3,105 |
| knapsack | 3,119 | longest_increasing_subsequence | 3,129 |
| coin_change | 3,132 | activity_selection | 3,123 |
| max_subarray | 3,119 | longest_common_subsequence | 3,113 |
| edit_distance | 3,114 | kmp_search | 3,101 |
| rabin_karp | 3,118 | sieve | 3,123 |
| gcd (+ lcm) | 3,136 | modular_power | 3,131 |
| n_queens | 3,107 | matrix_multiply | 3,111 |
| UnionFind | 3,108 | Trie | 3,143 |
| two_sum | 3,111 | sliding_window_maximum | 3,119 |
| permutations | 3,121 | subsets | 3,110 |

</details>

## File layout

Each file follows the same shape:

```
algorithms/algorithm-XXXX.py
├── imports            # heapq, math, bisect, collections
├── ALGORITHM BLOCKS   # shuffled definitions, each suffixed _XXXX_YYYY
├── LOOKUP_XXXX_NNN    # module constants (only when needed for exact line count)
```

**Naming convention:** `{algorithm}_{file_index}_{block_index}`

```python
interpolation_search_0042_0001
└──────┬─────────┘ └┬─┘ └┬─┘
   algorithm      file  block
```

The namespacing guarantees every symbol in the corpus is unique, so modules can be
imported together without collisions.

## Sample

Excerpt from `algorithms/algorithm-0042.py`:

```python
import heapq
import math
from bisect import bisect_left
from collections import deque

def interpolation_search_0042_0001(values, target):
    low = 0
    high = len(values) - 1
    while low <= high and values[low] <= target <= values[high]:
        if values[high] == values[low]:
            return low if values[low] == target else -1
        position = low + (target - values[low]) * (high - low) // (values[high] - values[low])
        if values[position] == target:
            return position
        if values[position] < target:
            low = position + 1
        else:
            high = position - 1
    return -1
```

## Quality gates

Every file in the dataset passed the following checks at generation time:

- ✅ **Compiles cleanly** — `compile(source, path, "exec")` succeeded for all 1,000 files.
- ✅ **Exact line budget** — each file matches its target length (100–4,000) to the line.
- ✅ **Pure code** — zero comments, zero docstrings, zero prose or filler text.
- ✅ **Deterministic** — a per-file seeded RNG reproduces the corpus byte-for-byte.
- ✅ **Collision-free symbols** — every definition carries a unique file/block suffix.
- ✅ **Consistent encoding** — UTF-8 with LF newlines.

## Intended use

| ✅ Good fit | ❌ Not a fit |
| :-- | :-- |
| Pretraining and fine-tuning code LLMs | Production or library code |
| Synthetic-data and curriculum experiments | Correctness-critical deployments |
| Tokenizer and context-length stress tests | Benchmarks of real-world code style |
| Retrieval and embedding experiments | Teaching reference implementations |
| Version-control and large-diff tooling tests | Anything requiring a test suite |

## Size distribution

| Lines per file | Files | Distribution |
| :-- | --: | :-- |
| 100 – 499 | 132 | `█████████████` |
| 500 – 999 | 167 | `████████████████` |
| 1,000 – 1,999 | 333 | `█████████████████████████████████` |
| 2,000 – 2,999 | 200 | `████████████████████` |
| 3,000 – 4,000 | 168 | `████████████████` |

## Generation pipeline

1. **Template bank** — 40 hand-written algorithm implementations in pure Python.
2. **Seeded shuffle** — a per-file RNG (`file_index * 104729 + 7`) orders the blocks.
3. **Line budget** — each file gets a target length between 100 and 4,000 lines.
4. **Exact fill** — a tail of module constants tops the file up to the exact target.
5. **Compile gate** — the module is compiled in memory before being written to disk.
6. **Publish** — 1,000 files committed and pushed in a single commit.

## Limitations

- **Synthetic and repetitive.** Files share a template bank, so stylistic diversity is
  far below that of human-written repositories.
- **Not executed.** Algorithms are compiled, not unit-tested; there are no assertions
  or runtime checks.
- **Filler tail.** Short files end with generated `LOOKUP_*` constants to hit the exact
  line target. They are valid code, but carry no algorithmic meaning.
- **Distribution skew.** Common textbook algorithms dominate; real-world code,
  libraries, and idiomatic patterns are absent.
- **No license yet.** A `LICENSE` file has not been added; choose one before
  redistributing the dataset.

## License & attribution

No license has been specified for this dataset yet. Until one is added, treat the
content as **all rights reserved** by the repository owner.

<div align="center">

---

**Repository:** [sukhee-2626/VersionControlData](https://github.com/sukhee-2626/VersionControlData)  
**Version 1.0** · 1,000 files · 1,739,445 lines · 53 MiB

</div>
