class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lft, rgt = 0, 0
        while rgt < len(nums):
            while rgt < len(nums) and nums[rgt] % 2:
                rgt += 1
            if lft == rgt:
                lft += 1
                rgt += 1
                continue
            if lft < len(nums) and rgt < len(nums):
                nums[lft], nums[rgt] = nums[rgt], nums[lft]
            lft += 1
        return nums