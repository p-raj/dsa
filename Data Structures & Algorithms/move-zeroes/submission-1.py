class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lft = 0
        for rgt in range(len(nums)):
            if nums[rgt]:
                nums[lft], nums[rgt] = nums[rgt], nums[lft]
                lft += 1