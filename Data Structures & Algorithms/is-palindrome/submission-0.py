class Solution:
    def isPalindrome(self, s: str) -> bool:
        strt, end = 0, len(s)-1
        while strt <= end:
            if not s[strt].isalnum():
                strt += 1
            if not s[end].isalnum():
                end -= 1

            if s[strt].lower() == s[end].lower():
                strt += 1
                end -= 1
            else:
                return False
        return True