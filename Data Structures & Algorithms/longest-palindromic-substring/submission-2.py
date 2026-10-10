class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l: int, r: int):
            nonlocal res

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)       # odd length palindromes
            expand(i, i + 1)   # even length palindromes

        return res
        