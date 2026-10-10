class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        H = heights
        rows = len(H)
        cols = len(H[0])

        adj_list = {}
        OcPa = set()
        OcAt = set()

        for r in range(rows):
            for c in range(cols):
                node = (r, c)
                adj_list[node] = set()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        # REVERSED edge
                        # from ocean inward, we can move to higher/equal cells
                        if H[nr][nc] >= H[r][c]:
                            adj_list[node].add((nr, nc))

                    elif nr < 0 or nc < 0:
                        OcPa.add(node)

                    elif nr == rows or nc == cols:
                        OcAt.add(node)

        def dfs(s, visited):
            if s in visited:
                return

            visited.add(s)

            for n in adj_list[s]:
                dfs(n, visited)

        pacific_reachable = set()
        atlantic_reachable = set()

        for s in OcPa:
            dfs(s, pacific_reachable)

        for s in OcAt:
            dfs(s, atlantic_reachable)

        res = pacific_reachable & atlantic_reachable

        return [list(cell) for cell in res]