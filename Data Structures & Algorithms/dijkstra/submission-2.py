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


class Solution:
    def shortestPath(self, n, edges, src):
        al = AdjacencyDict(n, edges).al
        print(al)
        dist = [math.inf] * n
        dist[src] = 0

        pque = [(0, src)]

        while pque:
            cur_wt, cur_node = heapq.heappop(pque)

            # 🔴 critical invariant guard
            if cur_wt > dist[cur_node]:
                continue

            for nxt, w in al.get(cur_node, {}).items():
                if dist[nxt] > cur_wt + w:
                    dist[nxt] = cur_wt + w
                    heapq.heappush(pque, (dist[nxt], nxt))

        return {i: (-1 if d == math.inf else d) for i, d in enumerate(dist)}
