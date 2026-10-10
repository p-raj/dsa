class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            self.ms.append(val)
        else:
            ms = self.getMin()
            if val > ms:
                self.ms.append(ms)
            else:
                self.ms.append(val)
        self.s.append(val)

    def pop(self) -> None:
        self.s.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.ms[-1]