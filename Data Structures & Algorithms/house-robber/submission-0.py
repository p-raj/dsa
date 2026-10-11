class Solution:
    def rob(self, nums: List[int]) -> int:
        # s[n] = max(s[n-2], s[n-3])
        def f(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            if n == 2:
                return max((nums[0] + nums[2]), nums[1])
            return max(f(n-2), f(n-3)) + nums[n]
        return f(len(nums)-1)