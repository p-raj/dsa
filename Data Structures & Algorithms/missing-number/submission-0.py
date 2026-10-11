class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        mn = min(nums)
        mx = max(nums)
        if mn != 0:
            return 0
        if mx != n:
            return mx
        return (n * (n + 1))//2 - sum(nums)