import heapq
import math
from bisect import bisect_left
from collections import deque

def max_subarray_0991_0001(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def kmp_search_0991_0002(text, pattern):
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

class Trie0991_0003:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0991_0003())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def breadth_first_0991_0004(graph, start):
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

class UnionFind0991_0005:
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

def longest_common_subsequence_0991_0006(left, right):
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

def ternary_search_0991_0007(values, target):
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

def modular_power_0991_0008(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def floyd_warshall_0991_0009(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def gcd_0991_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0991_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0991_0010(left, right)

def exponential_search_0991_0011(values, target):
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

def sliding_window_maximum_0991_0012(values, width=3):
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

def bellman_ford_0991_0013(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def topological_sort_0991_0014(graph):
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

def sieve_0991_0015(limit=272):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def edit_distance_0991_0016(left, right):
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

def counting_sort_0991_0017(values):
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

def depth_first_0991_0018(graph, start):
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

def knapsack_0991_0019(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def a_star_0991_0020(grid, start, goal):
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

def bubble_sort_0991_0021(values, early_exit=True):
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

def matrix_multiply_0991_0022(left, right):
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

def linear_search_0991_0023(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def selection_sort_0991_0024(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def coin_change_0991_0025(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def n_queens_0991_0026(size=8):
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

def longest_increasing_subsequence_0991_0027(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def insertion_sort_0991_0028(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def dijkstra_0991_0029(graph, source):
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

def jump_search_0991_0030(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def quick_sort_0991_0031(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0991_0031(lower) + equal + quick_sort_0991_0031(higher)

def subsets_0991_0032(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def interpolation_search_0991_0033(values, target):
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

def merge_sort_0991_0034(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0991_0034(values[:middle])
    right = merge_sort_0991_0034(values[middle:])
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

def permutations_0991_0035(values):
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

def partition_dutch_0991_0036(values, pivot):
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

def two_sum_0991_0037(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def rabin_karp_0991_0038(text, pattern, base=257, modulus=1000000007):
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

def binary_search_0991_0039(values, target):
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

def activity_selection_0991_0040(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def dijkstra_0991_0041(graph, source):
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

def sieve_0991_0042(limit=385):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sliding_window_maximum_0991_0043(values, width=5):
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

def max_subarray_0991_0044(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def ternary_search_0991_0045(values, target):
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

def counting_sort_0991_0046(values):
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

def modular_power_0991_0047(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def knapsack_0991_0048(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def permutations_0991_0049(values):
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

class Trie0991_0050:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0991_0050())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def jump_search_0991_0051(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def n_queens_0991_0052(size=8):
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

def selection_sort_0991_0053(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def matrix_multiply_0991_0054(left, right):
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

def longest_common_subsequence_0991_0055(left, right):
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

def exponential_search_0991_0056(values, target):
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

def kmp_search_0991_0057(text, pattern):
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

def insertion_sort_0991_0058(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def subsets_0991_0059(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def bellman_ford_0991_0060(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def longest_increasing_subsequence_0991_0061(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def gcd_0991_0062(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0991_0062(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0991_0062(left, right)

def interpolation_search_0991_0063(values, target):
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

def edit_distance_0991_0064(left, right):
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

def a_star_0991_0065(grid, start, goal):
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

def partition_dutch_0991_0066(values, pivot):
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

def breadth_first_0991_0067(graph, start):
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

def two_sum_0991_0068(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def linear_search_0991_0069(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

class UnionFind0991_0070:
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

def rabin_karp_0991_0071(text, pattern, base=257, modulus=1000000007):
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

def activity_selection_0991_0072(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def binary_search_0991_0073(values, target):
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

def floyd_warshall_0991_0074(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def depth_first_0991_0075(graph, start):
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

def bubble_sort_0991_0076(values, early_exit=True):
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

def merge_sort_0991_0077(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0991_0077(values[:middle])
    right = merge_sort_0991_0077(values[middle:])
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

def topological_sort_0991_0078(graph):
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

def quick_sort_0991_0079(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0991_0079(lower) + equal + quick_sort_0991_0079(higher)

def coin_change_0991_0080(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def merge_sort_0991_0081(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0991_0081(values[:middle])
    right = merge_sort_0991_0081(values[middle:])
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

def partition_dutch_0991_0082(values, pivot):
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

def interpolation_search_0991_0083(values, target):
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

def knapsack_0991_0084(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

class UnionFind0991_0085:
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

def two_sum_0991_0086(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def rabin_karp_0991_0087(text, pattern, base=257, modulus=1000000007):
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

def coin_change_0991_0088(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def floyd_warshall_0991_0089(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def gcd_0991_0090(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0991_0090(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0991_0090(left, right)

def sieve_0991_0091(limit=318):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def longest_increasing_subsequence_0991_0092(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def permutations_0991_0093(values):
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

def max_subarray_0991_0094(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def subsets_0991_0095(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def edit_distance_0991_0096(left, right):
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

def depth_first_0991_0097(graph, start):
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

def breadth_first_0991_0098(graph, start):
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

def sliding_window_maximum_0991_0099(values, width=4):
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

def dijkstra_0991_0100(graph, source):
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

def bellman_ford_0991_0101(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def matrix_multiply_0991_0102(left, right):
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

def topological_sort_0991_0103(graph):
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

def longest_common_subsequence_0991_0104(left, right):
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

def quick_sort_0991_0105(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0991_0105(lower) + equal + quick_sort_0991_0105(higher)

def counting_sort_0991_0106(values):
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

def modular_power_0991_0107(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def exponential_search_0991_0108(values, target):
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

def a_star_0991_0109(grid, start, goal):
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

def selection_sort_0991_0110(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def n_queens_0991_0111(size=6):
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

def binary_search_0991_0112(values, target):
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

def bubble_sort_0991_0113(values, early_exit=True):
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

def kmp_search_0991_0114(text, pattern):
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

class Trie0991_0115:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0991_0115())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def linear_search_0991_0116(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def ternary_search_0991_0117(values, target):
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

def jump_search_0991_0118(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def insertion_sort_0991_0119(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def activity_selection_0991_0120(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def breadth_first_0991_0121(graph, start):
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

def coin_change_0991_0122(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def merge_sort_0991_0123(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0991_0123(values[:middle])
    right = merge_sort_0991_0123(values[middle:])
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

def quick_sort_0991_0124(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0991_0124(lower) + equal + quick_sort_0991_0124(higher)

def bubble_sort_0991_0125(values, early_exit=True):
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

class UnionFind0991_0126:
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

def kmp_search_0991_0127(text, pattern):
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

def a_star_0991_0128(grid, start, goal):
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

def gcd_0991_0129(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0991_0129(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0991_0129(left, right)

def rabin_karp_0991_0130(text, pattern, base=257, modulus=1000000007):
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

def subsets_0991_0131(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def floyd_warshall_0991_0132(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def two_sum_0991_0133(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def n_queens_0991_0134(size=4):
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

class Trie0991_0135:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0991_0135())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def modular_power_0991_0136(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def longest_increasing_subsequence_0991_0137(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def interpolation_search_0991_0138(values, target):
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

def insertion_sort_0991_0139(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bellman_ford_0991_0140(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def binary_search_0991_0141(values, target):
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

def jump_search_0991_0142(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def selection_sort_0991_0143(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def edit_distance_0991_0144(left, right):
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

def ternary_search_0991_0145(values, target):
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

def dijkstra_0991_0146(graph, source):
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

def knapsack_0991_0147(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def sieve_0991_0148(limit=184):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def topological_sort_0991_0149(graph):
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

def activity_selection_0991_0150(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def sliding_window_maximum_0991_0151(values, width=7):
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

def linear_search_0991_0152(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def permutations_0991_0153(values):
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

def max_subarray_0991_0154(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best
LOOKUP_0991_001 = 645
LOOKUP_0991_002 = 677
LOOKUP_0991_003 = 302
LOOKUP_0991_004 = 707
LOOKUP_0991_005 = 912
LOOKUP_0991_006 = 965
LOOKUP_0991_007 = 513
LOOKUP_0991_008 = 699
LOOKUP_0991_009 = 730
LOOKUP_0991_010 = 979
LOOKUP_0991_011 = 228
LOOKUP_0991_012 = 256
