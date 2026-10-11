class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_ = -10_000
        i = 0
        res = []
        if k == 1:
            return nums

        while i < k:
            if max_ < nums[i]:
                max_ = nums[i]
            i += 1
        i = k
        res.append(max_)
        while i < len(nums):
            if max_ < nums[i]:
                max_ = nums[i]
            res.append(max_)
            i += 1
        return res