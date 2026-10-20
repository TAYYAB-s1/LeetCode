from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def match(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                return match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                return first_match and match(i + 1, j + 1)

        return match(0, 0)