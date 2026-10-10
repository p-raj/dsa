class Solution:
    def maximumProfit(
        self,
        profit: List[int],
        weight: List[int],
        capacity: int,
    ) -> int:
        # used_indexes = set()
        # dp[n] = dp[n-1] + max(profit that has wt < capacity)
        # You may either:
        # * take an item once
        # * or skip it
        # state = (idx, cap)
        # dp[i, c] = max(dp[i+1, c], p[i] + dp[i+1, c-w[i]])
        # dp[i+1, c] <- skipped the ith element
        # dp[i+1, c-w[i]] <- took the ith element
        # if i == len(p): dp[n, c] = 0
        memo = {}
        n = len(profit)

        def dp(i, c):
            if i == n:
                return 0
            if (i,c) in memo:
                return memo[(i,c)]

            best = dp(i+1, c)
            if weight[i] <= c:
                best = max(
                    best,
                    profit[i] + dp(i+1, c-weight[i])
                )
            memo[(i,c)] = best
            return best
        
        return dp(0, capacity)
