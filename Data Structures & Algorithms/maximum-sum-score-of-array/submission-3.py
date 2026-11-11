class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        N = nums
        len_ = len(N)
        pfx = [0] * (len_)
        pfx[0] = N[0]
        running_sm = 0
        for i in range(len_):
            running_sm += N[i]
            pfx[i] = running_sm
            running_sm = pfx[i]
            

        max_ = -100000
        for i in range(len_):
            num = N[i]
            max_ = max(pfx[-1] - pfx[i] + num, pfx[i] - pfx[0] + num)
        return max_
