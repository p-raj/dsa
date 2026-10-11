from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        lft = 1 if s[0] == "0" else 0
        c = Counter(s[1:])
        rgt = c.get("1", 0)
        score = lft + rgt
        i = 1
        l = s[0]
        while i < len(s):
            if s[i] == "1":
                rgt -= 1
            else:
                lft += 1
            l += s[i]
            score = max(score, (lft + rgt))
            i += 1
        return score
