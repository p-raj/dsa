class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lft = 0

        for rgt in range(len(nums)):
            if lft < 2 or nums[rgt] != nums[lft - 2]:
                nums[lft] = nums[rgt]
                lft += 1

        return lft