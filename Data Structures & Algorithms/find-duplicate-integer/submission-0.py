class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        mask = 0
        while n:
            mask =  mask << 1 | 1
            n -= 1
        n = len(nums) - 1
        while n:
            if (mask & (1 << nums[n])) == 0:
                return nums[n]
            mask = mask ^ (1 << nums[n])
            n -= 1
        