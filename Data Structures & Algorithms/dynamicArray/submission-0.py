class DynamicArray:
    
    def __init__(self, capacity: int):
        self._cap = capacity if capacity > 0 else 0
        self._size = 0
        self._arr = [0] * self._cap
    
    def _update_size(self, op="+") -> None:
        if op == "-":
            if self._size <= 0:
                self._size = 0
            else:
                self._size -= 1
        else:
            self._size += 1

    def get(self, i: int) -> int:
        return self._arr[i]

    def set(self, i: int, n: int) -> None:
        self._arr[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._cap:
            self.resize()
        self._arr.insert(self._size, n)
        self._update_size("+")

    def popback(self) -> int:
        self._update_size("-")
        return self._arr.pop(self._size)

    def resize(self) -> None:
        self._arr = self._arr + [0] * self._cap
        self._cap = self._cap * 2

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._cap
