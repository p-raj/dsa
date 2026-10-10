class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.kv = {}
        self.cap = capacity
    
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv
    
    def insert(self, node):
        prv = self.tail.prev
        prv.next = node
        self.tail.prev = node
        node.prev, node.next = prv, self.tail

    def get(self, key: int) -> int:
        if key in self.kv:
            self.remove(self.kv[key])
            self.insert(self.kv[key])
            return self.kv[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.remove(self.kv[key])
        self.kv[key] = Node(key, value)
        self.insert(self.kv[key])
        if len(self.kv) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.kv[lru.key]
