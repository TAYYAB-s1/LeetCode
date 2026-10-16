class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        B1 = [0] * (n + 2)
        B2 = [0] * (n + 2)

        def update(BIT, i, val):
            while i <= n + 1:
                BIT[i] += val
                i += i & (-i)

        def query(BIT, i):
            s = 0
            while i > 0:
                s += BIT[i]
                i -= i & (-i)
            return s

        def range_add(l, r, val):
            if l > r:
                return
            l1, r1 = l + 1, r + 1
            update(B1, l1, val)
            update(B1, r1 + 1, -val)
            update(B2, l1, val * (l1 - 1))
            update(B2, r1 + 1, -val * r1)

        def prefix_sum(i):
            if i <= 0:
                return 0
            return query(B1, i) * i - query(B2, i)

        def range_sum(l, r):
            if l > r:
                return 0
            l1, r1 = l + 1, r + 1
            return prefix_sum(r1) - prefix_sum(l1 - 1)

        last_seen = {}
        sum_sq = 0
        answer = 0

        for r in range(n):
            prev = last_seen.get(nums[r], -1)
            l_range, r_range = prev + 1, r - 1

            if l_range <= r_range:
                s = range_sum(l_range, r_range)
                m = r_range - l_range + 1
                delta = 2 * s + m
                sum_sq = (sum_sq + delta) % MOD
                range_add(l_range, r_range, 1)

            range_add(r, r, 1)
            sum_sq = (sum_sq + 1) % MOD

            answer = (answer + sum_sq) % MOD
            last_seen[nums[r]] = r

        return answer % MOD