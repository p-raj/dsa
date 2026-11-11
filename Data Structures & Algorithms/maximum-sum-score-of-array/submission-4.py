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
            prefix_score = pfx[i]
            suffix_score = pfx[-1] - pfx[i] + nums[i]
            max_ = max(max_, prefix_score, suffix_score)
        return max_
