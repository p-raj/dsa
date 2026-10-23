DBG = False
class Solution:
    def minimumLength(self, s: str) -> int:
        # aa<bccabb>a
        # b<cca>bb
        # cca
        lft = 0
        rgt = len(s) - 1
        if len(s) < 2:
            return len(s)
        while rgt >= lft:
            if s[lft] == s[rgt]:
                ch = s[lft]
            else:
                break
            while rgt >= lft and ((s[lft] == ch) or (s[rgt] == ch)):
                if s[lft] == ch:
                    lft += 1
                if s[rgt] == ch:
                    rgt -= 1
            DBG and print(f"{lft=}, {rgt=}, {ch=}, {s[lft]=}, {s[rgt]=}")
        return rgt - lft + 1 if lft < rgt else 0
