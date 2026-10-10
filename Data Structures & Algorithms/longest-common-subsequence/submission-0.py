class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # LCS(lft_i, rgt_i) -> int
        # edit distance problem
        # cost insert, cost delete = 1
        # cost match = 1 cost mismatch = inf
        # T1:<....>[i]....
        # T2:<....>[j]....
        # match = LCS(i+1, j+1) + 1
        # delete = LCS(i, j+1) + 1
        # insert = LCS(i+1, j) + 1
        # LCS(0,0) = 0
        T1 = text1
        T2 = text2
        memo = {}
        def Fn(li: int, ri: int) -> int:
            key = (li, ri)
            if key in memo:
                return memo[key]
            if li >= len(T1) or ri >= len(T2):
                return 0
            if T1[li] == T2[ri]:
                memo[key] = Fn(li+1, ri+1) + 1
            else:
                memo[key] = max(
                    Fn(li, ri+1),
                    Fn(li+1, ri)
                )
            return memo[key]
        return Fn(0,0)
