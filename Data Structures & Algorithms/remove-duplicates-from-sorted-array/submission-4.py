class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lft = 1
        for rgt in range(1, len(nums)):
            if nums[rgt] != nums[rgt-1]:
                nums[lft] = nums[rgt]
                lft += 1
        return lft