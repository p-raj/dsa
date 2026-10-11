from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        A = Counter(arr)
        res = 0
        for k,v in A.items():
            if k == v:
                res += 1
        return -1 if res == 0 else res