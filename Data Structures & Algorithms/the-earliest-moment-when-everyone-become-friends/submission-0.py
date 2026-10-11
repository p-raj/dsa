class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs = sorted(logs, key=lambda x: x[0])
        for t, a, b in logs:
            uf.union(a, b)
            if uf.is_fully_connected():
                return t
        return 0


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        # Track the total number of independent groups (components)
        self.count = size

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False

        # Two groups are merging, so reduce the group count by 1
        self.count -= 1

        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
            
        return True

    def is_fully_connected(self) -> bool:
        """Returns True if all elements are connected under one root."""
        return self.count == 1
