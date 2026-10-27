class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()

        for pinned in range(len(nums) - 2):
            lft = pinned + 1
            rgt = len(nums) - 1

            while lft < rgt:
                t_ = nums[pinned] + nums[lft] + nums[rgt]
                if t_ < target:
                    ans += rgt - lft
                    lft += 1
                else:
                    rgt -= 1
        return ans
