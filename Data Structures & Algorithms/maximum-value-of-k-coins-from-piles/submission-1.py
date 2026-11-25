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
        # pile_index = [0] * len(piles)
        # memo = {}
        # def Fn(pile_index, coins_left) -> int:
        #     if coins_left <= 0:
        #         return 0
        #     key = (tuple(pile_index), coins_left)
        #     if key in memo:
        #         return memo[key]
        #     best = -1
        #     for idx, pidx in enumerate(pile_index):
        #         if pidx >= len(piles[idx]):
        #             continue
        #         pile_index[idx] += 1
        #         best = max(best, Fn(pile_index, coins_left - 1) + piles[idx][pidx])
        #         pile_index[idx] -= 1
        #     memo[key] = best
        #     return memo[key]

        # return Fn(pile_index, k)
        ########################################################################################
        # Approach 2:
        # Instead of exploring all piles simultaneously and
        # maintaining the state of every pile, process piles
        # sequentially.
        #
        # For each pile, explore taking 0, 1, 2, ... coins,
        # subject to the remaining coin budget.
        #
        # Once a choice is made within a recursive branch,
        # move to the next pile without revisiting this pile.
        memo = {}
        piles_prefix_sum = []
        for pile in piles:
            pile_prefix_sum = [0]
            sm_ = 0
            for coin in pile:
                sm_ += coin
                pile_prefix_sum.append(sm_)
            piles_prefix_sum.append(pile_prefix_sum)

        def F(pile_index, coin_budget) -> int:
            key = (pile_index, coin_budget)
            if key in memo:
                return memo[key]

            if coin_budget <= 0:
                return 0

            if pile_index >= len(piles):
                return float("-inf")

            best = float("-inf")
            pile = piles[pile_index]
            choices = min(len(pile), coin_budget)
            for i in range(choices+1):
                val = piles_prefix_sum[pile_index][i]
                best = max(best, val + F(pile_index + 1, coin_budget - i))
            memo[key] = best
            return memo[key]

        return F(0, k)


########################################################################################
