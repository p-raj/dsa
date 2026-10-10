class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            sm = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] > nums[j-1]:
                sm += nums[j]
                j += 1
            res = max(res, sm)
            i = j
        return res