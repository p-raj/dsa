class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx1 = 0
        lft = 0
        while lft < len(nums):
            rgt = lft
            cur = 0
            while rgt < len(nums) and nums[rgt]:
                cur += 1
                rgt += 1
            mx1 = max(mx1, cur)
            lft = rgt + 1
        return mx1