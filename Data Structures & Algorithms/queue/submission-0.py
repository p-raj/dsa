class Deque:
    
    def __init__(self):
        self._list = []

    def isEmpty(self) -> bool:
        return len(self._list) == 0

    def append(self, value: int) -> None:
        self._list.insert(len(self._list), value)

    def appendleft(self, value: int) -> None:
        self._list.insert(0, value)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self._list.pop()

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        return self._list.pop(0)