class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        lft = 0
        while lft < len(nums):
            tot = 0
            rgt = lft
            while rgt < len(nums):
                tot += nums[rgt]
                rgt += 1
                if tot == k:
                    res += 1
            lft += 1
        return res