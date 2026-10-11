from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = Counter(s)
        print(smap)
        for c in t:
            if c not in smap or smap[c] == 0:
                return False
            smap[c] -= 1
        return True