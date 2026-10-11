class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cld = 0
        cok = 0
        while cld < len(g) and cok < len(s):
            if g[cld] <= s[cok]:
                cld += 1
                cok += 1
            else:
                cok += 1
        return cld