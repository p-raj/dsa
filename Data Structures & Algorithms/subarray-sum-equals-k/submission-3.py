from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # for lft in range(len(nums)):
        #     sm = 0
        #     for rgt in range(lft, len(nums)):
        #         if sum(sm[lft:rgt+1]) == k:
        #             count += 1
        # return count
        freq = defaultdict(int)
        freq[0] += 1
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            # prefix = sum(sm[lft:rgt+1])
            res += freq.get(prefix - k, 0)
            freq[prefix] += 1
        print(freq)
        return res
