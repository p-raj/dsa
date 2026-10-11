from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cs = Counter(s)
        i = 0
        ct = {}
        j = 0
        while i < len(t):
            while i < len(t) and t[i] != s[j]:
                i += 1
            i += 1
            j += 1
        return j == len(s)