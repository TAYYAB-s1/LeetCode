class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    total = 0
                    stack = [(r, c)]
                    total += grid[r][c]
                    grid[r][c] = 0

                    while stack:
                        x, y = stack.pop()

                        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] > 0:
                                total += grid[nx][ny]
                                grid[nx][ny] = 0
                                stack.append((nx, ny))

                    if total % k == 0:
                        count += 1

        return count