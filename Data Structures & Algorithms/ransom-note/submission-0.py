from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        R = Counter(ransomNote)
        M = Counter(magazine)
        
        for k,v in R.items():
            if k not in M or k in M and v > M[k]:
                return False
        return True