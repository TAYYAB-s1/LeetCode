class Solution:
    def sumOfSortable(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)

        s_nums = ''.join(chr(v) for v in nums)
        s_target = ''.join(chr(v) for v in target)

        total = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            sortable = True

            for start in range(0, n, k):
                block = s_nums[start:start + k]
                t_block = s_target[start:start + k]

                if t_block not in block + block:
                    sortable = False
                    break

            if sortable:
                total += k

        return total