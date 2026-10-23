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
            while (lft + 1) < rgt and s[lft + 1] == ch:
                lft += 1
            while lft < (rgt - 1) and s[rgt - 1] == ch:
                rgt -= 1
            lft += 1
            rgt -= 1
        return rgt - lft + 1
