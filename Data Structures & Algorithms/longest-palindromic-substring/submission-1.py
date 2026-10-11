class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def f(l: int, r: int):
            nonlocal res
            if l > r or r >= len(s) or l < 0:
                return
            mid = (l + r)//2
            if s[l] != s[r]:
                if len(res) < r-l:
                    res = s[l+1:r]
                f(l, mid-1)
                f(mid+1, r)
            else:
                f(l-1, r+1)
        if len(s) == 1:
            return s
        f(0, len(s)-1)
        print(res)
        return res
