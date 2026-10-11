from collections import Counter
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solns = set()
        
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
            r = freq.get(")",0)
            if r > l:
                return []
            return ["("] * (n-l) + [")"] * (n-r)

        def is_sol(state):
            return len(state) == 2 * n
        
        def proc(state):
            solns.add("".join(state))
        
        def move(state, c):
            state.append(c)
        
        def undo(state, c):
            state.pop()
        
        bt([])

        return list(solns)