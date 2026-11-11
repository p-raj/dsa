class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        max_ = float("-inf")
        prefix = 0
        for num in nums:
            prefix += num
            suffix = total - prefix + num
            max_ = max(max_, prefix, suffix)
        return max_
