class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack
        # when can we pop the item
        stack = []
        discount = []
        for p in prices:
            print(p, stack)
            disc = []
            while stack and stack[-1] >= p:
                e = stack.pop()
                d = e-p
                print(e, p, d, stack)
                disc.append(d)
            disc.reverse()
            discount += disc
            stack.append(p)
        return discount + stack
