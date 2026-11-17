class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for lft in range(len(nums) - 2):
            if nums[lft] == 0:
                for i in range(3):
                    nums[lft + i] ^= 1
                count += 1
        return count if nums[-1] == nums[-2] == 1 else -1
