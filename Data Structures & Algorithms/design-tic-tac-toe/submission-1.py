class TicTacToe:
    def __init__(self, n: int):
        cols = n
        rows = n
        self.B = [[0 for _ in range(cols)] for _ in range(rows)]
        self.w = {}
        r = 0
        c = 0
        while r < n:
            c = 0
            while c < n:
                k = (r, c)
                self.w[k] = list()
                c += 1
            r += 1
        self._build(n)

    def _build(self, n: int):
        d1 = list()
        r = 0
        c = 0
        while r < n and c < n:
            d1.append((r, c))
            r += 1
            c += 1
        d2 = list()
        r = n - 1
        c = 0
        while r >= 0 and c < n:
            d2.append((r, c))
            r -= 1
            c += 1

        self.w[(0, 0)].append(d1)
        self.w[(n - 1, n - 1)].append(d1)
        self.w[(0, n - 1)].append(d2)
        self.w[(n - 1, 0)].append(d2)

        r = 0
        while r < n:
            c = 0
            row = list()
            while c < n:
                row.append((r, c))
                c += 1
            c = 0
            while c < n:
                k = (r, c)
                self.w[k].append(row)
                c += 1
            r += 1

        c = 0
        while c < n:
            col = list()
            r = 0
            while r < n:
                col.append((r, c))
                r += 1
            r = 0
            while r < n:
                k = (r, c)
                self.w[k].append(col)
                r += 1
            c += 1

    def _check(self, row: int, col: int):
        return self.w[(row, col)]

    def move(self, row: int, col: int, player: int) -> int:
        self.B[row][col] = player
        checks = self._check(row, col)

        for moves in checks:
            matches = True
            for move in moves:
                matches = matches and (self.B[move[0]][move[1]] == player)
                if not matches:
                    break
            if matches:
                return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
