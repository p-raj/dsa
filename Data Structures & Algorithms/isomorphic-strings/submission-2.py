from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def comp(s: str, t: str) -> bool:
            MAP = {}
            i = 0
            while i < len(s):
                if s[i] not in MAP:
                    MAP[s[i]] = t[i]
                else:
                    if MAP[s[i]] != t[i]:
                        return False
                i += 1
            return True
        return comp(s, t) and comp(t,s)