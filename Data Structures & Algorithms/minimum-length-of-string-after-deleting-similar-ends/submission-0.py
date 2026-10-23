class Solution:
    def minimumLength(self, s: str) -> int:
        chars = [s[i] for i in range(len(s))]
        lft = 0
        rgt = len(chars) - 1
        while rgt > lft and chars[lft] == chars[rgt]:
            lft += 1
            rgt -= 1
        return rgt - lft + 1

