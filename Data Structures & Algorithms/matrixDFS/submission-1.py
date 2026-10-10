from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        paths = 0
        start = (0, 0)
        visited = {start}
        state = [start]

        def _bt(state, visited):
            if _is_a_soln(state):
                _process()
            else:
                for c in _candidates(state, visited):
                    _move(state, visited, c)
                    _bt(state, visited)
                    _undo(state, visited, c)

        def _is_a_soln(state):
            r, c = state[-1]
            return r == rows-1 and c == cols-1

        def _process():
            nonlocal paths
            paths += 1

        def _candidates(state, visited):
            r, c = state[-1]
            next_rc = []
            next_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for mx, my in next_moves:
                nxr, nxc = r + mx, c + my
                if (
                    (nxr, nxc) not in visited
                    and
                    0 <= nxr < rows
                    and
                    0 <= nxc < cols
                ) and grid[nxr][nxc] == 0:
                    next_rc.append((nxr, nxc))
            return next_rc

        def _move(state, visited, move):
            state.append(move)
            visited.add(move)

        def _undo(state, visited, move):
            move = state.pop()
            visited.remove(move)

        if grid[0][0] == 1:
            return 0
        _bt(state, visited)
        return paths
