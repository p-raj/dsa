class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DBG = False
        adj_list = {}
        # directio = [(-row), (+row), (-col), (+col)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        H = heights
        rows = len(H)
        cols = len(H[0])
        OcPa = set()
        OcAt = set()
        for r in range(rows):
            for c in range(cols):
                node = (r, c)
                adj_list[node] = set()
                for d in directions:
                    nr, nc = (node[0] + d[0], node[1] + d[1])
                    if (
                        nr >= 0
                        and nc >= 0
                        and nr < rows
                        and nc < cols
                    ):
                        if H[r][c] >= H[nr][nc]:
                            adj_list[node].add((nr, nc))
                    elif nr < 0 or nc < 0:
                        OcPa.add(node)
                    elif nr == rows or nc == cols:
                        OcAt.add(node)
        # for all the sources in
        # OcPa, if i run DFS and end up on a node in
        # OcAt node. We good.
        # And run DFS again on OCAt nodes and reach to OcPa
        def dfs(s, A):
            parents = {}
            def _main(s, A):
                for n in A[s]:
                    # parents can be used to track
                    # visited as well
                    if n in parents:
                        continue
                    parents[n] = s
                    _main(n, A)
            _main(s, A)
            return parents
        
        def get_parents(s, P: dict):
            parents = set()
            def _main(s, P):
                DBG and print(f"{s=}, {P=}")
                if s in P:
                    if P[s] in parents:
                        return
                    parents.add(P[s])
                    s = P[s]
                    _main(s, P)
            _main(s, P)
            return parents

        res = OcPa.intersection(OcAt)
        DBG and print(f"{OcPa=}")
        DBG and print(f"{OcAt=}")
        A = adj_list
        for s in OcPa:
            par_s = dfs(s, A)
            for k, v in par_s.items():
                DBG and print("[OcAt -> OcPa] ", k, v, OcAt)
                if k in OcAt:
                    p = get_parents(k, par_s)
                    DBG and print(f"{p=}")
                    res = res.union(p)

        for s in OcAt:
            par_s = dfs(s, A)
            for k, v in par_s.items():
                DBG and print("[OcAt -> OcPa] ", k, v, OcPa)
                if k in OcPa:
                    p = get_parents(k, par_s)
                    DBG and print(f"{p=}")
                    res = res.union(p)
        return [list(n) for n in res]
