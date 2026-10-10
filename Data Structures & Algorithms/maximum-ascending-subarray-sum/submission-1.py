class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = float("-inf")
        tot = 0
        prv = nums[0]
        for num in nums:
            if num <= prv:
                res = max(res, tot)
                tot = 0
            tot += num
            prv = num
        return max(res, tot)
