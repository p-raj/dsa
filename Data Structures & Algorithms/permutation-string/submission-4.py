from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        c2 = Counter(s2)
        lft, rgt = 0, 0
        while rgt < len(s2):
            lft = rgt
            while lft < len(s2) and s2[lft] not in c1:
                lft += 1
            if len(s2) - lft < len(s1):
                return False
            cs = {}
            for x in range(lft, lft + len(s1)):
                if s2[x] not in cs:
                    cs[s2[x]] = 0
                cs[s2[x]] += 1
            matches = True
            for k in cs:
                matches &= (k in c1 and c1[k] == cs[k])
            if matches:
                return matches
            rgt = lft + 1
        return False