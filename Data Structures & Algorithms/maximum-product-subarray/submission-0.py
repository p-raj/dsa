class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}
        def f(idx: int) -> int:
            if idx in memo:
                return memo[idx]
            if idx < 0 or idx >= len(nums):
                return 1
            memo[idx] = max(f(idx-1), 1) * nums[idx]
            return memo[idx]
        
        best = 0
        for i in range(len(nums)):
            best = max(best, f(i))
        return best