class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # nlogn
        # return sorted(list(map(lambda x: a * (x**2) + b * x + c, nums)))
        # sorted in n?
        # linear sort?
        nums = list(map(lambda x: a * (x**2) + b * x + c, nums))

        # lft = 0
        # rgt = len(nums) - 1

        # answer = []

        # while lft <= rgt:
        #     if a < 0:
        #         if nums[lft] < nums[rgt]:
        #             answer.append(nums[lft])
        #             lft += 1
        #         else:
        #             answer.append(nums[rgt])
        #             rgt -= 1
        #     else:
        #         if nums[lft] > nums[rgt]:
        #             answer.append(nums[lft])
        #             lft += 1
        #         else:
        #             answer.append(nums[rgt])
        #             rgt -= 1
        # return answer if a < 0 else list(reversed(answer))
        def counting_sort_for_radix(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = arr[i] // exp
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            for i in range(n):
                arr[i] = output[i]


        def radix_sort_unsigned(arr):
            if not arr:
                return arr
            max_val = max(arr)
            exp = 1
            while max_val // exp > 0:
                counting_sort_for_radix(arr, exp)
                exp *= 10
            return arr


        def radix_sort_with_negatives(arr):
            if not arr:
                return arr

            # Step 1: Split into positive and negative pools
            positives = [x for x in arr if x >= 0]
            negatives = [abs(x) for x in arr if x < 0]

            # Step 2: Sort both arrays using standard Radix Sort
            radix_sort_unsigned(positives)
            radix_sort_unsigned(negatives)

            # Step 3: Reconstruct the array
            # Reverse negatives because |-802| > |-45|, but -802 < -45
            sorted_negatives = [-x for x in reversed(negatives)]

            return sorted_negatives + positives


        # Example execution:
        return radix_sort_with_negatives(nums)
