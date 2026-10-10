class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.m = matrix

        # p[r][c] = sum(matrix[r][0:c+1])
        self.p = [[0] * self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            running = 0

            for c in range(self.cols):
                running += matrix[r][c]
                self.p[r][c] = running

    def update(self, row: int, col: int, val: int) -> None:
        old = self.m[row][col]
        diff = val - old

        # Every prefix ending at col or later contains matrix[row][col].
        for c in range(col, self.cols):
            self.p[row][c] += diff

        self.m[row][col] = val

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int
    ) -> int:

        total = 0

        for r in range(row1, row2 + 1):
            right = self.p[r][col2]

            left = 0
            if col1 > 0:
                left = self.p[r][col1 - 1]

            total += right - left

        return total