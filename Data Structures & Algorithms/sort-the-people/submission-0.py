class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hn = [(h,n) for h,n in zip(heights, names)]
        hn = sorted(hn, key=lambda x: x[0], reverse=True)
        return [n for _, n in hn]