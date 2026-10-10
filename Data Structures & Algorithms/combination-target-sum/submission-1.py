class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solns = set()

        def bt(state):
            sm = sum(state)
            # print(state, sm, sm == target)
            if is_a_solution(state, sm):
                process_solution(state)
            else:
                if tuple(sorted(state)) in solns:
                    return
                if sm > target:
                    return
                for c in construct_candidates(state, sm):
                    move(state, c)
                    bt(state)
                    undo(state, c)
        
        def is_a_solution(state, sm):
            return sm == target
        
        def process_solution(state):
            solns.add(tuple(sorted(state)))
        
        def construct_candidates(state, sm):
            return [
                n for n in nums if n <= (target - sm)
            ]
        
        def move(state, c):
            state.append(c)
        
        def undo(state, c):
            state.pop()
        
        bt([])
        return [list(s) for s in solns]

# Solution().combinationSum([3,4,5], 16)