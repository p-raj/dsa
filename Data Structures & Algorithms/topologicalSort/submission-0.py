class AdjacencyDict:
    def __init__(self, n, edges):
        self.al = {}
        for i in range(n):
            self.al[i] = {
                'idgri': 0,
                'odgri': 0,
                'next': {}
            }
        for u, v in edges:
            if v not in self.al[u]['next']:
                if u in self.al[v]['next']:
                    raise ValueError
                self.al[u]['odgri'] += 1
                self.al[u]['next'][v] = None
                self.al[v]['idgri'] += 1

class InvertedAdjacencyDict:
    def __init__(self, n, edges):
        inverted = [[v,u] for u,v in edges]
        self.al = AdjacencyDict(n, inverted).al

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        try:
            al = AdjacencyDict(n, edges).al
        except ValueError:
            return []
        
        def _zero_in() -> list:
            zin = []
            for u, conn in al.items():
                if conn['idgri'] == 0:
                    zin.append(u)
            return zin
        
        nodes_to_scan = _zero_in()
        visited = [False] * n
        dag = list()
        while nodes_to_scan:
            node = nodes_to_scan.pop()
            if visited[node]:
                continue
            visited[node] = True
            dag.append(node)
            for v in al[node]['next']:
                al[v]['idgri'] -= 1
                if al[v]['idgri'] == 0:
                    nodes_to_scan.append(v)
            al.pop(node, None)

        if len(dag) != n:
            return []
        return dag
