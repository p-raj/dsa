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
        max_ = 0
        for lft in range(len(C)-k):
            win_ = set()
            for i in range(lft, lft+k+1):
                if C[i] not in win_:
                    win_.add(C[i])
            if max_ < len(win_):
                max_ = len(win_)
        return max_