class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        r = len(grid)
        M = dict()
        S = set(range(1, (r*r)+1))
        i = 0
        res = [None, None]
        while i < r:
            j = 0
            while j < r:
                cur = grid[i][j]
                if cur not in M:
                    M[cur] = 0
                M[cur] += 1
                if M[cur] == 2:
                    res[0] = cur
                S.discard(cur)
                j += 1
            i += 1
        res[1] = S.pop()
        return res