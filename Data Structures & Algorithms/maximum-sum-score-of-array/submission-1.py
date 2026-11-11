class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        N = nums
        len_ = len(N)
        pfx = [0] * (len_ + 1)
        # pfx[1] = pfx[0] + N[0]
        for i in range(1, len(pfx)):
            pfx[i] = pfx[i - 1] + N[i - 1]

        max_ = -100000
        for i in range(len(pfx) - 1):
            max_ = max(pfx[-1] - pfx[i], pfx[i + 1] - pfx[0])
        return max_
