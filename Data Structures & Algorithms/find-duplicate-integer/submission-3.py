class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tracker_mask = 0
        n = 0
        while n < len(nums):
            pos = nums[n]
            if (tracker_mask & (1 << pos)) != 0:
                return pos
            tracker_mask |= (1 << pos)
            n += 1
        