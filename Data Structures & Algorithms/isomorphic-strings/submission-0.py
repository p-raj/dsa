from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        S = Counter(s)
        T = Counter(t)
        sv = sorted(S.values())
        tv = sorted(T.values())
        return sv == tv
