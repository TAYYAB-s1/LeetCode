class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return len(nums) * max(nums) - sum(nums)
