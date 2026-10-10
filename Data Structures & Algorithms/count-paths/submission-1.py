class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # what should the state represent?
        # the position in the grid
        # what should the subproblem output
        # count
        # what is the count when the grid size is 1,1 => 1
        # there is just one way to get out, you are standing on it
        # Fn<i,j> -> int
        # base case: Fn<0,0> = 1
        # Recurrance Relationship
        # From i,j -> (i+1, j) + (i, j+1)
        memo = {}
        memo[(m-1), (n-1)] = 1
        def Fn(row: int, col: int) -> int:
            key = (row,col)
            if key in memo:
                return memo[key]
            if row == m-1 and col == n-1:
                # there is only 1 way to exit
                return 1
            moves = []
            if row < m - 1:
                moves.append(Fn(row+1, col))
            if col < n - 1:
                moves.append(Fn(row, col+1))
            if not moves:
                return 0
            memo[key] = sum(moves)
            return memo[key]
        
        return Fn(0,0)