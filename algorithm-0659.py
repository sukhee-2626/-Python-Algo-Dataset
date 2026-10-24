import heapq
import math
from bisect import bisect_left
from collections import deque

def kmp_search_0659_0001(text, pattern):
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

def longest_increasing_subsequence_0659_0002(values):
    tails = []
    for value in values:
        position = bisect_left(tails, value)
        if position == len(tails):
            tails.append(value)
        else:
            tails[position] = value
    return len(tails)

def quick_sort_0659_0003(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0659_0003(lower) + equal + quick_sort_0659_0003(higher)

def topological_sort_0659_0004(graph):
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

def matrix_multiply_0659_0005(left, right):
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

def gcd_0659_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0659_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0659_0006(left, right)

def breadth_first_0659_0007(graph, start):
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

def a_star_0659_0008(grid, start, goal):
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

def floyd_warshall_0659_0009(matrix):
    size = len(matrix)
    result = [row[:] for row in matrix]
    for middle in range(size):
        for start in range(size):
            for end in range(size):
                through = result[start][middle] + result[middle][end]
                if through < result[start][end]:
                    result[start][end] = through
    return result

def linear_search_0659_0010(values, target):
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1
LOOKUP_0659_001 = 946
LOOKUP_0659_002 = 20
LOOKUP_0659_003 = 230
LOOKUP_0659_004 = 472
LOOKUP_0659_005 = 314
LOOKUP_0659_006 = 272
LOOKUP_0659_007 = 820
LOOKUP_0659_008 = 341
LOOKUP_0659_009 = 442
