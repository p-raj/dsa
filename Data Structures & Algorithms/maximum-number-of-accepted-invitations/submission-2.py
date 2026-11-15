class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        boys = len(grid)
        gals = len(grid[0])
        # bipartite graph
        # The task is then to find the largest subset of edges that do not share endpoints. 
        # That subset is called a matching.
        matched = [-1] * gals

        def try_match(boy):
            for g in range(gals):
                if grid[boy][g] == 0:
                    continue
                if g in visited:
                    continue
                visited.add(g)
                if matched[g] == -1 or try_match(matched[g]):
                    matched[g] = boy
                    return True
            return False

        count = 0
        for b in range(boys):
            visited = set()
            if try_match(b):
                count += 1
        print(matched)
        return count