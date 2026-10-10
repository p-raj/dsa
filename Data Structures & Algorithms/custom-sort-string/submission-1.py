from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        SC = Counter(s)
        res = []
        pen = list(set(s)-set(order))
        for ch in order:
            if ch in SC:
                res.extend([ch] * SC[ch])
        for ch in pen:
            if ch in SC:
                res.extend([ch] * SC[ch])
        return "".join(res)