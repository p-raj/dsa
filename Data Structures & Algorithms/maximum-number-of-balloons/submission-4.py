from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = 0
        H = Counter(text)
        B = [0, 0, 0, 0, 0]
        idx = {"b": 0, "a": 1, "l": 2, "o": 3, "n": 4}
        for c in "balloon":
            if c not in H:
                return count
            if c in idx:
                B[idx[c]] = H[c]
        while (
            B[idx["b"]] >= 1
            and B[idx["a"]] >= 1
            and B[idx["l"]] >= 2
            and B[idx["o"]] >= 2
            and B[idx["n"]] >= 1
        ):
            count += 1
            for c, i in idx.items():
                if c in "ban":
                    B[i] -= 1
                else:
                    B[i] -= 2
        return count
