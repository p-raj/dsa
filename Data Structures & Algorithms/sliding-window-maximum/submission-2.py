class Solution:
    def get_max(self, max_, maxi, nums, s, e):
        while s < e:
            if nums[s] > max_:
                max_ = nums[s]
                maxi = s
            s += 1
        return max_, maxi

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        max_ = -10_000
        maxi = -1
        i = 0
        res = []
        while i + k <= len(nums):
            if i > maxi:
                max_, maxi = self.get_max(-1, maxi, nums, i, i + k)
            if nums[i + k - 1] > max_:
                max_ = nums[i + k - 1]
                maxi = i + k - 1
            res.append(max_)
            i += 1
        return res
