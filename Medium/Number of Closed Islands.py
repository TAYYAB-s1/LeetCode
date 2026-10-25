class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def flood(r: int, c: int) -> None:
            stack = [(r, c)]
            grid[r][c] = 1

            while stack:
                x, y = stack.pop()

                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows - 1) or c in (0, cols - 1)) and grid[r][c] == 0:
                    flood(r, c)

        count = 0

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0:
                    count += 1
                    flood(r, c)

        return count
