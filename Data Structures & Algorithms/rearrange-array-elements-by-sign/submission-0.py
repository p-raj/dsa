class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = filter(lambda x: x < 0, nums)
        pos = filter(lambda x: x > 0, nums)
        res = []
        for p, n in zip(pos, neg):
            res.append(p)
            res.append(n)
        return res