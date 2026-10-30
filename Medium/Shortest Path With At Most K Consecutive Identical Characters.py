import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0

        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        width = k + 1
        INF = float('inf')
        dist = [INF] * (n * width)

        dist[0 * width + 1] = 0
        heap = [(0, 0, 1)]

        while heap:
            d, u, run = heapq.heappop(heap)

            if d > dist[u * width + run]:
                continue

            if u == n - 1:
                return d

            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    new_run = run + 1
                    if new_run > k:
                        continue
                else:
                    new_run = 1

                nd = d + w
                if nd < dist[v * width + new_run]:
                    dist[v * width + new_run] = nd
                    heapq.heappush(heap, (nd, v, new_run))

        return -1