class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums):
            nidx = abs(nums[idx]) - 1
            if nums[nidx] < 0:
                return abs(nums[idx])
            nums[nidx] = -nums[nidx]
            idx += 1