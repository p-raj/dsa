import copy

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        # len(nums) == 1 => (False)
        # len(nums) == 2 => (nums[0] == nums[1])

        # what is the shape of optimal solution?
        # output => Bool
        # input => index
        # Where should this index be placed?
        # in the first subset? in the second subset?
        # When would we know if we have made the right choice?
        # When i == len(nums) and sum(ss1) == sum(ss2)
        # There is no optimal solution, only exploration
        # of all possible states
        # Backtracking!

        if len(nums) == 1:
            return False
        if len(nums) == 2:
            return nums[0] == nums[1]

        # early pruning
        # if  sum(left-over) + sum(ss1) < sum(ss2) + num[i]
        # and sum(left-over) + sum(ss2) < sum(ss1) + num[i]

        # memoization
        # what happens to the sum when index is part of a subset
        # memo[(...<i>)] = sum((...)+num[i])
        # ss: {
        # 'sum': 0,
        # 'idx': (),
        # }
        # memo[idx] = sum
        # state(i, ss1, ss2)
        #
        ss1 = {"sum": 0, "idx": []}
        ss2 = {"sum": 0, "idx": []}
        memo = {}

        def move(d: dict, idx: int) -> dict:
            dc = copy.deepcopy(d)
            dc["idx"].append(idx)
            dc["sum"] = dc["sum"] + nums[idx]
            memo[tuple(dc["idx"])] = dc["sum"]
            return dc

        def Fn(idx: int, lft: dict, rgt: dict) -> bool:
            if idx >= len(nums):
                return lft["sum"] == rgt["sum"]

            lft_tup = tuple(lft["idx"])
            if lft_tup in memo:
                k = tuple([*lft["idx"], idx])
                memo[k] = memo[lft_tup] + nums[idx]

            rgt_tup = tuple(rgt["idx"])
            if rgt_tup in memo:
                k = tuple([*rgt["idx"], idx])
                memo[k] = memo[rgt_tup] + nums[idx]

            # Case 1:
            # move idx to lft
            return Fn(idx + 1, move(lft, idx), rgt) or Fn(idx + 1, lft, move(rgt, idx))
            # return Case1 OR Case2

        return Fn(0, ss1, ss2)
