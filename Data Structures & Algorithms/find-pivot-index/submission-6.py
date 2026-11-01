class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        len_ = len(nums)
        lft_sm = [0] * len_
        rgt_sm = [0] * len_

        for i in range(len_):
            if i == 0:
                delta = 0
            else:
                delta = lft_sm[i - 1]
            lft_sm[i] = delta + nums[i]

        for i in range(len_ - 1, -1, -1):
            if i == len_ - 1:
                delta = 0
            else:
                delta = rgt_sm[i + 1]
            rgt_sm[i] = delta + nums[i]

        for idx, num in enumerate(nums):
            if rgt_sm[idx] - num == lft_sm[idx] - num:
                return idx
        return -1

# Canonical Solution
#         total = sum(nums)
#         leftSum = 0
#         for i in range(len(nums)):
#             rightSum = total - nums[i] - leftSum <----- very cool
#             if leftSum == rightSum:
#                 return i
#             leftSum += nums[i]
#         return -1