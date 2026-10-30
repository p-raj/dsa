class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        # give away K candies
        # consecutive
        # [..(...)..]
        # keep before and after those and maximize the
        # unique candies
        C = candies
        if k >= len(C):
            return 0
        if k == 0:
            return len(set(C))
        max_dupes = 0
        max_lft = 0
        for lft in range(len(C)-k):
            win_ = set()
            dupes_ = 0
            for i in range(lft, lft+k):
                if C[i] not in win_:
                    win_.add(C[i])
                else:
                    dupes_ += 1
            if max_dupes < dupes_:
                max_dupes = dupes_
                max_lft = lft
        
        count = 0
        keep = set()
        skip = set(range(max_lft, max_lft + k))
        print(skip)
        for i in range(len(C)):
            if i not in skip and C[i] not in keep:
                keep.add(C[i])
        return len(keep)

