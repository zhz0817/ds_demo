import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 0x3f3f3f
        graph = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(INF)
            graph.append(temp)
            graph[i][i] = 0
        for i in range(len(times)):
            x = times[i][0] - 1
            y = times[i][1] - 1
            graph[x][y] = times[i][2]
        for i in range(n):
            for j in range(n):
                for p in range(n):
                    graph[j][p] = min(graph[j][p],graph[j][i]+graph[i][p])
        ans = 0
        for i in range(n):
            ans = max(ans,graph[k-1][i])
        if ans == INF:
            return -1
        return ans


if __name__ == '__main__':
    pass
