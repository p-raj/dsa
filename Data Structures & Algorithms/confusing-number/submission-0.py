class Solution:
    def len_num(self, n) -> int:
        pow_ = 1
        while 10 ** pow_ <= n:
            pow_ += 1
        return pow_

    def flip_num(self, n) -> int | None:
        map_ = {
                0:0,
                1:1,
                6:9,
                8:8,
                9:6
            }
        fnum = 0
        cpow = 0
        num_len = self.len_num(n)
        nums = []
        last = []
        while num_len-cpow > 0:
            last_ = n % 10
            n = (n-last_) // 10
            if last_ not in map_:
                return None
            fnum += ((10**(num_len-cpow-1)) * map_[last_])
            cpow+= 1
        return fnum


    def confusingNumber(self, n: int) -> bool:
        flipped = self.flip_num(n)
        return flipped and flipped != n