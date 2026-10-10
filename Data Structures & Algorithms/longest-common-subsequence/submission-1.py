class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            prev_diag = 0

            for j in range(n - 1, -1, -1):
                down = dp[j]

                if text1[i] == text2[j]:
                    dp[j] = 1 + prev_diag
                else:
                    dp[j] = max(dp[j], dp[j + 1])

                prev_diag = down

        return dp[0]