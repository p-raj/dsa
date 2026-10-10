from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = Counter(s)
        for c in t:
            if c not in smap:
                return False
            smap[c] -= 1
            if smap[c] == 0:
                smap.pop(c, None)
        return True if not smap else False