import heapq
import math
from bisect import bisect_left
from collections import deque

def longest_common_subsequence_0481_0001(left, right):
    rows = len(left) + 1
    columns = len(right) + 1
    table = [[0] * columns for _ in range(rows)]
    for row in range(1, rows):
        for column in range(1, columns):
            if left[row - 1] == right[column - 1]:
                table[row][column] = table[row - 1][column - 1] + 1
            else:
                table[row][column] = max(table[row - 1][column], table[row][column - 1])
    return table[-1][-1]

def rabin_karp_0481_0002(text, pattern, base=257, modulus=1000000007):
    if not pattern:
        return []
    pattern_hash = 0
    window_hash = 0
    power = 1
    for character in pattern:
        pattern_hash = (pattern_hash * base + ord(character)) % modulus
        power = power * base % modulus
    for index, character in enumerate(text):
        window_hash = (window_hash * base + ord(character)) % modulus
        if index >= len(pattern):
            window_hash = (window_hash - ord(text[index - len(pattern)]) * power) % modulus
        if index >= len(pattern) - 1 and window_hash == pattern_hash:
            start = index - len(pattern) + 1
            if text[start:index + 1] == pattern:
                return [start]
    return []

def max_subarray_0481_0003(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def bubble_sort_0481_0004(values, early_exit=True):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if early_exit and not swapped:
            break
    return result

def activity_selection_0481_0005(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def gcd_0481_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0481_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0481_0006(left, right)

def jump_search_0481_0007(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def partition_dutch_0481_0008(values, pivot):
    result = list(values)
    low = 0
    middle = 0
    high = len(result) - 1
    while middle <= high:
        if result[middle] < pivot:
            result[low], result[middle] = result[middle], result[low]
            low += 1
            middle += 1
        elif result[middle] > pivot:
            result[middle], result[high] = result[high], result[middle]
            high -= 1
        else:
            middle += 1
    return result

def subsets_0481_0009(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def sliding_window_maximum_0481_0010(values, width=5):
    candidates = deque()
    result = []
    for index, value in enumerate(values):
        while candidates and candidates[-1][1] <= value:
            candidates.pop()
        candidates.append((index, value))
        if candidates[0][0] <= index - width:
            candidates.popleft()
        if index >= width - 1:
            result.append(candidates[0][1])
    return result

def interpolation_search_0481_0011(values, target):
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

class UnionFind0481_0012:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left, right):
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return False
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1
        return True

def bellman_ford_0481_0013(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def selection_sort_0481_0014(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def binary_search_0481_0015(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def sieve_0481_0016(limit=394):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def exponential_search_0481_0017(values, target):
    length = len(values)
    if length == 0:
        return -1
    bound = 1
    while bound < length and values[bound] < target:
        bound *= 2
    low = bound // 2
    high = min(bound, length - 1)
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def matrix_multiply_0481_0018(left, right):
    rows = len(left)
    columns = len(right[0])
    shared = len(right)
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            total = 0
            for offset in range(shared):
                total += left[row][offset] * right[offset][column]
            result[row][column] = total
    return result

def topological_sort_0481_0019(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order

def dijkstra_0481_0020(graph, source):
    distances = {source: 0}
    heap = [(0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances.get(node, math.inf):
            continue
        for neighbor, weight in graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return distances

def merge_sort_0481_0021(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0481_0021(values[:middle])
    right = merge_sort_0481_0021(values[middle:])
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def insertion_sort_0481_0022(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def quick_sort_0481_0023(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0481_0023(lower) + equal + quick_sort_0481_0023(higher)

def knapsack_0481_0024(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def n_queens_0481_0025(size=8):
    columns = set()
    diagonals = set()
    anti_diagonals = set()
    count = 0

    def place(row):
        nonlocal count
        if row == size:
            count += 1
            return
        for column in range(size):
            if column in columns or row - column in diagonals or row + column in anti_diagonals:
                continue
            columns.add(column)
            diagonals.add(row - column)
            anti_diagonals.add(row + column)
            place(row + 1)
            columns.remove(column)
            diagonals.remove(row - column)
            anti_diagonals.remove(row + column)

    place(0)
    return count

def kmp_search_0481_0026(text, pattern):
    if not pattern:
        return []
    prefix = [0] * len(pattern)
    length = 0
    index = 1
    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            prefix[index] = length
            index += 1
        elif length:
            length = prefix[length - 1]
        else:
            prefix[index] = 0
            index += 1
    matches = []
    position = 0
    for cursor, character in enumerate(text):
        while position and character != pattern[position]:
            position = prefix[position - 1]
        if character == pattern[position]:
            position += 1
            if position == len(pattern):
                matches.append(cursor - len(pattern) + 1)
                position = prefix[position - 1]
    return matches

def permutations_0481_0027(values):
    results = []
    used = [False] * len(values)
    current = []

    def backtrack():
        if len(current) == len(values):
            results.append(tuple(current))
            return
        for index, value in enumerate(values):
            if used[index]:
                continue
            used[index] = True
            current.append(value)
            backtrack()
            current.pop()
            used[index] = False

    backtrack()
    return results

def breadth_first_0481_0028(graph, start):
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def floyd_warshall_0481_0029(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def counting_sort_0481_0030(values):
    if not values:
        return []
    lowest = min(values)
    highest = max(values)
    counts = [0] * (highest - lowest + 1)
    for value in values:
        counts[value - lowest] += 1
    result = []
    for offset, count in enumerate(counts):
        result.extend([offset + lowest] * count)
    return result

def ternary_search_0481_0031(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        third = (high - low) // 3
        middle_left = low + third
        middle_right = high - third
        if values[middle_left] == target:
            return middle_left
        if values[middle_right] == target:
            return middle_right
        if target < values[middle_left]:
            high = middle_left - 1
        elif target > values[middle_right]:
            low = middle_right + 1
        else:
            low = middle_left + 1
            high = middle_right - 1
    return -1

def edit_distance_0481_0032(left, right):
    previous = list(range(len(right) + 1))
    for left_index, left_char in enumerate(left, start=1):
        current = [left_index]
        for right_index, right_char in enumerate(right, start=1):
            cost = 0 if left_char == right_char else 1
            current.append(min(
                previous[right_index] + 1,
                current[right_index - 1] + 1,
                previous[right_index - 1] + cost,
            ))
        previous = current
    return previous[-1]

def a_star_0481_0033(grid, start, goal):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    open_heap = [(0, start)]
    distances = {start: 0}
    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            return distances[current]
        for delta_row, delta_column in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (current[0] + delta_row, current[1] + delta_column)
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]]:
                continue
            candidate = distances[current] + 1
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                priority = candidate + heuristic(neighbor)
                heapq.heappush(open_heap, (priority, neighbor))
    return -1

def depth_first_0481_0034(graph, start):
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order

def two_sum_0481_0035(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

class Trie0481_0036:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0481_0036())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def linear_search_0481_0037(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def coin_change_0481_0038(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def modular_power_0481_0039(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def longest_increasing_subsequence_0481_0040(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def dijkstra_0481_0041(graph, source):
    distances = {source: 0}
    heap = [(0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances.get(node, math.inf):
            continue
        for neighbor, weight in graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return distances

def floyd_warshall_0481_0042(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

class UnionFind0481_0043:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left, right):
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return False
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1
        return True

class Trie0481_0044:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0481_0044())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def partition_dutch_0481_0045(values, pivot):
    result = list(values)
    low = 0
    middle = 0
    high = len(result) - 1
    while middle <= high:
        if result[middle] < pivot:
            result[low], result[middle] = result[middle], result[low]
            low += 1
            middle += 1
        elif result[middle] > pivot:
            result[middle], result[high] = result[high], result[middle]
            high -= 1
        else:
            middle += 1
    return result

def counting_sort_0481_0046(values):
    if not values:
        return []
    lowest = min(values)
    highest = max(values)
    counts = [0] * (highest - lowest + 1)
    for value in values:
        counts[value - lowest] += 1
    result = []
    for offset, count in enumerate(counts):
        result.extend([offset + lowest] * count)
    return result

def jump_search_0481_0047(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def exponential_search_0481_0048(values, target):
    length = len(values)
    if length == 0:
        return -1
    bound = 1
    while bound < length and values[bound] < target:
        bound *= 2
    low = bound // 2
    high = min(bound, length - 1)
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def breadth_first_0481_0049(graph, start):
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def quick_sort_0481_0050(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0481_0050(lower) + equal + quick_sort_0481_0050(higher)

def depth_first_0481_0051(graph, start):
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order

def bubble_sort_0481_0052(values, early_exit=True):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if early_exit and not swapped:
            break
    return result

def activity_selection_0481_0053(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def binary_search_0481_0054(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def a_star_0481_0055(grid, start, goal):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    open_heap = [(0, start)]
    distances = {start: 0}
    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            return distances[current]
        for delta_row, delta_column in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (current[0] + delta_row, current[1] + delta_column)
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]]:
                continue
            candidate = distances[current] + 1
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                priority = candidate + heuristic(neighbor)
                heapq.heappush(open_heap, (priority, neighbor))
    return -1

def gcd_0481_0056(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0481_0056(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0481_0056(left, right)

def merge_sort_0481_0057(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0481_0057(values[:middle])
    right = merge_sort_0481_0057(values[middle:])
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def rabin_karp_0481_0058(text, pattern, base=257, modulus=1000000007):
    if not pattern:
        return []
    pattern_hash = 0
    window_hash = 0
    power = 1
    for character in pattern:
        pattern_hash = (pattern_hash * base + ord(character)) % modulus
        power = power * base % modulus
    for index, character in enumerate(text):
        window_hash = (window_hash * base + ord(character)) % modulus
        if index >= len(pattern):
            window_hash = (window_hash - ord(text[index - len(pattern)]) * power) % modulus
        if index >= len(pattern) - 1 and window_hash == pattern_hash:
            start = index - len(pattern) + 1
            if text[start:index + 1] == pattern:
                return [start]
    return []

def linear_search_0481_0059(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def knapsack_0481_0060(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def modular_power_0481_0061(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def longest_increasing_subsequence_0481_0062(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def n_queens_0481_0063(size=7):
    columns = set()
    diagonals = set()
    anti_diagonals = set()
    count = 0

    def place(row):
        nonlocal count
        if row == size:
            count += 1
            return
        for column in range(size):
            if column in columns or row - column in diagonals or row + column in anti_diagonals:
                continue
            columns.add(column)
            diagonals.add(row - column)
            anti_diagonals.add(row + column)
            place(row + 1)
            columns.remove(column)
            diagonals.remove(row - column)
            anti_diagonals.remove(row + column)

    place(0)
    return count

def selection_sort_0481_0064(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def subsets_0481_0065(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def sliding_window_maximum_0481_0066(values, width=3):
    candidates = deque()
    result = []
    for index, value in enumerate(values):
        while candidates and candidates[-1][1] <= value:
            candidates.pop()
        candidates.append((index, value))
        if candidates[0][0] <= index - width:
            candidates.popleft()
        if index >= width - 1:
            result.append(candidates[0][1])
    return result

def ternary_search_0481_0067(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        third = (high - low) // 3
        middle_left = low + third
        middle_right = high - third
        if values[middle_left] == target:
            return middle_left
        if values[middle_right] == target:
            return middle_right
        if target < values[middle_left]:
            high = middle_left - 1
        elif target > values[middle_right]:
            low = middle_right + 1
        else:
            low = middle_left + 1
            high = middle_right - 1
    return -1

def topological_sort_0481_0068(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order

def matrix_multiply_0481_0069(left, right):
    rows = len(left)
    columns = len(right[0])
    shared = len(right)
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            total = 0
            for offset in range(shared):
                total += left[row][offset] * right[offset][column]
            result[row][column] = total
    return result

def two_sum_0481_0070(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def coin_change_0481_0071(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def kmp_search_0481_0072(text, pattern):
    if not pattern:
        return []
    prefix = [0] * len(pattern)
    length = 0
    index = 1
    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            prefix[index] = length
            index += 1
        elif length:
            length = prefix[length - 1]
        else:
            prefix[index] = 0
            index += 1
    matches = []
    position = 0
    for cursor, character in enumerate(text):
        while position and character != pattern[position]:
            position = prefix[position - 1]
        if character == pattern[position]:
            position += 1
            if position == len(pattern):
                matches.append(cursor - len(pattern) + 1)
                position = prefix[position - 1]
    return matches

def interpolation_search_0481_0073(values, target):
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

def longest_common_subsequence_0481_0074(left, right):
    rows = len(left) + 1
    columns = len(right) + 1
    table = [[0] * columns for _ in range(rows)]
    for row in range(1, rows):
        for column in range(1, columns):
            if left[row - 1] == right[column - 1]:
                table[row][column] = table[row - 1][column - 1] + 1
            else:
                table[row][column] = max(table[row - 1][column], table[row][column - 1])
    return table[-1][-1]

def permutations_0481_0075(values):
    results = []
    used = [False] * len(values)
    current = []

    def backtrack():
        if len(current) == len(values):
            results.append(tuple(current))
            return
        for index, value in enumerate(values):
            if used[index]:
                continue
            used[index] = True
            current.append(value)
            backtrack()
            current.pop()
            used[index] = False

    backtrack()
    return results

def insertion_sort_0481_0076(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bellman_ford_0481_0077(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def max_subarray_0481_0078(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def sieve_0481_0079(limit=128):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def edit_distance_0481_0080(left, right):
    previous = list(range(len(right) + 1))
    for left_index, left_char in enumerate(left, start=1):
        current = [left_index]
        for right_index, right_char in enumerate(right, start=1):
            cost = 0 if left_char == right_char else 1
            current.append(min(
                previous[right_index] + 1,
                current[right_index - 1] + 1,
                previous[right_index - 1] + cost,
            ))
        previous = current
    return previous[-1]

def bubble_sort_0481_0081(values, early_exit=True):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if early_exit and not swapped:
            break
    return result

def depth_first_0481_0082(graph, start):
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order

def binary_search_0481_0083(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def quick_sort_0481_0084(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0481_0084(lower) + equal + quick_sort_0481_0084(higher)

def interpolation_search_0481_0085(values, target):
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

class UnionFind0481_0086:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left, right):
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return False
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1
        return True

def dijkstra_0481_0087(graph, source):
    distances = {source: 0}
    heap = [(0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances.get(node, math.inf):
            continue
        for neighbor, weight in graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return distances

def knapsack_0481_0088(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

class Trie0481_0089:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0481_0089())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def breadth_first_0481_0090(graph, start):
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def exponential_search_0481_0091(values, target):
    length = len(values)
    if length == 0:
        return -1
    bound = 1
    while bound < length and values[bound] < target:
        bound *= 2
    low = bound // 2
    high = min(bound, length - 1)
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def coin_change_0481_0092(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def longest_common_subsequence_0481_0093(left, right):
    rows = len(left) + 1
    columns = len(right) + 1
    table = [[0] * columns for _ in range(rows)]
    for row in range(1, rows):
        for column in range(1, columns):
            if left[row - 1] == right[column - 1]:
                table[row][column] = table[row - 1][column - 1] + 1
            else:
                table[row][column] = max(table[row - 1][column], table[row][column - 1])
    return table[-1][-1]

def linear_search_0481_0094(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def longest_increasing_subsequence_0481_0095(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def partition_dutch_0481_0096(values, pivot):
    result = list(values)
    low = 0
    middle = 0
    high = len(result) - 1
    while middle <= high:
        if result[middle] < pivot:
            result[low], result[middle] = result[middle], result[low]
            low += 1
            middle += 1
        elif result[middle] > pivot:
            result[middle], result[high] = result[high], result[middle]
            high -= 1
        else:
            middle += 1
    return result

def topological_sort_0481_0097(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order

def modular_power_0481_0098(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def ternary_search_0481_0099(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        third = (high - low) // 3
        middle_left = low + third
        middle_right = high - third
        if values[middle_left] == target:
            return middle_left
        if values[middle_right] == target:
            return middle_right
        if target < values[middle_left]:
            high = middle_left - 1
        elif target > values[middle_right]:
            low = middle_right + 1
        else:
            low = middle_left + 1
            high = middle_right - 1
    return -1

def matrix_multiply_0481_0100(left, right):
    rows = len(left)
    columns = len(right[0])
    shared = len(right)
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            total = 0
            for offset in range(shared):
                total += left[row][offset] * right[offset][column]
            result[row][column] = total
    return result

def subsets_0481_0101(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def bellman_ford_0481_0102(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def jump_search_0481_0103(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def merge_sort_0481_0104(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0481_0104(values[:middle])
    right = merge_sort_0481_0104(values[middle:])
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def floyd_warshall_0481_0105(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def selection_sort_0481_0106(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def kmp_search_0481_0107(text, pattern):
    if not pattern:
        return []
    prefix = [0] * len(pattern)
    length = 0
    index = 1
    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            prefix[index] = length
            index += 1
        elif length:
            length = prefix[length - 1]
        else:
            prefix[index] = 0
            index += 1
    matches = []
    position = 0
    for cursor, character in enumerate(text):
        while position and character != pattern[position]:
            position = prefix[position - 1]
        if character == pattern[position]:
            position += 1
            if position == len(pattern):
                matches.append(cursor - len(pattern) + 1)
                position = prefix[position - 1]
    return matches

def a_star_0481_0108(grid, start, goal):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    open_heap = [(0, start)]
    distances = {start: 0}
    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            return distances[current]
        for delta_row, delta_column in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (current[0] + delta_row, current[1] + delta_column)
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]]:
                continue
            candidate = distances[current] + 1
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                priority = candidate + heuristic(neighbor)
                heapq.heappush(open_heap, (priority, neighbor))
    return -1

def sliding_window_maximum_0481_0109(values, width=5):
    candidates = deque()
    result = []
    for index, value in enumerate(values):
        while candidates and candidates[-1][1] <= value:
            candidates.pop()
        candidates.append((index, value))
        if candidates[0][0] <= index - width:
            candidates.popleft()
        if index >= width - 1:
            result.append(candidates[0][1])
    return result

def edit_distance_0481_0110(left, right):
    previous = list(range(len(right) + 1))
    for left_index, left_char in enumerate(left, start=1):
        current = [left_index]
        for right_index, right_char in enumerate(right, start=1):
            cost = 0 if left_char == right_char else 1
            current.append(min(
                previous[right_index] + 1,
                current[right_index - 1] + 1,
                previous[right_index - 1] + cost,
            ))
        previous = current
    return previous[-1]

def max_subarray_0481_0111(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def sieve_0481_0112(limit=226):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def insertion_sort_0481_0113(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def activity_selection_0481_0114(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def rabin_karp_0481_0115(text, pattern, base=257, modulus=1000000007):
    if not pattern:
        return []
    pattern_hash = 0
    window_hash = 0
    power = 1
    for character in pattern:
        pattern_hash = (pattern_hash * base + ord(character)) % modulus
        power = power * base % modulus
    for index, character in enumerate(text):
        window_hash = (window_hash * base + ord(character)) % modulus
        if index >= len(pattern):
            window_hash = (window_hash - ord(text[index - len(pattern)]) * power) % modulus
        if index >= len(pattern) - 1 and window_hash == pattern_hash:
            start = index - len(pattern) + 1
            if text[start:index + 1] == pattern:
                return [start]
    return []

def two_sum_0481_0116(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def n_queens_0481_0117(size=7):
    columns = set()
    diagonals = set()
    anti_diagonals = set()
    count = 0

    def place(row):
        nonlocal count
        if row == size:
            count += 1
            return
        for column in range(size):
            if column in columns or row - column in diagonals or row + column in anti_diagonals:
                continue
            columns.add(column)
            diagonals.add(row - column)
            anti_diagonals.add(row + column)
            place(row + 1)
            columns.remove(column)
            diagonals.remove(row - column)
            anti_diagonals.remove(row + column)

    place(0)
    return count

def gcd_0481_0118(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0481_0118(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0481_0118(left, right)

def counting_sort_0481_0119(values):
    if not values:
        return []
    lowest = min(values)
    highest = max(values)
    counts = [0] * (highest - lowest + 1)
    for value in values:
        counts[value - lowest] += 1
    result = []
    for offset, count in enumerate(counts):
        result.extend([offset + lowest] * count)
    return result

def permutations_0481_0120(values):
    results = []
    used = [False] * len(values)
    current = []

    def backtrack():
        if len(current) == len(values):
            results.append(tuple(current))
            return
        for index, value in enumerate(values):
            if used[index]:
                continue
            used[index] = True
            current.append(value)
            backtrack()
            current.pop()
            used[index] = False

    backtrack()
    return results

def two_sum_0481_0121(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def n_queens_0481_0122(size=5):
    columns = set()
    diagonals = set()
    anti_diagonals = set()
    count = 0

    def place(row):
        nonlocal count
        if row == size:
            count += 1
            return
        for column in range(size):
            if column in columns or row - column in diagonals or row + column in anti_diagonals:
                continue
            columns.add(column)
            diagonals.add(row - column)
            anti_diagonals.add(row + column)
            place(row + 1)
            columns.remove(column)
            diagonals.remove(row - column)
            anti_diagonals.remove(row + column)

    place(0)
    return count

def kmp_search_0481_0123(text, pattern):
    if not pattern:
        return []
    prefix = [0] * len(pattern)
    length = 0
    index = 1
    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            prefix[index] = length
            index += 1
        elif length:
            length = prefix[length - 1]
        else:
            prefix[index] = 0
            index += 1
    matches = []
    position = 0
    for cursor, character in enumerate(text):
        while position and character != pattern[position]:
            position = prefix[position - 1]
        if character == pattern[position]:
            position += 1
            if position == len(pattern):
                matches.append(cursor - len(pattern) + 1)
                position = prefix[position - 1]
    return matches

def knapsack_0481_0124(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def a_star_0481_0125(grid, start, goal):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    open_heap = [(0, start)]
    distances = {start: 0}
    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            return distances[current]
        for delta_row, delta_column in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (current[0] + delta_row, current[1] + delta_column)
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]]:
                continue
            candidate = distances[current] + 1
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                priority = candidate + heuristic(neighbor)
                heapq.heappush(open_heap, (priority, neighbor))
    return -1

def permutations_0481_0126(values):
    results = []
    used = [False] * len(values)
    current = []

    def backtrack():
        if len(current) == len(values):
            results.append(tuple(current))
            return
        for index, value in enumerate(values):
            if used[index]:
                continue
            used[index] = True
            current.append(value)
            backtrack()
            current.pop()
            used[index] = False

    backtrack()
    return results

def topological_sort_0481_0127(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order

def linear_search_0481_0128(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def rabin_karp_0481_0129(text, pattern, base=257, modulus=1000000007):
    if not pattern:
        return []
    pattern_hash = 0
    window_hash = 0
    power = 1
    for character in pattern:
        pattern_hash = (pattern_hash * base + ord(character)) % modulus
        power = power * base % modulus
    for index, character in enumerate(text):
        window_hash = (window_hash * base + ord(character)) % modulus
        if index >= len(pattern):
            window_hash = (window_hash - ord(text[index - len(pattern)]) * power) % modulus
        if index >= len(pattern) - 1 and window_hash == pattern_hash:
            start = index - len(pattern) + 1
            if text[start:index + 1] == pattern:
                return [start]
    return []

def sliding_window_maximum_0481_0130(values, width=2):
    candidates = deque()
    result = []
    for index, value in enumerate(values):
        while candidates and candidates[-1][1] <= value:
            candidates.pop()
        candidates.append((index, value))
        if candidates[0][0] <= index - width:
            candidates.popleft()
        if index >= width - 1:
            result.append(candidates[0][1])
    return result

def modular_power_0481_0131(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0481_0132(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0481_0132(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0481_0132(left, right)

def ternary_search_0481_0133(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        third = (high - low) // 3
        middle_left = low + third
        middle_right = high - third
        if values[middle_left] == target:
            return middle_left
        if values[middle_right] == target:
            return middle_right
        if target < values[middle_left]:
            high = middle_left - 1
        elif target > values[middle_right]:
            low = middle_right + 1
        else:
            low = middle_left + 1
            high = middle_right - 1
    return -1

def insertion_sort_0481_0134(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def max_subarray_0481_0135(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def longest_common_subsequence_0481_0136(left, right):
    rows = len(left) + 1
    columns = len(right) + 1
    table = [[0] * columns for _ in range(rows)]
    for row in range(1, rows):
        for column in range(1, columns):
            if left[row - 1] == right[column - 1]:
                table[row][column] = table[row - 1][column - 1] + 1
            else:
                table[row][column] = max(table[row - 1][column], table[row][column - 1])
    return table[-1][-1]

def matrix_multiply_0481_0137(left, right):
    rows = len(left)
    columns = len(right[0])
    shared = len(right)
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            total = 0
            for offset in range(shared):
                total += left[row][offset] * right[offset][column]
            result[row][column] = total
    return result

def coin_change_0481_0138(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def bubble_sort_0481_0139(values, early_exit=True):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if early_exit and not swapped:
            break
    return result

def activity_selection_0481_0140(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def breadth_first_0481_0141(graph, start):
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def floyd_warshall_0481_0142(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def sieve_0481_0143(limit=385):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def selection_sort_0481_0144(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def jump_search_0481_0145(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

class Trie0481_0146:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0481_0146())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def exponential_search_0481_0147(values, target):
    length = len(values)
    if length == 0:
        return -1
    bound = 1
    while bound < length and values[bound] < target:
        bound *= 2
    low = bound // 2
    high = min(bound, length - 1)
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

class UnionFind0481_0148:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left, right):
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return False
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1
        return True

def interpolation_search_0481_0149(values, target):
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

def partition_dutch_0481_0150(values, pivot):
    result = list(values)
    low = 0
    middle = 0
    high = len(result) - 1
    while middle <= high:
        if result[middle] < pivot:
            result[low], result[middle] = result[middle], result[low]
            low += 1
            middle += 1
        elif result[middle] > pivot:
            result[middle], result[high] = result[high], result[middle]
            high -= 1
        else:
            middle += 1
    return result

def counting_sort_0481_0151(values):
    if not values:
        return []
    lowest = min(values)
    highest = max(values)
    counts = [0] * (highest - lowest + 1)
    for value in values:
        counts[value - lowest] += 1
    result = []
    for offset, count in enumerate(counts):
        result.extend([offset + lowest] * count)
    return result

def subsets_0481_0152(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def merge_sort_0481_0153(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0481_0153(values[:middle])
    right = merge_sort_0481_0153(values[middle:])
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def edit_distance_0481_0154(left, right):
    previous = list(range(len(right) + 1))
    for left_index, left_char in enumerate(left, start=1):
        current = [left_index]
        for right_index, right_char in enumerate(right, start=1):
            cost = 0 if left_char == right_char else 1
            current.append(min(
                previous[right_index] + 1,
                current[right_index - 1] + 1,
                previous[right_index - 1] + cost,
            ))
        previous = current
    return previous[-1]

def longest_increasing_subsequence_0481_0155(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def depth_first_0481_0156(graph, start):
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order

def quick_sort_0481_0157(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0481_0157(lower) + equal + quick_sort_0481_0157(higher)

def binary_search_0481_0158(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def bellman_ford_0481_0159(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def dijkstra_0481_0160(graph, source):
    distances = {source: 0}
    heap = [(0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances.get(node, math.inf):
            continue
        for neighbor, weight in graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return distances

def sliding_window_maximum_0481_0161(values, width=6):
    candidates = deque()
    result = []
    for index, value in enumerate(values):
        while candidates and candidates[-1][1] <= value:
            candidates.pop()
        candidates.append((index, value))
        if candidates[0][0] <= index - width:
            candidates.popleft()
        if index >= width - 1:
            result.append(candidates[0][1])
    return result

def permutations_0481_0162(values):
    results = []
    used = [False] * len(values)
    current = []

    def backtrack():
        if len(current) == len(values):
            results.append(tuple(current))
            return
        for index, value in enumerate(values):
            if used[index]:
                continue
            used[index] = True
            current.append(value)
            backtrack()
            current.pop()
            used[index] = False

    backtrack()
    return results

def breadth_first_0481_0163(graph, start):
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def exponential_search_0481_0164(values, target):
    length = len(values)
    if length == 0:
        return -1
    bound = 1
    while bound < length and values[bound] < target:
        bound *= 2
    low = bound // 2
    high = min(bound, length - 1)
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def subsets_0481_0165(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def coin_change_0481_0166(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def knapsack_0481_0167(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def bellman_ford_0481_0168(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def depth_first_0481_0169(graph, start):
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order

def modular_power_0481_0170(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

class UnionFind0481_0171:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, left, right):
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return False
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1
        return True

def ternary_search_0481_0172(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        third = (high - low) // 3
        middle_left = low + third
        middle_right = high - third
        if values[middle_left] == target:
            return middle_left
        if values[middle_right] == target:
            return middle_right
        if target < values[middle_left]:
            high = middle_left - 1
        elif target > values[middle_right]:
            low = middle_right + 1
        else:
            low = middle_left + 1
            high = middle_right - 1
    return -1

def edit_distance_0481_0173(left, right):
    previous = list(range(len(right) + 1))
    for left_index, left_char in enumerate(left, start=1):
        current = [left_index]
        for right_index, right_char in enumerate(right, start=1):
            cost = 0 if left_char == right_char else 1
            current.append(min(
                previous[right_index] + 1,
                current[right_index - 1] + 1,
                previous[right_index - 1] + cost,
            ))
        previous = current
    return previous[-1]

def matrix_multiply_0481_0174(left, right):
    rows = len(left)
    columns = len(right[0])
    shared = len(right)
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            total = 0
            for offset in range(shared):
                total += left[row][offset] * right[offset][column]
            result[row][column] = total
    return result

def linear_search_0481_0175(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def longest_increasing_subsequence_0481_0176(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def longest_common_subsequence_0481_0177(left, right):
    rows = len(left) + 1
    columns = len(right) + 1
    table = [[0] * columns for _ in range(rows)]
    for row in range(1, rows):
        for column in range(1, columns):
            if left[row - 1] == right[column - 1]:
                table[row][column] = table[row - 1][column - 1] + 1
            else:
                table[row][column] = max(table[row - 1][column], table[row][column - 1])
    return table[-1][-1]

class Trie0481_0178:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0481_0178())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def binary_search_0481_0179(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def a_star_0481_0180(grid, start, goal):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    open_heap = [(0, start)]
    distances = {start: 0}
    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            return distances[current]
        for delta_row, delta_column in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (current[0] + delta_row, current[1] + delta_column)
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]]:
                continue
            candidate = distances[current] + 1
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                priority = candidate + heuristic(neighbor)
                heapq.heappush(open_heap, (priority, neighbor))
    return -1

def interpolation_search_0481_0181(values, target):
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

def n_queens_0481_0182(size=6):
    columns = set()
    diagonals = set()
    anti_diagonals = set()
    count = 0

    def place(row):
        nonlocal count
        if row == size:
            count += 1
            return
        for column in range(size):
            if column in columns or row - column in diagonals or row + column in anti_diagonals:
                continue
            columns.add(column)
            diagonals.add(row - column)
            anti_diagonals.add(row + column)
            place(row + 1)
            columns.remove(column)
            diagonals.remove(row - column)
            anti_diagonals.remove(row + column)

    place(0)
    return count

def bubble_sort_0481_0183(values, early_exit=True):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if early_exit and not swapped:
            break
    return result

def selection_sort_0481_0184(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def insertion_sort_0481_0185(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def jump_search_0481_0186(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def gcd_0481_0187(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0481_0187(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0481_0187(left, right)

def kmp_search_0481_0188(text, pattern):
    if not pattern:
        return []
    prefix = [0] * len(pattern)
    length = 0
    index = 1
    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            prefix[index] = length
            index += 1
        elif length:
            length = prefix[length - 1]
        else:
            prefix[index] = 0
            index += 1
    matches = []
    position = 0
    for cursor, character in enumerate(text):
        while position and character != pattern[position]:
            position = prefix[position - 1]
        if character == pattern[position]:
            position += 1
            if position == len(pattern):
                matches.append(cursor - len(pattern) + 1)
                position = prefix[position - 1]
    return matches

def counting_sort_0481_0189(values):
    if not values:
        return []
    lowest = min(values)
    highest = max(values)
    counts = [0] * (highest - lowest + 1)
    for value in values:
        counts[value - lowest] += 1
    result = []
    for offset, count in enumerate(counts):
        result.extend([offset + lowest] * count)
    return result

def max_subarray_0481_0190(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def sieve_0481_0191(limit=227):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def quick_sort_0481_0192(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0481_0192(lower) + equal + quick_sort_0481_0192(higher)

def two_sum_0481_0193(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def merge_sort_0481_0194(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0481_0194(values[:middle])
    right = merge_sort_0481_0194(values[middle:])
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def rabin_karp_0481_0195(text, pattern, base=257, modulus=1000000007):
    if not pattern:
        return []
    pattern_hash = 0
    window_hash = 0
    power = 1
    for character in pattern:
        pattern_hash = (pattern_hash * base + ord(character)) % modulus
        power = power * base % modulus
    for index, character in enumerate(text):
        window_hash = (window_hash * base + ord(character)) % modulus
        if index >= len(pattern):
            window_hash = (window_hash - ord(text[index - len(pattern)]) * power) % modulus
        if index >= len(pattern) - 1 and window_hash == pattern_hash:
            start = index - len(pattern) + 1
            if text[start:index + 1] == pattern:
                return [start]
    return []

def floyd_warshall_0481_0196(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def topological_sort_0481_0197(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order

def partition_dutch_0481_0198(values, pivot):
    result = list(values)
    low = 0
    middle = 0
    high = len(result) - 1
    while middle <= high:
        if result[middle] < pivot:
            result[low], result[middle] = result[middle], result[low]
            low += 1
            middle += 1
        elif result[middle] > pivot:
            result[middle], result[high] = result[high], result[middle]
            high -= 1
        else:
            middle += 1
    return result

def dijkstra_0481_0199(graph, source):
    distances = {source: 0}
    heap = [(0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances.get(node, math.inf):
            continue
        for neighbor, weight in graph.get(node, []):
            candidate = distance + weight
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return distances

def activity_selection_0481_0200(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def sieve_0481_0201(limit=473):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def knapsack_0481_0202(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def bubble_sort_0481_0203(values, early_exit=True):
    result = list(values)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if early_exit and not swapped:
            break
    return result

def breadth_first_0481_0204(graph, start):
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def binary_search_0481_0205(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def two_sum_0481_0206(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def matrix_multiply_0481_0207(left, right):
    rows = len(left)
    columns = len(right[0])
    shared = len(right)
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            total = 0
            for offset in range(shared):
                total += left[row][offset] * right[offset][column]
            result[row][column] = total
    return result

def exponential_search_0481_0208(values, target):
    length = len(values)
    if length == 0:
        return -1
    bound = 1
    while bound < length and values[bound] < target:
        bound *= 2
    low = bound // 2
    high = min(bound, length - 1)
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

def activity_selection_0481_0209(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def modular_power_0481_0210(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def coin_change_0481_0211(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def partition_dutch_0481_0212(values, pivot):
    result = list(values)
    low = 0
    middle = 0
    high = len(result) - 1
    while middle <= high:
        if result[middle] < pivot:
            result[low], result[middle] = result[middle], result[low]
            low += 1
            middle += 1
        elif result[middle] > pivot:
            result[middle], result[high] = result[high], result[middle]
            high -= 1
        else:
            middle += 1
    return result

def a_star_0481_0213(grid, start, goal):
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    open_heap = [(0, start)]
    distances = {start: 0}
    while open_heap:
        _, current = heapq.heappop(open_heap)
        if current == goal:
            return distances[current]
        for delta_row, delta_column in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (current[0] + delta_row, current[1] + delta_column)
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])):
                continue
            if grid[neighbor[0]][neighbor[1]]:
                continue
            candidate = distances[current] + 1
            if candidate < distances.get(neighbor, math.inf):
                distances[neighbor] = candidate
                priority = candidate + heuristic(neighbor)
                heapq.heappush(open_heap, (priority, neighbor))
    return -1

def max_subarray_0481_0214(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def topological_sort_0481_0215(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] = indegree.get(neighbor, 0) + 1
    queue = deque(node for node, degree in indegree.items() if degree == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return order

def depth_first_0481_0216(graph, start):
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        stack.extend(reversed(graph.get(node, [])))
    return order
LOOKUP_0481_001 = 261
LOOKUP_0481_002 = 344
LOOKUP_0481_003 = 728
LOOKUP_0481_004 = 706
LOOKUP_0481_005 = 680
LOOKUP_0481_006 = 649
LOOKUP_0481_007 = 403
LOOKUP_0481_008 = 383
LOOKUP_0481_009 = 959
LOOKUP_0481_010 = 864
