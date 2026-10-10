class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums.sort()
        prev = nums[0]
        for n in nums[1:]:
            if n == prev:
                return True
            prev = n
        return False