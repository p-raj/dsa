import heapq
import math

class AdjacencyDict:
    def __init__(self, n: int, edges: List[List[int]]):
        self.al = {}
        self.edges = edges
        for n, e, w in edges:
            if e not in self.al:
                self.al[e] = {}
            if n not in self.al:
                self.al[n] = {}
            self.al[n][e] = w

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        al = AdjacencyDict(n, edges).al
        dist = [math.inf] * n
        # pq = tuple(wt, nd)
        pque = []
        dist[src] = 0
        heapq.heapify(pque)
        heapq.heappush(pque, (dist[src], src))
        while pque:
            cur_wt, cur_node = heapq.heappop(pque)
            nxt_nodes = al.get(cur_node)
            for n, w in nxt_nodes.items():
                if dist[n] > w + cur_wt:
                    dist[n] = w + cur_wt
                    heapq.heappush(pque, (dist[n], n))
        resp = {}
        for idx, dst in enumerate(dist):
            if dst == math.inf:
                dst = -1
            resp[idx] = dst
        return resp
