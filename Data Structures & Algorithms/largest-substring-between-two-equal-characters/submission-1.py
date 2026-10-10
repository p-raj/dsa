class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        D = {}
        mx = -1
        for idx, ch in enumerate(s):
            if ch not in D:
                D[ch] = [None, None]
            if D[ch][0] is None:
                D[ch][0] = idx
            else:
                D[ch][1] = idx
            if D[ch][0] is not None and D[ch][1] is not None:
                mx = max(mx, D[ch][1] - D[ch][0]-1)
        print(D)
        return mx
