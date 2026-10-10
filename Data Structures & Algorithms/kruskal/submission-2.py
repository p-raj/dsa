class UFO:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]

    def find(self, x: int) -> int:
        # Finds the root of x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        # Connects x and y
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False


class AdjacencyDict:
    def __init__(self, n, edges):
        self.al = {}
        for i in range(n):
            self.al[i] = {}
        for u, v, w in edges:
            if u not in self.al:
                self.al[u] = {}
            if v not in self.al:
                self.al[v] = {}
            if (v in self.al[u] and self.al[u][v] > w) or (v not in self.al[u]):
                self.al[u][v] = w
                self.al[v][u] = w


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        ad = AdjacencyDict(n, edges).al
        mst = []
        dj = UFO(n)
        sorted_ed = sorted(edges, key=lambda x: x[2], reverse=True)
        while sorted_ed:
            u, v, w = sorted_ed.pop()
            if dj.find(u) == dj.find(v):
                continue
            mst.append((u, v, w))
            dj.union(u, v)

        nodes = set()
        mst_wt = 0
        roots = set()
        for u, v, w in mst:
            if dj.find(u) != dj.find(v):
                root_count += 1
            roots.add(dj.find(u))
            nodes.add(u)
            nodes.add(v)
            mst_wt += w

        return mst_wt if len(roots) == 1 and len(nodes) == n else -1
