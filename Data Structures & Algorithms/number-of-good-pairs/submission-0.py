from collections import Counter
import math

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        C = Counter(nums)
        res = 0
        for v in C.values():
            if v > 2:
                res += math.comb(v, 2)
            elif v == 2:
                res += 1
        return res
