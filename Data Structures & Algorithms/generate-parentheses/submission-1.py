from collections import Counter


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solns = list()

        def bt(state):
            if is_sol(state):
                proc(state)
            else:
                for c in candidates(state):
                    move(state, c)
                    bt(state)
                    undo(state, c)

        def candidates(state):
            freq = Counter(state)
            l = freq.get("(", 0)
            r = freq.get(")", 0)
            cand = []
            if l < n:
                cand.append("(")
            if r < l:
                cand.append(")")
            return cand

        def is_sol(state):
            return len(state) == 2 * n

        def proc(state):
            solns.append("".join(state))

        def move(state, c):
            state.append(c)

        def undo(state, c):
            state.pop()

        bt([])
        print(len(solns))
        return list(solns)
