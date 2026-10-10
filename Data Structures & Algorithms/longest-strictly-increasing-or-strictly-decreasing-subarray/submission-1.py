class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        lft = 0
        i = 0
        d = 0
        while lft < len(nums):
            istack = 1
            dstack = 1
            rgt = lft + 1
            while rgt < len(nums) and nums[rgt-1] > nums[rgt]:
                dstack += 1
                rgt += 1
            rgt = lft + 1
            while rgt < len(nums) and nums[rgt-1] < nums[rgt]:
                istack += 1
                rgt += 1
            i = max(i, istack)
            d = max(d, dstack)
            lft += 1
        return max(i,d)
