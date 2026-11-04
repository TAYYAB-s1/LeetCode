class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            parts = []
            i = 0

            while i < len(result):
                j = i

                while j < len(result) and result[j] == result[i]:
                    j += 1

                parts.append(str(j - i))
                parts.append(result[i])
                i = j

            result = ''.join(parts)

        return result
