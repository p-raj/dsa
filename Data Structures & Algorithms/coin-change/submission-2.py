class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        best = float("inf")

        state = {
            "coins": [],
            "total": 0,
        }

        def bt(state):
            nonlocal best

            if is_solution(state):
                process_solution(state)
                return

            if should_prune(state):
                return

            for c in candidates(state):
                move(state, c)
                bt(state)
                undo(state, c)

        def candidates(state):
            amt_left = amount - state["total"]
            return [c for c in coins if c <= amt_left]

        def is_solution(state):
            return state["total"] == amount

        def process_solution(state):
            nonlocal best
            best = min(best, len(state["coins"]))

        def should_prune(state):
            return len(state["coins"]) >= best

        def move(state, m):
            state["coins"].append(m)
            state["total"] += m

        def undo(state, m):
            state["coins"].pop()
            state["total"] -= m

        bt(state)

        return -1 if best == float("inf") else best