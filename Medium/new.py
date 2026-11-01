import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]

        while heap:
            d, u, run = heapq.heappop(heap)
            if d > dist[u][run]:
                continue
            if u == n - 1:
                return d
            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    nrun = run + 1
                    if nrun > k:
                        continue
                else:
                    nrun = 1
                nd = d + w
                if nd < dist[v][nrun]:
                    dist[v][nrun] = nd
                    heapq.heappush(heap, (nd, v, nrun))

        return -1