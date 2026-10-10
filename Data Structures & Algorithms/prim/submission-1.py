import heapq
import math

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
    def dfs(self, src: int, adjacency_list: dict):
        stack = [1]
        visited = set()
        while stack:
            node = stack.pop()
            print(node)
            visited.add(node)
            for next_node in adjacency_list.get(node, {}).keys():
                if next_node not in visited:
                    stack.append(next_node)
        print(visited)

    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        ad = AdjacencyDict(n, edges).al
        opque = [(0,0)]
        heapq.heapify(opque)
        mst = {}
        while opque:
            weight, node = heapq.heappop(opque)
            if node in mst:
                continue
            mst[node] = weight
            if node not in ad:
                continue
            for next_node, edge_weight in ad[node].items():
                if next_node in mst:
                    continue
                heapq.heappush(opque, (edge_weight, next_node))

        if mst.keys() != ad.keys():
            return -1
        return sum(mst.values())