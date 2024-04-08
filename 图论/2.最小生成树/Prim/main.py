# https://leetcode.cn/problems/min-cost-to-connect-all-points/solutions/565990/prim-and-kruskal-by-yexiso-c500/
from typing import List
class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        return self.find(self.parents[x])

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parents[root_x] = root_y

    def is_union(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Edge:
    def __init__(self, node1: int, node2: int, weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


def getDist(points: List[List[int]], x: int, y: int) -> int:
    return abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        list1 = []
        for i in range(n):
            for j in range(i + 1, n):
                list1.append(Edge(i, j, getDist(points, i, j)))
        ans = 0
        count = 1
        list1 = sorted(list1, key=lambda x: x.weight, reverse=False)
        for info in list1:
            x = info.node1
            y = info.node2
            weight = info.weight
            if not uf.is_union(x, y):
                ans += weight
                count += 1
                uf.union(x, y)
                if count == n:
                    break
        return ans