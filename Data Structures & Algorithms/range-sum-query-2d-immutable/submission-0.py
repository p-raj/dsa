class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.M = matrix
        self.rows = len(self.M)
        self.cols = len(self.M[0])
        self.Pr = [[0] * self.cols for _ in range(self.rows)]
        self.Pc = [[0] * self.cols for _ in range(self.rows)]
        for r in range(self.rows):
            self.Pr[r][0] = self.M[r][0]
            for c in range(1, self.cols):
                self.Pr[r][c] = self.M[r][c] + self.Pr[r][c - 1]
        for c in range(self.cols):
            self.Pc[0][c] = self.M[0][c]
            for r in range(1, self.rows):
                self.Pc[r][c] = self.M[r][c] + self.Pc[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sm = 0
        for r in range(row1, row2 + 1):
            sm += self.Pr[r][col2] - self.Pr[r][col1] + self.M[r][col1]
        return sm


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
