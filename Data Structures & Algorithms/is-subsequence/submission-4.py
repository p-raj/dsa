class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        ct = {}
        j = 0
        while i < len(t) and j < len(s):
            while i < len(t) and t[i] != s[j]:
                i += 1
            i += 1
            j += 1
        return j == len(s)