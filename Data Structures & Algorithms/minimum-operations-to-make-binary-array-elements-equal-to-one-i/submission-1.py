class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = nums
        len_ = len(N)
        lft = 0
        count = 0
        while lft < len_:
            rgt = lft
            while rgt < len_ and N[rgt] == 1:
                rgt += 1
            if rgt == len_:
                return count
            if lft < len_ - 2:
                nums[lft] = 0 if nums[lft] else 1
                nums[lft + 1] = 0 if nums[lft + 1] else 1
                nums[lft + 2] = 0 if nums[lft + 2] else 1
                count += 1
            lft = rgt + 1
        return count
