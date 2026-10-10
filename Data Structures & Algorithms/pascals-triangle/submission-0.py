class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = numRows
        cols = numRows
        matrix = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                vals = []
                if r > 0:
                    if c > 0:
                        if matrix[r-1][c-1] != 0:
                            vals.append(matrix[r-1][c-1])
                    if matrix[r-1][c] != 0:
                        vals.append(matrix[r-1][c])
                    matrix[r][c] = sum(vals)
                else:
                    matrix[r][c] = 1
                    break
        return [[i for i in r if i > 0] for r in matrix]
