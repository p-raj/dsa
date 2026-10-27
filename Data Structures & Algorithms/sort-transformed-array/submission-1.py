class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # nlogn
        # return sorted(list(map(lambda x: a * (x**2) + b * x + c, nums)))
        # sorted in n?
        # linear sort?
        nums = list(map(lambda x: a * (x**2) + b * x + c, nums))

        lft = 0
        rgt = len(nums) - 1

        answer = []

        while lft <= rgt:
            if a < 0:
                if nums[lft] < nums[rgt]:
                    answer.append(nums[lft])
                    lft += 1
                else:
                    answer.append(nums[rgt])
                    rgt -= 1
            else:
                if nums[lft] > nums[rgt]:
                    answer.append(nums[lft])
                    lft += 1
                else:
                    answer.append(nums[rgt])
                    rgt -= 1
        return answer if a < 0 else list(reversed(answer))