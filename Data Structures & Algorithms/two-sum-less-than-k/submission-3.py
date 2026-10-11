class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_ = -1
        count_map = [0] * 1001
        for n in nums:
            count_map[n] += 1
        lo = 1
        hi = 1000

        while lo < hi:
            if lo + hi >= k or count_map[hi] == 0:
                hi -= 1
                continue

            if count_map[lo] and lo <= hi:
                max_ = max(max_, lo + hi)
            lo += 1
        return max_