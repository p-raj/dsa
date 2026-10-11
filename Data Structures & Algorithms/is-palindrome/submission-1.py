class Solution:
    def isPalindrome(self, s: str) -> bool:
        strt, end = 0, len(s) - 1
        while strt <= end:
            while not s[strt].isalnum():
                    strt += 1
            while not s[end].isalnum():
                end -= 1
            if s[strt].lower() != s[end].lower():
                return False
            strt += 1
            end -= 1
        return True
