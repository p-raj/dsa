class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) < 2:
            return 0
        i = 0
        evn = [0, 0]
        odd = [0, 0]
        while i < len(s):
            pos = evn
            if i % 2:
                pos = odd
            if s[i] == "0":
                pos[0] += 1
            else:
                pos[1] += 1
            i += 1
        # either all odds are 1 and odds 0
        # or all evens are 1 and odds 0
        tot = len(s)
        al_e = abs(tot - evn[1] - odd[0])
        al_o = abs(tot - odd[1] - evn[0])
        return min((al_e), (al_o))
