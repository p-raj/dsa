class TicTacToe:
    def __init__(self, n: int):
        cols = n
        rows = n
        self.B = [[0 for _ in range(cols)] for _ in range(rows)]

    def _check(self, row: int, col: int):
        w = {
            (0, 0): (((1, 1), (2, 2)), ((1, 0), (2, 0)), ((0, 1), (0, 2))),
            (0, 1): (((1, 1), (2, 1)), ((0, 0), (0, 2))),
            (0, 2): (((1, 2), (2, 2)), ((0, 0), (0, 1))),
            (1, 0): (((1, 1), (1, 2)), ((0, 0), (2, 0))),
            (1, 1): (((0, 0), (2, 2)), ((1, 0), (2, 0)), ((0, 1), (2, 1))),
            (1, 2): (((0, 2), (2, 2)), ((1, 1), (1, 0))),
            (2, 0): (((1, 0), (0, 0)), ((1, 1), (0, 2)), ((2, 1), (2, 2))),
            (2, 1): (((2, 0), (2, 2)), ((1, 1), (0, 1))),
            (2, 2): (((1, 1), (0, 0)), ((1, 2), (0, 2)), ((2, 0), (2, 1))),
        }
        return w[(row, col)]

    def move(self, row: int, col: int, player: int) -> int:
        self.B[row][col] = player
        checks = self._check(row, col)
        for moves in checks:
            m1, m2 = moves
            if self.B[row][col] == self.B[m1[0]][m1[1]] == self.B[m2[0]][m2[1]]:
                return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
