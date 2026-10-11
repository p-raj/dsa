class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        solns = []

        def bt(state):
            if is_solution(state):
                process_solution(state)
            else:
                for c in candidates(state):
                    move(state, c)
                    bt(state)
                    undo(state, c)
        
        def candidates(state):
            amt = amount - sum(state)
            return [
                c for c in coins if c <= amt
            ]
        
        def is_solution(state):
            return sum(state) == amount
        
        def process_solution(state):
            solns.append(len(state))
        
        def move(state, m):
            state.append(m)
        
        def undo(state, m):
            state.pop()
        
        bt([])
        return -1 if not solns else min(solns)