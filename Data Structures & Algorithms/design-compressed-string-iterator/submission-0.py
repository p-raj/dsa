class StringIterator:
    def _hydrate(self, compressedString: str):
        S = compressedString
        i = 0
        while i < len(compressedString) - 1:
            chr_ = S[i]
            cnt_ = int(S[i+1])
            self.chr_.append(chr_)
            self.idx_.append(cnt_)
            i += 2

    def __init__(self, compressedString: str):
        self.chr_ = []
        self.idx_ = []
        self.pos_ = 0
        self._hydrate(compressedString)

    def next(self) -> str:
        r = self.chr_[self.pos_]
        self.idx_[self.pos_] -= 1
        if self.idx_[self.pos_] == 0:
            self.pos_ += 1
        return r

    def hasNext(self) -> bool:
        return self.idx_[self.pos_] > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
