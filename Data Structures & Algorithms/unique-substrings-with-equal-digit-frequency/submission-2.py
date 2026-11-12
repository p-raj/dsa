DBG = False
from collections import defaultdict


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        # SC is {'0': <count>, '1': <count>}
        # if i start from left and grow towards the right
        # whenever i add a character, i know the count of
        # all the other characters, 0-9, only 10 of those
        # can be a quick check O(1)
        # but how long should the left keep expanding?
        # till the end, because strings like 011100
        # match counts at the end
        # a single char is always added to the outcome
        # we can use set() for tracking outcome
        # 01 and 10 are different, but 0 0 and 1 1 are the same
        # 0110 -> 0, 1, 01, 10, 0110
        # 001100 -> 0, 00, 0011, 01, 0110, 1, 11, 1100
        # the production would be O(n2)
        # how to go from O(n2) -> O(n)? Can we?
        # whats the repeat work that we are doing?
        # when going from left to right, we are recalculating
        # the patterns for a sub-string of the original string
        # how can that be optimized?
        # Approach: Brute force
        lft = 0

        def check_(SC):
            DBG and print(SC, set(SC.values()), len(set(SC.values())))
            return SC and len(set(SC.values())) == 1

        sstrs = set()
        while lft < len(s):
            SC = defaultdict(int)
            rgt = lft
            powr = 1
            base = 100
            sstr = 0
            while rgt < len(s):
                ch = ord(s[rgt])
                sstr += ch * (base**powr)
                SC[ch] += 1
                if check_(SC):
                    sstrs.add(sstr)
                rgt += 1
                powr += 1
            lft += 1
        DBG and print(sstrs)
        return len(sstrs)
