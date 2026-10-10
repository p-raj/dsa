class Solution:
    def minSwaps(self, s: str) -> int:
        # how to do this with DP?
        # A + B = AB, [ + C + ] = [C]
        # greedy, swap leftest with rightest
        # and hope that [C] case builds up
        stack = []
        for c in s:
            if c == '[':
                stack.append(c)
            elif stack:
                stack.pop()
        return (len(stack)+1)//2