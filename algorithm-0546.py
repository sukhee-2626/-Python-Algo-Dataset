import heapq
import math
from bisect import bisect_left
from collections import deque

def activity_selection_0546_0001(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def partition_dutch_0546_0002(values, pivot):
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

def longest_common_subsequence_0546_0003(left, right):
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

def subsets_0546_0004(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def selection_sort_0546_0005(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def edit_distance_0546_0006(left, right):
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

def modular_power_0546_0007(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def a_star_0546_0008(grid, start, goal):
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

def breadth_first_0546_0009(graph, start):
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

def max_subarray_0546_0010(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def bellman_ford_0546_0011(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def interpolation_search_0546_0012(values, target):
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

def merge_sort_0546_0013(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0546_0013(values[:middle])
    right = merge_sort_0546_0013(values[middle:])
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

def ternary_search_0546_0014(values, target):
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

def sieve_0546_0015(limit=398):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0546_0016(left, right):
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

def linear_search_0546_0017(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def longest_increasing_subsequence_0546_0018(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def dijkstra_0546_0019(graph, source):
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

def permutations_0546_0020(values):
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

def rabin_karp_0546_0021(text, pattern, base=257, modulus=1000000007):
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

def floyd_warshall_0546_0022(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

class Trie0546_0023:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0546_0023())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def gcd_0546_0024(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0546_0024(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0546_0024(left, right)

def kmp_search_0546_0025(text, pattern):
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

def sliding_window_maximum_0546_0026(values, width=3):
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

def insertion_sort_0546_0027(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bubble_sort_0546_0028(values, early_exit=True):
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

class UnionFind0546_0029:
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

def binary_search_0546_0030(values, target):
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

def exponential_search_0546_0031(values, target):
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

def two_sum_0546_0032(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def quick_sort_0546_0033(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0546_0033(lower) + equal + quick_sort_0546_0033(higher)

def depth_first_0546_0034(graph, start):
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

def coin_change_0546_0035(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def topological_sort_0546_0036(graph):
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

def n_queens_0546_0037(size=8):
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

def counting_sort_0546_0038(values):
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

def jump_search_0546_0039(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def knapsack_0546_0040(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def depth_first_0546_0041(graph, start):
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

def jump_search_0546_0042(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def quick_sort_0546_0043(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0546_0043(lower) + equal + quick_sort_0546_0043(higher)

def activity_selection_0546_0044(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def matrix_multiply_0546_0045(left, right):
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

def two_sum_0546_0046(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def interpolation_search_0546_0047(values, target):
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

def ternary_search_0546_0048(values, target):
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

def longest_common_subsequence_0546_0049(left, right):
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

def selection_sort_0546_0050(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def n_queens_0546_0051(size=6):
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

def insertion_sort_0546_0052(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def sliding_window_maximum_0546_0053(values, width=4):
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

def bubble_sort_0546_0054(values, early_exit=True):
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

def coin_change_0546_0055(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def knapsack_0546_0056(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def partition_dutch_0546_0057(values, pivot):
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

def subsets_0546_0058(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def permutations_0546_0059(values):
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

def dijkstra_0546_0060(graph, source):
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

def merge_sort_0546_0061(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0546_0061(values[:middle])
    right = merge_sort_0546_0061(values[middle:])
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

def linear_search_0546_0062(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def gcd_0546_0063(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0546_0063(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0546_0063(left, right)

def bellman_ford_0546_0064(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

class Trie0546_0065:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0546_0065())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def modular_power_0546_0066(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def longest_increasing_subsequence_0546_0067(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

class UnionFind0546_0068:
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

def sieve_0546_0069(limit=194):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def binary_search_0546_0070(values, target):
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

def kmp_search_0546_0071(text, pattern):
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

def counting_sort_0546_0072(values):
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

def exponential_search_0546_0073(values, target):
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

def a_star_0546_0074(grid, start, goal):
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

def max_subarray_0546_0075(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def rabin_karp_0546_0076(text, pattern, base=257, modulus=1000000007):
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

def breadth_first_0546_0077(graph, start):
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

def edit_distance_0546_0078(left, right):
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

def floyd_warshall_0546_0079(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def topological_sort_0546_0080(graph):
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

def counting_sort_0546_0081(values):
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

def bubble_sort_0546_0082(values, early_exit=True):
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

def depth_first_0546_0083(graph, start):
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

def jump_search_0546_0084(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def two_sum_0546_0085(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def max_subarray_0546_0086(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def floyd_warshall_0546_0087(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

class UnionFind0546_0088:
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

def exponential_search_0546_0089(values, target):
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

def binary_search_0546_0090(values, target):
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

def dijkstra_0546_0091(graph, source):
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

class Trie0546_0092:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0546_0092())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def breadth_first_0546_0093(graph, start):
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

def gcd_0546_0094(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0546_0094(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0546_0094(left, right)

def rabin_karp_0546_0095(text, pattern, base=257, modulus=1000000007):
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

def bellman_ford_0546_0096(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def insertion_sort_0546_0097(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def coin_change_0546_0098(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def subsets_0546_0099(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def matrix_multiply_0546_0100(left, right):
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

def longest_common_subsequence_0546_0101(left, right):
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

def n_queens_0546_0102(size=8):
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

def activity_selection_0546_0103(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def sliding_window_maximum_0546_0104(values, width=5):
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

def quick_sort_0546_0105(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0546_0105(lower) + equal + quick_sort_0546_0105(higher)

def modular_power_0546_0106(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0546_0107(limit=295):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def longest_increasing_subsequence_0546_0108(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def selection_sort_0546_0109(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def partition_dutch_0546_0110(values, pivot):
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

def interpolation_search_0546_0111(values, target):
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

def permutations_0546_0112(values):
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

def merge_sort_0546_0113(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0546_0113(values[:middle])
    right = merge_sort_0546_0113(values[middle:])
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

def kmp_search_0546_0114(text, pattern):
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

def linear_search_0546_0115(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def edit_distance_0546_0116(left, right):
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

def ternary_search_0546_0117(values, target):
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

def a_star_0546_0118(grid, start, goal):
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

def knapsack_0546_0119(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def topological_sort_0546_0120(graph):
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

def bubble_sort_0546_0121(values, early_exit=True):
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

def breadth_first_0546_0122(graph, start):
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

def sliding_window_maximum_0546_0123(values, width=2):
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

def kmp_search_0546_0124(text, pattern):
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

def permutations_0546_0125(values):
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

def quick_sort_0546_0126(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0546_0126(lower) + equal + quick_sort_0546_0126(higher)

def modular_power_0546_0127(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def longest_increasing_subsequence_0546_0128(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def selection_sort_0546_0129(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def jump_search_0546_0130(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def two_sum_0546_0131(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def bellman_ford_0546_0132(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

class UnionFind0546_0133:
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

def coin_change_0546_0134(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def binary_search_0546_0135(values, target):
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

def gcd_0546_0136(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0546_0136(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0546_0136(left, right)

def matrix_multiply_0546_0137(left, right):
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

def exponential_search_0546_0138(values, target):
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

def ternary_search_0546_0139(values, target):
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

def max_subarray_0546_0140(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def insertion_sort_0546_0141(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def counting_sort_0546_0142(values):
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

def longest_common_subsequence_0546_0143(left, right):
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

def depth_first_0546_0144(graph, start):
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

def floyd_warshall_0546_0145(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

class Trie0546_0146:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0546_0146())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def dijkstra_0546_0147(graph, source):
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

def n_queens_0546_0148(size=4):
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

def partition_dutch_0546_0149(values, pivot):
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

def a_star_0546_0150(grid, start, goal):
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

def interpolation_search_0546_0151(values, target):
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

def activity_selection_0546_0152(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def sieve_0546_0153(limit=159):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def linear_search_0546_0154(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def rabin_karp_0546_0155(text, pattern, base=257, modulus=1000000007):
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

def subsets_0546_0156(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def edit_distance_0546_0157(left, right):
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

def knapsack_0546_0158(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def merge_sort_0546_0159(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0546_0159(values[:middle])
    right = merge_sort_0546_0159(values[middle:])
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

def topological_sort_0546_0160(graph):
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

def longest_common_subsequence_0546_0161(left, right):
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

def selection_sort_0546_0162(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def subsets_0546_0163(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def linear_search_0546_0164(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def edit_distance_0546_0165(left, right):
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

def counting_sort_0546_0166(values):
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

class UnionFind0546_0167:
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

def interpolation_search_0546_0168(values, target):
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

def knapsack_0546_0169(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

class Trie0546_0170:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0546_0170())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def max_subarray_0546_0171(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def bellman_ford_0546_0172(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def dijkstra_0546_0173(graph, source):
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

def n_queens_0546_0174(size=5):
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

def insertion_sort_0546_0175(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def sieve_0546_0176(limit=148):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def exponential_search_0546_0177(values, target):
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

def activity_selection_0546_0178(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def a_star_0546_0179(grid, start, goal):
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

def permutations_0546_0180(values):
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

def jump_search_0546_0181(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def breadth_first_0546_0182(graph, start):
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

def matrix_multiply_0546_0183(left, right):
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

def floyd_warshall_0546_0184(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def modular_power_0546_0185(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def topological_sort_0546_0186(graph):
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

def depth_first_0546_0187(graph, start):
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

def sliding_window_maximum_0546_0188(values, width=6):
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

def bubble_sort_0546_0189(values, early_exit=True):
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

def partition_dutch_0546_0190(values, pivot):
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

def rabin_karp_0546_0191(text, pattern, base=257, modulus=1000000007):
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

def coin_change_0546_0192(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def binary_search_0546_0193(values, target):
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

def longest_increasing_subsequence_0546_0194(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def gcd_0546_0195(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0546_0195(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0546_0195(left, right)

def kmp_search_0546_0196(text, pattern):
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

def quick_sort_0546_0197(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0546_0197(lower) + equal + quick_sort_0546_0197(higher)

def two_sum_0546_0198(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def ternary_search_0546_0199(values, target):
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

def merge_sort_0546_0200(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0546_0200(values[:middle])
    right = merge_sort_0546_0200(values[middle:])
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

def ternary_search_0546_0201(values, target):
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

def exponential_search_0546_0202(values, target):
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

def dijkstra_0546_0203(graph, source):
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

def binary_search_0546_0204(values, target):
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

class UnionFind0546_0205:
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

def interpolation_search_0546_0206(values, target):
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

def depth_first_0546_0207(graph, start):
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

class Trie0546_0208:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        node = self
        for character in word:
            node = node.children.setdefault(character, Trie0546_0208())
        node.terminal = True

    def contains(self, word):
        node = self
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]
        return node.terminal

def knapsack_0546_0209(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def max_subarray_0546_0210(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best

def selection_sort_0546_0211(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result

def subsets_0546_0212(values):
    collected = []
    for mask in range(1 << len(values)):
        subset = [values[index] for index in range(len(values)) if mask & (1 << index)]
        collected.append(subset)
    return collected

def topological_sort_0546_0213(graph):
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

def a_star_0546_0214(grid, start, goal):
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

def sliding_window_maximum_0546_0215(values, width=4):
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

def insertion_sort_0546_0216(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def rabin_karp_0546_0217(text, pattern, base=257, modulus=1000000007):
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

def longest_common_subsequence_0546_0218(left, right):
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

def edit_distance_0546_0219(left, right):
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

def quick_sort_0546_0220(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0546_0220(lower) + equal + quick_sort_0546_0220(higher)

def counting_sort_0546_0221(values):
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

def sieve_0546_0222(limit=246):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def longest_increasing_subsequence_0546_0223(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def floyd_warshall_0546_0224(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def bellman_ford_0546_0225(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def two_sum_0546_0226(values, target):
    seen = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None

def matrix_multiply_0546_0227(left, right):
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

def kmp_search_0546_0228(text, pattern):
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

def bubble_sort_0546_0229(values, early_exit=True):
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

def partition_dutch_0546_0230(values, pivot):
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

def permutations_0546_0231(values):
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

def coin_change_0546_0232(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def merge_sort_0546_0233(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0546_0233(values[:middle])
    right = merge_sort_0546_0233(values[middle:])
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

def breadth_first_0546_0234(graph, start):
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

def modular_power_0546_0235(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def activity_selection_0546_0236(activities):
    ordered = sorted(activities, key=lambda interval: interval[1])
    selected = []
    last_end = -math.inf
    for start, end in ordered:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected

def n_queens_0546_0237(size=7):
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

def jump_search_0546_0238(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def linear_search_0546_0239(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def gcd_0546_0240(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0546_0240(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0546_0240(left, right)

def merge_sort_0546_0241(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0546_0241(values[:middle])
    right = merge_sort_0546_0241(values[middle:])
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

def modular_power_0546_0242(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0546_001 = 407
LOOKUP_0546_002 = 782
LOOKUP_0546_003 = 848
LOOKUP_0546_004 = 702
LOOKUP_0546_005 = 295
LOOKUP_0546_006 = 226
LOOKUP_0546_007 = 103
LOOKUP_0546_008 = 456
LOOKUP_0546_009 = 45
LOOKUP_0546_010 = 78
LOOKUP_0546_011 = 691
LOOKUP_0546_012 = 816
LOOKUP_0546_013 = 58
LOOKUP_0546_014 = 436
LOOKUP_0546_015 = 495
LOOKUP_0546_016 = 61
LOOKUP_0546_017 = 261
LOOKUP_0546_018 = 662
LOOKUP_0546_019 = 541
