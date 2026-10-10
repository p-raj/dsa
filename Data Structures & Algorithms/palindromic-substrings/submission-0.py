class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        def is_pal(lft: int, rgt: int) -> bool:
            key = (lft, rgt)
            if key in memo:
                return memo[key]
            if lft >= rgt:
                memo[key] = True
                return memo[key]
            memo[key] = s[lft] == s[rgt] and is_pal(lft+1, rgt-1)
            return memo[key]
        
        if len(s) <= 1:
            return 1
        
        counter = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_pal(i,j):
                    counter += 1
        
        return counter