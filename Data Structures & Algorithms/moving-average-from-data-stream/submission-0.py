class MovingAverage:

    def __init__(self, size: int):
        self.win = [0] * size
        self.cur = 0
        self.cnt = 0

    def next(self, val: int) -> float:
        self.win[self.cur] = val
        self.cur += 1
        self.cur = self.cur % len(self.win)
        if self.cnt < len(self.win):
            self.cnt += 1
        return sum(self.win)/self.cnt


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
