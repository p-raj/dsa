class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def qs(l, r):
            if l >= r:
                return

            pivot = 1

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
