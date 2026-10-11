class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        goal = (rows-1, cols-1)
        steps_to_process = []
        visited = set()
        start = (0, 0)
        steps_to_process.append(start)
        if grid[start[0]][start[1]] == 1:
            return -1

        count_steps = 0
        while steps_to_process:
            # act as a queue
            # not as a stack
            # process this level first
            for _ in range(len(steps_to_process)):
                step = steps_to_process.pop(0)
                if step == goal:
                    return count_steps

                curr, curc = step
                visited.add((curr, curc))
                
                next_moves = [(0, -1), (-1, 0),(1, 0), (0, 1)]
                for mx, my in next_moves:
                    nxr, nxc = curr + mx, curc + my
                    if ((nxr, nxc) not in visited and 0 <= nxr < rows and 0 <= nxc < cols) and grid[
                        nxr
                    ][nxc] == 0:
                        steps_to_process.append((nxr, nxc))
            count_steps += 1