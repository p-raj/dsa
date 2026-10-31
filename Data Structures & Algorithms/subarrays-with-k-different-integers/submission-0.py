class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(k):
            h = defaultdict(int)
            res = 0
            lft = 0
            unq = 0
            for rgt in range(len(nums)):
                rnum = nums[rgt]
                if h[rnum] == 0:
                    unq += 1
                h[rnum] += 1

                while unq > k:
                    xnum = nums[lft]
                    h[xnum] -= 1
                    if h[xnum] == 0:
                        unq -= 1
                    lft += 1

                res += rgt - lft + 1
            return res

        return at_most_k(k) - at_most_k(k - 1)
