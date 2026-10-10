class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solns = []
        state = []

        def bt(l, r):
            if len(state) == 2 * n:
                solns.append("".join(state))
                return

            if l < n:
                state.append("(")
                bt(l + 1, r)
                state.pop()

            if r < l:
                state.append(")")
                bt(l, r + 1)
                state.pop()

        bt(0, 0)
        return solns