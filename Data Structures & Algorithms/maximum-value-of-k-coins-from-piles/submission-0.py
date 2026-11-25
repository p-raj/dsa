class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # 1 <= piles.length <= 1000
        # 1 <= piles[i][j] <= 100000
        # 1 <= k <= the total number of coins <= 2000.

        # this is clearly a DP, but the piles.length is 1000
        # choose 1 coin from 1000 = 1000 choices
        # k-1 choices remain
        # do this k times => 1000**k possibilities
        # this could timeout
        # greedy is not the best solution
        # [[2,20],[10]] => 10 + 2 = 12 (greedy), best = 2 + 20 = 22
        # another reason for DP is that sub-problem contributes
        # to the bigger problem, once a coin has been removed -> sub-problem
        # sub-problem needs to be solved in the best way
        # i think the best optimization would come from the state
        # of the problem, how can i manage state?
        # choice -> contributes to k-1 & total + choice
        # another solution - backtracking, that would be
        # even more exhaustive
        pile_index = [0] * len(piles)
        memo = {}
        def Fn(pile_index, coins_left) -> int:
            if coins_left <= 0:
                return 0
            key = (tuple(pile_index), coins_left)
            if key in memo:
                return memo[key]
            best = -1
            for idx, pidx in enumerate(pile_index):
                if pidx >= len(piles[idx]):
                    continue
                pile_index[idx] += 1
                best = max(best, Fn(pile_index, coins_left - 1) + piles[idx][pidx])
            memo[key] = best
            return memo[key]

        return Fn(pile_index, k)
