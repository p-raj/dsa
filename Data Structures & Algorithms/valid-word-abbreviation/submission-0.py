class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = [c for c in word]
        a = []
        lft = 0
        while lft < len(abbr):
            if abbr[lft].isalpha():
                a.append(abbr[lft])
                lft += 1
            else:
                if abbr[lft] == '0':
                    return False
                digits = ""
                while lft < len(abbr) and abbr[lft].isdigit():
                    digits += abbr[lft]
                    lft += 1
                spaces = [" "] * int(digits)
                a += spaces

        if len(a) != len(w):
            return False
        
        lft = 0
        while lft < len(a):
            if a[lft] == ' ' or a[lft] == w[lft]:
                lft += 1
            else:
                return False

        return True