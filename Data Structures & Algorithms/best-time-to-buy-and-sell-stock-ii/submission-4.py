class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {len(prices): 0, len(prices) - 1: 0}

        def fn(i: int) -> int:
            if i not in memo:
                val = fn(i + 1)  # skipped on ith day
                # bought on ith day
                # sold on kth
                for k in range(i + 1, len(prices)):
                    val = max(val, fn(k) + (prices[k] - prices[i]))
                memo[i] = val
            return memo[i]
        return fn(0)
