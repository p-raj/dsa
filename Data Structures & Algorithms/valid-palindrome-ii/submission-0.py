class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.strip()
        strt, end = 0, len(s) - 1
        removed = False
        while strt < end:
            while not s[strt].isalnum() and strt < end:
                strt += 1
            while not s[end].isalnum() and strt < end:
                end -= 1
            print(s[strt].lower(), s[end].lower())
            if not (s[strt].lower() == s[end].lower()):
                if removed:
                    return False
                elif s[strt + 1].lower() == s[end].lower():
                    strt += 1
                    removed = True
                elif s[strt].lower() == s[end - 1].lower():
                    end -= 1
                    removed = True
                else:
                    return False
            strt += 1
            end -= 1
        return True
