class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        lft = 0
        rgt = len(s) - 1

        while lft < rgt and s[lft] != s[rgt]:
            lft += 1
            if s[lft] == s[rgt]:
                break
            rgt -= 1
            if s[lft] == s[rgt]:
                break
        return rgt - lft - 1