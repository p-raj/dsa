class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append(price)
            return 1

        tmp = self.prices[-1]
        self.prices.append(price)

        if tmp > price:
            return 1
        else:
            j = len(self.prices) - 2
            while j >= 0 and self.prices[j] <= price:
                j -= 1
            return len(self.prices) - 1 - j


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
