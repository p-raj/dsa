import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def qs(l, r):
            if l >= r:
                return

            pivot = nums[random.randint(l, r)]

            lt = l
            i = l
            gt = r

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

                else:
                    i += 1

            qs(l, lt - 1)
            qs(gt + 1, r)

        qs(0, len(nums) - 1)

        return nums