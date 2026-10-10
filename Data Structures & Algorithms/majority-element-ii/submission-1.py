import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        third = math.floor(len(nums)/3)
        lft = 0
        res = set()
        while lft < len(nums):
            rgt = lft + 1
            count = 0
            while rgt < len(nums) and nums[rgt] == nums[lft]:
                count += 1
                rgt += 1
            if count >= third:
                res.add(nums[lft])
            print(count, nums[lft], third)
            lft = rgt
        return list(res)