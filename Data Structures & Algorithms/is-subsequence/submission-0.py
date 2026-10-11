from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cs = Counter(s)
        i = 0
        ct = {}
        while i < len(t):
            if t[i] in cs:
                ct[t[i]] = ct.get(t[i], 0)
                if ct[t[i]] < cs[t[i]]:
                    ct[t[i]] = 1 + ct.get(t[i], 0)
            i += 1
        return ct == cs
            
