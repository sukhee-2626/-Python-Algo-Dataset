import heapq
import math
from bisect import bisect_left
from collections import deque

def breadth_first_0653_0001(graph, start):
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

def quick_sort_0653_0002(values):
    if len(values) <= 1:
        return list(values)
    pivot = values[len(values) // 2]
    lower = [item for item in values if item < pivot]
    equal = [item for item in values if item == pivot]
    higher = [item for item in values if item > pivot]
    return quick_sort_0653_0002(lower) + equal + quick_sort_0653_0002(higher)

def knapsack_0653_0003(weights, values, capacity):
    table = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current in range(capacity, weight - 1, -1):
            candidate = table[current - weight] + value
            if candidate > table[current]:
                table[current] = candidate
    return table[capacity]

def merge_sort_0653_0004(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort_0653_0004(values[:middle])
    right = merge_sort_0653_0004(values[middle:])
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

def modular_power_0653_0005(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

class UnionFind0653_0006:
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

def selection_sort_0653_0007(values):
    result = list(values)
    for start in range(len(result) - 1):
        smallest = start
        for index in range(start + 1, len(result)):
            if result[index] < result[smallest]:
                smallest = index
        if smallest != start:
            result[start], result[smallest] = result[smallest], result[start]
    return result
LOOKUP_0653_001 = 827
LOOKUP_0653_002 = 786
LOOKUP_0653_003 = 241
LOOKUP_0653_004 = 251
LOOKUP_0653_005 = 836
LOOKUP_0653_006 = 132
LOOKUP_0653_007 = 861
LOOKUP_0653_008 = 75
LOOKUP_0653_009 = 593
LOOKUP_0653_010 = 466
LOOKUP_0653_011 = 315
LOOKUP_0653_012 = 325
LOOKUP_0653_013 = 393
LOOKUP_0653_014 = 286
LOOKUP_0653_015 = 136
LOOKUP_0653_016 = 527
LOOKUP_0653_017 = 709
LOOKUP_0653_018 = 531
LOOKUP_0653_019 = 778
