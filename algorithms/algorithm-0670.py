import heapq
import math
from bisect import bisect_left
from collections import deque

def sliding_window_maximum_0670_0001(values, width=2):
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

def linear_search_0670_0002(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def partition_dutch_0670_0003(values, pivot):
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

def coin_change_0670_0004(coins, amount):
    best = [math.inf] * (amount + 1)
    best[0] = 0
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return -1 if best[amount] == math.inf else best[amount]

def a_star_0670_0005(grid, start, goal):
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

def dijkstra_0670_0006(graph, source):
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

def rabin_karp_0670_0007(text, pattern, base=257, modulus=1000000007):
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

def longest_common_subsequence_0670_0008(left, right):
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

def depth_first_0670_0009(graph, start):
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

def counting_sort_0670_0010(values):
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

class UnionFind0670_0011:
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

def bubble_sort_0670_0012(values, early_exit=True):
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

def jump_search_0670_0013(values, target):
    length = len(values)
    step = max(1, int(math.sqrt(length)))
    start = 0
    while start < length and values[start] < target:
        start += step
    for index in range(max(0, start - step), min(length, start + 1)):
        if values[index] == target:
            return index
    return -1

def sieve_0670_0014(limit=183):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def merge_sort_0670_0015(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0670_0015(values[:middle])
    right = merge_sort_0670_0015(values[middle:])
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
LOOKUP_0670_001 = 235
LOOKUP_0670_002 = 658
