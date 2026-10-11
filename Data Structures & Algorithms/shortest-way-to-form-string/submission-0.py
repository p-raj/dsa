class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        S = source
        T = target

        if not T:
            return 0

        chars = set(S)
        if any(c not in chars for c in T):
            return -1

        memo = {}

        def fn(s, t):
            k = (s, t)

            if k in memo:
                return memo[k]

            # Entire target has been constructed.
            if t >= len(T):
                return 0

            # Current source subsequence is exhausted.
            if s >= len(S):
                memo[k] = 1 + fn(0, t)
                return memo[k]

            if S[s] == T[t]:
                memo[k] = fn(s + 1, t + 1)
            else:
                memo[k] = fn(s + 1, t)

            return memo[k]

        # First source subsequence.
        return 1 + fn(0, 0)