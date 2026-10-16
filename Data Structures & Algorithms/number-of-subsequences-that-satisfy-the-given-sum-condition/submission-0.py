class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        res = 0

        def is_solution(state):
            if not state:
                return False

            values = [nums[i] for i in state]
            return min(values) + max(values) <= target

        def record(state):
            nonlocal res
            res = (res + 1) % MOD

        def candidates(start):
            return range(start, len(nums))

        def move(state, i):
            state.append(i)

        def undo(state, i):
            state.pop()

        def bt(start, state):
            # Count the current subsequence if valid.
            if is_solution(state):
                record(state)

            # Continue exploring regardless of validity.
            for i in candidates(start):
                move(state, i)
                bt(i + 1, state)
                undo(state, i)

        bt(0, [])
        return res