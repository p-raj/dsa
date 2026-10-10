from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        S = Counter(s)
        P = {k: (v // 2) * 2 for k, v in S.items()}
        S = {k: (v - P[k]) for k, v in S.items() if (v - P[k])}
        return sum(P.values()) + (1 if bool(S) else 0)
