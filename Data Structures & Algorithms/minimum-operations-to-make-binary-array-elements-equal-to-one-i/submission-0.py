class Solution:
    def minOperations(self, nums: List[int]) -> int:
        lft = 0
        count = 0
        while lft < len(nums):
            rgt = lft
            # skip 
            while rgt < len(nums) and nums[rgt] == 1:
                rgt += 1
            if rgt == len(nums):
                return count
            lft = rgt
            if lft < len(nums) and lft + 1 < len(nums) and lft + 2 < len(nums):
                if nums[lft] == nums[lft+1] == nums[lft+2] == 0:
                    count += 1
                    lft += 3
                else:
                    return -1
            else:
                return -1
        return count