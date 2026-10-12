class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lft, rgt = 0, 0

        while rgt < len(nums):
            value = nums[rgt]
            start = rgt

            # Find the end of this group
            while rgt < len(nums) and nums[rgt] == value:
                rgt += 1

            delta = rgt - start

            # Retain at most 2 occurrences
            for _ in range(min(delta, 2)):
                nums[lft] = value
                lft += 1

        return lft