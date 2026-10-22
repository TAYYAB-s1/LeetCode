class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        c = nums[0]
        best = float('inf')

        if all(nums[i] == (c + i) % n for i in range(n)):
            best = 0 if c == 0 else min(n - c, c + 2)

        if all(nums[i] == (c - i) % n for i in range(n)):
            m = (c + 1) % n
            best = min(best, 1 if m == 0 else min(m, n - m) + 1)

        return -1 if best == float('inf') else best