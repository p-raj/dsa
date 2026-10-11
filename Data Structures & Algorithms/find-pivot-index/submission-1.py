class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lft = -1
        lsum = 0
        rsum = sum(nums)
        while lft < len(nums):
            if lsum == rsum:
                return lft
            else:
                temp = 0 if lft < 0 else nums[lft]
                lft += 1
                rsum -= nums[lft] if lft < len(nums) else 0
                lsum += temp
        return lft if 0 <= lft < len(nums) else -1