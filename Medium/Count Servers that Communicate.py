class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    row_count[r] += 1
                    col_count[c] += 1

        total = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (row_count[r] > 1 or col_count[c] > 1):
                    total += 1

        return total