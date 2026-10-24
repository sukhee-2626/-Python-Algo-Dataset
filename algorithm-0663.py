import heapq
import math
from bisect import bisect_left
from collections import deque

def topological_sort_0663_0001(graph):
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

def n_queens_0663_0002(size=5):
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

def bubble_sort_0663_0003(values, early_exit=True):
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

def partition_dutch_0663_0004(values, pivot):
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

def bellman_ford_0663_0005(edges, node_count, source):
    distances = [math.inf] * node_count
    distances[source] = 0
    for _ in range(node_count - 1):
        for start, end, weight in edges:
            candidate = distances[start] + weight
            if candidate < distances[end]:
                distances[end] = candidate
    return distances

def merge_sort_0663_0006(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0663_0006(values[:middle])
    right = merge_sort_0663_0006(values[middle:])
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

def sieve_0663_0007(limit=444):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def a_star_0663_0008(grid, start, goal):
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

def gcd_0663_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0663_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0663_0009(left, right)

def binary_search_0663_0010(values, target):
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
LOOKUP_0663_001 = 571
LOOKUP_0663_002 = 718
LOOKUP_0663_003 = 495
LOOKUP_0663_004 = 162
LOOKUP_0663_005 = 696
LOOKUP_0663_006 = 490
LOOKUP_0663_007 = 664
LOOKUP_0663_008 = 297
LOOKUP_0663_009 = 962
LOOKUP_0663_010 = 889
LOOKUP_0663_011 = 249
LOOKUP_0663_012 = 324
LOOKUP_0663_013 = 636
LOOKUP_0663_014 = 393
LOOKUP_0663_015 = 849
LOOKUP_0663_016 = 168
LOOKUP_0663_017 = 95
LOOKUP_0663_018 = 711
