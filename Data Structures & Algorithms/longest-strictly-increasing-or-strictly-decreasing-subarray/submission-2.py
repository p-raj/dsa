class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curLen = res = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] or (
                (nums[i - curLen] < nums[i - curLen + 1]) != (nums[i - 1] < nums[i])
            ):
                curLen = 1 if (nums[i] == nums[i - 1]) else 2
                continue

            curLen += 1
            res = max(res, curLen)

        return res
