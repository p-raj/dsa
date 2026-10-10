class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if (nr, nc) in visited:
                    continue

                # reverse flow: neighbor can flow down into current
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        pacific = set()
        atlantic = set()

        for r in range(rows):
            dfs(r, 0, pacific)          # left border
            dfs(r, cols - 1, atlantic)  # right border

        for c in range(cols):
            dfs(0, c, pacific)          # top border
            dfs(rows - 1, c, atlantic)  # bottom border

        return [list(cell) for cell in pacific & atlantic]