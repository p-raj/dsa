from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        best = float("inf")
        seen = {}

        state = {
            "coins": 0,
            "total": 0,
        }

        def bt(state, coin_idx):
            nonlocal best

            if is_solution(state):
                process_solution(state)
                return

            if should_prune(state):
                return

            for idx in candidates(state, coin_idx):
                move(state, idx)
                bt(state, idx)
                undo(state, idx)

        def candidates(state, coin_idx):
            return [
                i
                for i in range(coin_idx, len(coins))
                if coins[i] <= amount - state["total"]
            ]

        def is_solution(state):
            return state["total"] == amount

        def process_solution(state):
            nonlocal best
            best = min(best, state["coins"])

        def should_prune(state):
            used = state["coins"]
            remain = amount - state["total"]

            # Prune 1: already worse than best complete answer
            if used >= best:
                return True

            # Prune 2: optimistic lower bound
            max_coin = coins[0]
            min_extra_needed = math.ceil(remain / max_coin)

            if used + min_extra_needed >= best:
                return True

            # Prune 3: dominated state memoization
            if remain in seen and seen[remain] <= used:
                return True

            seen[remain] = used
            return False

        def move(state, m):
            state["coins"] += 1
            state["total"] += coins[m]

        def undo(state, m):
            state["coins"] -= 1
            state["total"] -= coins[m]

        bt(state, coin_idx=0)

        return -1 if best == float("inf") else best