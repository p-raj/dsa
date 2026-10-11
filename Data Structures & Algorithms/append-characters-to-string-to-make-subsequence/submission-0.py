class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        def rec(si: int, ti: int) -> int:
            if len(t) == ti or len(s) == si:
                return ti
            if s[si] == t[ti]:
                return rec(si+1, ti+1)
            else:
                return rec(si+1, ti)
        tmax = rec(0,0)
        return len(t[tmax:])