class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def fn(day: int, is_holding: bool) -> int:
            key = (day, is_holding)
            if key in memo:
                return memo[key]
            
            if day == len(prices):
                if not is_holding:
                    memo[key] = 0
                    return memo[key]
                else:
                    # holding on the last day
                    # is invalid state
                    memo[key] = float("-inf")
                    return memo[key]
            
            # cases
            if not is_holding:
                val = max(
                    fn(day+1, False),  # skip
                    fn(day+1, True) - prices[day]  # buy
                )
            else:
                val = max(
                    fn(day+1, True),  # skip selling
                    fn(day+1, False) + prices[day]  # sold
                )
            memo[key] = val
            return memo[key]
        
        return fn(0, False)