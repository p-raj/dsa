class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def fn(i:int) -> int:
            if i in memo:
                return memo[i]
            if i == len(prices)-1:
                memo[i] = 0
                return memo[i]
            val = fn(i+1)
            for k in range(i+1, len(prices)):
                val = max(val, fn(k) + (prices[k]-prices[i]))
            memo[i] = val
            return memo[i]
        return fn(0)