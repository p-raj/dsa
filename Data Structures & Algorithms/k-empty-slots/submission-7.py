DBG = False


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        Bidx = {d - 1: idx for idx, d in enumerate(bulbs)}
        # day = 0
        # while day < len(bulbs):
        #     day += 1
        #     oidx = Bidx[day]
        #     # which one would be the closest "on" from the left?
        #     # which one would be the closest "on" from the right?
        #     # beyond those, rest of the elements wont matter
        #     # "on" lights would be the ones that have bulbs[i] < bulbs[curr]
        # we need to construct a peak finder
        # left and right of the peak would be on before peak is on
        # so the delta between the lft and right of the peak if equals
        # k+1 we can find our answer
        min_days = len(bulbs)
        lft = 0
        while lft < len(bulbs):
            rgt = lft + k + 1
            print(f"{lft=}, {rgt=}")
            if rgt >= len(bulbs):
                break
            dlft = Bidx[lft]
            drgt = Bidx[rgt]
            # if lft and rgt can remain on
            # without any light in between them
            # min(lft, rgt) is the answer
            # all the elements in lft and rgt range
            # should be gt lft and rgt
            dmax = max(dlft, drgt)
            nxt_ = lft + 1
            while nxt_ < rgt and Bidx[nxt_] > dmax:
                nxt_ += 1
            if nxt_ == rgt:
                min_days = min(min_days, dmax)
            lft = nxt_
        return -1 if min_days == len(bulbs) else min_days + 1
