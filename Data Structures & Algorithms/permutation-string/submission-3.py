from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1 = sorted(s1)
        c1 = Counter(s1)
        c2 = Counter(s2)
        lft, rgt = 0, 0
        while rgt < len(s2):
            lft = rgt
            while lft < len(s2) and s2[lft] not in c1:
                lft += 1
            if len(s2) - lft < len(s1):
                return False
            s_ = s2[lft: lft + len(s1)]
            s_ = sorted(s_)
            if s_ == s1:
                return True
            rgt = lft + 1
        return False