class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = {}
        def rec(si: int, ti: int) -> bool:
            if len(s) == si:
                return True
            if len(t) == ti:
                return False
            if (si, ti) in memo:
                return memo[(si, ti)]
            if s[si] == t[ti]:
                memo[(si, ti)] = True
                return rec(si+1, ti+1)
            else:
                memo[(si, ti)] = False
                return rec(si, ti+1)
        return rec(0, 0)