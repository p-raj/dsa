class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.wch = 0
        self.i1 = 0
        self.i2 = 0
        self.v1 = v1
        self.v2 = v2

    def next(self) -> int:
        res = None
        while res is None:
            if self.wch == 0:
                if self.i1 < len(self.v1):
                    res = self.v1[self.i1]
                    self.i1 += 1
                    self.wch = 1
                    break
                self.wch = 1
            if self.wch == 1:
                if self.i2 < len(self.v2):
                    res = self.v2[self.i2]
                    self.i2 += 1
                    self.wch = 0
                    break
                self.wch = 0
        return res

    def hasNext(self) -> bool:
        return (
            (self.i1 < len(self.v1))
            or
            (self.i2 < len(self.v2))
        )

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
