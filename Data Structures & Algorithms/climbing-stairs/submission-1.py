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
        # return f(n)

        zer, one = 1, 1
        k = 0

        while k < n:
            tmp = zer
            zer = one
            one = one + tmp
            k += 1

        return zer