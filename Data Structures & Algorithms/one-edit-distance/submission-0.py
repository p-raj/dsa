class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # to this point [x]
        # s[x-1] == t[x-1]
        # at point x
        # 3 things can happen
        # all cost 1
        # increase s
        # decrease t
        # replace 1 char
        """
        f(si, tj) = min(
            f(si+1, tj) + 1,
            f(si, tj+1) + 1,
            f(si+1, tj+1)
        )
        """
        memo = {}

        def f(si: int, tj: int):
            key = (si, tj)
            if key in memo:
                return memo[key]
            if si >= len(s) and tj < len(t):
                memo[key] = len(t) - tj
                return memo[key]
            if tj >= len(t) and si < len(s):
                memo[key] = len(s) - si
                return memo[key]
            if si >= len(s) and tj >= len(t):
                memo[key] = 0
                return memo[key]
            if s[si] == t[tj]:
                memo[key] = f(si + 1, tj + 1)
            else:
                memo[key] = 1 + min(f(si + 1, tj), f(si, tj + 1), f(si + 1, tj + 1))
            return memo[key]

        return f(0, 0) == 1
