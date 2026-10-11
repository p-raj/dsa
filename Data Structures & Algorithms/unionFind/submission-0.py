class Node:
    def __init__(self, root: Node | None = None):
        self.root = root

class UnionFind:
    
    def __init__(self, n: int):
        self.ds = {
            x: Node()
            for x in range(n)
        }
        self.num_comps = n

    def find(self, x: int) -> int:
        comp = self.ds.get(x)
        while comp.root:
            comp = self.ds.get(comp.root)
        return comp


    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        comp_y = self.find(y)
        comp_y.root = x
        self.num_comps -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_comps
