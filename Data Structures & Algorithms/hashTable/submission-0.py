class HashTable:
    
    def __init__(self, capacity: int):
        self.table = []
        while capacity > 0:
            self.table.append([])
            capacity -= 1
        self.size = 0

    # bad hash
    def _get_hash(self, key: int) -> int:
        return key % self.getCapacity()

    def insert(self, key: int, value: int) -> None:
        bucket = self._get_hash(key)
        arr = self.table[bucket]
        for idx, kv in enumerate(arr):
            if kv[0] == key:
                arr[idx] = (key, value)
                return
        arr.append((key, value))
        self.size += 1
        if self.getSize()/self.getCapacity() >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        bucket = self._get_hash(key)
        arr = self.table[bucket]
        for (k,v) in arr:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> bool:
        bucket = self._get_hash(key)
        arr = self.table[bucket]
        for idx, kv in enumerate(arr):
            if kv[0] == key:
                break
        arr[idx], arr[-1] = arr[-1], arr[idx]
        arr.pop()
        self.size -= 1
        return True


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return len(self.table)


    def resize(self) -> None:
        extension = HashTable(self.getCapacity())
        self.table.extend(extension.table)

