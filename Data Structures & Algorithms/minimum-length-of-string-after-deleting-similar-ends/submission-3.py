DBG = False
class Solution:
    def minimumLength(self, s: str) -> int:
        # aa<bccabb>a
        # b<cca>bb
        # cca
        lft = 0
        rgt = len(s) - 1
        while lft < rgt:
            if s[lft] == s[rgt]:
                ch = s[lft]
            else:
                break
            while lft < rgt and s[lft] == ch:
                lft += 1
            if lft == rgt:
                return 0
            while lft < rgt and s[rgt] == ch:
                rgt -= 1
            if lft == rgt:
                return 0
            DBG and print(f"{lft=}, {rgt=}, {ch=}, {s[lft]=}, {s[rgt]=}")
        return rgt - lft + 1
