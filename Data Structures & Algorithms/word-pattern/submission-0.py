class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        S = dict()
        P = dict()
        p = pattern
        if len(p) != len(s):
            return False

        for i in range(len(s)):
            if s[i] not in S:
                S[s[i]] = p[i]
            else:
                if S[s[i]] != p[i]:
                    return False
            if p[i] not in P:
                P[p[i]] = s[i]
            else:
                if P[p[i]] != s[i]:
                    return False
        return True
