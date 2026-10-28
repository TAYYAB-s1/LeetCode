class Solution:
    def minXorPath(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [set() for _ in range(n)]

        for i in range(m):
            cur = [set() for _ in range(n)]

            for j in range(n):
                v = grid[i][j]

                if i == 0 and j == 0:
                    cur[j] = {v}
                    continue

                reachable = set()

                if i > 0:
                    reachable |= {x ^ v for x in prev[j]}

                if j > 0:
                    reachable |= {x ^ v for x in cur[j - 1]}

                cur[j] = reachable

            prev = cur

        return min(prev[n - 1])