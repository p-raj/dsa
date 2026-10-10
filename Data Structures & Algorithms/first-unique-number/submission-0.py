class Node:
    def __init__(self, val: int | None = None, nxt: Node | None = None, prv: Node | None = None)->None:
        self.val = val
        self.nxt = nxt
        self.prv = prv

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prv = self.head

    def add(self, val: int):
        node = Node(val)
        prv = self.tail.prv
        prv.nxt = node
        node.prv = prv
        node.nxt = self.tail
        self.tail.prv = node
        return node

    def remove(self, node: Node):
        prv = node.prv
        nxt = node.nxt
        prv.nxt = nxt
        nxt.prv = prv
        node.prv = None
        node.nxt = None

    def search(self, val: int) -> Node:
        node = self.head.nxt
        while node:
            if node.val == val:
                return node
            node = node.nxt
        raise Exception("No node found")

class FirstUnique:
    def _add(self, num: int):
        if num in self.elem:
            if self.elem[num] is not None:
                node = self.elem[num]
                self.dll.remove(node)
                self.elem[num] = None
        else:
            node = self.dll.add(num)
            self.elem[num] = node

    def __init__(self, nums: List[int]):
        self.elem = {}
        self.dll = DLL()
        for num in nums:
            self._add(num)

    def showFirstUnique(self) -> int:
        if self.dll.head.nxt.val is None:
            return -1
        else:
            return self.dll.head.nxt.val

    def add(self, value: int) -> None:
        self._add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
