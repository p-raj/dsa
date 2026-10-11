from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        H = Counter(text)
        B = [0,0,0,0,0]
        idx = {
            "b": 0,
            "a": 1,
            "l": 2,
            "o": 3,
            "n": 4
        }
        for c in "balloon":
            if c not in H:
                return 0
            if c in idx:
                B[idx[c]] = H[c]
        
        return min(B)