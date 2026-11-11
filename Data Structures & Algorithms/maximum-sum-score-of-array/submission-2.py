class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        N = nums
        len_ = len(N)
        pfx = [0] * (len_)
        pfx[0] = N[0]
        # pfx[1] = pfx[0] + N[0]
        for i in range(1, len_):
            pfx[i] = pfx[i - 1] + N[i - 1]

        max_ = -100000
        for i in range(len_):
            num = N[i]
            max_ = max(pfx[-1] - pfx[i] + num, pfx[i] - pfx[0] + num)
        return max_
