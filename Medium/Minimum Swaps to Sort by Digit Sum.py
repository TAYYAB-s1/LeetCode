class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)

        def digit_sum(x: int) -> int:
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))

        visited = [False] * n
        cycles = 0

        for start in range(n):
            if visited[start]:
                continue

            cycles += 1
            k = start

            while not visited[k]:
                visited[k] = True
                k = order[k]

        return n - cycles