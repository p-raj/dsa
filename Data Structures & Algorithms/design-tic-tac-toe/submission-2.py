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
        # Main diagonal
        d1 = []
        r = 0
        c = 0

        while r < n and c < n:
            d1.append((r, c))
            r += 1
            c += 1

        # Anti-diagonal
        d2 = []
        r = n - 1
        c = 0

        while r >= 0 and c < n:
            d2.append((r, c))
            r -= 1
            c += 1

        # Every cell on a diagonal must know about that diagonal.
        for cell in d1:
            self.w[cell].append(d1)

        for cell in d2:
            self.w[cell].append(d2)

        # Rows
        r = 0
        while r < n:
            c = 0
            row = []

            while c < n:
                row.append((r, c))
                c += 1

            c = 0
            while c < n:
                self.w[(r, c)].append(row)
                c += 1

            r += 1

        # Columns
        c = 0
        while c < n:
            col = []
            r = 0

            while r < n:
                col.append((r, c))
                r += 1

            r = 0
            while r < n:
                self.w[(r, c)].append(col)
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
