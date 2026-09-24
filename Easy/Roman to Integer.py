class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            current = values[s[i]]
            next_val = values[s[i + 1]] if i + 1 < n else 0

            if current < next_val:
                total -= current
            else:
                total += current

        return total