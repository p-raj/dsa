class Solution:
    def rob(self, nums: List[int]) -> int:
        # s[n] = max(s[n-2], s[n-3])
        memo = {}
        def f(n):
            if n in memo:
                return memo[n]
            if n == 0:
                memo[0] = nums[0]
                return memo[0]
            if n == 1:
                memo[1] = max(nums[0], nums[1])
                return memo[1]
            if n == 2:
                memo[2] = max((nums[0] + nums[2]), nums[1])
                return memo[2]
            memo[n] = max(f(n-2), f(n-3)) + nums[n]
            return memo[n]
        return f(len(nums)-1)