class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        # base case
        # f(0) = 1
        # f(1) = 1
        # def f(n):
        #     if n == 0:
        #         return 1
        #     if n == 1:
        #         return 1
        #     return f(n-1) + f(n-2)
        zer, one = 1, 1
        while one <= n:
            tmp = zer
            # f(n-2) -> f(n-1)
            zer = one
            # f(n) -> f(n-1) + f(n-2)
            one = one + tmp
        return zer
        # return f(n)