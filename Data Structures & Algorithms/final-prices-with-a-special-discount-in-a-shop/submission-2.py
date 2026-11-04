
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic stack
        # when can we pop the item
        mstack = []
        answer = []
        
        for p in prices:
            temp = []
            while mstack and mstack[-1] >= p:
                temp.insert(0, mstack[-1]-p)
                mstack.pop()
            answer += temp
            mstack.append(p)

        return answer +  mstack