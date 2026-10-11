class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lft, rgt = 0, 0
        while rgt < len(nums):
            nums[lft] = nums[rgt]
            while rgt < len(nums) and nums[lft] == nums[rgt]:
                rgt += 1
            lft += 1
        return lft