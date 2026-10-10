class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        solns = []

        def bt(idx, sm, nlst):
            if sm == target:
                solns.append(nlst.copy())
                return
            if sm > target or idx >= len(nums):
                return
            nlst.append(nums[idx])
            bt(idx+1, sm+nums[idx], nlst)
            nlst.pop()
            # we have explored this
            # element fully
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            bt(idx+1, sm, nlst)

        bt(0,0,[])
        return solns