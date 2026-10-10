class Solution:
    def firstUniqChar(self, s: str) -> int:
        D = {}
        for idx, ch in enumerate(s):
            if ch not in D:
                D[ch] = [None, None]
            if D[ch][0] is None:
                D[ch][0] = idx
                D[ch][1] = 0
            D[ch][1] += 1
        return next((D[ch][0] for ch in D if D[ch][1] == 1), -1)