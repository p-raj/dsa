from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        c2 = Counter(s2)
        i = 0
        while i < len(s2):
            # search for the first match
            j = i
            while j < len(s2) and s2[j] not in c1:
                j += 1
            if len(s2) - j < len(s1):
                return False
            k = j
            while j < len(s2) and s2[j] in c1:
                j += 1
            if j-k == len(s1):
                return True
            i = j
        return False