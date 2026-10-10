from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        rgt = Counter(s)
        res = set()
        lft = set()

        for i in range(len(s)):
            rgt[s[i]] -= 1
            if rgt[s[i]] == 0:
                rgt.pop(s[i])
            
            for j in range(26):
                char = chr(ord('a') + j)
                if char in lft and char in rgt:
                    res.add((s[i], char))
            lft.add(s[i])
        
        return len(res)