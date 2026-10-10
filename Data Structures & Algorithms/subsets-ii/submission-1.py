class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        soln = []

        def is_a_soln(a, k, data):
            return k == len(data)

        def process_soln(a, k, data):
            subset = [
                data[idx - 1]
                for idx, val in enumerate(a)
                if idx > 0 and val is True
            ]
            soln.append(subset)

        def construct_candidates(a, k, data):
            # k is 1-indexed position in decision vector
            # nums index is k - 1

            candidates = [False]

            # Include is normally allowed,
            # except when nums[k-1] duplicates nums[k-2]
            # and the previous duplicate was NOT included.
            if not (
                k > 1
                and data[k - 1] == data[k - 2]
                and a[k - 1] is False
            ):
                candidates.append(True)

            return candidates

        def bt(a, k, data):
            if is_a_soln(a, k, data):
                process_soln(a, k, data)
                return

            k += 1
            for c in construct_candidates(a, k, data):
                a[k] = c
                bt(a, k, data)
                a[k] = None

        bt([None] * (len(nums) + 1), 0, nums)
        return soln