class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        strt, end = 0, len(s) - 1
        while strt < end:
            while not s[strt].isalnum() and strt < end:
                strt += 1
            while not s[end].isalnum() and strt < end:
                end -= 1
            print(s[strt].lower(), s[end].lower())
            # if not (s[end].isalnum() and s[strt].isalnum()):
            #     return False
            if not (s[strt].lower() == s[end].lower()):
                return False
            strt += 1
            end -= 1
        return True