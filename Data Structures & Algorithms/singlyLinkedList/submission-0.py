class Node:
    def __init__(self, val):
        self._val = val
        self._nxt = None
    
    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val
    
    
    @property
    def nxt(self):
        return self._nxt
    
    @nxt.setter
    def nxt(self, node: Node) -> None:
        self._nxt = node


class LinkedList:
    
    def __init__(self):
        self._head = None
        self._tail = None

    def get(self, index: int) -> int:
        h = self._head
        while index > 0 and h:
            h = h.nxt
            index -= 1
        return h.val if h and index == 0 else -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        h = self._head
        if self._head is None:
            self._tail = node
        node.nxt = h
        self._head = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        if self._tail is None:
            self._head = self._tail = node
            return
        self._tail.nxt = node
        self._tail = node
        
    def remove(self, index: int) -> bool:
        h = self._head
        prv = None
        while index > 0 and h:
            index -= 1
            prv = h
            h = h.nxt
        if index and not h:
            return False
        if not prv:
            return False
        if prv.nxt is None:
            #reached tail
            self._tail = prv

        prv.nxt = h.nxt
        h.nxt = None
        return True

    def getValues(self) -> List[int]:
        lst = []
        h = self._head
        while h:
            lst.append(h.val)
            h = h.nxt
        return lst
