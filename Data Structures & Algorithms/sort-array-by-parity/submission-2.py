class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lft = 0
        for rgt in range(len(nums)):
            if nums[rgt] %2 == 0:
                nums[lft], nums[rgt] = nums[rgt], nums[lft]
                lft += 1
        return nums