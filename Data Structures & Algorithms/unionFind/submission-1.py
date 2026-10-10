from dataclasses import dataclass

@dataclass
class Node:
    root: None | int = None

class UnionFind:

    def __init__(self, n: int):
        self.ds = {
            x: Node()
            for x in range(n)
        }
        self.num_comps = n

    def find(self, x: int) -> int:
        comp, node = x, self.ds.get(x)
        while node.root is not None:
            comp, node = node.root, self.ds.get(node.root)
        return comp


    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        comp_y = self.find(y)
        if self.isSameComponent(x, y):
            return False
        self.ds[comp_y] = Node(root=x)
        self.num_comps -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_comps
