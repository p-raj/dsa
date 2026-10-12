import itertools


class Solution:

    def twoSum(self, start: int, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        fst, lst = start, len(nums)-1
        res = []
        while fst < lst:
            sum_ = nums[fst] + nums[lst]
            if sum_ == target:
                res.append([fst, lst])
                fst += 1
            elif sum_ > target:
                lst -= 1
            else:
                fst += 1
        return res

    def threeSum(self, nums: List[int], start: int, k: int) -> List[List[int]]:
        solutions = set()
        for idx in range(start, len(nums)):
            num = nums[idx]
            target = k - num
            fst_lst = self.twoSum(idx+1, nums, target)
            for (fst, lst) in fst_lst:
                solutions.add((num, nums[fst], nums[lst]))
        return list(solutions)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # idxs = list(range(len(nums)))
        # combo = itertools.combinations(idxs, 4)
        # res = set()
        # for c in combo:
        #     n = tuple(sorted([nums[i] for i in c]))
        #     if sum(n) == target:
        #         res.add(n)
        # # print(res)
        # return list(list(x) for x in res)
        res = set()
        nums.sort()
        for idx, num in enumerate(nums):
            solns = self.threeSum(nums, idx+1, target - num)
            for soln in solns:
                res.add(
                    (num, *soln)
                )
        print(res)
        return list(list(x) for x in res)