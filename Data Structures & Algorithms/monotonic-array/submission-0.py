class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        for lft in range(1, len(nums)):
            if ((nums[0] < nums[1]) and (nums[lft - 1] > nums[lft])) or (
                (nums[0] > nums[1]) and (nums[lft - 1] < nums[lft])
            ):
                return False
        return True
