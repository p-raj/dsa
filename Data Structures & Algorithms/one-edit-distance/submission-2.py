class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if abs(len(s)-len(t)) > 1:
            return False
        if len(s) > len(t):
            s, t = t, s
        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        return len(s) + 1 == len(t)