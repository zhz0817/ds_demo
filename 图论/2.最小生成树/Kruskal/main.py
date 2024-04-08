# https://leetcode.cn/problems/min-cost-to-connect-all-points/solutions/565990/prim-and-kruskal-by-yexiso-c500/
# https://leetcode.cn/problems/min-cost-to-connect-all-points/description/

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        start = 0
        n = len(points)
        ans = 0
        graph = []
        for i in range(n):
            temp = [0] * n
            graph.append(temp)
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i][j] = dist
                graph[j][i] = dist
        min_dist = [0x3f3f3f3f] * n
        is_visited = [False] * n
        is_visited[start] = True
        for i in range(n):
            if i == start:
                continue
            min_dist[i] = graph[i][start]
        count = 1
        while count < n:
            count += 1
            min_index = -1
            min_val = 0x3f3f3f
            for i in range(n):
                if not is_visited[i] and min_dist[i] < min_val:
                    min_index = i
                    min_val = min_dist[i]
            is_visited[min_index] = True
            ans += min_val
            for i in range(n):
                if not is_visited[i] and graph[i][min_index] < min_dist[i]:
                    min_dist[i] = graph[i][min_index]
        return ans