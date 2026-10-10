class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def fn(i: int, j: int) -> int:
            key = (i, j)
            if key in memo:
                return memo[key]
            if i >= j:
                memo[key] = 0
                return memo[key]
            val = fn(i+1, j)
            for k in range(i+1, j + 1):
                val = max(val, fn(k, j) + (prices[k] - prices[i]))
            memo[key] = val
            return val

        return fn(0, len(prices) - 1)
