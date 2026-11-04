class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack
        # when can we pop the item
        mstack = []
        answer = [0] * len(prices)

        for idx, prc in enumerate(prices):
            while mstack and mstack[-1][1] >= prc:
                answer[mstack[-1][0]] = mstack[-1][1] - prc
                mstack.pop()
            mstack.append((idx, prc))
        while mstack:
            answer[mstack[-1][0]] = mstack[-1][1]
            mstack.pop()
        return answer
