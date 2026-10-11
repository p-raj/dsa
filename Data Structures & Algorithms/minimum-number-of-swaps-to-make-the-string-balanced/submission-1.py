class Solution:
    def minSwaps(self, s: str) -> int:
        # how to do this with DP?
        # A + B = AB, [ + C + ] = [C]
        # greedy, swap leftest with rightest
        # and hope that [C] case builds up
        s = [c for c in s]
        lft = 0
        rgt = len(s) - 1
        count = 0
        while lft < rgt:
            # A
            if (s[lft] == '[' and s[lft+1] == ']'):
                lft += 2
            # B
            elif (s[rgt-1] == '[' and s[rgt] == ']'):
                rgt -= 2
            # case C
            elif s[lft] == '[' and s[rgt] == ']':
                lft += 1
                rgt -= 1
            else:
                # print("B4] ", "".join(s), f" {lft=} {rgt=} ")
                if (s[lft] == ']' and s[rgt] == '['):
                    s[lft], s[rgt] = s[rgt], s[lft]
                    count += 1
                elif (s[lft] == '[' and s[rgt] == '['):
                    lft += 1
                elif (s[lft] == ']' and s[rgt] == ']'):
                    rgt -= 1
                # print("AF] ", "".join(s), f" {lft=} {rgt=} ")
                # print("."*4)
        return count
