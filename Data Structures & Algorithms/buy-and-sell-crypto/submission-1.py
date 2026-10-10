class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        i = 0
        while i < len(prices) - 1:
            j = i + 1
            print(prices[j], prices[i])
            while j < len(prices) and prices[j] > prices[i]:
                if prices[j] - prices[i] > mp:
                    mp = prices[j] - prices[i]
                j += 1
            i = j
        return mp