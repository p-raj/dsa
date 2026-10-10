class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        components = []
        visited = []
        for r in range(rows):
            visited.append([])
            for c in range(cols):
                visited[r].append(False)
                if grid[r][c] == "0":
                    visited[r][c] = True 

        def dfs(row, col, component):
            visited[row][col] = True
            component.append((row, col))
            neighbours = []
            if row - 1 >= 0 and grid[row - 1][col] == "1":
                neighbours.append((row - 1, col))
            if row + 1 < rows and grid[row + 1][col] == "1":
                neighbours.append((row + 1, col))
            if col - 1 >= 0 and grid[row][col - 1] == "1":
                neighbours.append((row, col - 1))
            if col + 1 < cols and grid[row][col + 1] == "1":
                neighbours.append((row, col + 1))
            for r, c in neighbours:
                if not visited[r][c]:
                    dfs(r, c, component)

        for r in range(rows):
            for c in range(cols):
                if not visited[r][c]:
                    cc = []
                    dfs(r, c, cc)
                    components.append(cc)

        return len(components)
