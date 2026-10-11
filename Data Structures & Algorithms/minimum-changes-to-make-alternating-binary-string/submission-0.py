class Solution:
    def minOperations(self, s: str) -> int:
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
        half = len(s)//2
        al_evn_1 = abs(half - evn[1])
        al_odd_1 = abs(half - odd[1])
        al_evn_0 = abs(half - evn[0])
        al_odd_0 = abs(half - odd[0])
        print(f"{evn=}, {odd=}\n{al_evn_1=}\n{al_odd_1=}\n{al_evn_0=}\n{al_odd_0=}")
        return abs(max(al_evn_1, al_odd_1)-max(al_evn_0, al_odd_0))
