class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_ = -1
        rgt = len(nums) - 1
        while rgt > 0:
            lft = rgt - 1
            while lft >= 0:
                sm_ =  nums[rgt] + nums[lft]
                if sm_ <= k:
                    max_ = max(max_, sm_)
                lft -= 1
            rgt -= 1
        return max_