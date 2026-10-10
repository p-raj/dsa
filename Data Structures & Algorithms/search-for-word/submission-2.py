class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.has_word = False
        self.dbg = False
        def debug(state):
            if not self.dbg:
                return
            print(
                make_word(state),
                " | ",
                state,
                " | ",
                self.has_word,
                " | ",
                word == make_word(state),
                " | ",
                word in make_word(state),
            )

        def make_word(state):
            s = ""
            for i, j in state:
                s += board[i][j]
            return s

        def bt(state):
            debug(state)
            if self.has_word:
                return
            if is_soln(state):
                return process(state)
            else:
                if len(state) > len(word):
                    return
                for c in candidates(state):
                    move(state, c)
                    bt(state)
                    undo(state, c)

        def is_soln(state):
            return len(state) == len(word) and word == make_word(state)

        def process(state):
            self.has_word = True

        def candidates(state):
            if not state:
                cs = []
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        cs.append((i, j))
                return cs
            else:
                last_move = state[-1]
                cs = []
                if last_move[1] + 1 < len(board[0]):
                    cs.append((last_move[0], last_move[1] + 1))
                if last_move[0] + 1 < len(board):
                    cs.append((last_move[0] + 1, last_move[1]))
                if last_move[1] - 1 >= 0:
                    cs.append((last_move[0], last_move[1] - 1))
                if last_move[0] - 1 >= 0:
                    cs.append((last_move[0] - 1, last_move[1]))
                return list(set(cs) - set(state))

        def move(state, m):
            state.append(m)

        def undo(state, m):
            state.pop()

        bt([])
        return self.has_word
