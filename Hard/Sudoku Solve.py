class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                digit = board[r][c]

                if digit == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[(r // 3) * 3 + (c // 3)].add(digit)

        def backtrack(index: int) -> bool:
            if index == len(empties):
                return True

            r, c = empties[index]
            b = (r // 3) * 3 + (c // 3)

            for d in '123456789':
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    continue

                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)

                if backtrack(index + 1):
                    return True

                board[r][c] = '.'
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[b].remove(d)

            return False

        backtrack(0)