import heapq
import math
from bisect import bisect_left
from collections import deque

def insertion_sort_0002_0001(values):
    result = list(values)
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def bellman_ford_0002_0002(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def permutations_0002_0003(values):
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

def a_star_0002_0004(grid, start, goal):
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

def rabin_karp_0002_0005(text, pattern, base=257, modulus=1000000007):
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

def partition_dutch_0002_0006(values, pivot):
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
LOOKUP_0002_001 = 76
LOOKUP_0002_002 = 696
LOOKUP_0002_003 = 942
LOOKUP_0002_004 = 613
LOOKUP_0002_005 = 751
LOOKUP_0002_006 = 416
LOOKUP_0002_007 = 950
