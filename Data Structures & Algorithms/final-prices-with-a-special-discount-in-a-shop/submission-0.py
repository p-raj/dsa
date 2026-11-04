class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack
        # when can we pop the item
        stack = []
        discount = []
        for p in prices:
            while stack and stack[-1] >= p:
                e = stack.pop()
                d = e-p if e >= p else e
                discount.append(d)
            stack.append(p)
        return discount + stack
