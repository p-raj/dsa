class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solns = []

        def bt(state):
            if is_a_soln(state):
                process(state)
            else:
                for c in candidates(state):
                    move(state, c)
                    bt(state)
                    undo(state, c)

        
        def candidates(state):
            return set(nums) - set(state)
        
        def move(state, m):
            state.append(m)
        
        def undo(state, m):
            state.pop()
        
        def is_a_soln(state):
            return len(state) == len(nums)
        
        def process(state):
            solns.append(state.copy())

        # inde
        bt([])

        return solns