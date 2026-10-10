class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        def is_pln(lft: int, rgt: int) -> bool:
            if (lft, rgt) in memo:
                return memo[(lft, rgt)]
            if lft >= rgt:
                return True
            # match and shrink
            memo[(lft, rgt)] = s[lft] == s[rgt] and is_pln(lft+1, rgt-1)
            return memo[(lft, rgt)]
        
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_pln(i, j):
                    if j - i + 1 > len(res):
                        res = s[i:j+1]
        return res
        