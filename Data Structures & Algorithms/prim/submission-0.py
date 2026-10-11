import heapq
import math

class AdjacencyDict:
    def __init__(self, n, edges):
        self.al = {}
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
                heapq.heappush(opque, (edge_weight, next_node))
        print(set(mst.keys()), set(ad.keys()))
        if set(mst.keys()) != set(ad.keys()):
            return -1
        return sum(mst.values())