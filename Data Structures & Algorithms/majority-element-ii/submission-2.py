import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        third = math.floor(len(nums)/3)
        lft = 0
        res = set()
        while lft < len(nums):
            rgt = lft + 1
            while rgt < len(nums) and nums[rgt] == nums[lft]:
                rgt += 1
            if (rgt-lft) > third:
                res.add(nums[lft])
            lft = rgt
        return list(res)