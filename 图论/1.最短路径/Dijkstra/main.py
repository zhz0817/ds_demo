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
        for i in range(len(times)):
            x = times[i][0] - 1
            y = times[i][1] - 1
            graph[x][y] = times[i][2]
        dis = [INF] * n
        dis[k - 1] = 0
        is_visited = [False] * n
        for i in range(n):
            x = -1
            for y in range(n):
                if is_visited[y] is False and (x == -1 or dis[y] < dis[x]):
                    x = y
            is_visited[x] = True
            for y in range(n):
                dis[y] = min(dis[y], dis[x] + graph[x][y])
        ans = 0
        for i in range(n):
            ans = max(ans, dis[i])
        if ans == INF:
            return -1
        return ans


if __name__ == '__main__':
    pass
