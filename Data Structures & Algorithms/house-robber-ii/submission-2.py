class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob2(nums: List[int]) -> int:
            memo = {}
            def f(n):
                if n < 0:
                    return 0
                if n == 0:
                    memo[0] = nums[0]
                if n == 1:
                    memo[1] = max(nums[0], nums[1])

                if n in memo:
                    return memo[n]

                memo[n] = max(
                    f(n - 1),
                    f(n - 2) + nums[n]
                )
                return memo[n]
            return f(len(nums)-1)
        
        if len(nums) == 1:
            return nums[0]
        return max(
            rob2(nums[1:]),
            rob2(nums[:-1]),
        )