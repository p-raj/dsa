class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_ = -1
        bitmap = [0] * 1001
        for n in nums:
            bitmap[n] = 1
        lo = 1
        hi = 1000

        while lo < hi:
            if lo + hi >= k or bitmap[hi] == 0:
                hi -= 1
            else:
                if bitmap[lo] and lo < hi:
                    max_ = max(max_, lo + hi)
                lo += 1
        return max_