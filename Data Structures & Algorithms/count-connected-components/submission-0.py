class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        A = {}
        for ns, nd in edges:
            A[ns] = set()
            A[nd] = set()
        for ns, nd in edges:
            A[ns].add(nd)
            A[nd].add(ns)

        cc = list()
        visited = set()
        def dfs(node, cc):
            cc.add(node)
            visited.add(node)
            for nn in A[node]:
                if nn not in visited:
                    dfs(nn, cc)

        for n in A:
            if n not in visited:
                _cc = set()
                dfs(n, _cc)
                cc.append(_cc)
        
        print(cc)
        return len(cc)