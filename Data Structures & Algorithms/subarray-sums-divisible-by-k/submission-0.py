from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # res = 0
        # for lft in range(len(nums)):
        #     sm = 0
        #     for rgt in range(lft, len(nums)):
        #         sm += nums[rgt]
        #         if sm % k == 0:
        #             res += 1
        # return res
        prefix_freq = defaultdict(int)
        prefix_freq[0] = 1
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            rem = prefix % k
            res += prefix_freq.get(rem, 0)
            prefix_freq[rem] += 1
        return res
