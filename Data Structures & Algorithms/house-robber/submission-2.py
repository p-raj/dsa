class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def f(n):
            if n < 0:
                return 0
            if n in memo:
                return memo[n]

            memo[n] = max(
                f(n - 1),
                f(n - 2) + nums[n]
            )
            return memo[n]

        return f(len(nums) - 1)