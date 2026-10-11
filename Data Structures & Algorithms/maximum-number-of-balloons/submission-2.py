from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        H = Counter(text)
        B = [0, 0, 0, 0, 0]
        idx = {"b": 0, "a": 1, "l": 2, "o": 3, "n": 4}
        for c in "balloon":
            if c not in H:
                return 0
            if c in idx:
                B[idx[c]] = H[c]
        count = 0
        while True:
            if (
                B[idx["b"]] < 1
                or B[idx["a"]] < 1
                or B[idx["n"]] < 1
                or B[idx["l"]] < 2
                or B[idx["o"]] < 2
            ):
                return count
            count += 1
            B = [i-1 for i in B]
        return count
