class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        mask = 0
        while n:
            mask =  mask << 1 | 1
            n -= 1
        tracker_mask = 0
        n = 0
        while n < len(nums):
            pos = nums[n]
            if (tracker_mask & (1 << pos)) != 0:
                return pos
            tracker_mask |= (1 << pos)
            print(bin(tracker_mask))
            n += 1
        