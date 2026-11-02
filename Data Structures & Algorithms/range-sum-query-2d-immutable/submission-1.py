from pprint import pp


class NumMatrix:
    def prefix_calc(self):
        for ridx in range(self.rows):
            row = self.M[ridx]
            tot = 0
            for idx, num in enumerate(row):
                tot += num
                self.pfxM[ridx][idx][0] = tot

        for cidx in range(self.cols):
            tot = 0
            for ridx in range(self.rows):
                num = self.M[ridx][cidx]
                tot += num
                self.pfxM[ridx][cidx][1] = tot

    def __init__(self, matrix: List[List[int]]):
        self.M = matrix
        self.rows = len(self.M)
        self.cols = len(self.M[0])
        self.pfxM = [[[0, 0] for _ in range(self.cols)] for _ in range(self.rows)]
        self.prefix_calc()
        # pp(self.pfxM)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tot = 0
        for r in range(row1, row2 + 1):
            tot += self.pfxM[r][col2][0] - self.pfxM[r][col1][0] + self.M[r][col1]
        return tot


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
