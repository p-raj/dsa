class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def f(amt: int) -> int:
            if amt in memo:
                return memo[amt]
            if amt < 0:
                return -1
            if amt == 0:
                return 0
            best = float("inf")
            for c in coins:
                if amt >= c:
                    best = min(best, 1+f(amt-c))
            memo[amt] = best
            return memo[amt]
        
        ans = f(amount)
        return ans if ans != float("inf") else -1