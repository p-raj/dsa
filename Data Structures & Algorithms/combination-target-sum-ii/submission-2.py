class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        nums = candidates
        solns = set()

        def bt(state, sm):
            if is_a_solution(state, sm):
                process_solution(state)
            else:
                if sm > target:
                    return
                for idx in construct_candidates(state, sm):
                    move(state, idx)
                    sm += nums[idx]
                    bt(state, sm)
                    undo(state, idx)
                    sm -= nums[idx]

        def is_a_solution(state, sm):
            return sm == target

        def process_solution(state):
            s = []
            for idx in state:
                s.append(nums[idx])
            solns.add(tuple(sorted(s)))

        def construct_candidates(state, sm):
            return [idx for idx, n in enumerate(nums) if n <= (target - sm) and idx not in state]

        def move(state, idx):
            state.append(idx)

        def undo(state, idx):
            state.pop()

        bt([], 0)
        return [list(s) for s in solns]


# Solution().combinationSum([3,4,5], 16)
