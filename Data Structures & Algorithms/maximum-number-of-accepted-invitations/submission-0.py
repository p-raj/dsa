class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        boys = len(grid)
        gals = len(grid[0])

        sm_b = 0
        for c in range(gals):
            sm_ = 0
            for r in range(boys):
                sm_ += grid[r][c]
            sm_b = max(sm_b, sm_)
        
        sm_g = 0
        for c in range(gals):
            sm_ = 0
            for r in range(boys):
                sm_ += grid[r][c]
            sm_g = max(sm_g, sm_)
        return max(sm_b, sm_g)
