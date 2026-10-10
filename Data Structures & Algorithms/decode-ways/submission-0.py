class Solution:
    def numDecodings(self, s: str) -> int:
        delta = 64
        map_ = {}
        for i in range(65, 91):
            map_[str(i - delta)] = chr(i)

        def is_decodable(num: str) -> bool:
            if num.startswith("0"):
                return False
            return num in map_

        # every step of the way
        # i have two options
        # take[1] or take[2] nums
        # eg 123 -> 1, 23 or 12, 3, or 1,2,3
        # the previous string is already decoded
        # if i am at s[i] - ith index
        # the s[:i-1] is already resolved
        # we record a solution if and only if
        # the complete string has been decoded
        # We can use backtracking (easy)
        # Dynamic programming - figure-out the sub-problem
        # f(i) = (f(i-1) or f(i-2))
        # that is when i am taking in the ith character of s
        # i might have come in from 1 or 2 chars
        # f(i-1) & is_decodable(s[i]) or f(i-2) & is_decodable(s[i-2:i])

        memo = {}

        def f(i: int) -> int:
            # number of ways to decode s[:i]
            if i in memo:
                return memo[i]
            if i == 0:
                return 1
            total = 0
            # take last 1 digit
            if is_decodable(s[i-1:i]):
                total += f(i - 1)
            # take last 2 digits
            if i >= 2 and is_decodable(s[i-2:i]):
                total += f(i - 2)
            memo[i] = total
            return total

        return f(len(s))