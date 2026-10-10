from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        A = Counter(arr)
        res = -1
        for k,v in A.items():
            if k == v:
                res = max(res, k)
        return res